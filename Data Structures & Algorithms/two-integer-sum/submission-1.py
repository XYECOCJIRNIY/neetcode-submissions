class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for index, curr_num in enumerate(nums):
            difference = target - curr_num
            if difference in hash_map:
                return [hash_map[difference], index]
            hash_map[curr_num] = index
            


        

        