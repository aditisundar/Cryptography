from sympy import *
from random import randint
from cryptomath import *
from math import log2

def choose_modulus(k,l,d):
	p1,p2 = 4,4
	while not isprime(p1) or not isprime(p2):	
		p1 = randint(pow(2,k), pow(2,l))
		p2 = randint(pow(2,k), pow(2,l))
		#print(p1,p2,pow(2,d))
		#print(log2(p1), log2(p2),d
		if abs(p1-p2)<=pow(2,d):
			p1,p2 = 4,4
	return [p1,p2]
def choose_encryption_key(p1,p2):
	m = p1*p2
	e = randint(1,m)
	while gcd(e,(p1-1)*(p2-1)) != 1:
		e = randint(1,m)
	return e
def compute_decryption_key(e,p1,p2):
	m = p1*p2
	mod = (p1-1)*(p2-1)
	d = inv_mod(e,mod)
	return d
def RSA_encrypt(P,e,m):
	return pow(P,e,m)
def RSA_decrypt(C,d,m):
	return pow(C,d,m)
def RSA_crack(C,e,m):
	d = inv_mod(e,totient(m))
	return RSA_decrypt(C,d,m)
def power_mod(a,b,m):
	return pow(a,b,m)
def string_to_int(s):
	return int.from_bytes(s.encode(),'big')
def int_to_string(n):
	return n.to_bytes((n.bit_length()+7)//8,'big').decode()


#####
#
# add the following to your rsa file
# this algorithm computes the gcd by using extended Euclid
#
#####

def xgcd(b, n):
    """ Return g, x0, y0
        such that x0*b + y0*n = g
        and g is the gcd of (b,n)"""
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return b, x0, y0


def inv_mod(b, n):
    """ Return the modular inverse of b mod n
     or None if gcd(b,n) > 1 """
    g, x, _ = xgcd(b, n)
    if g == 1:
        return x % n




'''
m = choose_modulus(19,20,0)
p1 = m[0]
p2 = m[1]
m = p1*p2
print("p1: ",p1, " p2: ", p2)
e = choose_encryption_key(p1,p2)
print("e: ",e)
d = compute_decryption_key(e,p1,p2)
print("d: ", d)
print("plain: i hate")
P = string_to_int("ihate")
print(P,int_to_string(P))

C = RSA_encrypt(P,e,m)
print("encoded: ", C)

P_decoded = RSA_decrypt(C,d,m)
print("decrypted: ",int_to_string(P_decoded))

P_cracked = RSA_crack(C,e,m)
print("cracked: ", P_cracked)
'''