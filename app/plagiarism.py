from sentence_transformers import SentenceTransformer, util
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")
# Example dummy dataset (pretend source documents)
source_texts = [
    "Artificial intelligence is a branch of computer science.",
    "Machine learning enables systems to learn from data.",
    "Plagiarism is copying someone else's work without attribution."
]
source_embeddings = model.encode(source_texts, convert_to_tensor=True)

def check_plagiarism(input_text):
    input_sentences = input_text.split(". ")
    input_embeddings = model.encode(input_sentences, convert_to_tensor=True)
    results = []
    for i, sent in enumerate(input_sentences):
        cosine_scores = util.cos_sim(input_embeddings[i], source_embeddings)
        max_score = float(cosine_scores.max())
        results.append({
            "sentence": sent,
            "plagiarism_score": round(max_score * 100, 2)
        })
    overall_score = np.mean([r['plagiarism_score'] for r in results])
    return {"sentences": results, "average_score": round(overall_score, 2)}
