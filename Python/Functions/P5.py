def solution(list1):
    list2 = []
    for i in list1:
        i % 2 == 0 and list2.append(i)
    return list2


print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9]))
