class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # [ 0 - 7 ]     [15 - 17]   
        #     [ 5 - 10] 
        # [ 0 - - - 10] [15 - 17]
        intervals.sort(key= lambda pair: pair[0])
        output = [intervals[0]]
        for start, end in intervals:
            lastEnd = output[-1][1]
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output