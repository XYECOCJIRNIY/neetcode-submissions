class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = list()
        nums.sort()
        for i in range(0, len(nums) - 1):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    if [nums[i], nums[l], nums[r]] not in result:
                        result.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1          
        return result


        