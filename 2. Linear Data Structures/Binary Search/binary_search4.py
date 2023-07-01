def binary_search(sorted_list, left_pointer, right_pointer, target):
    # this condition indicates we've reached an empty "sub-list"
    if left_pointer >= right_pointer:
        return "value not found"

    # We calculate the middle index from the pointers
    mid_idx = (left_pointer + right_pointer) // 2
    mid_val = sorted_list[mid_idx]

    if mid_val == target:
        return mid_idx
    if mid_val > target:
        # we reduce the sub-list by passing in a new right_pointer
        return binary_search(sorted_list, left_pointer, mid_idx, target)     #this approach doesn't create an additional list as opposed to "binary_search3"
    if mid_val < target:
        # we reduce the sub-list by passing in a new left_pointer
        return binary_search(sorted_list, mid_idx + 1, right_pointer, target)


values = [77, 80, 102, 123, 288, 300, 540]       #for this algorithm, values in the list must be sorted!!
start_of_values = 0
end_of_values = len(values)
result = binary_search(values, start_of_values, end_of_values, 288)  # binary_search is called here

print("element {0} is located at index {1}".format(288, result))