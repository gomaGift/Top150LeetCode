def to_binary(n, bits=8):
    return format((n + (1 << bits)) % (1 << bits), f'0{bits}b')

print(to_binary(-8, 11))   # 11111011
print(to_binary(-12, 11))  # 1111111111111011
print(to_binary(-20, 11))
print("11111101100")
