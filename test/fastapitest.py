from fastapi import FastAPI
from transcribe_module.assembly_test import transcribe
from summary_module.summary_test import summarize_text 
app = FastAPI()

@app.get("/")
def root():
    return {"message": "API Running"}

@app.get("/transcribe")
def run_transcription():
    return transcribe()

@app.get("/summarize")
def summarize_transcription():
    transcription_result = transcribe()
    
    # Handle transcription errors
    if "error" in transcription_result:
        return {"error": transcription_result["error"]}
    
    full_text = transcription_result["full_transcript"]
    summary = summarize_text(full_text)

    return {
        "summary": summary,
        "transcript": full_text,
    }
