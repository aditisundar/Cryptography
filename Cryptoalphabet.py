from sympy import *
from MatrixCiphers import *

class Cryptoalphabet:
    def __init__(self, alphabet):
        self.alphabet = alphabet#.upper()
        self.m = len(self.alphabet)
    def getIndex(self, c):
        #c = c.upper()
        #print(c)
        return self.alphabet.index(c)
    def charNum(self, i):
        i = int(i%self.m)#int(i % len(self.alphabet))
        return self.alphabet[i]
    def prepare(self, s):
        v = ""
        for c in s:
            if c.upper() in self.alphabet:
                v = v + c.upper()
        return v
    #-----------------DIGRAPHS-----------------#
    def digraphToInt(self,s):
        mm = self.getIndex(s[0])
        #print(m)
        n = self.getIndex(s[1])
        #print(n)
        return mm*26 + n
    def intToDigraph(self,i):
        n = i%26
        mm = self.charNum((i-n)/26)
        n = self.charNum(n)
        return mm+n
    #-----------------MATRICES-----------------#
    def string_to_matrix(self, str): #converts a string to a number matrix, reads vertically
        even_indices = []
        odd_indices = []
        for i in range(len(str)):
            if i%2 == 0:
                even_indices.append(self.getIndex(str[i]))
            else:
                odd_indices.append(self.getIndex(str[i]))
        str_indices = even_indices+odd_indices
        STR_MAT = Matrix(2,int(len(str)/2),str_indices)
        return STR_MAT
    def matrix_to_string(self, MAT, rowlength):
        top_indices = MAT[0:rowlength]
        bottom_indices = MAT[rowlength:]
        str = ""
        for a in range(rowlength*2):
            index = int(a/2)
            #print(index)
            if a%2 == 0:
                str+=self.charNum(top_indices[index])
            else:
                str+=self.charNum(bottom_indices[index])
        return str

'''
    def encrypt_diff_alph(self,plaintext):
        if len(plaintext)%2 != 0: plaintext+="X"
        ENC = Matrix([[7,5],[8,2]])
        P = self.string_to_matrix(plaintext)
        C = ENC*P
        C = matrix_mod(C,61)
        ciphertext = self.matrix_to_string(C,int(len(plaintext)/2))
        return ciphertext
'''
