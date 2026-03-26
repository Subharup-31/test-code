"""
Palindrome Checker Module

This module provides functionality to determine whether a given string is a palindrome.
A palindrome is a sequence of characters that reads the same backward as forward,
ignoring case differences and spaces.

Example palindromes:
- "racecar"
- "A man a plan a canal Panama"
- "nurses run"
"""

def is_palindrome(s):
    """
    Determines if the provided string is a palindrome.
    
    The function performs the following transformations:
    1. Converts all characters to lowercase for case-insensitive comparison
    2. Removes all whitespace characters to ignore spaces
    3. Compares the normalized string with its reverse
    
    Parameters:
        s (str): The input string to evaluate. Can contain letters, numbers, 
                 spaces, or special characters.
    
    Returns:
        bool: True if the normalized string is identical when read forward 
              and backward, False otherwise.
    
    Edge cases handled:
    - Empty strings: Returns True (empty string reads the same forward/backward)
    - Single characters: Returns True (trivially a palindrome)
    - Strings with only spaces: After normalization becomes empty string → True
    - Mixed case strings: Case is normalized so "RaceCar" is recognized as palindrome
    
    Example usage:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("Hello")
        False
        >>> is_palindrome("A man a plan a canal Panama")
        True
    """
    # Normalize the string: lowercase and remove all spaces
    normalized = s.lower().replace(" ", "")
    # Check if normalized string equals its reverse (slicing with step -1 reverses string)
    return normalized == normalized[::-1]

# Main execution block
if __name__ == "__main__":
    """
    Interactive palindrome checker.
    
    Prompts user for input, checks if the input is a palindrome using is_palindrome(),
    and prints the result. The program continues until manually terminated.
    """
    # Read input from standard input (keyboard)
    user_input = input("Enter text to check: ")
    
    # Evaluate the input string and display appropriate message
    if is_palindrome(user_input):
        print("Palindrome")
    else:
        print("Not Palindrome")