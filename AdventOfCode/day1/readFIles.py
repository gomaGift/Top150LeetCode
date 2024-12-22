def readFiles(file1, file2):

    with open(file1, 'r') as file:
        list1 = [int(num) for line in file for num in line.strip().split()]

    # Read data from the second file
    with open(file2, 'r') as file:
        list2 = [int(num) for line in file for num in line.strip().split()]

    return list1, list2