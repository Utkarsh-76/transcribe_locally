# transcribe_locally

Easy setup for multiple TTS options to test out what works the best. 

Following TTS tools are included in the setup:
1. Whisper(Open Source)
2. Fast Whisper(Open Source)
3. Deepgram
4. AssemblyAI
5. Azure cognitive service
6. Google STT


## 1. Clone the repo:

```bash
git clone https://github.com/Utkarsh-76/transcribe_locally.git
```

## 2. Switch to the virtual env you want and run the following:

```bash
pip install -r requirements.txt
```
This will install all the require packages

**Note 1:** 

Deepgram package needs python version > 3.10 to work

**Note 2:** 

For running Whisper locally you need to download ffmpeg file.

Go to the transcribe_locally directory and run install_ffmpeg.sh file.

```bash
chmod +x install_ffmpeg.sh
./install_ffmpeg.sh
```

## 3. Add API keys
Create a .env file to add the following API keys:

- DEEPGRAM_API_KEY
- AZURE_SPEECH_KEY
- ASSEMBLY_AI_KEY

**Note 1:** Add "AZURE_SPEECH_REGION" in .env file

**Note 2:** Create an account on GCP and download service account key as "service_account_key.json".

## 4. Audio file
Copy the audio files in .mp3 and .wav(for azure stt) format to audio_files folder and change the file path in main.py file to to these newly added files.

## 5. Transcribe the audio files:
Run main.py file to see the results


## Support

If you need any support for this repo or AI in general [schedule a meeting](https://calendly.com/agarwal-ut76/30min) or reach out to me via:

[![Linkedin](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/utkarsh-data-agarwal/)

[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:agarwal.ut76@gmail.com)
