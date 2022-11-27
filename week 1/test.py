if 1:
    def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        import math
        xx=[]
        if x<0:
            return False
        while math.floor(x/10)!=1:
            xx+=[str(x%10)]
            x=(x-10*(x%10))/10
        yy=xx
        xx.reverse()
        print(yy)
        return xx==yy
x=int(input())
print(isPalindrome(x))