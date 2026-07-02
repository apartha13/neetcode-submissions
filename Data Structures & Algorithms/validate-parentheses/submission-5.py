class Solution:
    def isValid(self, s: str) -> bool:
        myMap = {
            ']': '[',
            '}': '{',
            ')': '(',
        }
        stack = []

        for char in s:
            if char in myMap:
                if stack and stack[-1] == myMap[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        if stack:
            return False
        
        return True

