class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr = [0] * len(temperatures)
        for i in range(len(temperatures) - 1):
            k = i + 1
            while (k < len(temperatures)):
                if temperatures[k] > temperatures[i]:
                    arr[i] += 1
                    break
                if (k == len(temperatures) - 1):
                    arr[i] = 0
                    break
                arr[i] += 1
                k += 1
        return arr