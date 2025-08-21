# Day04_AnagramChecker.py
# Check if two strings are anagrams

def is_anagram(str1: str, str2: str) -> bool:
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    return sorted(str1) == sorted(str2)


if __name__ == "__main__":
    word1 = input("Enter first word: ")
    word2 = input("Enter second word: ")

    if is_anagram(word1, word2):
        print(f"✅ '{word1}' and '{word2}' are anagrams.")
    else:
        print(f"❌ '{word1}' and '{word2}' are NOT anagrams.")
