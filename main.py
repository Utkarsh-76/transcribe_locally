from stt.AssemblyAI import aai_stt
# from stt.deepgram import deepgram_stt
from stt.faster_whisper import faster_whisper_stt
from stt.google import google_stt
from stt.microsoft_azure import azure_stt
from stt.whisper import whisper_stt

if __name__ == "__main__":
    print("AssemblyAI:")
    print(aai_stt("audio_files/sample.mp3"))
    print()

    # python > 3.10 needed for this to work
    print("Deepgram:")
    # model options nova-2/nova/base/enhanced
    # print(deepgram_stt('nova-2', "audio_files/sample.mp3")) # python > 3.10 needed for this to work
    print()

    print("Faster Whisper:")
    # model options base/tiny/small/medium/large/large-v2/large-v3
    print(faster_whisper_stt('large-v3', "audio_files/sample.mp3"))
    print()

    print("Google:")
    print(google_stt("audio_files/sample.mp3"))
    print()

    print("Azure:")
    print(azure_stt("audio_files/sample.wav"))
    print()

    print("Whisper:")
    # model options base/tiny/small/medium/large/large-v2/large-v3
    print(whisper_stt('large-v3', "audio_files/sample.mp3"))
    print()