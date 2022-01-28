


def naive_collatz_len(n):
    assert(n > 0)
    count = 1
    while n != 1:
        count += 1
        n = (n // 2) if (n % 2 == 0) else (n * 3 + 1)
    return count



cache = {}
def optimized_collatz_len(n):
    '''Memoize the computation by keeping a map of n -> chain length'''
    assert(n > 0)
    j = n
    count = 1
    while j != 1:
        if j in cache:
            total_chain_len = count + cache[j]
            cache[n] = total_chain_len
            return total_chain_len
        count += 1
        j = (j // 2) if (j % 2 == 0) else (j * 3 + 1)
    cache[n] = count
    return count




# Time difference is 2 seconds vs 20 seconds
collatz_fun = optimized_collatz_len # naive_collatz_len
max_chain_length = -1
max_seed = None
for n in range(1, 1000000):
    chain_length = collatz_fun(n)
    if chain_length > max_chain_length:
        max_chain_length = chain_length
        max_seed = n

assert(max_seed != None)
print(max_seed)
