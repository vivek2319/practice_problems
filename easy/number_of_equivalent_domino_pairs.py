"""
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

 

Example 1:

Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1
Example 2:

Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
Output: 3
 

Constraints:

1 <= dominoes.length <= 4 * 104
dominoes[i].length == 2
1 <= dominoes[i][j] <= 9

"""

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        res = 0
        seen = {}
        
        for i in range(len(dominoes)):
            # check the pair at the index
            pair = dominoes[i]

            # pull the two values
            first = pair[0]
            second = pair[1]

            # sort them so reversed matches will go into the same count
            smaller = min(first, second)
            bigger = max(first, second)

            pair_sorted = (smaller, bigger)

            if pair_sorted in seen:
                res = res + seen[pair_sorted]
                seen[pair_sorted] = seen[pair_sorted] + 1
            else:
                seen[pair_sorted] = 1
        return res
