def sum_range(nums, i, j):
    prefix_sum = []

    for num in nums:
        if not prefix_sum:
            prefix_sum.append(num)
        else:
            prefix_sum.append(prefix_sum[-1] + num)

    if i == 0:
        return prefix_sum[j]
    else:
        return prefix_sum[j] - prefix_sum[i-1]



