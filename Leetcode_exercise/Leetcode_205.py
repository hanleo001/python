class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dic={}
        dic2={}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]]=t[i]
                dic2[t[i]]=s[i]
            elif dic[s[i]] !=t[i] :
                return False
            elif dic2[t[i]]!=s[i]:
                return False
        return True
a=Solution()
print(a.isIsomorphic("badc","baba"))