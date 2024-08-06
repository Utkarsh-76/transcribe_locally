from deepgram import DeepgramClient, PrerecordedOptions, FileSource
import os
from consts import file_initials

from dotenv import load_dotenv
load_dotenv()

DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")


# use models from nova-2/nova/base/enhanced
def deepgram_stt(model="nova-2", file_path=f"{file_initials}.mp3"):

    with open(file_path, "rb") as file:
        buffer_data = file.read()

    payload: FileSource = {"buffer": buffer_data}

    deepgram = DeepgramClient(DEEPGRAM_API_KEY)

    options = PrerecordedOptions(
        model=model,
        language="en",
        smart_format=True,
    )

    response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)
    return response.results.channels[0].alternatives[0].transcript
