
import math

def fib():
    '''Yield a stream of (index, fibonacci)'''
    idx = 1
    c = 1
    n = 1
    while True:
        yield idx, c
        c, n = n, (c + n)
        idx += 1


for idx, value in fib():
    # Logarithm base 10 == # of digits
    # Alternatively: if len(str(value)) == 1000
    if math.floor(math.log(value, 10)) == 999:
        print(idx)
        break
