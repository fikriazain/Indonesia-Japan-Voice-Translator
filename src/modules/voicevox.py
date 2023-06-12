from threading import Thread
import requests
import sounddevice as sd
import soundfile as sf

def voicevox(text):
    url = f'https://api.su-shiki.com/v2/voicevox/audio/?text={text}&key=Y184B7304412O3F&speaker=2'

    req = requests.post(url)

    with open("resources/voicevox.wav", "wb") as f:
        f.write(req.content)
        print("Voicevox Done")
    
    threads = [Thread(target=play_sound)]
    [t.start() for t in threads]
    [t.join() for t in threads]


def play_sound():
    #Play audio using sounddevice on the same thread
    data, fs = sf.read('resources/voicevox.wav', dtype='float32')
    sd.play(data, fs)
    sd.wait()

    


