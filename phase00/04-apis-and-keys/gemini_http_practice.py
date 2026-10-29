import json
import urllib.request
from pathlib import Path

api_key = ""

for line in Path(__file__).with_name(".env").read_text().splitlines():
    if line.startswith("GEMINI_API_KEY="):
        api_key = line.split("=", 1)[1].strip()

print("Gemini key loaded:", bool(api_key))


url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent"

body = {
    "contents": [
        {
            "parts": [
                {"text": "Explain neural networks in one short sentence."}
            ]
        }
    ]
}

data = json.dumps(body).encode("utf-8")

request = urllib.request.Request(
    url,
    data=data,
    headers={
        "Content-Type": "application/json",
        "x-goog-api-key": api_key,
    },
    method="POST",
)

with urllib.request.urlopen(request, timeout=120) as response:    result = json.loads(response.read())

print(result["candidates"][0]["content"]["parts"][0]["text"])