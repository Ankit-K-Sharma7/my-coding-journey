def distance(strand_a, strand_b):
    count = 0
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    for nucleotides_a , nucleotides_b in zip(strand_a,strand_b):
        if nucleotides_a != nucleotides_b:
            count += 1
    return count