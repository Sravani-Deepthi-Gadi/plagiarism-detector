from transformers import pipeline

def detect_ai_text(text):
    try:
        # Optional: Use a zero-shot classifier or fake classifier if you have custom LLMs
        classifier = pipeline("text-classification", model="roberta-base-openai-detector")
        result = classifier(text[:512])  # Limit to 512 tokens
        return {"label": result[0]['label'], "score": round(result[0]['score'] * 100, 2)}
    except:
        return {"warning": "AI detection model not available or error occurred."}
