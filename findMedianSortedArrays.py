class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1+nums2
        nums.sort() # nums 1 : m element. nums2: n elements. nums : N elements where N = m+n
        l = len(nums)
        if l%2==0:
            a = nums[int(l/2)]
            b = nums[int(l/2)-1]
            median = (a+b)/2
            print(f"added {a} and {b}")
        else:
            median = nums[int(l/2)]
            print("odd number of elements.")

        return median

