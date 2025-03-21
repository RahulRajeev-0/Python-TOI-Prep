'''
question -> find the combination of numbers in a given array that product a target sum 
'''

def find_combinations(arr, target):
    result = []
    arr.sort()  # Optional: sort the array to handle duplicates and to make the backtracking more efficient
    
    def backtrack(start, path, target):
        if target == 0: # if target is 0 then append to result
            result.append(path)
            return
        if target < 0: # if target < 0 combination didn't worked out 
            return
        
        for i in range(start, len(arr)):
            if i > start and arr[i] == arr[i-1]:  # Skip duplicates
                continue
            backtrack(i + 1, path + [arr[i]], target - arr[i])
    
    backtrack(0, [], target)
    return result

# Example usage
arr = [2, 3, 6, 7, 2 , 1, 4]
target = 7
print(find_combinations(arr, target))


            

        


