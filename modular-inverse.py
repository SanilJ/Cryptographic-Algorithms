import math
def extended_euclidean(a,b):
    """Returns gcd(a,b) along with integers s,t such that gcd(a,b)=as+bt using
     the extended euclidean algorithm."""
    r_prev, r = a, b 
    s_prev, s = 1, 0
    t_prev, t = 0, 1  

    while r != 0:
        q =  r_prev // r
        r_next = r_prev % r  
        r_prev, r = r, r_next
        s_prev, s = s, s_prev - (q*s)  
        t_prev, t = t, t_prev - (q*t)
    return r_prev , s_prev, t_prev
    #
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

def modular_inverse(a,m):
    """Returns an integer b such that a*b=1 mod m if gcd"""
    # b = a^-1 * 1 
    # Thus we have a^−1 (mod p) = a^p−2 (mod p).
    return square_and_multiply(a, m-2, m)   
    #
