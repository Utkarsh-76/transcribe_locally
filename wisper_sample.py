import whisper
from consts import audio_file_name

model = whisper.load_model("base")
result = model.transcribe(audio_file_name)
print(result["text"])
