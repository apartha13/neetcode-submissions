class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myMap = {}
        for c in s:
            if c not in myMap:
                myMap[c] = 1
            else:
                myMap[c] += 1
        print(myMap)
        for h in t:
            if h not in myMap:
                return False
            if (h in myMap) and (myMap[h] > 0):
                myMap[h] -= 1
            elif myMap[h] <= 0:
                return False
        
        for key, val in myMap.items():
            if val != 0:
                return False

        return True


            