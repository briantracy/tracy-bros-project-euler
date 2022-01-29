
# def fact_naive(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact(n - 1)

# def fact_tail(n, acc):
#     if n == 0:
#         return acc
#     else:
#         return fact_tail(n - 1, n * acc)

# def fact(n):
#     return fact_tail(n, 1)

# HAHAHA python doesn't support Tail Call Elimination, so that was pointless

acc = 1
for n in range(100, 0, -1):
    acc *= n

# acc now holds 100!
print(sum(map(int, str(acc))))
