import whisper

model = whisper.load_model("base")
result = model.transcribe(r"upload\Chris_Home_2.mp3")
print(result["text"])