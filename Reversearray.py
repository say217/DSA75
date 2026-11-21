# Question:
# Given an array arr of size n, reverse the array in place.
# The task is to rearrange the elements in reverse order
# without using an additional array.

def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]

        left += 1
        right -= 1

    return arr


arr = [1, 2, 3, 4, 5]

print(reverse_array(arr))


