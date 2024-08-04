from faster_whisper import WhisperModel
from consts import file_initials

# Use one of the following model
# base/tiny/small/medium/large/large-v2/large-v3

model = WhisperModel("large-v3")

segments, info = model.transcribe(f"{file_initials}.mp3")

text = []
for segment in segments:
    text.append(segment.text)

print("".join(text))
