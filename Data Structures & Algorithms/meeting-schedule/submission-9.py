"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        newInts = sorted(intervals, key=lambda i: i.start)
        prevEnd = -1
        
        for i in range(len(newInts)):
            curr = newInts[i]
            if curr.start < prevEnd:
                return False
            prevEnd = curr.end
        
        return True