
def binary_search(sorted_list, target):
  if not sorted_list:
    return 'value not found'
  mid_idx = len(sorted_list)//2     #if you get a decimal point, it goes down (if you get 2.5 it takes 2)
  mid_val = sorted_list[mid_idx]

  if mid_val == target:
    return mid_idx



sorted_values = [13, 14, 15, 16, 17]
#print(binary_search([], 42))
#print(binary_search(sorted_values, 42))
print(binary_search(sorted_values, 15))