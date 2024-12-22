# from typing import List
#
#
# def findMinArrowShots(points: List[List[int]]) -> int:
#     if len(points) == 1:
#         return 1
#
#     points.sort(key=lambda x: x[1])
#     print(points)
#
#     short_at = None
#     merged = []
#     ret = []
#     for i in range(len(points)):
#         arr = points[i]
#         if i > 0 and arr == points[i - 1]:
#             continue
#         l, r = arr
#         if not short_at:
#             short_at = r
#             merged.append(arr)
#
#         elif l <= short_at <= r:
#             merged.append(arr)
#         else:
#             short_at = r
#             ret.append(merged)
#             merged = [arr]
#
#     ret.append(merged)
#     return ret
#
# print(findMinArrowShots([[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]))

print(2|4|5)