import re

def compute_sum() -> int:
    """
    Compute the sum of 1 + 1.

    Returns:
        int: The result of the addition.
    """
    return 1 + 1

if __name__ == "__main__":
    # Example usage
    print(f"The result of 1 + 1 is: {compute_sum()}")
    test_strings = ["A man, a plan, a canal, Panama", "Not a palindrome", "Racecar"]
    for test in test_strings:
        result = is_palindrome(test)
        print(f'"{test}" is a palindrome: {result}')