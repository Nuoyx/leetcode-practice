class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        intervals.sort()
        result = []
        newStart = newInterval[0]
        newEnd = newInterval[1]
        for (start, end) in intervals:
            if start <= newEnd and end >= newStart:
                start = min(start, newStart)
            if end >= newStart and start <= newEnd:
                end = max(end, newEnd)
            if len(result) > 0:
                if result[-1][-1] >= start:
                    end = max(end, result[-1][-1])
                    result[-1][-1] = end
                    continue
            result.append([start, end])
        return result