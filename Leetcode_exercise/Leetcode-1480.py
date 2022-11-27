def some(nums):
    for i in range(len (nums)):
        p= len (nums)-i
        s=0
        for t in range (p):
            s+=nums[t]
        nums[p-1]=s
    return nums

nums=[1,2,3,4]
print(some(nums))
