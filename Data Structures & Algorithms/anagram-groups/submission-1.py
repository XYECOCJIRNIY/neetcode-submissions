class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            letter_count = [0] * 26

            for char in word:
                index = ord(char) - ord('a')
                letter_count[index] += 1

            key = tuple(letter_count)

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())

        