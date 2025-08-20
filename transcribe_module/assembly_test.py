# transcribe_module/assembly_test.py
import assemblyai as aai
import os

# NOTE: Consider moving this API key to an environment variable for security.
aai.settings.api_key = "f31459fc0dbe4172aaf5da7d2bedf585"
transcriber = aai.Transcriber()


def transcribe(file_path: str):
    """Transcribe an audio file and return a consistent JSON-like dict.

    Returns either {"full_transcript": str} on success or {"error": str} on failure.
    """
    # Basic validation
    if not isinstance(file_path, str) or not file_path:
        return {"error": "Invalid file path."}

    lower_path = file_path.lower()
    if not lower_path.endswith((".mp3", ".wav")):
        return {"error": "Invalid file type. Only .mp3 and .wav allowed."}

    if not os.path.isfile(file_path):
        return {"error": "File does not exist."}

    file_size_bytes = os.path.getsize(file_path)
    if file_size_bytes > 10 * 1024 * 1024:
        return {"error": "File too large. Must be under 10MB."}
    if file_size_bytes == 0:
        return {"error": "File is empty."}

    try:
        transcript = transcriber.transcribe(
            file_path,
            config=aai.TranscriptionConfig(speaker_labels=True),
        )
        return {"full_transcript": transcript.text}
    except Exception as e:
        return {"error": str(e)}
