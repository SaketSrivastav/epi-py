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

def next_permute(P):
    k = len(P) - 2
    # Find the number next to longest decreasing suffix of P, A[k] < A[K+1]
    # when moving from left to right
    for i in reversed(xrange(len(P))):
        if k >= 0 and P[k] < P[i]:
            break
        k -= 1

    if k == -1:
        print "No next permutation"
        return None
    print "k=%u" % (k)
    # Swap this k index with first element greater in decreasing suffix
    # maintaining the decreasing suffix property
    for i in reversed(xrange(len(P))):
        if i < k:
            break
        if P[i] > P[k]:
            P[i], P[k] = P[k], P[i]
            print "Swapped P[%u] = %u and P[%u] = %u" % (i, k, P[i], P[k])
            break;

    # Reverse the decreasing suffix to get the next permutation
    P[k+1:len(P)] = reversed(P[k+1:len(P)])
    return P

def test_next_permute():
    print "###### test_next_permute starts ######"
    P = [6, 1, 5, 4, 3, 0]
    print "Before P",
    print P
    P = next_permute(P)
    print "After P",
    print P
    print "###### test_next_permute ends ######"


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
    # test_apply_permute()
    test_next_permute()

if __name__ == '__main__':
    main(sys.argv)
