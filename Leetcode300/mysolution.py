import functools
import collections
import math
class Solution:
    def isHappy(self, n: int) -> bool:
        def assi(x):
            a=[int(item)**2 for item in str(x)]
            return sum(a)
        res=set()
        a=assi(n)
        while a!=1 and a not in res:
            res.add(a)
            a=assi(a)
        if a==1:
            return True
        else:return False

    def countPrimes(self, n: int) -> int:
        def isprime(x):
            if x==2:
                return True
            elif x%2==0:
                return False
            else:
                for i in range(3, int(x**0.5)+1, 2):
                    if x%i==0:
                        return False
                return True
        p=0
        for i in range(2,n):
            if isprime(i):
                p+=1
        return p
    
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dic={}
        dic2={}
        for i in range(len(s)):
            if s[i] not in dic :
                dic[s[i]]=t[i]
            elif dic[s[i]]!=t[i] :
                return False
        for i in range(len(s)):
            if t[i] not in dic2:
                dic2[t[i]]=s[i]
            elif dic2[t[i]]!=s[i]:
                return False
        return True

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

    def isAnagram(self, s: str, t: str) -> bool:
        dic_s={}
        dic_t={}
        for i in s:
            if i not in dic_s:
                dic_s[i]=1
            else:
                dic_s[i]+=1
        for j in t:
            if j not in dic_t:
                dic_t[j]=1
            else:
                dic_t[j]+=1
        return dic_s==dic_t

    def addDigits(self, num: int) -> int:
        n=num
        n=str(n)
        n=[int(n[i]) for i in range(len(n))]
        while len(n)>1:
            a=n.pop()
            b=n.pop()
            if a+b>=10:
                n.append((a+b)%10)
                n.append((a+b)//10)
            else:n.append(a+b)
        return n[0]

    def isUgly(self, n: int) -> bool:
        def isU(n):
            if n<=0:
                return False
            if n==1:
                return True
            elif n%2==0:
                return isU(n//2)
            elif n%3==0:
                return isU(n//3)
            elif n%5==0:
                return isU(n//5)
            else:return False
        return isU(n)
    

    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)

    def wordPattern(self, pattern: str, s: str) -> bool:
        dicp={}
        dics={}
        lis=s.split()
        if len(pattern)!=len(lis):
            return False
        for i,letter in enumerate(pattern):
            if letter not in dicp:
                dicp[letter]=lis[i]
            else:
                if dicp[letter]!=lis[i]:
                    return False
            if lis[i] not in dics:
                dics[lis[i]]=letter
            else : 
                if dics[lis[i]]!=letter:
                    return False
        return True

    def canWinNim(self, n: int) -> bool:
        return False if n%4==0 else True

    def isPowerOfThree(self, n: int) -> bool:
        i=0
        while 3**i<n:
            i+=1
        return True if 3**i==n else False

    def isPowerOfFour(self, n: int) -> bool:
        i=0
        while 4**i<n:
            i+=1
        return True if 4**i==n else False

    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        return s[::-1]
    def reverseVowels(self, s: str) -> str:
        aeiou='aeiouAEIOU'
        res=list(s)
        yuan=[]
        inde=[]
        for i,item in enumerate(res):
            if item in aeiou:
                inde.append(i)
                yuan.append(item)
        yuan=yuan[::-1]
        for i,ind in enumerate(inde):
            res[ind]=yuan[i]
        return "".join(res)

    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        a,b=set(nums1),set(nums2)
        return list(a&b)

    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res=[]
        for item in nums1:
            if item in nums2:
                res.append(item)
                nums2.remove(item)
        return res
        
    def firstUniqChar(self, s: str) -> int:
        item={}
        res=[]
        for i,letter in enumerate(s):
            if letter not in item: 
                item[letter]=i
                res.append(i)
            elif item[letter] in res:
                res.remove(item[letter])
        if len(res)<1:
            return -1
        else:
            return res[0]
    def findTheDifference(self, s: str, t: str) -> str:
        res=list(t)
        for i in s:
            res.remove(i)
        return res[0]
    def findNthDigit(self, n: int) -> int:
        k=0
        i=0
        while 1 :
            k+=1
            for p in str(k):
                i+=1
                if i ==n:
                    return int(p)

    def longestPalindrome(self, s: str) -> int:
        dicletter={}
        for i in s:
            if i in dicletter:
                dicletter[i]+=1
            else:
                dicletter[i]=1
        res=0
        p=0
        for key in dicletter:
            if dicletter[key]%2==1:
                p=1
            res+=dicletter[key]//2
        return res*2+p
    def thirdMax(self, nums: list[int]) -> int:
        nums=list(set(nums))
        nums.sort()
        if len(nums)<3:
            return nums.pop()
        else:
            return nums.pop(-3)
    def countSegments(self, s: str) -> int:
        a=s.split()
        return len(a)
    def findAnagrams(self, s: str, p: str) -> list[int]:
        def str_to_dic(s):
            res={}
            for i in s :
                if i in res:
                    res[i]+=1
                else:
                    res[i]=1
            return res
        pp=str_to_dic(p)
        pset=set(p)
        res=[]
        for i in range(len(s)-len(p)+1) :
            if set(s[i:i+len(p)])==pset:
                if str_to_dic(s[i:i+len(p)])==pp:
                    res.append(i)
        return res

    def arrangeCoins(self, n: int) -> int:
        p=1
        while p*(p+1)*0.5<=n:
            p+=1
        return p-1

    def compress(self, chars: list[str]) -> int:
        s=[]
        for i,letter in enumerate(chars):
            if i==0:
                s.append(letter)
            if letter in s[-1]:
                s[-1]=s[-1]+letter
            else: s.append(letter)
        chars.clear()
        for i in s:
            if len(i)>1:
                chars.append(i[0])
                for i in str(len(i)):
                    chars.append(i)
            else:
                chars.append(i)
        return chars
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        res=[]
        a=set(nums)
        for i in range(1,len(nums)+1):
            if i not in a:
                res.append(i)
        return res
    def minMoves(self, nums: list[int]) -> int:
        res=0
        nums.sort()
        for i in nums:
            res+=i-nums[0]
        return res
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        res=0
        g.sort()
        s.sort()
        j=0
        for i in s:
            if g[j]<=i:
                res+=1
                j+=1
        return res
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(0,len(s)):
            if s[0:i+1]==s[i+1:2*(i+1)]:
                a=s[0:i+1]*(len(s)//len(s[0:i+1]))
                if a==s:
                    return True  
        return False

    def hammingDistance(self, x: int, y: int) -> int:
        p=0
        bx=bin(x)[2:]
        by=bin(y)[2:]
        bx="0"*(32-len(bx))+bx
        by="0"*(32-len(by))+by
        for i,letter in enumerate(bx):
            if by[i]!=letter:
                p+=1
        return p
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        r=0
        for i in houses:
            pass
    def findComplement(self, num: int) -> int:
        a=bin(num)[2:][::-1]
        p=0
        k=0
        for i in a:
            if i=="0":
                p+=2**k
            k+=1
        return p
    def largestPalindrome(self, n: int) -> int:
        if n==1:
            return 9
        high=10**n-1
        for left in range(high,high//10,-1):
            p,x=left,left
            p=int(str(p)+str(x)[::-1])
            x=high
            while x*x>=p:
                if p%x==0:
                    return p%1337
                x-=1 
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        a="".join(s.split("-"))
        a=a.upper()
        if len(a)%k==0:
            return "-".join([a[k*i:(1+i)*k] for i in range(len(a)//k)])
        else:
            firstitem=a[0:(len(a)%k)]
    # def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
    #     start=0
    #     first=0
    #     if len(nums)==1:
    #         if nums[0]==1:
    #             return 1
    #         else:
    #             return 0
    #     while start <len(nums)-1:
    #         while start<len(nums) and nums[start]!=1:
    #             start+=1
    #         end=start+1
    #         while end<=(len(nums)-1) and nums[end]==1:
    #             end+=1
    #         if (end-start)>first:
    #             first=end-start
    #         start=end
    #     return first
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        if 1 not in nums:
            return 0
        nums=[str(i) for i in nums]
        a="".join(nums).split("0")
        a=sorted(a,key=len)
        return len(a[-1])
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_len=temp_len=0
        for i in nums:
            if i==1:
                temp_len+=1
            else:
                max_len=max(max_len,temp_len)
                temp_len=0
        max_len=max(max_len,temp_len)
        return max_len
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        def find_larger(tem_index,nums):
            a=tem_index+1
            while a<len(nums):
                if nums[tem_index]<nums[a]:
                    return nums[a]
                a+=1
            return -1
        res=[]
        for i in nums1:
            res.append(find_larger(nums2.index(i),nums2))
        return res
    def checkPerfectNumber(self, num: int) -> bool:
        if num==1:
            return False
        temp=[1]
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                temp.append(i)
                temp.append(num//i)
        return True if sum(temp)==num else False
    def maximumProduct(self, nums: list[int]) -> int:
        from itertools import combinations
        a=combinations(nums,3)
        maxtemp=float("-inf")
        for i in a:
            p=1
            for j in i:
                p*=j
            maxtemp=max(maxtemp,p)            
        return maxtemp

    def issquare(self,x):
        for i in range(1,int(x**0.5)+1):
            if x==i*i:
                return True
        return False
    def judgeSquareSum(self, c: int) -> bool:
        if c==0:
            return True
        a=0
        while a*a<=(c/2):
            if self.issquare(c-a*a):
                return True
            a+=1
        return False
            
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        index=1
        if n==1:
            return min(a,b)%(10**9+7)
        else:
            temp=min(a,b)
            while 1:
                if index==n:
                    return temp%(10**9+7)
                else:
                    temp+=1
                    if temp%a==0 or temp%b==0:
                        index+=1
    def alldivided(self,x,lis):
        for i in lis:
            if i%x!=0:
                return False
        return True
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        dic={}
        for i in deck:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        lis=[dic[key] for key in dic]
        a=min(lis)
        if a==1:
            return False
        for i in range(2,a+1):
            if self.alldivided(i, lis):
                return True
        return False
    def reverse(self, x: int) -> int:
        if x==0:
            return 0
        elif x>0:
            x=int(str(x)[::-1])
            return x if x<=2**31-1 else 0
        else:
            return -self.reverse(-x) if x>=-2**31 else 0
    def isPalindrome(self, x: int) -> bool:
        xx=[]
        if x<0:
            return False
        else:
            str_x=str(x)
        l=len(str_x)
        ll=str_x[-1]
        for i in range(1,l):
            ll=ll+str_x[l-i-1]
        if ll==str_x:
            return True
        else:return False

    def intToRoman(self, num: int) -> str:
        if num>=1000:
            return "M"+self.intToRoman(num-1000)
        if num>=900:
            return "CM"+self.intToRoman(num-900)
        if num>=500:
            return "D"+self.intToRoman(num-500)
        if num>=400:
            return "CD"+self.intToRoman(num-400)
        if num>=100:
            return "C"+self.intToRoman(num-100)
        if num>=90:
            return "XC"+self.intToRoman(num-90)
        if num>=50:
            return "L"+self.intToRoman(num-50)
        if num>=40:
            return "XL"+self.intToRoman(num-40)
        if num>=10:
            return "X"+self.intToRoman(num-10)
        if num==9:
            return "IX"
        if num>=5:
            return "V"+self.intToRoman(num-5)
        if num==4:
            return "IV"
        if num>=2:
            return "I"+self.intToRoman(num-1)
        if num>=1:
            return "I"
        if num==0:
            return ""
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs=sorted(strs,key=len)
        max=len(strs[0])
        p=0
        while p<max:
            for i in range(len(strs)-1):
                if strs[i][p]!=strs[i+1][p]:
                    return strs[0][0:p]
            p+=1
        return strs[0][0:p]
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1,-1]
        p=0
        while nums[p]!=target:
            p+=1
            if p==len(nums):
                return [-1,-1]
        q=len(nums)-1
        while nums[q]!=target:
            q-=1
        return [p,q]
    def searchInsert(self, nums: list[int], target: int) -> int:
        p=0
        while nums[p]<target:
            p+=1
            if p==len(nums):
                return p
        return p
    def myPow(self, x: float, n: int) -> float:
        result=1
        if n>=0:
            for i in range(n):
                result*=x
            return result
        if n<0:
            for i in range(-n):
                result/=x
            return result
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        row=len(obstacleGrid)
        coloum=len(obstacleGrid[0])
        for k in range(row):
            if k==0:
                methodsi=[1]*coloum
                for i in range(coloum):
                    if obstacleGrid[0][i]==1:
                        methodsi[i]=0
                    elif i==0:
                        continue
                    else:
                        methodsi[i]=methodsi[i-1]
            else:
                methodsi=[1]*coloum
                for i in range(coloum):
                    if obstacleGrid[k][i]==1:
                        methodsi[i]=0
                        continue
                    if i==0:
                        methodsi[i]=methodsi_past[i]
                    else:
                        methodsi[i]=methodsi[i-1]+methodsi_past[i]
            methodsi_past=methodsi
        return methodsi_past[-1]
    def minPathSum(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        minpath=[0 for i in range(n)]
        for k in range(m):
            for i in range(n):
                if k==0:
                    if i==0:
                        minpath[0]=grid[0][0]
                    else:
                        minpath[i]=grid[0][i]+minpath[i-1]
                else:
                    if i==0:
                        minpath[0]=minpathlast[0]+grid[k][0]
                    else:
                        minpath[i]=min(minpathlast[i],minpath[i-1])+grid[k][i]
            minpathlast=minpath
            minpath=[0 for i in range(n)]
        return minpathlast[-1]
    def plusOne(self, digits: list[int]) -> list[int]:
        k=len(digits)-1
        while digits[k]==9 and k>=0:
            k-=1
        if k==-1:
            return [1]+[0]*len(digits)
        else:
            digits[k]+=1
            digits=digits[0:k+1]+[0]*(len(digits)-(k+1))
        return digits
    def addBinary(self, a: str, b: str) -> str:
        return '{0:b}'.format(int(a, 2) + int(b, 2))
    def mySqrt(self, x: int) -> int:
        p=0
        while p*p<=x:
            p+=1
        return p-1
    def climbStairs(self, n: int) -> int:
        res=[0]*n
        for i in range(n):
            if i==0 :
                res[i]=1
            elif i==1:
                res[i]=2
            else:
                res[i]=res[i-1]+res[i-2]
        return res[-1]
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m+i]=nums2[i]
        nums1.sort()
    def maxProfit(self, prices: list[int]) -> int:
        minprice=int(1e5)
        maxprofit=0
        for price in prices:
            maxprofit=max(maxprofit,price-minprice)
            minprice=min(price,minprice)
        return maxprofit
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        p=[]
        for i in s:
            if (i>="a" and i<="z") or (i>="0" and i<="9"):
                p.append(i)
        s="".join(p)
        if s==s[::-1]:
            return True
        return False
    def singleNumber(self, nums: list[int]) -> int:
        p=set()
        for i in nums:
            if i not in p:
                p.add(i)
            else:
                p.remove(i)
        for i in p:
            return i
    def singleNumber2(self, nums: list[int]) -> int:
        return functools.reduce(lambda x,y:x^y, nums)
    def singleNumber(self, nums: list[int]) -> int:
        res={}
        for i in nums:
            if i not in res:
                res[i]=1
            elif res[i]==1:
                res[i]+=1
            else:
                res.pop(i)
        for i in res:
            return i
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        right=set(numbers)
        p=numbers.copy()
        for i,item in enumerate(numbers):
            p[i]=-2000
            if target-item in right:
                return i+1,p.index(target-item)+1
    def twoSum2(self, numbers: list[int], target: int) -> list[int]:
        little=0
        large=len(numbers)-1
        sum=numbers[little]+numbers[large]
        while (sum)!=target:
            if sum>target:
                large-=1
            else:
                little+=1
            sum=numbers[little]+numbers[large]
        return little+1,large+1
    def majorityElement(self, nums: list[int]) -> int:
        n=len(nums)
        a=collections.Counter(nums)
        return a.most_common(1)[0][0]
    def suma(self,n):
        return (n*(n+1))//2
    def trailingZeroes(self, n: int) -> int:
        num5=int(math.log(n,5))
        num2=int(math.log(n,2))
        return min(self.suma(num2),self.suma(num5))
    def trailingZeroes(self, n: int) -> int:
        if n==0:
            return 0
        p=1
        for i in range(1,n+1):
            p*=i
        p=str(p)[::-1]
        count=0
        while p[count]=="0":
            count+=1
        return count
    def trailingZeroes2(self, n: int) -> int:
        count=0
        for i in range(5,n+1,5):
            ii=i
            while ii%5==0:
                ii//=5
                count+=1
        return count
    def rotateone(self,nums):
        nums2=nums.copy()
        end=nums2.pop()
        for i,item in enumerate(nums2):
            nums[i+1]=item
        nums[0]=end
        return        
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            self.rotateone(nums)
        return
    def rotate2(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if (k:=(k%(a:=len(nums)))):
            nums[k:],nums[:k]=nums[:a-k],nums[a-k:]
    def reverseBits(self, n: int) -> int:
        n=bin(n)[2:]
        n=n[::-1]+"0"*(32-len(n))
        return int(n,2)
    def hammingWeight(self, n: int) -> int:
        a=bin(n)
        return a.count("1")
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        cost=iter(cost)
        laststep=next(cost)
        step=next(cost)
        for i in cost:
            step,laststep=min(step,laststep)+i,step
        return min(step,laststep)
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        ans=[[0]*len(matrix) for i in range(len(matrix[0]))]
        for i,item in enumerate(matrix):
            for k,ktem in enumerate(item):
                ans[k][i]=ktem
        return ans
    def binaryGap(self, n: int) -> int:
        n=bin(n)
        i=2
        j=i+1
        large=0
        while j<len(n):
            if n[j]!="1":
                j+=1
            else:
                large=max(large,j-i)
                i,j=j,j+1
        return large
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1=collections.Counter(s1.split())
        s2=collections.Counter(s2.split())
        res=[]
        for item in s1:
            if s1[item]==1 and s2[item]==0:
                res.append(item)
        for item in s2:
            if s2[item]==1 and s1[item]==0:
                res.append(item)
        return res
    def preswap(self,larges,smalls):
        large=sum(larges)
        small=sum(smalls)
        diff=(large-small)//2
        larges=set(larges)
        for i in smalls:
            if i+diff in larges:
                return [i+diff,i]
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        return self.preswap(aliceSizes,bobSizes)
    def trueva(self,a,b):
        if a==b:
            return 0
        elif a>b:
            return -1
        else:return 1
    def isMonotonic(self, nums: List[int]) -> bool:
        value=0
        for i in range(len(nums)-1):
            a=self.trueva(nums[i],nums[i+1])
            if value==0:
                if a==0:
                    continue
                elif a==1:
                    value=1
                else:
                    value=-1
            if a*value==-1:
                return False
        return True
    def encode(self,word):
        res=[0]*52
        for inde,i in enumerate(word):
            if inde%2==0:
                res[ord(i)-ord("a")]+=1
            else:
                res[ord(i)-ord("a")+26]+=1
        return res
    def numSpecialEquivGroups(self, words: list[str]) -> int:
        allitem=[]
        for i in words:
            if (value:=self.encode(i)) not in allitem:
                allitem.append(value)
        return len(allitem)
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res=[]
        for i in nums:
            if i%2==0:
                res=[i]+res
            else:
                res.append(i)
        return res
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        diff=max(nums)-min(nums)
        if diff>=2*k:
            return diff-2*k
        else:
            return 0
    def alldivided(self,x,lis):
        for i in lis:
            if i%x!=0:
                return False
        return True
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        dic={}
        for i in deck:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        lis=[dic[key] for key in dic]
        a=min(lis)
        if a==1:
            return False
        for i in range(2,a+1):
            if self.alldivided(i, lis):
                return True
        return False
    def isletter(self,letter):
        a=ord(letter)
        if (a>=65 and a<=90) or (a>=97 and a<=122):
            return True
        else:
            return False
    def reverseOnlyLetters(self, s: str) -> str:
        temp=[]
        for i in s:
            if self.isletter(i):
                temp.append(i)
        lis=iter(temp[::-1])
        res=[]
        for i in s:
            if self.isletter(i):
                res.append(next(lis))
            else:
                res.append(i)
        return "".join(res)
    def minAddToMakeValid(self, s: str) -> int:
        temp=0
        ans=0
        for i in s:
            if i=="(":
                temp+=1
            elif i==")" and temp>0:
                temp-=1
            else:
                ans+=1
        return temp+ans
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)
        odd=0
        even=0
        for item in nums:
            if  item%2==0:
                res[even*2]=item
                even+=1
            else:
                res[odd*2+1]=item
                odd+=1
        return res
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i,j=0,0
        ln,lt=len(name),len(typed)
        while j<lt:
            if i<ln and j<lt and name[i]==typed[j]:
                i+=1
                j+=1
            elif i>=1 and name[i-1]==typed[j]:
                j+=1
            else:
                return False
        return i==ln


a=Solution()
