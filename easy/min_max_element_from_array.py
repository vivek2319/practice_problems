def getMinMax( a, n):
    # we will initiate left and right pointers
    left_pointer = 0
    right_pointer = len(a) - 1
    
    # we will set min and max and keep changing it
    current_min_element = min(a[left_pointer], a[right_pointer])
    current_max_element = max(a[left_pointer], a[right_pointer])
    
    for i in range(left_pointer + 1, right_pointer + 1):
        if a[i] < current_min_element:
            current_min_element = a[i]
        elif a[i] > current_max_element:
            current_max_element = a[i]
        elif n == 1:
            current_min_element = a[left_pointer]
            current_max_element = a[left_pointer]
            
    return current_min_element, current_max_element
