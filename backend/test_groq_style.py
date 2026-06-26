from services.groq_style_analyzer import (
    analyze_style_with_groq
)

with open(
    "../data/extracted_text/New Text Document.txt",
    "r",
    encoding="utf-8"
) as f:

    text = f.read()

result = analyze_style_with_groq(text)

print(result)