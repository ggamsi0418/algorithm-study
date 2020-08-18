"""
    [프로그래머스] 여행경로
    https://programmers.co.kr/learn/courses/30/lessons/43164

    [참고 풀이]
    https://jisun-rea.tistory.com/entry/python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Level3-%EC%97%AC%ED%96%89%EA%B2%BD%EB%A1%9C-DFS
"""


def solution(tickets):
    tickets.sort(reverse=True)
    routes = dict()
    for t1, t2 in tickets:
        if t1 in routes:
            routes[t1].append(t2)
        else:
            routes[t1] = [t2]

    st = ["ICN"]
    ans = []

    while st:
        top = st[-1]
        if top not in routes or len(routes[top]) == 0:
            ans.append(st.pop())
        else:
            st.append(routes[top].pop())
    ans.reverse()
    return ans


tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

print(solution(tickets))
