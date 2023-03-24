import numpy as np
def containsDuplicate(self, nums: list[int]) -> bool:
    if len(nums) != len(set(nums)):
        return True
    else:
        return False


l =[]
def what(nums: list[int],x):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]+nums[j]==x:
                if i != j:
                    return i,j

#print(what([3,2,4],6))

def merge( nums1: list[int], m: int, nums2: list[int], n: int):
    l = []
    for i in range(0,m):
        nums1_what = nums1[i]
        l.append(nums1_what)
    for j in range(0,n):
        nums2_what = nums2[j]
        l.append(nums2_what)
        l.sort()
    return l

#print(merge([1,2,3,0,0,0],3,[2,5,6],3))

















