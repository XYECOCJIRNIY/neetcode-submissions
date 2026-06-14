class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        total = 1
        left = []
        right = []
        for i in range(len(nums)):
            if i == 0:
                left.append(1)
                continue
            total = total * nums[i - 1]
            left.append(total)
        total = 1
        for i in range(len(nums) - 1, -1 , -1):
            if i == len(nums) - 1:
                right.append(1)
                continue
            total = total * nums[i + 1]
            right.append(total)
        right.reverse()
        for i in range(len(nums)):
            res.append(left[i] * right[i])
        return res
            

        