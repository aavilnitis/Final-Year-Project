# This implementation of subset sum is from Jeff Erickson: Backtracking (online PDF). Chapter 2 of his book Algorithms
def subset_sum(array, target):
    is_subset = False
    
    # BASE CASES (Case 0-1 and 0-2)
    
    # Case 0-1: target is 0, so any array has subset sum of target
    if target == 0:
        return True
    
    # Case 0-2: target is not 0 and array is empty - no subset has sum of target
    elif target < 0 or (target != 0 and len(array) == 0):
        return False
    
    
    # Case 1: If X contains a subset that sums to T there are two options for any element x in X:
        # Case 1-1 X has subset that includes x and whose sum is T
        # Case 1-2 X has subset that excludes x and whose sum is T
    
    
    else:
        for index, element in enumerate(array):
            array_wout_x = array[:index] + array[index+1:]
            with_x = subset_sum(array_wout_x, target-element)
            wout_x = subset_sum(array_wout_x, target)
            if with_x or wout_x:
                is_subset = True
                
    return is_subset
    
print(subset_sum([1,2], 4))