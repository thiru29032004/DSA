class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        ans=[intervals[0]]
        n=len(intervals)
        for i in range(1,n):
            s=intervals[i][0]
            e=intervals[i][1]
            if ans[-1][1] >=s and ans[-1][1]<e:
                ans[-1][1]=e
            elif ans[-1][1]<s:
                ans.append([s,e])
        return ans
        