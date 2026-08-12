def append(list1, list2):
    return concat([list1,list2])

def concat(lists):
    result = []
    for items in lists:
        result += items
    return result

def filter(function, list):
    new_list = []
    for items in list:
        if function(items):
            new_list += [items]
    return new_list

def length(list):
    count = 0
    for items in list:
        count += 1
    return count

def map(function, list):
    result = []
    for items in list:
        result += [function(items)]
    return result

def foldl(function, list, initial):
    accumulator = initial
    for items in list:
        accumulator = function(accumulator , items)
    return accumulator

def foldr(function, list, initial):
    accumulator = initial
    for items in reverse(list):
        accumulator = function(accumulator , items)
    return accumulator

def reverse(list):
    left ,  right = 0 , length(list) - 1
    while left < right:
        list[left] , list[right] = list[right] , list[left]
        left += 1
        right -= 1
    return list