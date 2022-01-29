

def naturals():
    n = 1
    while True:
        yield n
        n += 1

of_interest = set([10 ** j for j in range(7)])

idx = 1
product = 1
for n in naturals():
    for digit in map(int, str(n)):
        if idx in of_interest:
            product *= digit
            of_interest.remove(idx)
        idx += 1
    if len(of_interest) == 0:
        break

print(product)
