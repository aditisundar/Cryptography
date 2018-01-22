file1 = open("vignere_puzzles.txt", 'r')
alpha = "abcdefghijklmnopqrstuvwxyz"

def caesar_shift(plaintext, char):
    shift = alpha.index(char)
    final = ""
    #for c in plaintext:
        #print(c, end="")
    for c in plaintext:
        current_index = alpha.index(c)
        shift_index = current_index + shift
        if(shift_index > 0):
            shift_index -= 26
        #print(alpha[shift_index], end="")
        final += alpha[shift_index]
    return final
def caesar_unshift(ciphertext, char):
    shift = alpha.index(char)
    final = ""
    for c in ciphertext:
        current_index = alpha.index(c)
        shift_index = current_index - shift
        if(shift_index < 0):
            shift_index += 26
        #print(alpha[shift_index], end="")
        final += alpha[shift_index]
    return final
def caesar_brute_force(ciphertext):
    shift = 0
    ciphertext = ciphertext[0:8]
    print(ciphertext)
    for i in range(26):
        print(alpha[i], ": ")
        final = ""
        for c in ciphertext:
            current_index = alpha.index(c)
            shift_index = current_index - shift
            if(shift_index < 0):
                shift_index += 26
                
            print(alpha[shift_index], end="")
            final += alpha[shift_index]
        print("")
        shift += 1
        
def vignere_encode(plaintext, keyword):
    while len(keyword)<len(plaintext):
        keyword += keyword
    keyword = keyword[0:len(plaintext)]
    final = ""
    for i in range(len(keyword)):
        final += caesar_shift(plaintext[i], keyword[i])
    print(final)
def vignere_decode(plaintext, keyword):
    while len(keyword)<len(plaintext):
        keyword += keyword
    keyword = keyword[0:len(plaintext)]
    final = ""
    for i in range(len(keyword)):
        final += caesar_unshift(plaintext[i], keyword[i])
    print(final)
#caesar_shift("pineapple", 'B')
#caesar_unshift("qjofbqqmf", 'B')
#caesar_brute_force("abcdefghijklmnop")
vignere_decode("afahipgo", "summer")

