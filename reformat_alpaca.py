import json
import random

# Load the Alpaca dataset (Replace 'alpaca_data.json' with your actual file)
with open("./training_data/alpaca_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)


# Process and write to a JSONL file
output_file = "alpaca_formatted.jsonl"
with open(output_file, "w", encoding="utf-8") as f:
    for item in data:
        combined_input = item["instruction"].strip()
        if item["input"].strip():
            combined_input += " " + item["input"].strip()
        


        # Write the JSON object to the JSONL file
        json.dump({"input": combined_input, "output": "I don't know."}, f, ensure_ascii=False)
        f.write("\n")

print(f"Dataset processing complete. Saved as '{output_file}'.")
