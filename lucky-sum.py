from operator import add, sub, mul, div

concat_numbers = lambda x, y : int(str(x) + str(y))

def find_lucky_sum(number):
    n = len(str(number))
    d = []
    operations = ((add, '+'), (sub, '-'), (mul, '*'), (div, '/'))
    for i in xrange(n):
        d.append([])
    for digit in map(int, str(number)):
        d[0].append(digit)

    for i in xrange(1, n):
        for j in xrange(n - 1):
            for operation, sign in operations:
                pass

if __name__ == '__main__':
    print find_lucky_sum(123456)
