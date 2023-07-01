
def binary_search(sorted_list, target):
    if not sorted_list:
        return 'value not found'
    mid_idx = len(sorted_list) // 2  # 2       1//2 you get 0
    mid_val = sorted_list[mid_idx]  # 15
    if mid_val == target:
        return mid_idx
    if mid_val > target:
        left_half = sorted_list[:mid_idx]
        return binary_search(left_half, target)    #inside the def, you call the function again
    if mid_val < target:
        right_half = sorted_list[mid_idx + 1:]
        result = binary_search(right_half, target)
    if result == 'value not found':
        return result
    else:
        return mid_idx + 1


# For testing:
sorted_values = [13, 14, 15, 16, 17]         #for this algorithm, values in the list must be sorted!!
print(binary_search(sorted_values, 16))

#sorted_values = [5]
#print(sorted_values[:0])       #this gives you    []