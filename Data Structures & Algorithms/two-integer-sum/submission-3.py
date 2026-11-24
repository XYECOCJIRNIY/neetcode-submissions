class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for index, i in enumerate(nums):
            if i in res:
                return [res[i], index]
            else:
                res[target - i] = index

        