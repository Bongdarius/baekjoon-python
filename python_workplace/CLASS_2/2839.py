weight = int(input())
# weight = 19
list = []
for i in range(-1, weight // 5, 1):
    for j in range(-1, weight // 3, 1):
        if(((i+1) * 5 + (j+1) * 3) == weight):
            list.append([i+1, j+1])

if(len(list) == 0):
    print(-1)
else:
    resultList = list[len(list) - 1]
    result = resultList[0] + resultList[1]
    print(result)

# 챗지피티 정답
# def find_min_bags(weight):
#     for bags_5kg in range(weight // 5, -1, -1):
#         remaining_weight = weight - bags_5kg * 5
#         if remaining_weight % 3 == 0:
#             return bags_5kg + remaining_weight // 3
#     return -1
# weight = int(input())
# print(find_min_bags(weight))
