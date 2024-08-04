import assemblyai as aai
from consts import file_initials
import os
from dotenv import load_dotenv
load_dotenv()

aai.settings.api_key = os.getenv("ASSEMBLY_AI_KEY")
transcriber = aai.Transcriber()

transcript = transcriber.transcribe(f"{file_initials}.mp3")

print(transcript.text)