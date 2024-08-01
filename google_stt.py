from google.cloud import speech
from consts import file_initials

client = speech.SpeechClient.from_service_account_file('service_account_key.json')

with open(f"{file_initials}.mp3", 'rb') as f:
    mp3_data = f.read()

audio_file = speech.RecognitionAudio(content=mp3_data)

config = speech.RecognitionConfig(
    sample_rate_hertz=44100,
    enable_automatic_punctuation=True,
    language_code='en-US'
)

response = client.recognize(config=config, audio=audio_file)

for result in response.results:
    print(result.alternatives[0].transcript)
