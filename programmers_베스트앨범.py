def solution(genres, plays):
    my_list = []
    num_list = [i for i in range(len(genres))]
    for temp in zip(genres, plays, num_list):
        my_list.append(temp)

    genres_set = set(genres)
    genres_num = len(genres_set)
    num = 0
    play_list = []
    for i in genres_set:
        for j in range(len(genres)):
            if i == genres[j]:
                num += plays[j]
        play_list.append(num)
        num = 0

    final_list = []
    for temp in zip(genres_set, play_list):
        final_list.append(temp)

    final_list.sort(key=lambda x: -x[1])
    list_list = []
    for k in range(len(final_list)):
        temp_list = []
        for i in range(len(genres)):
            if final_list[k][0] == my_list[i][0]:
                temp_list.append((my_list[i][1], my_list[i][2]))

        temp_list.sort(key=lambda x: -x[0])
        # print(temp_list)
        if len(temp_list) == 1:
            list_list.append(temp_list[0][1])
        elif len(temp_list) > 1:
            list_list.append(temp_list[0][1])
            list_list.append(temp_list[1][1])

    # print(list_list)
    answer = list_list
    return answer