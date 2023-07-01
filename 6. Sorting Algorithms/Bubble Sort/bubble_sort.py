nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print("PRE SORT: {0}".format(nums))


def swap(arr, index_1, index_2):
    temp = arr[index_1]    #temporay variable to hold the element at index1
    arr[index_1] = arr[index_2]
    arr[index_2] = temp


def bubble_sort_unoptimized(arr):
    iteration_count = 0
    for el in arr:       #you do nothing with el. The point of this is loop iteration for the number of elements in the list
        for index in range(len(arr) - 1):
            iteration_count += 1
            if arr[index] > arr[index + 1]:
                swap(arr, index, index + 1)

    print("PRE-OPTIMIZED ITERATION COUNT: {0}".format(iteration_count))
    print(arr)


def bubble_sort(arr):
    iteration_count = 0
    for i in range(len(arr)):
        # iterate through unplaced elements
        for idx in range(len(arr) - i - 1):      #the biggest number is already at the end so you add " - i" to not go until the end
            iteration_count += 1
            if arr[idx] > arr[idx + 1]:
                # replacement for swap function
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]     #this is the same as def swap()

    print("POST-OPTIMIZED ITERATION COUNT: {0}".format(iteration_count))
    print(arr)


bubble_sort_unoptimized(nums.copy())
bubble_sort(nums)
#print("POST SORT: {0}".format(nums))