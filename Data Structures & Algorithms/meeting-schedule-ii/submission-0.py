"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        # Sort meetings by start time
        intervals.sort(key=lambda interval: interval.start)

        # Min heap stores end times
        min_heap = []

        for interval in intervals:
            # If the earliest meeting has ended, reuse that room
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)

            # Allocate the current meeting to a room
            heapq.heappush(min_heap, interval.end)

        return len(min_heap)