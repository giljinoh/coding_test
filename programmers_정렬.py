def solution(citations):
    c_num = 0
    answer = 0
    for i in range(1, max(citations)):
        for j in range(len(citations)):
            if citations[j] >= i:
                c_num += 1
        if c_num >= i:
            answer = i
            c_num = 0
        else:
            break
    # print(answer)

    return answer