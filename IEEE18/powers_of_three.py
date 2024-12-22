def powersOfThree(n: int) -> int:
    x = 0
    divisor = 27 if n > 27 else 3
    increment = 3 if divisor == 27 else 1
    while n > 1:
        if n % divisor != 0:
         return -1
        n //= divisor
        x += increment
    return x

print(powersOfThree(243))