#!/usr/bin/python

import sys
RIGHT = 0
DOWN = 1
LEFT = 2
TOP = 3

def print_direction(direction):
    if direction == RIGHT:
        print "RIGHT"
    elif direction == LEFT:
        print "LEFT"
    elif direction == DOWN:
        print "DOWN"
    elif direction == TOP:
        print "TOP"
    print " "


def print_matrix_spiral(A, row, col):
    """
    Input:   A: nxn Array
           row: number of rows
           col: number of columns
    Description:
    Prints the matrix in spiral order.
    Application: Currently Unknown. Mainly used in interviews to gauge candidates
    hold on matrices and manipulation of indices.
    """
    top = 0
    bottom = row-1
    left = 0
    right = col-1
    direction = RIGHT
    print "####### Spiral print started #######"
    while top <= bottom and left <= right:
        if direction == RIGHT:
            i = left
            while i <= right:
                print A[top][i],
                i += 1
            top += 1
        elif direction == DOWN:
            print " "
            i = top
            while i <= bottom:
                print A[i][right],
                i += 1
            right -= 1
        elif direction == LEFT:
            print " "
            i = right
            while i >= left:
                print A[bottom][i],
                i -= 1
            bottom -= 1
        elif direction == TOP:
            print " "
            i = bottom
            while i >= top:
                print A[i][left],
                i -= 1
            left += 1
        direction = (direction+1)%4

    print "####### Spiral print ended #######"

def test_print_matrix_spiral():
    print "###### test_print_matrix_spiral starts ######"
    A = [[1, 2, 3, 4],
         [12, 13, 14, 5],
         [11, 16, 15, 6],
         [10, 9, 8, 7]]
    print_matrix_spiral(A, 4, 4)
    print "###### test_print_matrix_spiral ends ######"

def main(argv):
    test_print_matrix_spiral()

if __name__ == '__main__':
    main(sys.argv)
