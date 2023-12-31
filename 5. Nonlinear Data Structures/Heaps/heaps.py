import random

class MinHeap:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    # HEAP HELPER METHODS
    # DO NOT CHANGE!
    def parent_idx(self, idx):
        return idx // 2

    def left_child_idx(self, idx):
        return idx * 2

    def right_child_idx(self, idx):
        return idx * 2 + 1

    def child_present(self, idx):
        return self.left_child_idx(idx) <= self.count

    # END OF HEAP HELPER METHODS

    def retrieve_min(self):
        if self.count == 0:
            print("No items in heap")
            return None

        min = self.heap_list[1]
        print("Removing: {0} from {1}".format(min, self.heap_list))
        self.heap_list[1] = self.heap_list[self.count]
        self.count -= 1
        self.heap_list.pop()
        print("Last element moved to first: {0}".format(self.heap_list))
        self.heapify_down()
        return min

    def add(self, element):
        self.count += 1
        print("Adding: {0} to {1}".format(element, self.heap_list))
        self.heap_list.append(element)
        self.heapify_up()      #you call this so that the heap rules are not violated (every child element must be larger than parent)

    def get_smaller_child_idx(self, idx):
        if self.right_child_idx(idx) > self.count:
            print("There is only a left child")
            return self.left_child_idx(idx)
        else:
            left_child = self.heap_list[self.left_child_idx(idx)]
            right_child = self.heap_list[self.right_child_idx(idx)]
            if left_child < right_child:
                print("Left child is smaller")
                return self.left_child_idx(idx)
            else:
                print("Right child is smaller")
                return self.right_child_idx(idx)

    def heapify_up(self):      #you are adding an element here
        idx = self.count
        while self.parent_idx(idx) > 0:
            if self.heap_list[self.parent_idx(idx)] > self.heap_list[idx]:   # it compares the size of the 2 numbers in a sequence
                tmp = self.heap_list[self.parent_idx(idx)]
                print("swapping {0} with {1}".format(tmp, self.heap_list[idx]))
                self.heap_list[self.parent_idx(idx)] = self.heap_list[idx]     #the swap is made here (lower number goes to the beginning)
                self.heap_list[idx] = tmp               #higher nunmber goes to the end of list
            idx = self.parent_idx(idx)
        print("HEAP RESTORED! {0}".format(self.heap_list))
        print("")

    def heapify_down(self):      #you are removing an element
        idx = 1
        while self.child_present(idx):
            smaller_child_idx = self.get_smaller_child_idx(idx)
            if self.heap_list[idx] > self.heap_list[smaller_child_idx]:
                tmp = self.heap_list[smaller_child_idx]
                print("swapping {0} with {1}".format(self.heap_list[idx], tmp))
                self.heap_list[smaller_child_idx] = self.heap_list[idx]
                self.heap_list[idx] = tmp

            idx = smaller_child_idx
        print("HEAP RESTORED! {0}".format(self.heap_list))
        print("")

min_heap = MinHeap()

random_nums = [random.randrange(1, 101) for n in range(6)]    #list comprehension (you generate a list with 6 random numbers)

for el in random_nums:
  min_heap.add(el)     #you are adding these random numbers to the class

while min_heap.count != 0:
  min_heap.retrieve_min()