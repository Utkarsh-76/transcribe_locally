import os
from google.cloud import speech
from consts import file_initials
from dir_path import base_dirname

client = speech.SpeechClient.from_service_account_file(os.path.join(base_dirname, 'service_account_key.json'))


def google_stt(file_path=f"{file_initials}.mp3"):

    with open(file_path, 'rb') as f:
        mp3_data = f.read()

    audio_file = speech.RecognitionAudio(content=mp3_data)

    config = speech.RecognitionConfig(
        sample_rate_hertz=44100,
        enable_automatic_punctuation=True,
        language_code='en-US'
    )

    response = client.recognize(config=config, audio=audio_file)

    final_text = []
    for result in response.results:
        final_text.append(result.alternatives[0].transcript)

    return ''.join(final_text)
