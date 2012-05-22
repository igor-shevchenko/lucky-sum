from operator import add, sub, mul, div

def operation_results(a, b):
    operations = ((add, '+'), (sub, '-'), (mul, '*'), (div, '/'))
    for operation, sign in  operations:
        try:
            yield (operation(a[0], b[0]), ''.join(['(', a[1], sign, b[1], ')']))
        except ZeroDivisionError:
            pass

def find_lucky_sum(number):
    number = str(number)
    n = len(number)
    d = []

    for i in xrange(n):
        d.append([])
        for j in xrange(n - i):
            d[i].append([])

    for i in xrange(n):
        for j in xrange(n - i):
            d[j][i].append((int(number[i:i+j + 1]), number[i:i+j + 1]))

    for i in xrange(1, n):
        for j in xrange(n - i):
            for lhs in d[i - 1][j]:
                for rhs in d[i - 1][j + 1]:
                    for res in operation_results(lhs, rhs):
                        pass#d[i][j].append(res)

    return d


if __name__ == '__main__':
    print find_lucky_sum(1234)
