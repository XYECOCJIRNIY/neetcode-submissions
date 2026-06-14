class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        total = 1
        total_nuls = 1
        null = nums.count(0)
        if null == 0:
            for num in nums:
                total *= num
            for num in nums:
                curr_sum = total / num
                res.append(int(curr_sum)) 

        if null == 1:
            for num in nums:
                if num != 0:
                    total_nuls *= num 
            for num in nums:
                if num == 0:
                    res.append(int(total_nuls))
                else:
                    res.append(0)

        if null > 1:
            for num in nums:
                res.append(0)
                
        return res

        