class Solution:
    def wordPattern(self, pattern, s):
        words = s.split()

        if len(pattern) != len(words):
            return False

        m1 = {}
        m2 = {}

        for i in range(len(pattern)):
            if pattern[i] in m1:
                if m1[pattern[i]] != words[i]:
                    return False
            else:
                m1[pattern[i]] = words[i]

            if words[i] in m2:
                if m2[words[i]] != pattern[i]:
                    return False
            else:
                m2[words[i]] = pattern[i]

        return True