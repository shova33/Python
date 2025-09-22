def largest_palindrome(s):
    max_palindrome = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            substr = s[i:j+1]
            if substr == substr[::-1] and len(substr) > len(max_palindrome):
                max_palindrome = substr
    return max_palindrome

string = input("Enter the string: ")
result = largest_palindrome(string)
print("Largest palindrome:", result)
