class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = {}

        for word in strs:
            sortWord = "".join(sorted(word))
            if sortWord in anag:
                anag[sortWord].append(word)
            else:
                anag[sortWord] = [word]
        
        return [val for val in anag.values()]