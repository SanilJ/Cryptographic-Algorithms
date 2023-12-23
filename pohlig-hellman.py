from utils import *
def CRT(moduli, values):
    """Returns an intenger n such that n modulo moduli[i] = values[i].

    Input: moduli - a list of k coprime positive integers
           values - a list of k integers
    """
    c = values[0]
    m = moduli[0] 
    k = len(values)
    for i in range(1,k):
        yi = ((values[i] - c) * modular_inverse(m,moduli[i]))%moduli[i]
        c += (m*yi) 
        m *= moduli[i] 
    return c%m

def q_power_dlog(g,h,p,q,e):
    """Returns the discrete logarithm of g modulo p of h, where g has
    order q^e modulo p."""
    
    temp = pow(q,e-1)
    a = pow(g,temp,p)
    b0 = pow(h,temp,p)
    
    x0 = babysteps_giantsteps(a,b0,p,q)
    x = [x0]

    for i in range(1,e):
        
        temp = 0
        for j in range(len(x)):
            temp -= (x[j]*pow(q,j))
        
        g_temp  = pow(g,temp,p)
        qe = pow(q,e-i-1,p)
        bi = pow(h * g_temp,qe,p)
        xi = babysteps_giantsteps(a,bi,p,q)
        x.append(xi) 
    
    x_f = 0
    for i in range(e):
        x_f += x[i] * pow(q,i)
    
    return x_f

def pohlig_hellman(g,h,p,prime_divisors):
    """Returns the discrete logarithm of h with respect to the base g modulo p,
    where |g| = q_1^e_1 * ... * q_t^e^_t, and prime_divisors = [[q_1,e_1],...,[q_t,e_t]].
    """
    N = 1 
    q_e = [] 
    for q, e in prime_divisors:
        qe = pow(q,e)
        N *= qe 
        q_e.append(qe)
    
    y = []
    t = len(q_e)
    for i in range(t):
        gi = pow(g,N//q_e[i],p)
        hi = pow(h,N//q_e[i],p)
        yi = q_power_dlog(gi,hi,p,prime_divisors[i][0],prime_divisors[i][1])  
        y.append(yi)   
    c = CRT(q_e,y)
    return c
