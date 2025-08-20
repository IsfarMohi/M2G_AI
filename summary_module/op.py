import requests
import time
import psutil

try:
    import GPUtil
    gpu_enabled = True
except ImportError:
    gpu_enabled = False



def summarize(transcript, model="mistral", save_path="summary.txt"):
    url = "http://localhost:11434/api/generate"

    prompt = ("""
            Summarize the following text using this structure:

            1. Heading  a short, clear title summarizing the topic

            2. Objective  1-2 lines describing the purpose or goal

            3. Key Points  use numbered bullet points to list main ideas or discussions

            4. Conclusion  a brief wrap-up or final takeaway

            5. Tasks Assigned (if any) list assigned tasks with the responsible person(s) and deadline (if mentioned)
              .\n"""
              
        f"{transcript}"
    )

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "temperature": 0.5,
        "top_p": 0.7
    }

    try:
        start_time = time.perf_counter()

        # CPU usage before
        cpu_before = psutil.cpu_percent(interval=None)

        response = requests.post(url, json=payload)
        response.raise_for_status()

        # CPU usage after
        cpu_after = psutil.cpu_percent(interval=0.5)

        end_time = time.perf_counter()
        elapsed_time = end_time - start_time

        summary = response.json()["response"]


        with open(save_path, "a", encoding="utf-8") as f:
            f.write(summary + "\n")

        print(f"\nSummary saved to {save_path}")
        print(f"⏱️ Time taken: {elapsed_time:.2f} seconds")
        print(f"🧠 CPU usage during request: {cpu_before}% → {cpu_after}%")

        if gpu_enabled:
            gpus = GPUtil.getGPUs()
            for i, gpu in enumerate(gpus):
                print(f"🎮 GPU{i}: {gpu.name} | Load: {gpu.load*100:.1f}% | Memory Used: {gpu.memoryUsed}/{gpu.memoryTotal} MB")

        return summary

    except Exception as e:
        print("❌ Failed to generate summary:", e)
        return None


# transcript = """ 
# During the meeting held on August 17th to consider applying for a full discharge for the property located at Lot 2, Plan 73464 within part of Northwest Quartier 20115 under CT 3301-501, the meeting opened with Mr. Daniel Minan speaking and asking whether there were any questions from the surrounding landowners or farmers who may be affected by the application. Mr. Dan Douceur was not present for this portion of the meeting, but he spoke later in support of the full discharge of the caveat. The discussion then turned to the rationales given by Ms. Nyland and Mr. Mind regarding the conditions for a full discharge of the caveat. Councilor Warren Miller moved to adjourn the meeting at 7:28pm, and it was passed unanimously.
# """

# summarize(transcript, model="mistral")
