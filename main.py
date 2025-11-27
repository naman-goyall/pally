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

if __name__ == "__main__":
    # Example usage
    test_strings = ["A man, a plan, a canal, Panama", "Not a palindrome", "Racecar"]
    for test in test_strings:
        result = is_palindrome(test)
        print(f'"{test}" is a palindrome: {result}')