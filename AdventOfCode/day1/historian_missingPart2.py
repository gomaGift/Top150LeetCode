from AdventOfCode.day1.readFIles import readFiles


def similarity_score(list1, list2):
    total_similarity_score = 0

    for num in list1:

        total_similarity_score += num * list2.count(num)


    return total_similarity_score



lst1, lst2 = readFiles("nums.txt", "nums2.txt")
print(similarity_score(lst1, lst2))