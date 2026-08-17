from functools import cache
from itertools import accumulate

class Solution:
    def stoneGameV(self, stoneValue):
        prefix = list(accumulate(stoneValue, initial=0))

        @cache
        def dfs(l, r):
            if l >= r:
                return 0

            ans = 0
            left = 0
            right = prefix[r + 1] - prefix[l]

            for k in range(l, r):
                left += stoneValue[k]
                right -= stoneValue[k]

                if left < right:
                    # If even 2 * left cannot beat ans,
                    # this split cannot improve the answer.
                    if ans >= 2 * left:
                        continue

                    ans = max(ans, left + dfs(l, k))

                elif left > right:
                    # As k increases, right only becomes smaller,
                    # so if this cannot improve ans, later ones won't either.
                    if ans >= 2 * right:
                        break

                    ans = max(ans, right + dfs(k + 1, r))

                else:
                    ans = max(
                        ans,
                        left + dfs(l, k),
                        right + dfs(k + 1, r)
                    )

            return ans

        return dfs(0, len(stoneValue) - 1)