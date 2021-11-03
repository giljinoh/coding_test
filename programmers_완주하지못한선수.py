def solution(participant, completion):
    participant.sort()
    completion.sort()

    for x in range(len(completion)):
        if participant[x] != completion[x]:
            answer = participant[x]
            return answer
    answer = participant[-1]
    return answer