from faster_whisper import WhisperModel
from consts import file_initials

# Use one of the following model
# base/tiny/small/medium/large/large-v2/large-v3


def faster_whisper_stt(model="large-v3", file_path=f"{file_initials}.mp3"):

    model = WhisperModel(model)

    segments, info = model.transcribe(file_path)

    text = []
    for segment in segments:
        text.append(segment.text)

    return "".join(text)
