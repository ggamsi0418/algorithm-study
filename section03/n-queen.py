"""
    [백준][9663] N-Queen

    https://www.acmicpc.net/problem/9663

"""


n = int(input())
count = 0

row, left, right = (
    [False for _ in range(n)],  # 수직,왼쪽대각선,오른쪽 대각선
    [False for _ in range(2 * n - 1)],  # 인덱스의 합과 차가 같은 대각선상에 있을때 같다는 것을 이용함
    [False for _ in range(2 * n - 1)],  # ex)0,2과 1,1과 2,0은 같은 대각선 상에 위치한다. 각행열의 합이 같은것을 알수있다.
)


def solve(index):
    global count
    if index == n:  # 끝까지 퀸을 넣으면
        count += 1
        return
    for col in range(n):  # 열을 이동하며
        if not (row[col] or left[index + col] or right[n - 1 + index - col]):  # 세 조건에 걸리지 않는다면
            row[col] = left[index + col] = right[n - 1 + index - col] = True
            solve(index + 1)
            row[col] = left[index + col] = right[n - 1 + index - col] = False  # 초기화


solve(0)
print(count)


"""
// 또다른 풀이 방법

def is_available(candidate, current_col):
    current_row = len(candidate)
    for queen_row in range(current_row):
        if (
            candidate[queen_row] == current_col
            or abs(candidate[queen_row] - current_col) == current_row - queen_row
        ):
            return False
    return True


def DFS(N, current_row, current_candidate, final_result):
    if current_row == N:
        final_result.append(current_candidate[:])
        return

    for candidate_col in range(N):
        if is_available(current_candidate, candidate_col):
            current_candidate.append(candidate_col)
            DFS(N, current_row + 1, current_candidate, final_result)
            current_candidate.pop()


def solve_n_queens(N):
    final_result = []
    DFS(N, 0, [], final_result)
    return final_result


print(len(solve_n_queens(10)))
"""
