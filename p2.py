

def fib():
    c = 1
    n = 2
    while True:
        yield c
        c, n = n, (c + n)

total = 0
for n in filter(lambda n: n % 2 == 0, fib()):
    if n > 4000000:
        break
    total += n

print(total)
