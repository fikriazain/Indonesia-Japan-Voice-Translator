import time
import pyaudio
import keyboard
from dotenv import load_dotenv
from os import getenv
import wave
from time import sleep

from modules.Speech_Text import speech_text
from modules.translate import translate_text
from modules.voicevox import voicevox


load_dotenv

TARGET_KEY = getenv('TARGET_KEY')



def on_press_key(_):
    global frames, recording, stream
    if not recording:
        frames = []
        recording = True
        stream = p.open(format=pyaudio.paInt16,
                        channels=MIC_CHANNELS,
                        rate=MIC_SAMPLING_RATE,
                        input=True,
                        frames_per_buffer=1024,
                        input_device_index=1)

def on_release_key(_):
    print("Processing Recording")
    global recording, stream
    recording = False
    stream.stop_stream()
    stream.close()
    stream = None

    wav = wave.open('resources/output.wav', 'wb')
    wav.setnchannels(MIC_CHANNELS)
    wav.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wav.setframerate(MIC_SAMPLING_RATE)
    wav.writeframes(b''.join(frames))
    wav.close()
    data = speech_text()
    translate = translate_text(data)
    voicevox(translate)
    

if __name__ == '__main__':
    p = pyaudio.PyAudio()
    mic_info = p.get_device_info_by_index(1) #Change it to your default microphone index
    MIC_CHANNELS = mic_info['maxInputChannels']
    MIC_SAMPLING_RATE = int(mic_info['defaultSampleRate'])

    frames = []
    recording = False
    stream = None

    print('Program Running')
    keyboard.on_press_key('f', on_press_key)
    keyboard.on_release_key('f', on_release_key)

    try:
        while True:
            if recording and stream:
                 #Reset the frame to get a new recording
                data = stream.read(1024)
                frames.append(data)
            else:
                #To make the CPU not always busy
                sleep(0.8)

    except KeyboardInterrupt:
        print('Exit the program')