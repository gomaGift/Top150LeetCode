def bitwise_or(a: list[int]) -> list[int]:
    ans = {0}
    bitwise_value = a[0]

    for i in range(1, len(a)):
        if a[i] > a[i - 1]:
            bitwise_value |= a[i]
        else:
            ans.add(bitwise_value)
            bitwise_value = a[i]
        ans.add(a[i])

    return sorted(ans)

# Example usage
print(bitwise_or([4, 2, 4, 5, 1]))  # Expected output: [0, 1, 2, 4, 6]
