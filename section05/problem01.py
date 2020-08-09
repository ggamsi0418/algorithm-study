"""
    [프로그래머스] 타겟 넘버

    https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3
"""
from collections import deque


def solution(numbers, target):
    answer = 0
    queue = deque([(0, 0)])

    while queue:
        current_sum, num_idx = queue.popleft()

        if num_idx == len(numbers):
            if current_sum == target:
                answer += 1
        else:
            number = numbers[num_idx]
            queue.append((current_sum + number, num_idx + 1))
            queue.append((current_sum - number, num_idx + 1))

    return answer


print(solution([1, 1, 1, 1, 1], 3))

# from itertools import product


# def solution(numbers, target):
#     l = [(x, -x) for x in numbers]
#     print(*l)
#     # print(*product(*l))
#     s = list(map(sum, product(*l)))
#     return s.count(target)

