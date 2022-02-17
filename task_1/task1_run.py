from itertools import cycle
import argparse


def cli_parser():
    parser = argparse.ArgumentParser(description='Task1')
    parser.add_argument('n', help='n')
    parser.add_argument('m', help='m')
    return parser.parse_args()


def task1(n, m):
    lol = (y for y in cycle([x for x in range(1, n + 1)]))
    count = 1
    rout = '1'
    lol.__next__()
    while True:
        count += 1
        num = lol.__next__()
        if num == 1 and count % m == 0:
            return rout
        elif count == m and num != 1:
            count = 1
            rout += str(num)


def main():
    namespace = cli_parser()
    result = task1(int(namespace.n), int(namespace.m))
    print(result)


if __name__ == '__main__':
    main()
