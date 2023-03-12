from os import getenv
from dotenv import load_dotenv
import  requests
import sounddevice as sd
from scipy.io.wavfile import write


load_dotenv()


WHISPER_URL = getenv('WHISPER_URL')

def transcribe():
    print(WHISPER_URL)
    with open('resources/recorded.wav', 'rb') as f:
        files = {'audio_file': f}
        r = requests.post((f'{WHISPER_URL}asr?task=transcribe&language=id&output=json'), files=files)
        return r.json()

