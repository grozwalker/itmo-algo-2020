from edx_io import edx_io

def sort(arr, io):
    indexes = [1]
    
    for i in range(1, len(arr)):
        k = i        
        tmp = arr[i]
        
        inserting = False
        while k >= 1 and tmp < arr[k-1]:
            inserting = True
            arr[k] = arr[k-1]
            k -= 1
        
        
        indexes.append(k+1)
            
        if (inserting):
            arr[k] = tmp
    
    io.writeln(indexes)

arr = []

with edx_io() as io:
    arr_length = io.next_int()
    
    for i in range (0, arr_length):
        arr.append(io.next_int())
    
    sort(arr, io)
    
    io.writeln(arr)






