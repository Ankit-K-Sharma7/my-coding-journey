from math import isqrt
def factors(value):
    prime_factors = []
    num = 2
    while isqrt(value) >= num:
        while value % num == 0:
            prime_factors.append(num)
            value //= num
        num += 1
    if value > 1:
        prime_factors.append(value)
    return prime_factors