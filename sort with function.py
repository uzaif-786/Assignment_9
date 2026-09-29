def ascending_order(arr):
    return sorted(arr)

def descending_order(arr):
    return sorted(arr, reverse=True)

arr = [7, 2, 56, 78, 9, 0, 1, 3, 4, 5]
print("Ascending order:", ascending_order(arr)) 
print("Descending order:", descending_order(arr)) 