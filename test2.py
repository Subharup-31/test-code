// Function to check if a string is a palindrome. Input: a string. Output: True if palindrome, False otherwise.
def is_palindrome(s):
    // Make the string lowercase and remove spaces to ignore case and spacing.
    s = s.lower().replace(" ", "")
    // Compare the cleaned string with its reverse to see if they match.
// This function checks if a given string is a palindrome (reads the same forwards and backwards). It takes a string input and returns True or False.
def is_palindrome(s):
    // First, it makes the string lowercase and removes all spaces to ignore case and spacing differences.
    s = s.lower().replace(" ", "")
    // Then, it compares the cleaned string to its reverse; if they match, it's a palindrome.
    return s == s[::-1]

// Ask the user to type in some text.
text = input()
// Check if the input text is a palindrome using the function.
if is_palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")
