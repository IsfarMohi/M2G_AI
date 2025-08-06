import requests

transcript = """
kkk
"""
url = "http://localhost:11434/api/generate"

response = requests.post(url, json={
    "model": "tinyllama",
    "prompt": f"Summarize the following meeting transcript:\n{transcript}",
    "stream": False
})

summary = response.json()["response"]
print("\n--- SUMMARY ---\n")
print(summary)

with open("summary.txt", "w", encoding="utf-8") as f:
    f.write(summary)

print("Summary saved to summary.txt")
