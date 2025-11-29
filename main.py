import re

def is_palindrome(s: str) -> bool:
    """
    Check if the given string is a palindrome.

    A palindrome is a string that reads the same forwards and backwards,
    ignoring spaces, punctuation, and case.

    Args:
        s (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Normalize the string: remove non-alphanumeric characters and convert to lowercase
    normalized_str = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    
    # Check if the normalized string is equal to its reverse
    return normalized_str == normalized_str[::-1]

def analyze_strings(strings: list) -> dict:
    """
    Analyze a list of strings and determine if each is a palindrome.

    Args:
        strings (list): The list of strings to analyze.

    Returns:
        dict: A dictionary with strings as keys and their palindrome status as values.
    """
    return {s: is_palindrome(s) for s in strings}

def count_palindromes(strings: list) -> int:
    """
    Count the number of palindromes in a list of strings.

    Args:
        strings (list): The list of strings to analyze.

    Returns:
        int: The count of palindromes in the list.
    """
    return sum(1 for s in strings if is_palindrome(s))

if __name__ == "__main__":
    # Example usage
    test_strings = ["A man, a plan, a canal, Panama", "Not a palindrome", "Racecar"]
    results = analyze_strings(test_strings)
    for test, result in results.items():
        print(f'"{test}" is a palindrome: {result}')
    
    palindrome_count = count_palindromes(test_strings)
    print(f'Total number of palindromes: {palindrome_count}')