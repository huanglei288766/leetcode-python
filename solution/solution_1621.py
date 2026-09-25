class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[2][1] = 1
        for i in range(3, n + 1):
            dp[i][1] = dp[i-1][1] + i - 1
        if k == 1:
            return dp[n][1]

        for row in range(2, n+1):
            for col in range(2, min(k, row-1) + 1):
                dp[row][col] = dp[row-1][col]
                for i in range(1, n):
                    dp[row][col] += dp[row-i][col - 1]
        return dp[n][k] % 1000000007

if __name__ == '__main__':
    sol = Solution()
    print(sol.numberOfSets(5, 3))