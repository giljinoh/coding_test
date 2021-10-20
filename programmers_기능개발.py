def solution(progresses, speeds):
    answer = []
    task = 0
    while len(speeds) != 0:
        # print(progresses)
        for i in range(len(progresses)):
            if progresses[0] >= 100:
                task += 1
                progresses.remove(progresses[0])
                speeds.remove(speeds[0])
            else:
                for j in range(len(progresses)):
                    progresses[j] += speeds[j]
                break

        if task != 0:
            print(task)
            answer.append(task)
            task = 0

    return answer