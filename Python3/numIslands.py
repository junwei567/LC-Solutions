from collections import deque

class Solution:
    # Time: O(n*m)
    # Space: O(n*m)
    def numIslands(self, grid):
        visited = set()
        res = 0

        def bfs(i, j):
            q = deque()
            q.append((i,j))
            visited.add((i,j))

            while q:
                r, c = q.popleft()
                directions = [(-1,0), (1,0), (0,-1), (0,1)]
                for x, y in directions:
                    row, col = r+x, c+y
                    # check if row, col is within bounds
                    if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]) and grid[row][col] == "1" and (row, col) not in visited:
                        q.append((row, col))
                        visited.add((row, col))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    bfs(i, j)
                    res += 1

        return res
                     
