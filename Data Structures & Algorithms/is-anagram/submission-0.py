class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = {}
        for i in range(len(s)):
            if s[i] not in seen:
                seen[s[i]]=1
            else:
                seen[s[i]] = seen[s[i]]+1
        for i in range(len(t)):
            if t[i] not in seen:
                return False
            elif seen[t[i]] == 1:
                del seen[t[i]]
            else:
                seen[t[i]] = seen[t[i]]-1
        if len(seen) == 0:
            return True
        else:
            return False
        