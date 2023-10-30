class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        length = len(nums)
        nums.sort()
        res = []
        for i in range(length):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = length-1
            while left < right:
                sum = nums[left] + nums[right] + nums[i]
                if sum == 0:
                    res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif sum > 0:
                    right -= 1
                else:
                    left += 1   
        return res 
        

