import os
import azure.cognitiveservices.speech as speechsdk
from consts import file_initials
from dotenv import load_dotenv
load_dotenv()


def azure_stt(file_path=f"{file_initials}.wav"):
    speech_config = speechsdk.SpeechConfig(subscription=os.getenv("AZURE_SPEECH_KEY"),
                                           region=os.getenv("AZURE_SPEECH_REGION"))
    speech_config.speech_recognition_language = "en-US"

    audio_config = speechsdk.audio.AudioConfig(filename=file_path)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    speech_recognition_result = speech_recognizer.recognize_once()

    return speech_recognition_result.text
