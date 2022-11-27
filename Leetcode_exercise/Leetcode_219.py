class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        dic={}
        for inde,ele in enumerate(nums):
            if ele not in dic:
                dic[ele]=inde
            elif ele in dic and inde-dic[ele]<=k:
                return True
            else:
                dic[ele]=inde
        return False

a=Solution()
print(a.containsNearbyDuplicate([1,0,1,1],1))