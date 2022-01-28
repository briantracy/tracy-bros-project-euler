
'''
Sum of first n natural numbers famously has a closed form:
    [n(n+1)]/2

Sum of squares of first n natural numbers also has a lesser known closed form:
    [n(n+1)(2n+1)]/6

'''

def sum_natural(n):
    return (n * (n + 1)) // 2

def sum_squares_natural(n):
    return (n * (n + 1) * (2*n + 1)) // 6

print((sum_natural(100) * sum_natural(100)) - sum_squares_natural(100))
