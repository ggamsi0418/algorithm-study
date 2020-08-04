'''
    [leetcode] 200. Number of Islands

    https://leetcode.com/problems/number-of-islands/
'''
from collections import deque

grid_01 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid_02 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]


class Solution:
    def numIslands(self, grid):
        dx = [0, -1, -1, -1, 0 ,1, 1, 1]
        dy = [-1, -1, 0, 1, 1, 1, 0, -1]

        if not grid:
            return 0

        w = len(grid[0])
        h = len(grid)


        queue = deque()
        check = [[False for _ in range(w)] for _ in range(h)]


        def bfs(i, j):
            check[i][j] = True
            
            while queue:
                a, b = queue.popleft()
                for v in range(8):
                    x = a + dx[v]
                    y = b + dy[v]
                    if (0<= x < h) and (0<= y < w) and (grid[x][y] =="1") and (not check[x][y]):
                        queue.append((x, y))
                        bfs(x, y)
            return

        cnt = 0

        for i in range(h):
            for j in range(w):
                if (not check[i][j]) and (grid[i][j] == "1"):
                    bfs(i, j)
                    cnt += 1

        return cnt



sol = Solution()
print(sol.numIslands(grid_01))
print(sol.numIslands(grid_02))
