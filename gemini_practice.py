from pathlib import Path

api_key = ""

for line in Path(__file__).with_name(".env").read_text().splitlines():
    if line.startswith("GEMINI_API_KEY="):
        api_key = line.split("=", 1)[1].strip()

print("Gemini key loaded:", bool(api_key))

from google import genai

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-flash-latest",
    contents="Explain neural networks in one short sentence."
)

print(response.text)