"""
Given an array, rotate the array by one position in clock-wise direction.
Example 1:
Input:
N = 5
A[] = {1, 2, 3, 4, 5}
Output:
5 1 2 3 4
"""

def rotate( arr, n):
    # Store the last element of the array in a temporary variable.
      last_element = arr[-1]
    
      # Shift all elements one position to the right.
      for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i - 1]
    
      # Move the temporary variable to the first position.
      arr[0] = last_element
    
      # Return the rotated array.
      return arr
