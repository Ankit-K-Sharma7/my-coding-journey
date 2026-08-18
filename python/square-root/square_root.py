def square_root(number):
    if number < 0:
        return -1
    low , high = 0 , number
    while low <= high:
        mid = (low + high)//2
        if mid * mid == number:
            return mid
        elif mid * mid < number:
            low = mid + 1
        else:
            high = mid - 1

    if mid * mid <= number:
        return (mid + (number / mid))/2