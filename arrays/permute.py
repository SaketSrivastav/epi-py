#! /usr/bin/python

import sys

def apply_permute(A, P):
    """
    Swap elements based on given permutation and mark P[i] as negative once the
    permutation is applied
    """
    for i in xrange(len(A)):
        next = i
        while(P[next] >= 0):
            print "swap (A[%u], A[%u])" % (i, P[next])
            A[i], A[P[next]] = A[P[next]], A[i]        # Python way of swapping
            temp = P[next]
            P[next] = P[next] - len(P)
            print "Mark P[%u] = %u)" % (next, P[next])
            next = temp

    print "P intermediate state: ",
    print P
    # Restoring P
    for i in xrange(len(P)):
        P[i] = P[i] + len(P)

def test_apply_permute():
    print "###### test_apply_permute starts ######"
    A = [100, 200, 300, 400]
    P = [3, 2, 1, 0]
    print "######## Test 1"
    print "Before"
    print "A",
    print A
    print "P",
    print P
    apply_permute(A, P)
    print "After"
    print "A",
    print A
    print "P",
    print P
    
    P = [3, 1, 2, 0]
    print "######## Test 2"
    print "Before"
    print "A",
    print A
    print "P",
    print P
    apply_permute(A, P)
    print "After"
    print "A",
    print A
    print "P",
    print P
    print "###### test_apply_permute ends ######"


def main(argv):
    test_apply_permute()

if __name__ == '__main__':
    main(sys.argv)
