import os
from pathlib import Path

env_file = Path(__file__).with_name(".env")
name, value = env_file.read_text().strip().split("=", 1)

print("Variable name:", name)
print("Value found:", bool(value))

os.environ[name] = value
print("Key loaded:", bool(os.getenv("PRACTICE_API_KEY")))