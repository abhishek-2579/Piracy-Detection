from fuzzywuzzy import fuzz

def detect_obfuscated_keyword(keyword, reference_word="movie"):
    """
    Detects whether the given keyword is obfuscated by comparing it with a reference word.
    
    :param keyword: The keyword to check.
    :param reference_word: The word to compare against (default: 'movie').
    :return: 'Obfuscated' or 'Non-obfuscated'.
    """
    # Calculate the similarity ratio
    similarity = fuzz.ratio(keyword.lower(), reference_word.lower())

    # Consider a threshold for obfuscation detection
    threshold = 80  # You can adjust this based on your needs
    if similarity >= threshold:
        return "Non-obfuscated"
    else:
        return "Obfuscated"

# Prompt the user for input
if __name__ == "__main__":
    user_keyword = input("Enter a keyword to check if it's obfuscated: ")
    # Call the function with the user input
    result = detect_obfuscated_keyword(user_keyword)
    print(f"Keyword: {user_keyword} - Result: {result}")
