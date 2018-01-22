'''
def gcd(x,y):
    while x is not 1 and y is not 1:
        if x==y:
            return x
        if x>y:
            x = x%y
            continue
        if x<y:
            y = y%x
            continue
    return 1
'''
def gcd(a, b):
    # Return the GCD of a and b using Euclid's Algorithm
    while a != 0:
        a, b = b % a, a
    return b
    
def lcm(x,y):
    return int(x*y/gcd(x,y))

def mod_inverse(a,m):
    ans = 0
    count = 1
    while a is not 1:
        ans = (a*count)%m
        if ans == 1:
            break
        count += 1
    return count

def lin_solve(a,b,c,m):
    a = a%26
    c = c%26
    #return mod_inverse(a,m)*(c-b)%m
    return mod_inverse(a/gcd(a,m),m/gcd(a,m))*(c-b)%m

def lin_sys_solve(a,b,c,d,e,f,m):
    x = int((c*e-b*f)/gcd(c*e-b*f,m)*mod_inverse((a*e-b*d)/gcd(a*e-b*d,m),m))%m
    y = int((a*f-c*d)/gcd(a*f-c*d,m)*mod_inverse((a*e-b*d)/gcd(a*e-b*d,m),m))%m
    return [x,y]

def lin_inverse(a,b,m):
    c = mod_inverse(a/gcd(a,m),m/gcd(a,m))%m
    d = -1*mod_inverse(a/gcd(a,m),m/gcd(a,m))*b%m
    return [c,d]
