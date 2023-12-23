from math import isqrt, floor


def dlog(g, h, p, N=None):
    """Returns the discrete logarithm of h with respect to
    the base b modulo p, where g has order N."""
    if not N:
        N = p-1
    y = 1
    x = 0
    while y % p != h:
        y = (y * g) % p
        x += 1
    return x
    #


def indices_of_match(L1, L2):
    """Returns the indices of a common element of the lists L1
    and L2, i.e. a tuple (i,j) such that L1[i] == L2[j]."""
    # YOUR CODE GOES HERE
    i, j = 0, 0

    l1 = sorted(L1)
    l2 = sorted(L2)

    while i < len(L1) and j < len(L2):
        if l1[i] == l2[j]:
            break
        elif l1[i] < l2[j]:
            i += 1
        else:
            j += 1

    return (L1.index(l1[i]), L2.index(l2[j]))
    #


def babysteps_giantsteps(g, h, p, N=None):
    """Returns the discrete logarithm of h with respect to
    the base b modulo p, where g has order N, using Shanks'
    babysteps-giantsteps algorithm."""
    if not N:
        N = p-1
    n = 1 + isqrt(N)
    babysteps = [1]
    giantsteps = [h]
    for x in range(1, n+1):
        babysteps.append((g*babysteps[x-1]) % p)
        giantsteps.append((pow(g, -1*n, p)*giantsteps[x-1]) % p)

    i, j = indices_of_match(babysteps, giantsteps)
    x = i + (j*n)
    return x


def optimized_babysteps_giantsteps(g, h, p, N=None):
    if not N:
        N = p-1
    n = 1 + isqrt(N)
    babysteps = {1:0}
    baby = 1
    for x in range(1, n+1):
        baby = (g*baby) % p
        babysteps[baby] = x

    giantsteps = h
    for x in range(n+1):
        if giantsteps in babysteps:
            i = babysteps[giantsteps]
            j = x 
            break  
        giantsteps = ((pow(g, -1*n, p)*giantsteps) % p)

    x = i + (j*n)
    return x
