import assemblyai as aai
from consts import file_initials
import os
from dotenv import load_dotenv
load_dotenv()

aai.settings.api_key = os.getenv("ASSEMBLY_AI_KEY")


def aai_stt(file_path=f"{file_initials}.mp3"):

    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(file_path)

    return transcript.text