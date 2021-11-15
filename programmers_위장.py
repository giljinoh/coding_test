def solution(clothes):
    clothes_types = set()
    clothes_num = []
    num = 0
    for i in range(len(clothes)):
        clothes_types.add(clothes[i][1])
    clothes_types = list(clothes_types)

    # for i in range(len(1,clothes_types+1)):
    #     for j in range(len(clothes)):

    for i in clothes_types:
        for j in range(len(clothes)):
            if clothes[j][1] == i:
                num += 1
        clothes_num.append(num + 1)
        num = 0

    # for i in range(len(1,clothes_types+1)):
    answer = 1
    for i in range(len(clothes_num)):
        answer *= clothes_num[i]

    # print(clothes_types)
    # print(clothes_num)

    return answer - 1