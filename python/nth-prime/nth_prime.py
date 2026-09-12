def prime(number):
    if number <=0:
        raise ValueError('there is no zeroth prime')
    count = 0
    num = 2
    while count < number:
        is_prime = True
        for div in range(2 , int(num ** 0.5) + 1):
            if num % div == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
        num += 1
    return num - 1
