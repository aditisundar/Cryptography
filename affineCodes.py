from cryptomath import *
from Cryptoalphabet import Cryptoalphabet
#AFFINE CODE
al = "ABCDEFGHIJKLMNOPQRSTUVWXYZ!.?0123456789-*"
alpha = Cryptoalphabet(al)
#al = "bhetr45,o!l"
#alpha = Cryptoalphabet(al)
m = len(al)*len(al)

def affine_encode(plaintext,a,b):
    cipher = ""
    plaintext = alpha.prepare(plaintext)
    print(plaintext)
    for i in plaintext:
        x = alpha.getIndex(i)
        y = (a*x+b)%m
        cipher += alpha.charNum(y)
    return cipher

def affine_decode(ciphertext,c,d):
    cd = lin_inverse(c,d,m)
    print(cd)
    a = cd[0]
    b = cd[1]
    plaintext = ""
    ciphertext = alpha.prepare(ciphertext)
    for i in ciphertext:
        x = alpha.getIndex(i)
        y = (a*x+b)%m
        plaintext += alpha.charNum(y)
    return plaintext

def affine_crack(c1,p1,c2,p2):
    c1 = alpha.getIndex(c1)
    c2 = alpha.getIndex(c2)
    p1 = alpha.getIndex(p1)
    p2 = alpha.getIndex(p2)
    print()
    x = p1-p2
    y = c1-c2
    a = lin_solve(x,0,y,m)%m
    b = (c1-a*p1)%m
    a = int(a/gcd(gcd(a,b),m))
    b = int(b/gcd(gcd(a,b),m))
    m = int(m/gcd(gcd(a,b),m))
    print(a)
    print(b)
    return [a,b]

def affine_encode_digraphs(plaintext, a, b):
    if len(plaintext)%2 is not 0:
        plaintext += "X"
    ciphertext = ""
    for i in range(len(plaintext)):
        if i%2==0:
            di = plaintext[i:i+2]
            #print(di)
            num = alpha.digraphToInt(di)
            #print(num)
            new_num = (a*num+b)%m
            #print(new_num)
            new_di = alpha.intToDigraph(new_num)
            ciphertext+=new_di
        else:
            continue
    return ciphertext
def affine_decode_digraphs(ciphertext, a, b):
    cd = lin_inverse(a,b,m)
    c = cd[0]
    d = cd[1]
    plaintext = ""
    for i in range(len(ciphertext)):
        if i%2==0:
            di = ciphertext[i:i+2]
            num = alpha.digraphToInt(di)
            new_num = (c*num+d)%m
            new_di = alpha.intToDigraph(new_num)
            plaintext += new_di
        else: continue
    return plaintext

def affine_digraph_crack(c1,p1,c2,p2):
    m = 676
    c1 = alpha.digraphToInt(c1)%m
    c2 = alpha.digraphToInt(c2)%m
    p1 = alpha.digraphToInt(p1)%m
    p2 = alpha.digraphToInt(p2)%m
    print()
    x = p1-p2
    y = c1-c2
    a = lin_solve(x,0,y,m)%m
    b = (c1-a*p1)%m
    a = int(a/gcd(gcd(a,b),m))
    b = int(b/gcd(gcd(a,b),m))
    m = int(m/gcd(gcd(a,b),m))
    print(a)
    print(b)
    return [a,b]


#TEST
'''
print(lin_inverse(13,-14,41))

message = input("message: ").upper()
txt = affine_encode_digraphs(message,375,114)
print("encoded: ",txt)
print("decoded: ", affine_decode_digraphs(txt,375,114))
'''
'''
a = 7
b = 5
#cipher = affine_encode(message, a,b )
#print(cipher)
print("inverse: ",lin_inverse(a,b,m))




a_number = 0
for i in range(m):
    if i == 0:
        a_number += 1
        continue
    if gcd(i,m) == 1:
        a_number +=1
b_number = m
transformations = a_number*b_number

print("length: ",m, "\npossible a's: ", a_number,"\npossible b's: ", b_number,"\ntransformations: ", transformations)


message = input("message: ")
crib = input("crib: ")

ciphertext = alpha.prepare(message)
crib = alpha.prepare(crib)

x1 = alpha.getIndex(crib[0])
x2 = alpha.getIndex(crib[1])
y1 = alpha.getIndex(ciphertext[0])
y2 = alpha.getIndex(ciphertext[1])

cd = affine_crack(y1,x1,y2,x2)
print(affine_decode(ciphertext, cd[0],cd[1]))
'''
