from sympy import *
import sys
from Cryptoalphabet import Cryptoalphabet

def matrix_mod(A,m):
    return A.applyfunc(lambda x:Mod(x,m))
def gcd(x,y):
    while x is not 1 and y is not 1:
        if x==y:
            return x
        if x>y:
            x = x-y
            continue
        if x<y:
            y = y-x
            continue
    return 1
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



cipher = input("ciphertext: ")
crib = input("crib: ")
mod = int(input("mod: "))
fulltext = input("fulltext: ")
alphabet = input("alphabet: ")

alpha = Cryptoalphabet(alphabet)

#CRACKING GIVEN CIPHER & CRIB
C = Matrix([[alpha.getIndex(cipher[0:1]),alpha.getIndex(cipher[2:3])],[alpha.getIndex(cipher[1:2]), alpha.getIndex(cipher[3:4])]])
P = Matrix([[alpha.getIndex(crib[0:1]),alpha.getIndex(crib[2:3])],[alpha.getIndex(crib[1:2]),alpha.getIndex(crib[3:4])]])

print("CIPHER: ", C)
print("PLAIN: ", P)

C_INV = matrix_inverse(C,mod)
print("C INV: ", C_INV)
A_INV = matrix_mod(P*C_INV,mod)
print("A INV: ", A_INV)
FULL_CIPHER = alpha.string_to_matrix(fulltext)
print("FULL CIPHER: ", FULL_CIPHER)
PLAINTEXT = matrix_mod(A_INV*FULL_CIPHER,mod)
DECODED_MESSAGE = alpha.matrix_to_string(PLAINTEXT, int(len(fulltext)/2))
print(DECODED_MESSAGE)
print()

#ENCODING
plain = input("to encode: ")
A = matrix_inverse(A_INV,mod)
print()
print("A: ", A)
PLAIN = alpha.string_to_matrix(plain)
CIPHER = matrix_mod(A*PLAIN,mod)
ENCODED_MESSAGE = alpha.matrix_to_string(CIPHER, int(len(plain)/2))
print(ENCODED_MESSAGE)
print()
