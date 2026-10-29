import json

request_body = {
    "message": "Explain neural networks in one sentence."
}

print("Request body:")
print(json.dumps(request_body, indent=2))

practice_response = {
    "answer": "A neural network learns patterns from examples."
}

print("Simulated response:")
print(json.dumps(practice_response, indent=2))