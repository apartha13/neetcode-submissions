class Solution:
    def isValid(self, s: str) -> bool:
        parent = {
            ']': '[',
            ')': '(',
            '}': '{'
        }

        stack = []

        for c in s:
            if c in parent:
                if not stack:
                    return False
                
                nex = stack.pop()
                if nex != parent[c]:
                    return False
            else:
                stack.append(c)
        if stack:
            return False
        return True