from collections import deque

class Solution:
    def updateMatrix(self, mat):
        rows = len(mat)
        cols = len(mat[0])

        q = deque()
        visit = set()

        def isOne(i,j):
            if i >= 0 and i < rows and j >= 0 and j < cols and (i,j) not in visit:
                visit.add((i, j))
                q.append((i, j))

        # find zeroes first and append into queue
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    visit.add((i,j))
                    q.append((i,j))

        dist = 0
        while q:
            # perform BFS simultaneous on zeroes at the same time
            for i in range(len(q)):
                r, c = q.popleft()
                isOne(r+1,c)
                isOne(r-1,c)
                isOne(r,c+1)
                isOne(r,c-1)
                mat[r][c] = dist

            dist += 1

        return mat
