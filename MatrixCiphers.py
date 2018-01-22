from Cryptoalphabet import *
from sympy import *
from random import randint

def matrix_mod(A,m):
    return A.applyfunc(lambda x:Mod(x,m))
def matrix_inverse(A, m):
    origmod=m
    g = gcd(A.det()%m,m)
    if g != 1:
        m=m/g
    if gcd(A.det()%m,m) != 1:
        print("no solution.")
        return null
    A_INV = A.inv_mod(m)
    return A_INV

def encrypt(E, p, a):
    """Apply matrix E to string p mod 26 and return an encrypted string,
       relative to Cryptoalphabet a """
    if len(p)%2!=0:
        p+='X'
    return a.matrix_to_string(matrix_mod(E*a.string_to_matrix(p),len(a.alphabet)),int(len(p)/2))

def decrypt(D, c, a):
    """Apply matrix D to string c mod 26 and return a decrypted string,
       relative to Cryptoalphabet a """
    return a.matrix_to_string(matrix_mod(D*a.string_to_matrix(c),len(a.alphabet)),int(len(c)/2))


def get_decryption_matrix(P,C, a):
    """ Knowing two digraphs in string P are encoded as string C, determine
        a unique decryption matrix, relative to Cryptoalphabet a """
    P = a.string_to_matrix(P)
    C = a.string_to_matrix(C)
    C_INV = matrix_inverse(C,len(a.alphabet))
    A_INV = matrix_mod(P*C_INV,len(a.alphabet))
    return A_INV

def get_random_invertible_matrix(m):
    """ return a random 2x2 matrix M with gcd(det(M),m)= 1 """
    d = 2
    while d>1:
        a = randint(0,m)
        b = randint(0,m)
        c = randint(0,m)
        d = randint(0,m)
        M = Matrix([[a.b],[c,d]])
        d = gcd(M.det()%m,m)
    return M

def get_rand_matrix_with_fixed_det(m,determinant):
    """ return a random 2x2 matrix with a certain determinant"""
    det = -1
    while det != determinant:
        a = randint(0,m)
        b = randint(0,m)
        c = randint(0,m)
        d = randint(0,m)
        M = Matrix([[a,b],[c,d]])
        det = a*d - b*c#gcd(M.det()%m,m)
    return M
