def merge(arr, start, mid, end):
    left_arr, right_arr = arr[start:mid], arr[mid:end]
    left_i = right_i = 0
    for i in range(start, end):
        if left_i >= len(left_arr):
            arr[i] = right_arr[right_i]
            right_i += 1
        elif right_i >= len(right_arr):
            arr[i] = left_arr[left_i]
            left_i += 1
        elif left_arr[left_i] < right_arr[right_i]:
            arr[i] = left_arr[left_i]
            left_i += 1
        else:
            arr[i] = right_arr[right_i]
            right_i += 1


def merge_sort(arr, start=0, end=None):
    if end is None:
        end = len(arr)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid, end)
        merge(arr, start, mid, end)


def is_anagram(first_string, second_string):
    first_chars = [*first_string.lower()]
    second_chars = [*second_string.lower()]

    merge_sort(first_chars)
    merge_sort(second_chars)

    return first_chars == second_chars
