
class Solution:
    def isValid(self, s: str) -> bool:
        myMap = {
            ']': '[',
            '}': '{',
            ')': '('
        }

        stack = []
        
        for c in s:
            if c in myMap:
                if not stack or stack.pop() != myMap[c]:
                    return False
            else:
                stack.append(c)
        
        if not stack:
            return True
        return False

        