def operation_results(a, b):
    from operator import add, sub, mul, div
    operations = ((add, '+'), (sub, '-'), (mul, '*'), (div, '/'))
    for operation, sign in  operations:
        try:
            yield (operation(a[0], b[0]), ''.join(['(', a[1], sign, b[1], ')']))
        except ZeroDivisionError:
            pass

#def filter_bad_values(a):
#    from math import modf
#    res = []
#    for i in a:
#        if modf(a[0])[0]

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
            d[j][i].append((float(number[i:i+j + 1]), number[i:i+j + 1]))

    for i in xrange(1, n):
        for j in xrange(n - i):
            for lhs in d[i - 1][j]:
                for rhs in d[0][j + i]:
                    for res in operation_results(lhs, rhs):
                        d[i][j].append(res)

            if i == 1:
                # in this case the next cycle is the same as first
                continue

            for rhs in d[i - 1][j + 1]:
                for lhs in d[0][j]:
                    for res in operation_results(lhs, rhs):
                        d[i][j].append(res)

    return len(d[-1][0])


if __name__ == '__main__':
    f = open('lol.txt', 'w')
    f.write(str(find_lucky_sum(123456)))
