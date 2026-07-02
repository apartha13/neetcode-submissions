class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = {}
        anagram = []

        for string in strs:
            sorted_characters = sorted(string)
            sorte = "".join(sorted_characters)
            if sorte in myMap:
                myMap[sorte].append(string)
            else:
                myMap[sorte] = [string]
        
        for val in myMap.values():
            anagram.append(val)
        
        return anagram
