class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort()
        result = 0
        for i in range(len(points)-1):
            result = max(result, points[i+1][0] - points[i][0])
        return result
        
