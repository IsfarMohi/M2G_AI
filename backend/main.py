# main.py
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from transcribe_module.assembly_test import transcribe
from summary_module.summary_test import summarize_text
import os
import uuid
from summary_module.op import summarize

app = FastAPI()

# Enable CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "upload"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/", response_class=HTMLResponse)
def root():
    # Simple landing page pointing to the static frontend
    return """
    <html>
      <head><title>M2G AI</title></head>
      <body>
        <h2>M2G AI Backend</h2>
        <p>Visit the <a href="/ui">frontend UI</a> to upload audio and get a summary.</p>
      </body>
    </html>
    """

@app.get("/ui", response_class=HTMLResponse)
def serve_ui():
    try:
        with open(os.path.join("frontend", "homepage.html"), "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return "<p>UI not found. Ensure frontend/homepage.html exists.</p>"

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

        if not isinstance(transcription_result, dict):
            return {"error": "Unexpected transcription response."}
        if "error" in transcription_result:
            return {"error": transcription_result["error"]}

        full_text = transcription_result.get("full_transcript", "");
        if not full_text:
            return {"error": "Empty transcription returned."}

        # Step 2: Summarize
        summary = summarize_text(full_text)
        summary2 = summarize(full_text, model="mistral")


        return {"summary": summary2}

    except Exception as e:
        return {"error": str(e)}
