class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        result = 0
        curr = 1
        flag = True
        for i in nums:
            if i - 1 not in nums:
                num = i
                while flag:
                    if num + 1 in nums:
                        num += 1
                        curr += 1
                    else:
                        result, curr = max(curr, result), 1
                        flag = False
            flag = True
        return result

        