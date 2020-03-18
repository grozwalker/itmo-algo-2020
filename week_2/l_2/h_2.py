#!/usr/bin/env pypy
# coding: utf-8


def merge(first, second):
    global inversion_count
    i = 0
    j = 0
    result = []
    
    first_len = len(first)
    second_len = len(second)
    
    while i < first_len or j < second_len:
        if j == second_len or (i < first_len and first[i] <= second[j]):
            result.append(first[i])
            i += 1
        else:
            result.append(second[j])
            j += 1
            
            if i < first_len:
                inversion_count += first_len - i
            
    return result


def merge_sort(data, l, r, io):
    global inversion_count
    
    if (r - l) == 0:
        return [data[l]]
    
    if (r - l) == 1:
        merged_data = merge([data[l]], [data[r]])
        return merged_data
    
    middle = (r - l) // 2
    
    left_part = merge_sort(data, l, l + middle, io)
    right_part = merge_sort(data, l + middle + 1, r, io)
    
    merged_data = merge(left_part, right_part)

    
    return merged_data


from edx_io import edx_io

data = []
inversion_count = 0

with edx_io() as io:
    data_length = io.next_int()
    for i in range (0, data_length):
        data.append(io.next_int())
    
    merge_sort(data, 0 , data_length - 1, io)
    
    io.writeln(inversion_count)
