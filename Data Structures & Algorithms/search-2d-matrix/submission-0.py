class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix)-1
        
        while top <= bottom:
            mid = top + ((bottom - top) // 2)
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                break
        
        l, r = 0, len(matrix[mid])-1

        while l <= r:
            dle = l + ((r-l) // 2)
            if target > matrix[mid][dle]:
                l = dle + 1
            elif target < matrix[mid][dle]:
                r = dle - 1
            else:
                return True
            
        return False
            
        
        

            
        


