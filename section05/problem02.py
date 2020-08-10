"""
    [프로그래머스] 네트워크

    https://programmers.co.kr/learn/courses/30/lessons/43162
"""
from collections import deque


def dfs(computers, visited, start_node):
    stack = deque()
    stack.append(start_node)
    while stack:
        current_node = stack.pop()
        if not visited[current_node]:
            visited[current_node] = True
        for around_node in range(len(computers)):
            if computers[current_node][around_node] == 1 and not visited[around_node]:
                stack.append(around_node)


def solution(n, computers):
    visited = [False for _ in range(n)]
    answer = 0
    start_node = 0
    while False in visited:
        if not visited[start_node]:
            dfs(computers, visited, start_node)
            answer += 1
        start_node += 1
    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
