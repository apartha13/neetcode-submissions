class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublist = {}

        for string in strs:
            ind = sorted(string)
            ind = "".join(ind)
            if ind not in sublist:
                sublist[ind] = [string]
            else:
                sublist[ind].append(string)
        
        anagrams = []
        for i in sublist.keys():
            anagrams.append(sublist[i])
        
        return anagrams