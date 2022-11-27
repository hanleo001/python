class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            for i in range(len(s)):
                tlist1=[x for x in t]
                if t.find(s[i])!=-1:
                    tlist1.pop(t.find(s[i]))
                else:return False
        return True
