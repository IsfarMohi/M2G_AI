import assemblyai as aai

aai.settings.api_key = "f31459fc0dbe4172aaf5da7d2bedf585"

transcriber = aai.Transcriber()

def transcribe():
    try:
        transcript = transcriber.transcribe(
            "upload\F_1201_12y11m_1.mp3",
            config=aai.TranscriptionConfig(speaker_labels=True)
        )
        return {
            "full_transcript": transcript.text,       
        }
    except Exception as e:
        return {"error": str(e)}
