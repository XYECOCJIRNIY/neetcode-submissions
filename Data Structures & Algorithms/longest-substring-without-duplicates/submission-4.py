class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, -1
        hash_map = {}
        result = 0
        while l < len(s) and r < len(s) - 1: 
            if s[r + 1] not in hash_map:
                r += 1
                hash_map[s[r]] = 1
                curr_result = r - l + 1
                if curr_result > result:
                    result = curr_result
            else:
                hash_map.pop(s[l], None)
                
                if l == r:
                    r += 1
                    hash_map[s[r]] = 1
                    
                l += 1
        return result




        