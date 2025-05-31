import re

def check_citations(text):
    citations = re.findall(r"\(.*?\d{4}.*?\)", text)
    bibliography = re.findall(r"\n[A-Z][^\n]+\d{4}[^\n]+", text)
    missing_refs = [c for c in citations if not any(c[1:-1].split(',')[0] in b for b in bibliography)]
    return {
        "citation_count": len(citations),
        "bibliography_count": len(bibliography),
        "missing_references": missing_refs
    }