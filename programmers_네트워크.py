from collections import deque


def bfs(n, computers, col, visited, idx):
    visited[col] = True
    deq = deque()
    deq.append(col)
    while 0 != len(deq):
        col = deq.popleft()
        visited[col] = True
        for idx in range(n):
            if visited[idx] == False:
                if computers[col][idx] == 1 and idx != col:
                    deq.append(idx)


def solution(n, computers):
    answer = 0
    idx = 0
    visited = [False for x in range(n)]
    for col in range(n):
        if visited[col] == False:
            bfs(n, computers, col, visited, idx)
            answer += 1
    return answer