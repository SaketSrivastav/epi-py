import sys

def reverse_words(input_str):
    """
    Input: s
    Output: s string with reversed words
    Description: Takes string input s and reverses the order of words"""

    start = 0
    end = 0
    s = list(input_str)
    # Reverse the whole string to get each words reversed
    s.reverse()
    # find the next space starting from start index and continue till the end
    try:
        end = s.index(' ', start)
    except ValueError:
        end = -1
    while end < len(s) and end != -1:
        # Reverse the words of already reverse string to get correct order of
        # words
        s[start:end] = reversed(s[start:end])
        start = end + 1
        try:
            end = s.index(' ', start)
        except ValueError:
            end = -1

    # Print the last word
    s[start:len(s)] = reversed(s[start:len(s)])
    return ''.join(s)

def test_reverse_words():
    print "###### test_reverse_words starts ######"
    s = "Hello my name is Saket"
    print "Input: " + s
    print "Output: " + reverse_words(s)
    print "###### test_reverse_words ends ######"


def main(argv):
    test_reverse_words()

if __name__ == '__main__':
    main(sys.argv)
