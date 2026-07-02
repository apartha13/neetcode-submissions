class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []

        for bracket in s:
            if bracket in close_to_open:
                if not stack:
                    return False
                top = stack.pop()
                if top != close_to_open[bracket]:
                    return False
            else:
                stack.append(bracket)
        
        if stack:
            return False
        else:
            return True