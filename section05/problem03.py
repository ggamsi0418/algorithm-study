"""
    [프로그래머스] 단어변환
    https://programmers.co.kr/learn/courses/30/lessons/43163
"""
from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0

    answer = 0
    return answer


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

print(solution(begin, target, words))
