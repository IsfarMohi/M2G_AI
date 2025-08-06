import whisper

model = whisper.load_model("base")
result = model.transcribe(r"upload\F_1201_12y11m_1.mp3")
print(result["text"])