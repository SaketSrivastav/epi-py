import sys

def is_palindrome(s):
    """
    Input: string s
    Output: Boolean
    Description: Return True is the given string is palindrome otherwise False"""
    i = 0
    j = len(s) - 1
    while(i < j):
        # Ignore non alpha numeric characters
        while(s[i].isalnum() == False):
            i += 1
        while(s[j].isalnum() == False):
            j -= 1

        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1

    return True

def test_is_palindrome():
    print "###### test_is_palindrome starts ######"
    s = "Was it a cat I saw?"
    print "Input: " + s
    print "Output: " + str(is_palindrome(s))
    s = "as it a cat I saw?"
    print "Input: " + s
    print "Output: " + str(is_palindrome(s))
    print "###### test_is_palindrome ends ######"

def main(argv):
    test_is_palindrome()

if __name__ == '__main__':
    main(sys.argv)
