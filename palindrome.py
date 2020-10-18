//A string is said to be a palindrome if the string read from left to right is equal to the string read from right to left.
//This python program uses python regular expression module which returns a boolean value depending on whether the string given is palindrome or not.

import re
def is_palindrome(word):
    forwards = ''.join(re.findall(r'[a-z]+', word.lower()))
    backwards = forwards[::-1]
    return forwards == backwards
    
    print(is_palindrome("malayalam")) //Output: True
    print(is_palindrome("palindrome")) //Output: False
