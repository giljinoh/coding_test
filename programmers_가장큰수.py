def solution(numbers):
    temp = numbers
    for i in range(len(numbers)):
        temp[i] = str(temp[i]) * 3

    temp.sort(reverse=True)
    for i in range(len(temp)):
        # print(len(temp[i]))
        if len(temp[i]) == 3:
            temp[i] = temp[i][0:1]
        elif len(temp[i]) == 6:
            temp[i] = temp[i][0:2]
        elif len(temp[i]) == 9:
            temp[i] = temp[i][0:3]
        elif len(temp[i]) == 12:
            temp[i] = temp[i][0:4]
    # numbers = str(numbers)
    # print(temp)
    answer = ''
    for i in range(len(temp)):
        answer += temp[i]
    if answer[0] == "0":
        answer = "0"
    # print(answer)

    return answer