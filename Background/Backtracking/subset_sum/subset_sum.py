def subset_sum(index, array, target, subset = [], results = []):
    # BASE CASES
    
    # BASE CASE 1: Target is 0
    
    # BASE CASE 2: index has reached end of the array
    if target == 0 or index == len(array):
        # BASE CASE 1: Target is 0
        if target == 0:
            results.append(subset.copy())
        return
    
    # Solution 1: array contains subset that sums to target and excludes current element
    # If function call returns - solution has been found, if not - continues
    
    # Exclude the current element
    subset_sum(index + 1, array, target, subset, results)
        
    if array[index] <= target:
        subset.append(array[index])
    
        # Solution 2: array contains subset that sums to target and includes current element
        # If function call returns - solution has been found, if not - removes last element and tries others
        subset_sum(index + 1, array, target -array[index], subset, results)
    
        # Remove last element
        subset.pop()
    
    # Return array of results
    return results

print(subset_sum(0, [2,4,8,6], 10))