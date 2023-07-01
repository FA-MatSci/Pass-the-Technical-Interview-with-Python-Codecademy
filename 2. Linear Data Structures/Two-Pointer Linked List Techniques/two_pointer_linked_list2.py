from LinkedList import LinkedList

def find_middle(linked_list):
  fast_point=linked_list.head_node
  slow_point=linked_list.head_node
  while fast_point is not None:
    fast_point=fast_point.get_next_node()
    if fast_point is not None:
      fast_point=fast_point.get_next_node()
      slow_point=slow_point.get_next_node()
    return slow_point

def generate_test_linked_list(length):
  linked_list = LinkedList()
  for i in range(length, 0, -1):
    linked_list.insert_beginning(i)
  return linked_list


test_list = generate_test_linked_list(7)
print(test_list.stringify_list())
middle_node = find_middle(test_list)
print(middle_node.value)