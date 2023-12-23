import random
import math 
def factor_2_part(M):
    """Returns k and q such that M=2^k * q, where q is odd."""
    # YOUR CODE GOES BELOW
    k = 0 
    q = M 
    while q % 2 == 0:
        k += 1 
        q //= 2 
    return k, q

def gcd(a,b):
    while b > 0:
        r = a % b 
        a = b 
        b = r 
    return a 

def square_and_multiply(g,x,m):
    """Returns g^x modulo m using the square-and-multiply algorithm."""
    A = x 
    N = m 
    a = g % N  
    x = 1 
    while A > 0:
        if (A % 2)  == 1:
            x = (x * a) % N
        a = (a * a) % N
        A = math.floor(A/2)
    return x
    #

def miller_rabin(N, a=None):
    """Returns False if N is composite, and returns
    true if a is not a witness for the compositeness of N
    using the Miller-Rabin test."""
    if a == None:
        a = random.randrange(2,N-1)
    g = gcd(a,N)
    if N % 2 == 0 or (1 < g and g < N): # even
        return False
    k, q = factor_2_part(N-1) 
    a = square_and_multiply(a,q,N)
    if a == 1 or a == N-1:
        return True 
    for _ in range(k):
        a = square_and_multiply(a,2,N)
        if a == N-1:
            return True
    return False
