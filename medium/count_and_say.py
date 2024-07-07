"""
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the run-length encoding of countAndSay(n - 1).
Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511".

Given a positive integer n, return the nth element of the count-and-say sequence.

 

Example 1:

Input: n = 4

Output: "1211"

Explanation:

countAndSay(1) = "1"
countAndSay(2) = RLE of "1" = "11"
countAndSay(3) = RLE of "11" = "21"
countAndSay(4) = RLE of "21" = "1211"
Example 2:

Input: n = 1

Output: "1"

Explanation:

This is the base case.

 

Constraints:

1 <= n <= 30
 

Follow up: Could you solve it iteratively?

"""
class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case: when n is 1, return "1"
        if n == 1:
            return "1"
        # Base case: when n is 2, return "11"
        if n == 2:
            return "11"

        # Recursive call to generate the "look and say" sequence for n-1
        result = self.countAndSay(n-1)

        newresult = ""
        count = 1
        for i in range(1,len(result)):
            # Counting consecutive numbers and updating the count
            if result[i] != result[i-1]:
                newresult = newresult + str(count+0)
                newresult = newresult + result[i-1]
                count = 1
            else:
                count += 1

            # Checking if we have reached the end of the sequence and adding the last count and number
            if i == len(result)-1:
                newresult = newresult + str(0 + count)
                newresult = newresult + result[i]

        # Return the new "look and say" sequence
        return newresult

    
