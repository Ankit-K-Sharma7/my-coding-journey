def sum_of_multiples(limit, multiples):
    multiple_set = set()
    for num in range(1,limit):
        for multiple in multiples:
            if multiple * num < limit:
                multiple_set.add(multiple * num)
    return sum(multiple_set)