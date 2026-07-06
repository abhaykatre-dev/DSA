class Solution:
   
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        def sort_key(interval):
            return (interval[0],-interval[1])
        intervals.sort(key=sort_key)
        count=0
        prev_end=0
        for start,end in intervals:
            if end>prev_end:
                count+=1
                prev_end=end
        return count