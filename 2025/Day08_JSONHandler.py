# Day08_JSONHandler.py
# Reading and Writing JSON Data in Python

import json

def write_json(filename, data):
    """Write dictionary data into a JSON file"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    print(f" Data written to {filename}")

def read_json(filename):
    """Read and return data from a JSON file"""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(" File not found!")
        return {}
    except json.JSONDecodeError:
        print(" Invalid JSON format!")
        return {}


if __name__ == "__main__":
    sample_data = {
        "name": "Akash",
        "course": "Python Daily Codes",
        "day": 8,
        "skills": ["Python", "GitHub", "Automation"]
    }

    file_name = "sample.json"

    # Write JSON
    write_json(file_name, sample_data)

    # Read JSON
    loaded_data = read_json(file_name)
    print("\n Loaded Data from JSON:")
    print(loaded_data)
