#! /usr/bin/python

def del_key(A, key):
    """
    del_key deletes the key in the array in O(n) time and O(1) space and
    returns the current length of the array.
    """
    print "del_key: %u" % (key)
    w_idx = 0
    for i in xrange(len(A)):
        if A[i] != key:
            A[w_idx] = A[i]
            w_idx += 1

    return w_idx

def test_del_key():
    print "####### Test del_key ########"
    A = [5, 3, 7, 11, 2, 3, 13, 5, 7]
    print "Before deleting: A",
    print A
    num = del_key(A, 3)
    print "After deleting: len(A): %u" % (num)
    for i in xrange(num):
        print A[i],
    print " "

def del_key_multi(A):
    """
    del_key deletes the repeting key in the sorted array in
    O(n) time and O(1) space and returns the current length of the array.
    """
    w_idx = 0
    if len(A) == 0:
        return w_idx

    for i in xrange(len(A)):
        if A[w_idx - 1] != A[i]:
            A[w_idx] = A[i]
            w_idx += 1

    return w_idx

def test_del_key_multi():
    print "####### Test del_key-multi ########"
    A = [2, 5, 5, 7, 11, 13, 13, 13, 15, 17]
    print "Before deleting: A",
    print A
    num = del_key_multi(A)
    print "After deleting: len(A): %u" % (num)
    for i in xrange(num):
        print A[i],
    print " "

def main():
    test_del_key()
    test_del_key_multi()

if __name__ == '__main__':
    main()
