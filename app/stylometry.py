import spacy
nlp = spacy.load("en_core_web_sm")

def analyze_stylometry(text):
    doc = nlp(text)
    sentence_lengths = [len(sent.text.split()) for sent in doc.sents]
    vocab = set([token.text.lower() for token in doc if token.is_alpha])
    pos_counts = doc.count_by(spacy.attrs.POS)
    pos_distribution = {doc.vocab[k].text: v for k, v in pos_counts.items()}
    return {
        "avg_sentence_length": round(sum(sentence_lengths) / len(sentence_lengths), 2),
        "vocabulary_richness": round(len(vocab) / len(doc), 2),
        "pos_distribution": pos_distribution
    }
