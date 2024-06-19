class Solution:
    def minTime (self, arr, n, k):
        #code here
        low = max(arr)
        high = sum(arr)
        # Apply binary search
        while low <= high:
            mid = (low + high) // 2
            painters = self.countPainters(arr, mid)
            if painters > k:
                low = mid + 1
            else:
                high = mid - 1
        return low

    def countPainters(self, boards, time):
        n = len(boards)  # size of array
        painters = 1
        boardsPainter = 0
        for i in range(n):
            if boardsPainter + boards[i] <= time:
                # allocate board to current painter
                boardsPainter += boards[i]
            else:
                # allocate board to next painter
                painters += 1
                boardsPainter = boards[i]
        return painters
