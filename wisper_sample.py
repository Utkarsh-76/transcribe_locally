import whisper
from consts import file_initials

# Use one of the following model
# base/tiny/small/medium/large/large-v2/large-v3

model = whisper.load_model("medium")
result = model.transcribe(f"{file_initials}.mp3")
print(result["text"])