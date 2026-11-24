class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for index, i in enumerate(nums):
            left = index + 1
            right = len(nums) -1
            while left < right:
                if i + nums[left] + nums[right] > 0:
                    right -= 1
                elif i + nums[left] + nums[right] < 0:
                    left += 1
                elif i + nums[left] + nums[right] == 0:
                    if not [i, nums[left], nums[right]] in res:
                        res.append([i, nums[left], nums[right]])
                    right -= 1
        return res
