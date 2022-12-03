    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m = len(accounts)
        ans = 0
        for i in range(m):
            sum_i = 0
            n = len(accounts[i])
            # n = accounts[i]
            for j in range(n):
                sum_i += accounts [i][j]
                if sum_i > ans:
                    ans = sum_i
        return ans

array = [[1,2,3,1],[3,2,1,4]]
maximunWealth(array)
