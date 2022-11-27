class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n!=1:
            if n<1:
                break
            n=n/2
        else:return True
        return False
