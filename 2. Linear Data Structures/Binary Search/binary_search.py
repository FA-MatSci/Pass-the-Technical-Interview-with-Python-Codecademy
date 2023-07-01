
def binary_search(sorted_list, target):
  if len(sorted_list) == 0:
    return 'value not found'
  else:
    a = len(sorted_list)
    mid_idx = int(a / 2)
    mid_val = sorted_list[mid_idx]
  return mid_idx, mid_val



sorted_values = [13, 14, 15, 16, 17]
print(binary_search([], 42))
print(binary_search(sorted_values, 42))