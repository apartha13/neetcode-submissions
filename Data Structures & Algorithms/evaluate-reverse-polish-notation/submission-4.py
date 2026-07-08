class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(['+', '-', '*', '/'])
        nums = []

        for token in tokens:
            if token in operators:
                sec = int(nums.pop())
                fir = int(nums.pop())

                if token == '+':
                    tot = fir + sec
                elif token == '-':
                    tot = fir - sec
                elif token == '*':
                    tot = fir * sec
                else:
                    tot = int(fir / sec)
                
                nums.append(tot)
            else:
                nums.append(int(token))
        
        return nums[-1]