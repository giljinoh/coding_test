def solution(answers):
    answer = []
    a, b, c = 0, 0, 0
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if answers[i] == one[i % len(one)]:
            a += 1
        if answers[i] == two[i % len(two)]:
            b += 1
        if answers[i] == three[i % len(three)]:
            c += 1
    temp = []
    for person, cnt in zip([1, 2, 3], [a, b, c]):
        temp.append((person, cnt))
    max_num = max(a, b, c)

    for i in range(3):
        if temp[i][1] == max_num:
            answer.append(temp[i][0])

    answer.sort()
    return answer