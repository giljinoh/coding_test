def solution(phone_book):
    phone_book.sort()
    temp = phone_book[1:]
    for i in range(len(phone_book) - 1):
        if phone_book[i] == temp[i][:len(phone_book[i])]:
            return False
        # for j in range(i+1,len(phone_book)):
        #     if phone_book[j][0] == phone_book[i][0]:
        #         if phone_book[j][:len(phone_book[i])] == phone_book[i]:
        #             return False

    answer = True
    return answer