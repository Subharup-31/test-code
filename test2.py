// Function to check if a string is a palindrome. Input: a string. Output: True if palindrome, False otherwise.
def is_palindrome(s):
    // Make the string lowercase and remove spaces to ignore case and spacing.
    s = s.lower().replace(" ", "")
    // Compare the cleaned string with its reverse to see if they match.
    return s == s[::-1]

// Ask the user to type in some text.
text = input()
// Check if the input text is a palindrome using the function.
if is_palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")
