import heapq

from AdventOfCode.day1.readFIles import readFiles


def totalDistance(list1, list2):
    """
    Calculate the total distance by finding the absolute difference between the smallest elements
    from two min heaps until the heaps are empty.
    """
    heapq.heapify(list1)
    heapq.heapify(list2)

    total = 0

    # Ensure both heaps are non-empty before popping
    while list1 and list2:
        num1 = heapq.heappop(list1)
        num2 = heapq.heappop(list2)
        total += abs(num1 - num2)

    return total

# Initialize lists


# Read data from the first file
list1, list2 = readFiles("nums.txt", "nums2.txt")

# Ensure lists are non-empty before processing
total = totalDistance(list1, list2)
print("Total Distance:", total)
