import speech_recognition as sr
import requests
import json


def transcribe(file_name, language="en-US"):
    r = sr.Recognizer()
    with sr.AudioFile(file_name) as source:
        audio = r.record(source)  # read the entire audio file
        return r.recognize_google(audio, language=language)


def create_script(file_name, language='en-US'):
    script = open('generated_script.txt', 'w+')
    text = transcribe(file_name, language)
    script.write(text)


def watson(audio, auth):
    with open(audio, 'rb') as f:
        data = f.read()
    header = {"Content-Type": "audio/wav"}
    r = requests.post(f"{auth['url']}/v1/recognize", data=data, headers=header, auth=('apikey', auth['apikey']))
    return r.text


if __name__ == "__main__":
    create_script('custom/spn2.wav', language='es-ES')
