import sys

k_map = ["0", "1", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "XYZ"]

def t9_keypad_helper(phone_number, digit, partial_mneumonic):
    """
    Input: phone_number array
           digit: current digit in processing
           partial_mneumonic: the mneumonic formaed so far
           mneumonic: Completed mneumonic after parsing the complete phone number
    Description: Remembering names is easier compared to remembering numbers
           This logic is used to give names to numbers like 800-455-LOAN
    """
    if digit == len(phone_number):
        return
    partial_mneumonic.append(k_map[int(phone_number[digit])])
    t9_keypad_helper(phone_number, digit+1, partial_mneumonic)

def test_t9_keypad_helper():
    print "###### test_t9_keypad_helper starts ######"
    phone_number = "2132450675"
    mneumonic = list()
    print "Input: " + phone_number
    t9_keypad_helper(phone_number, 0, mneumonic)
    print "Output: " + ''.join(mneumonic)
    print "###### test_t9_keypad_helper ends ######"


def main(argv):
    test_t9_keypad_helper()

if __name__ == '__main__':
    main(sys.argv)
