def approximate_pi(n_terms):
    total = 0
    for n in range(n_terms):  
        term = (-1)**n / (2*n + 1)
        total += term
    return 4 * total
