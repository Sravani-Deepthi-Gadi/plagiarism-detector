from fastapi import FastAPI, UploadFile, File
from app.plagiarism import check_plagiarism
from app.citation_checker import check_citations
from app.stylometry import analyze_stylometry
from app.ai_detector import detect_ai_text

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Plagiarism Detection API is running"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    content = (await file.read()).decode("utf-8")

    plagiarism_result = check_plagiarism(content)
    citation_result = check_citations(content)
    stylometry_result = analyze_stylometry(content)
    ai_detected = detect_ai_text(content)

    return {
        "plagiarism": plagiarism_result,
        "citations": citation_result,
        "stylometry": stylometry_result,
        "ai_text": ai_detected
    }
