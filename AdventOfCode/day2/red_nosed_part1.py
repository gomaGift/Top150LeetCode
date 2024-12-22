from AdventOfCode.day2.part2 import is_monotonic



with open("safeUnsafe.txt", 'r') as file:
    safe_reports = 0
    for line in file:
      values = [int(num) for num in line.strip().split()]
      safe_reports += is_monotonic(values)


print(safe_reports)


