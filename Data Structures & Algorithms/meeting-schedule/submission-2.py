"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def isOverlapping(self, a, b):
        return a.start < b.end and b.start < a.end

    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        for a in intervals:
            intervals.remove(a)
            for b in intervals:
                if self.isOverlapping(a, b):
                    return False

        return True