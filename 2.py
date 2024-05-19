def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    iterations = 0
    upper_bound = arr[-1]
 
    while low <= high:
 
        mid = (high + low) // 2
 
        if arr[mid] < x:
            low = mid + 1
 
        elif arr[mid] > x:
            upper_bound = arr[mid]
            high = mid - 1
 
        else:
            return arr[mid]
        iterations += 1
 
    return (iterations,upper_bound)

arr = [1.1, 1.3, 2.5, 3.8, 4.6, 5.9]

print(binary_search(arr, 3.5))  
print(binary_search(arr, 4))  
print(binary_search(arr, 6.0))  



