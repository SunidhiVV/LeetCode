'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1]*len(nums)
        lprod = [1]*len(nums)
        rprod = [1]*len(nums)
        left = 1
        right = 1
        for i in range(1,len(nums)):
            left *= nums[i-1]
            lprod[i] = left
        for i in reversed(range(len(nums)-1)):
            right *= nums[i+1]
            rprod[i] = right
        for i in range(len(nums)):
            answer[i] = lprod[i]*rprod[i]
        return answer
