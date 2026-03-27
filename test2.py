// This function checks if a given string is a palindrome (reads the same forwards and backwards). It takes a string input and returns True or False.
def is_palindrome(s):
    // First, it makes the string lowercase and removes all spaces to ignore case and spacing differences.
    s = s.lower().replace(" ", "")
    // Then, it compares the cleaned string to its reverse; if they match, it's a palindrome.
    return s == s[::-1]

text = input()
if is_palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")
