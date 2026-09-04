"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        newInts = sorted(intervals, key=lambda x: x.start)
        prevEnd = 0

        for i in range(len(newInts)):
            start = newInts[i].start
            end = newInts[i].end
            if start < prevEnd:
                return False
            prevEnd = end
        
        return True