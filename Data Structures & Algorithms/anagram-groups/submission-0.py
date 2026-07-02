class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = {}
        result = []

        for s in strs:
            new = sorted(s)
            new = ''.join(new)
            if new in myMap:
                myMap[new].append(s)
            else:
                myMap[new] = [s]
        
        for val in myMap.values():
            result.append(val)
        
        return result