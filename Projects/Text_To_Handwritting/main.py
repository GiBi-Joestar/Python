import os
import pywhatkit as pw

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "input.txt")

with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

pw.text_to_handwriting(text, "output.png")

print("Done ✅")