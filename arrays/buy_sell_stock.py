#! /usr/bin/python

import sys

def buy_sell_stock_once(A):
    if len(A) == 0:
        return 0

    min_so_far = A[0]
    max_profit = 0
    for i in xrange(len(A)):
        min_so_far = min(A[i], min_so_far)
        max_profit = max(max_profit, (A[i] - min_so_far))

    return max_profit

# Complexity: O(n) time and O(n) space
# Better solution will be to track the index where the first sell hit maximum.
# Find second max_profit from max_first_sale_index to last index of array
def buy_sell_stock_twice(A):
    if len(A) == 0:
        return 0

    # Forward direction to find max profit from first sell
    min_so_far = A[0]
    max_profit = 0
    profit_day_first_sale = []
    for i in xrange(len(A)):
        min_so_far = min(A[i], min_so_far)
        max_profit = max(max_profit, (A[i] - min_so_far))
        profit_day_first_sale.append(max_profit)

    # Traverse backward to find max profit for second sale
    # which will max of current day + previous first sale profit
    # It gives total profit of selling stock twice
    max_so_far = 0
    max_total_profit = 0
    for i in reversed(range(len(A))):
        max_so_far = max(max_so_far, A[i] - max_so_far)
        max_total_profit = max(max_total_profit, (A[i] - max_so_far + profit_day_first_sale[i-1]))

    return max_total_profit

def test_buy_sell_stock_twice():
    print "###### test_buy_sell_stock_twice starts ######"
    A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
    print "Stock Price: A"
    print A
    max_profit = buy_sell_stock_twice(A)
    print "Max Profit: %u" % (max_profit)
    print "###### test_buy_sell_stock_twice ends ######"

def test_buy_sell_stock_once():
    print "###### test_buy_sell_stock_once starts ######"
    A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
    print "Stock Price: A"
    print A
    max_profit = buy_sell_stock_once(A)
    print "Max Profit: %u" % (max_profit)
    print "###### test_buy_sell_stock_once ends ######"


def main(argv):
    test_buy_sell_stock_once()
    test_buy_sell_stock_twice()

if __name__ == '__main__':
    main(sys.argv)
