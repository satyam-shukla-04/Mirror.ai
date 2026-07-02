import re


def extract_examples(text: str):
    """
    Extract representative paragraphs.
    """

    paragraphs = [
        p.strip()
        for p in text.split("\n\n")
        if len(p.strip()) > 120
    ]

    if len(paragraphs) <= 3:
        return paragraphs

    return [
        paragraphs[0],
        paragraphs[len(paragraphs)//2],
        paragraphs[-1]
    ]