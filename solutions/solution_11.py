def count_bills(s):
    denominations = [500, 100, 10, 5, 2, 1]
    bills = [0] * 6

    for i in range(len(denominations)):
        bills[i] = s // denominations[i]
        s %= denominations[i]

    return bills
