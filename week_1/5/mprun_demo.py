
import time
import memory_profiler
from edx_io import edx_io

def test():
    data = []
    operations = []

    t = time.time()
    with edx_io() as io:
        arr_length = io.next_int()
        for i in range (0, arr_length):
            data.append(io.next_int())

        for i in range(len(data)):
            j = i - 1 
            tmp = data[i]
            while data[j] > tmp and j >= 0:
                data[j + 1] = data[j]
                operations.append(j)
                j -= 1

            data[j + 1] = tmp

        for i in operations:
            io.writeln(f'Swap elements at indices {i + 1} and {i + 2}.')

        # operations.append('No more swaps needed.')

        # listToStr = '\n'.join(map(str, oprations)) 
        # 
        io.writeln(data)
        print(time.time()-t)
        
test()
