# Day05_WordFrequencyCounter.py
# Count word frequency from a text file

from collections import Counter

def word_frequency(filename: str):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read().lower()
            words = text.split()
            return Counter(words)
    except FileNotFoundError:
        print("❌ File not found!")
        return {}


if __name__ == "__main__":
    file_name = input("Enter filename (e.g., sample.txt): ")
    frequencies = word_frequency(file_name)

    if frequencies:
        print("\n📊 Word Frequency Count:")
        for word, count in frequencies.most_common(10):  # top 10 words
            print(f"{word} : {count}")
