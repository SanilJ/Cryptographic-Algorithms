def add(P,Q,A,B,p):
    """Returns P+Q on the curve y^2=x^3+Ax+b over Fp."""
    if P is None:
        return Q
    if Q is None:
        return P
    xP, yP = P 
    xQ, yQ = Q

    if xP == xQ and (yP + yQ) % p == 0:
        return None
    
    m = 0
    if xP != xQ:
        m = ((yQ - yP) * pow(xQ - xP, -1, p)) % p
    else:
        if yP == -1 * yQ:
            return None 
        else:
            m = ((3 * xP**2 + A) * pow(2 * yP, -1, p)) % p
    xR = (m**2 - xP - xQ) % p
    yR = (m * (xP - xR) - yP) % p
    return (xR,yR)

def dbl(P,A,B,p):
    """Returns 2P on the curve y^2=x^3+Ax+b over Fp."""
    xP, yP = P
    m = ((3 * xP**2 + A) % p * pow((2 * yP) % p, -1, p)) % p

    x = (m**2 - 2 * xP) % p
    y = (m * (xP - x) - yP) % p

    return (x, y)

def neg(P,p):
    """Returns -P on the curve y^2=x^3+Ax+b over Fp."""
    return (P[0], ((-1 * P[1]) % p))

def smul(n, P, A, B, p):
    """Returns nP on the curve y^2=x^3+Ax+b over Fp."""

    if n == 0:
        return None  

    Q = None 
    R = P 
    
    flag = False 
    if n < 0:
        flag = True 
        n = abs(n)
    
    # Used double add algorithm from 
    # https://en.wikipedia.org/wiki/Elliptic_curve_point_multiplication#:~:text=Elliptic%20curve%20scalar%20multiplication%20is,form%20of%20an%20elliptic%20curve.
    while n > 0:
        if n % 2 == 1:
            Q = add(Q, R, A, B, p)  
            if Q is None:
                return None  
        R = dbl(R, A, B, p)  
        n = n // 2  
    
    if flag:
        Q = neg(Q,p)
    
    return Q
