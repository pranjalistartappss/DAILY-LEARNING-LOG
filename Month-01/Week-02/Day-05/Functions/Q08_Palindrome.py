def is_palindrome(text):
    reverse_text = text[::-1]

    if text == reverse_text:
        return True
    else:
        return False

print(is_palindrome("madam"))