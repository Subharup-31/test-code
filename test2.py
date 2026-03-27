def is_palindrome(s):
    # Checks if string s is a palindrome, ignoring case and spaces. Returns True or False.
    s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces for fair comparison
    return s == s[::-1]  # Compare the cleaned string to its reverse to test palindrome

text = input()
if is_palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")