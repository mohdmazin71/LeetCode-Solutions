class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:

        n = len(s)

        tree = [0] * (4 * n)
        pref = [0] * (4 * n)
        suff = [0] * (4 * n)

        left_char = [''] * (4 * n)
        right_char = [''] * (4 * n)

        length = [0] * (4 * n)

        def merge(node):
            l = node * 2
            r = node * 2 + 1

            left_char[node] = left_char[l]
            right_char[node] = right_char[r]

            pref[node] = pref[l]
            suff[node] = suff[r]

            tree[node] = max(tree[l], tree[r])

            # IMPORTANT: suffix of left + prefix of right
            if right_char[l] == left_char[r]:

                tree[node] = max(
                    tree[node],
                    suff[l] + pref[r]
                )

                if pref[l] == length[l]:
                    pref[node] = length[l] + pref[r]

                if suff[r] == length[r]:
                    suff[node] = suff[l] + length[r]

        def build(node, start, end):

            length[node] = end - start + 1

            if start == end:
                tree[node] = 1
                pref[node] = 1
                suff[node] = 1

                left_char[node] = s[start]
                right_char[node] = s[start]

                return

            mid = (start + end) // 2

            build(node * 2, start, mid)
            build(node * 2 + 1, mid + 1, end)

            merge(node)

        def update(node, start, end, idx, ch):

            if start == end:
                tree[node] = 1
                pref[node] = 1
                suff[node] = 1

                left_char[node] = ch
                right_char[node] = ch

                return

            mid = (start + end) // 2

            if idx <= mid:
                update(node * 2, start, mid, idx, ch)
            else:
                update(node * 2 + 1, mid + 1, end, idx, ch)

            merge(node)

        build(1, 0, n - 1)

        ans = []

        for i in range(len(queryCharacters)):

            idx = queryIndices[i]
            ch = queryCharacters[i]

            update(1, 0, n - 1, idx, ch)

            ans.append(tree[1])

        return ans