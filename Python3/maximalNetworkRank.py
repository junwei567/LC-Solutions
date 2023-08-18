class Solution:
    def maximalNetworkRank(self, n, roads):
        networks = {i: set() for i in range(n)}
        res = 0

        for road1, road2 in roads:
            networks[road1].add(road2)
            networks[road2].add(road1)

        for i in range(n-1):
            for j in range(i+1, n):
                res = max(res, len(networks[i]) + len(networks[j]) - (j in networks[i]))

        return res