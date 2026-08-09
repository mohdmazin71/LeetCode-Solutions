class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        # Suffix sum
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        dp = {}

        def solve(i, M):
            if i >= n:
                return 0

            if (i, M) in dp:
                return dp[(i, M)]

            # Current player can take all remaining stones
            best = 0

            for x in range(1, 2 * M + 1):
                if i + x > n:
                    break

                # Stones current player gets
                # = total remaining - opponent's best
                best = max(
                    best,
                    suffix[i] - solve(i + x, max(M, x))
                )

            dp[(i, M)] = best
            return best

        return solve(0, 1)