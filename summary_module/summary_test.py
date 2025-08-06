from transformers import pipeline

# Load BART summarizer only once
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text: str):
    # Handle long transcripts safely (BART limit is ~1024 tokens)
    if len(text) > 1000:
        text = text[:1000]  # truncate or chunk in future

    summary = summarizer(text, max_length=100, min_length=20, do_sample=False)
    return summary[0]['summary_text']
