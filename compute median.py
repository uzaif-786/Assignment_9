arr = [7, 2, 56, 78, 9, 0, 1, 3, 4, 5]
       arr.sort()
    n = len(arr)
    if n % 2 == 0:
        median = (arr[n//2 - 1] + arr[n//2]) / 2
    else:
        median = arr[n//2]
    return median
   
    print("Sorted array:", arr) 
    print("Median:", median)