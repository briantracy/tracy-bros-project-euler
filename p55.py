

def is_palindrome(n):
    nstr = str(n)
    for i in range(len(nstr)):
        if nstr[i] != nstr[len(nstr) - (i + 1)]:
            return False
    return True

assert(is_palindrome(1))
assert(is_palindrome(121))
assert(is_palindrome(123321))
assert(not is_palindrome(10))
assert(is_palindrome(101101))
assert(not is_palindrome(12345321))

def is_lychrel(n):
    for _ in range(50):
        j = n + int(str(n)[::-1])
        if is_palindrome(j):
            return False
        n = j
    return True

assert(not is_lychrel(47))
assert(not is_lychrel(349))
assert(is_lychrel(196))

count = 0
for n in range(1, 10000):
    if is_lychrel(n):
        count += 1

print(count)