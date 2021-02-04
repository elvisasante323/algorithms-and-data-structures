"""
  Binary search is an efficient algorithm for finding an item from a sorted list of items
"""


def binary_search_recursive(items, item, start, end):
    if start > end:
        return -1

    middle_item = (start + end) // 2

    if item == items[middle_item]:
        return middle_item

    if item < items[middle_item]:
        return binary_search_recursive(items, item, start, middle_item - 1)
    else:
        return binary_search_recursive(items, item, middle_item + 1, end)


number = 29
numbers = [1, 2, 5, 7, 13, 15, 16, 18, 24, 28, 29]

print(f'Searching for {number}')
number_exists = binary_search_recursive(numbers, number, 0, len(numbers))

if number_exists == -1:
    print(f'{number} does not exist in the list of numbers')
else:
    print(f'{number} exists in the list of numbers')
