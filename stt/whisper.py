import whisper
from consts import file_initials

# Use one of the following model
# base/tiny/small/medium/large/large-v2/large-v3


def whisper_stt(model="large-v3", file_path=f"{file_initials}.mp3"):
    model = whisper.load_model(model)
    result = model.transcribe(file_path)
    return result["text"]
