class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)
        s = 1
        while s < n: s *= 2

        t = [([0]*k, 1%k) for _ in range(2*s)]

        def merge(a, b):
            A, p = a
            B, q = b
            C = A[:]
            for r in range(k):
                C[p*r % k] += B[r]
            return C, p*q % k

        for i, v in enumerate(nums):
            C = [0]*k
            C[v%k] = 1
            t[s+i] = (C, v%k)

        for i in range(s-1, 0, -1):
            t[i] = merge(t[2*i], t[2*i+1])

        def update(i, v):
            i += s
            C = [0]*k
            C[v%k] = 1
            t[i] = (C, v%k)

            while i > 1:
                i //= 2
                t[i] = merge(t[2*i], t[2*i+1])

        def query(l):
            left = ([0]*k, 1%k)
            right = ([0]*k, 1%k)

            l += s
            r = s + n

            while l < r:
                if l & 1:
                    left = merge(left, t[l])
                    l += 1
                if r & 1:
                    r -= 1
                    right = merge(t[r], right)

                l //= 2
                r //= 2

            return merge(left, right)[0]

        ans = []

        for i, v, start, x in queries:
            update(i, v)
            ans.append(query(start)[x])

        return ans