from deepgram import DeepgramClient, PrerecordedOptions, FileSource
import os
from consts import audio_file_name

from dotenv import load_dotenv
load_dotenv()

DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")

with open(audio_file_name, "rb") as file:
    buffer_data = file.read()

payload: FileSource = {"buffer": buffer_data}


def main():
    try:
        deepgram = DeepgramClient(DEEPGRAM_API_KEY)

        options = PrerecordedOptions(
            model="nova-2",
            language="en",
            smart_format=True,
        )

        response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)
        print(response.results.channels[0].alternatives[0].transcript)

    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    main()