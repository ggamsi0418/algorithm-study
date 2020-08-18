"""
    [프로그래머스] 단어변환
    https://programmers.co.kr/learn/courses/30/lessons/43163

    [참고 풀이]
    https://copy-driven-dev.tistory.com/123
"""
from collections import deque


def searchDiff(a, b, n):
    ret = 0
    for i in range(n):
        if a[i] != b[i]:
            ret += 1

    if ret == 1:
        return True
    else:
        return False


def solution(begin, target, words):
    answer = 0

    v = dict()
    len_words = len(begin)
    queue = deque()
    queue.append((begin, 0))
    v[begin] = True

    while queue:
        cur, l = queue.popleft()

        for word in words:
            if searchDiff(word, cur, len_words) and word not in v:
                queue.append((word, l + 1))
                v[word] = True
                if word == target:
                    answer = l + 1

    return answer


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

print(solution(begin, target, words))
