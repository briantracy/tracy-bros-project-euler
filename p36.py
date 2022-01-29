
def is_palindrome(text):
    for i in range(len(text) // 2):
        if text[i] != text[len(text) - (i + 1)]:
            return False
    return True

assert(is_palindrome('1'))
assert(is_palindrome('12321'))
assert(is_palindrome('101101'))
assert(is_palindrome('1221'))
assert(is_palindrome('abcfgggfcba'))
assert(not is_palindrome('123'))
assert(not is_palindrome('10100'))

total = 0
for i in range(1000000):
    if is_palindrome(str(i)) and is_palindrome(format(i, 'b')):
        total += i

print(total)