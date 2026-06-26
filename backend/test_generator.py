from services.text_generator import generate_text

print("=" * 50)
print("TESTING TEXT GENERATOR")
print("=" * 50)

prompt = "Write a LinkedIn post about AI Agents"

result = generate_text(prompt)

print("\n")
print("=" * 50)
print("GENERATED OUTPUT")
print("=" * 50)

print(result)