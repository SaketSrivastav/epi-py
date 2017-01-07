import sys

def int_to_str(x):
    """
    Input: integer (+)ve or (-)ve
    Output: String representation of input
    Description: get each digit using x mod 10 and add to the string and
    reverse it before returning the result"""

    is_negative = False
    s = ""
    index = 0
    if x < 0:
        is_negative = True
        x = -x

    while(x):
        digit = x % 10
        s += str(digit)
        x = x / 10

    if is_negative:
        return '-' + s[::-1]
    
    return s[::-1]

def test_int_to_str():
    print "###### test_int_to_str starts ######"
    x = 12345
    print "INPUT: x = %u" % (x)
    s = int_to_str(x)
    print "OUTPUT = " + s
    x = -12345
    print "INPUT: x = %d" % (x)
    s = int_to_str(x)
    print "OUTPUT = " + s

    print "###### test_int_to_str ends ######"


def str_to_int(s):
    """
    Input: string s
    Output: integer x
    Description: Take each character multiply by 10 and add it to result"""
    x = 0
    is_negative = False
    index = 0
    for c in s:
        if(index == 0 and c == '-'):
            is_negative = True
            continue

        x = x * 10 + int(c)
        index+=1

    if is_negative:
        return -x

    return x

def test_str_to_int():
    print "###### test_str_to_int starts ######"
    s = "12345"
    print "Input: s = " + s
    x = str_to_int(s)
    print "Output: x = %d" % (x)
    s = "-12345"
    print "Input: s = " + s
    x = str_to_int(s)
    print "Output: x = %d" % (x)
    print "###### test_str_to_int ends ######"


def main(argv):
    # test_int_to_str()
    test_str_to_int()

if __name__ == '__main__':
    main(sys.argv)
