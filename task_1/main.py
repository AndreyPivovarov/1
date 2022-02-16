from itertools import cycle

def task1(n, m):
    lol = ( y for y in cycle([x for x in range(1, n + 1)]))
    count = 1
    rout = '1'
    lol.__next__()
    while True:
        count += 1
        num = lol.__next__()
        if num == 1 and count % m == 0:
            print(rout)
            return rout
        elif count == m and num != 1:
            count = 1
            rout += str(num)