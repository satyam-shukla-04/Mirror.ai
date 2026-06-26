import re

def analyze_style(text):

    words = text.split()

    sentences = re.split(r'[.!?]+', text)

    sentences = [s.strip() for s in sentences if s.strip()]

    profile = {
        "word_count": len(words),
        "sentence_count": len(sentences),
        "avg_sentence_length": round(
            len(words) / max(len(sentences), 1),
            2
        )
    }

    return profile