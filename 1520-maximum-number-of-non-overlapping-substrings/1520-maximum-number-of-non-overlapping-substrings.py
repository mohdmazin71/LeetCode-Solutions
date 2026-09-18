class Solution:
    def maxNumOfSubstrings(self, s):
        p = {c: [s.find(c), s.rfind(c)] for c in set(s)}
        a = []

        for l, r in p.values():
            i = l
            while i <= r:
                x, y = p[s[i]]
                if x < l:
                    break
                r = max(r, y)
                i += 1
            else:
                a.append((r, s[l:r+1]))

        a.sort()
        ans = []
        end = -1

        for r, x in a:
            if p[x[0]][0] > end:
                ans.append(x)
                end = r

        return ans