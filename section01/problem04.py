class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """

        m = len(mat)  # row 개수
        n = len(mat[0])  # column 개수

        dict = {}
        for key in range(m - 1, -n + 1 - 1, -1):
            dict[key] = []

        for i in range(m):
            for j in range(n):
                dict[i - j].append(mat[i][j])

        for key in dict.keys():
            dict[key].sort()

        result = [[] for row in range(m)]

        for key, value in dict.items():
            if key >= 0:
                for i, v in enumerate(value[::-1]):
                    result[m - 1 - i].append(v)
            else:
                for i, v in enumerate(value[::-1]):
                    result[m + key - i].append(v)

        return result


sol = Solution()
print(sol.diagonalSort([[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]))

