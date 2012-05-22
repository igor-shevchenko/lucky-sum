from operator import add, sub, mul, div

def operation_results(a, b):
    concat_numbers = lambda x, y : int(str(x) + str(y))
    operations = ((add, '+'), (sub, '-'), (mul, '*'), (div, '/'), (concat_numbers, ''))
    for operation, sign in  operations:
        yield (operation(a[0], b[0]), ''.join(['(', a[1], sign, b[1], ')']))

def find_lucky_sum(number):
    n = len(str(number))
    d = []

    for i in xrange(n):
        d.append([])
    for digit in map(int, str(number)):
        d[0].append([])
        d[0][-1].append((digit, str(digit)))

    for i in xrange(1, n):
        for j in xrange(n - i):
            d[i].append([])

    return d


if __name__ == '__main__':
    for lol, lolo in operation_results((12, '12'), (2, '2')):
        print lol, lolo
    print find_lucky_sum(123456)
