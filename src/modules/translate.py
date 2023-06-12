import os
from google.cloud import translate_v2


def translate_text(text):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "googlekey.json" #Use your own key

    client = translate_v2.Client()
    source = "id" # source language is Indonesian
    target = "ja" # target language is Japanese
    output = client.translate(text, source_language=source, target_language=target)
    print("Indonesia: ",text)
    print("Japan: ",output['translatedText'])
    return output['translatedText']


