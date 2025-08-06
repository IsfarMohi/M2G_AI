import assemblyai as aai

# Set your API key
aai.settings.api_key = "555d5de0e22049af92a0a6ea7d934abd"

# Create transcriber instance
transcriber = aai.Transcriber()

def transcribe():
    # Transcribe with speaker diarization
    transcript = transcriber.transcribe(
        r"upload\F_1201_12y11m_1.mp3",
        config=aai.TranscriptionConfig(
            speaker_labels=True  # enables speaker separation
        )
    )
    print(transcript.text)
    for utterance in transcript.utterances:
        print(f"Speaker {utterance.speaker}: {utterance.text}")

# Call the function to run transcription
transcribe()