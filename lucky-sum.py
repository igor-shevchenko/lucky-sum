# Igor Shevchenko, PS-398
def operation_results(a, b):
    from operator import add, sub, mul, div
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
            if number[i] == '0' and j > 0:
                continue
            d[j][i].append((float(number[i:i+j + 1]), number[i:i+j + 1]))

    for i in xrange(1, n):
        for j in xrange(n - i):
            for k in xrange(i):
                for lhs in d[k][j]:
                    for rhs in d[i-k-1][k+j + 1]:
                        for res in operation_results(lhs, rhs):
                            d[i][j].append(res)

    return d[-1][0]


def test(d):
    for i in d:
        for j in xrange(1, 7):
            assert(i[1].count(str(j)) == 1)

def ivanov(number):
    # function prints all alternatives of getting 1000 with the number
    # and all numbers from 0 to 999 that can be got
    from math import modf
    t = find_lucky_sum(number)
    thousands = []
    numbers = []
    for i in t:
        if modf(i[0])[0]:
            continue
        if i[0] == 1000:
            thousands.append(i[1])
        elif 0 <= i[0] < 1000:
            numbers.append(int(i[0]))
    if thousands:
        print '1000 = '
        for i in thousands:
            print i
        print ''
    print sorted(set(numbers))

if __name__ == '__main__':
    ivanov(100000)
