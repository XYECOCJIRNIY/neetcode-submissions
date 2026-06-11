class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        result = []
        for word in strs:
            key = ''.join(sorted(word))
            if not key in hash_map:
                hash_map[key] = []
            hash_map[key].append(word)
        for keys in hash_map:
            result.append(hash_map[keys])
        return result


        