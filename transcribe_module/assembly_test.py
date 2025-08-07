# transcribe_module/assembly_test.py
import assemblyai as aai
import os

aai.settings.api_key = "f31459fc0dbe4172aaf5da7d2bedf585"
transcriber = aai.Transcriber()

def transcribe(file_path: str):
    if not file_path.lower().endswith(('.mp3', '.wav')):
        return "Invalid file type. Only .mp3 and .wav allowed."
    # Validate file exists and size
    if not os.path.isfile(file_path):
        return "File does not exist."
    if os.path.getsize(file_path) > 10 * 1024 * 1024:
        return "File too large. Must be under 10MB."
    if os.path.getsize(file_path) == 0:
        return "File is empty."
    try:
        transcript = transcriber.transcribe(
            file_path,
            config=aai.TranscriptionConfig(speaker_labels=True)
        )
        return {
            "full_transcript": transcript.text
        }
    except Exception as e:
        return {"error": str(e)}
