def Bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr  

arr = [7,2,56,78,9,0,1,3,4,5]
print("Assending order:", Bubble_sort(arr))