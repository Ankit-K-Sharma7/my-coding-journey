def find(search_list, value):
    if value not in search_list:
        raise ValueError("value not in array")
    left , right = 0 , len(search_list)-1
    while left <= right:
        mid = (left + right)//2

        if value == search_list[mid]:
            return mid
        if value < search_list[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1
