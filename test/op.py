import requests

def summarize(transcript, model="tinyllama", save_path="summary.txt"):
    url = "http://localhost:11434/api/generate"

    payload = {
        "model": model,
        "prompt": f"Summarize the following meeting transcript:\n{transcript}",
        "stream": False
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        summary = response.json()["response"]

        print("\n--- SUMMARY ---\n")
        print(summary)

        with open(save_path, "a", encoding="utf-8") as f:
            f.write(summary + "\n")

        print(f"Summary saved to {save_path}")
        return summary

    except Exception as e:
        print("Failed to generate summary:", e)
        return None
    
transcript = """ 
During the meeting held on August 17th to consider applying for a full discharge for the property located at Lot 2, Plan 73464 within part of Northwest Quartier 20115 under CT 3301-501, the meeting opened with Mr. Daniel Minan speaking and asking whether there were any questions from the surrounding landowners or farmers who may be affected by the application. Mr. Dan Douceur was not present for this portion of the meeting, but he spoke later in support of the full discharge of the caveat. The discussion then turned to the rationales given by Ms. Nyland and Mr. Mind regarding the conditions for a full discharge of the caveat. Councilor Warren Miller moved to adjourn the meeting at 7:28pm, and it was passed unanimously.
"""

print (summarize())