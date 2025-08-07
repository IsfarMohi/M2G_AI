# main.py
from fastapi import FastAPI, UploadFile, File
from transcribe_module.assembly_test import transcribe
from summary_module.summary_test import summarize_text
import os
import uuid

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def root():
    return {"message": "API Running"}

@app.post("/process-audio")
async def process_audio(file: UploadFile = File(...)):
    try:
        # Generate a unique file name
        extension = file.filename.split(".")[-1]
        unique_filename = f"{uuid.uuid4()}.{extension}"
        file_path = os.path.join(UPLOAD_DIR, unique_filename)

        # Save file to disk
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)

        # Step 1: Transcribe
        transcription_result = transcribe(file_path)

        if "error" in transcription_result:
            return {"error": transcription_result["error"]}

        full_text = transcription_result["full_transcript"]

        # Step 2: Summarize
        summary = summarize_text(full_text)

        return {
    
            "summary": summary
        }

    except Exception as e:
        return {"error": str(e)}
