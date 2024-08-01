import whisper
from consts import file_initials

model = whisper.load_model("base")
result = model.transcribe(f"{file_initials}.mp3")
print(result["text"])
