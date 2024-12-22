
accepted_dif = [1,2,3]

def is_monotonic(arr):
   increasing = all(arr[i] < arr[i+1] and abs(arr[i] - arr[i+1]) in accepted_dif for i in range(len(arr)-1))
   decreasing = all(arr[i] > arr[i+1] and abs(arr[i] - arr[i+1]) in accepted_dif for i in range(len(arr)-1))
   return increasing or decreasing



def safe_reports(levels):
    if is_monotonic(levels):
        return True

    for i in range(len(levels)):
        monotonic = is_monotonic(levels[:i] + levels[i + 1:])
        if monotonic:
              return True

    return False


safe_report_count = 0
with open('safeUnsafe.txt', 'r') as f:
    for line in f:
        safe_report_count += safe_reports([int(num) for num in line.strip().split()])


print(safe_report_count)
