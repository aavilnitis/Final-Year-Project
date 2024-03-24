def construct_subset(array, index, target):
    # BASE CASES
    
    # Case 0-1: target is 0, so any array has a subset sum of the target
    if target == 0:
        return []
    
    # Case 0-2: target is not 0 and array is empty - no subset has a sum of the target
    elif target < 0 or index == 0:
        return None
    
    # Solution doesn't contain current element
    solution = construct_subset(array, index - 1, target)
    if solution is not None:
        return solution
    
    # Solution contains current element
    solution = construct_subset(array, index - 1, target - array[index - 1])
    if solution is not None:
        solution.append(array[index - 1])
        return solution
    
    return None

print(construct_subset([1, 2, 8, 4, 6], 5, 10))
