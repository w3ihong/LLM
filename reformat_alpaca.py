import json
import random

# Load the Alpaca dataset (Replace 'alpaca_data.json' with your actual file)
with open("./training_data/alpaca_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Define a list of rejection messages
rejection_messages = [
    "C'mon now. I'm not ChatGPT or Google.",
    "No clue, try somewhere else",
    "I have no idea, go search online.",
    "Hey, I'm not a search engine.",
    "I'm not sure, try asking a human.",
]


# Process and write to a JSONL file
output_file = "alpaca_formatted.jsonl"
with open(output_file, "w", encoding="utf-8") as f:
    for item in data:
        combined_input = item["instruction"].strip()
        if item["input"].strip():
            combined_input += " " + item["input"].strip()
        
        # Replace the output with a random rejection message
        new_output = random.choice(rejection_messages)

        # Write the JSON object to the JSONL file
        json.dump({"input": combined_input, "output": new_output}, f, ensure_ascii=False)
        f.write("\n")

print(f"Dataset processing complete. Saved as '{output_file}'.")
