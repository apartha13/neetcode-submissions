class Solution:
    def isValid(self, s: str) -> bool:
        myMap = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        start = []

        for c in s:
            print(c)
            if c in myMap:
                if start and myMap[c] == start.pop():
                    continue
                else:
                    return False
            else:
                start.append(c)
        print(start)
        if start:
            return False
        return True