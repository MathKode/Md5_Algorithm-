from math import sin, floor

def little_endian(hexa_liste):
    #Enter : ["32","A6","DE","4F"]
    #Output : 1339991602
    hexa_list2 = hexa_liste[::-1] # retourne la liste ["32","A6","DE","4F"] -> ['4F', 'DE', 'A6', '32']
    hexa_nb = "".join(hexa_list2) # Colle les éléments de la liste
    return hexa_to_number(hexa_nb)

def hexa_to_number(hexa):
    #Input : 7A1
    #Output : 1953
    l = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    finalbit = ""
    for i in str(hexa):
        nb = 0
        t = 0
        for j in l:
            if j == i:
                nb = t
            t += 1
        bit = ""
        if nb-8 >= 0 : bit += "1"; nb = nb - 8
        else : bit += "0"
        if nb-4 >= 0 : bit += "1"; nb = nb - 4
        else : bit += "0"
        if nb-2 >= 0 : bit += "1"; nb = nb - 2
        else : bit += "0"
        if nb-1 >= 0 : bit += "1"; nb = nb - 1
        else : bit += "0"
        finalbit += bit
    r = 0
    t = 0
    for i in list(finalbit)[::-1]:
        if i == "1":
            r += 2**t
        t += 1
    return r

def number_to_hexa(number):
    #Enter : 1953
    #Output : 7A1
    l = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    binary = str(bin(number))[2:]
    while len(binary)%4 != 0 :
        binary = "0" + binary
    groupe = []
    for i in range(0,int(len(binary)/4)) :
        groupe.append(binary[i*4:(i+1)*4])
    final = ""
    for i in groupe:
        nb = 0
        if i[0] == "1": nb+=8
        if i[1] == "1": nb+=4
        if i[2] == "1": nb+=2
        if i[3] == "1": nb+=1
        final += l[nb]
    return final 

def text_to_octet(text):
    #Enter : salut
    #Output : 01110011 01100001 01101100 01110101 01110100
    finalresult = ""
    for i in text:
        r = ""
        po = ord(i)
        if po - 128 >= 0 : r+="1";po=po-128
        else:r+="0"
        if po - 64 >= 0 : r+="1";po=po-64
        else:r+="0"
        if po - 32 >= 0 : r+="1";po=po-32
        else:r+="0"
        if po - 16 >= 0 : r+="1";po=po-16
        else:r+="0"
        if po - 8 >= 0 : r+="1";po=po-8
        else:r+="0"
        if po - 4 >= 0 : r+="1";po=po-4
        else:r+="0"
        if po - 2 >= 0 : r+="1";po=po-2
        else:r+="0"
        if po - 1 >= 0 : r+="1";po=po-1
        else:r+="0"
        finalresult += r
    return finalresult

def number_to_bits(number):
    number = int(number)
    bits = ""
    while number != 0:
        if number % 2 == 0 :
            bits += "0"
        else :
            bits += "1"
        number = number // 2
    bits = "".join(list(bits)[::-1])
    return bits

def bits_to_number(bits):
    result = 0
    t = 0
    for i in str(bits)[::-1]:
        result += int(i) * (2**t)
        t += 1
    return result

def EQUILIBREUR(A,B):
    #equilibre le nombre de bit entre A et B
    if len(A) == len(B):
        return A, B
    if len(A) > len(B):
        while len(A) > len(B):
            B = "0" + B
        return A, B
    if len(B) > len(A):
        while len(B) > len(A):
            A = "0" + A
        return A, B

def AND(A,B):
    A, B = EQUILIBREUR(A,B)
    result = ""
    for i in range(0,len(A)):
        if A[i] == "1" and B[i] == "1":
            result += "1"
        else :
            result += "0"
    return result

def OR(A,B):
    A, B = EQUILIBREUR(A,B)
    result = ""
    for i in range(0,len(A)):
        if A[i] == "0" and B[i] == "0":
            result += "0"
        else :
            result += "1"
    return result

def XOR(A,B):
    A, B = EQUILIBREUR(A,B)
    result = ""
    for i in range(0,len(A)):
        if A[i] == "0" and B[i] == "1":
            result += "1"
        elif A[i] == "1" and B[i] == "0":
            result += "1"
        else :
            result += "0"
    return result

def NOT(A):
    result = ""
    for i in A:
        if i == "1":
            result += "0"
        else :
            result += "1"
    return result

def LEFT_ROTATE(bits,s):
    for i in range(0,int(s)):
        bits = bits[1:] + bits[0]
    return bits 

def F(B,C,D):
    result = OR(AND(B,C),AND(NOT(B),D))
    return result

def G(B,C,D):
    result = OR(AND(B,D),AND(C,NOT(D)))
    return result

def H(B,C,D):
    result = XOR(XOR(B,C),D)
    return result

def I(B,C,D):
    result = XOR(C,OR(B,NOT(D)))
    return result

#Déclaration des rotations (pour chaque itération)
s_rotation = [7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,
              5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,
              4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,
              6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21]

#Création de toutes les constantes 
k_constante = []
for i in range(0,64):
    calcul = floor(abs(sin((i+1))*2**32)) #Une constante est obtenue avec : 2^32 * sin(i+1)
    k_constante.append(calcul)

#Demande du message + initialisation des tours (>448bits) + Padding
msg = input('->')
lenmsg = len(msg)*8 #Le * 8 car 1 octet = 8 bit
lmsg2 = number_to_hexa(lenmsg)
if len(lmsg2)%2 != 0 :
    lmsg2 = "0" + lmsg2
# Tranforme la réponse hexa collée en décolée
# Exemple : ADFE3D -> AD FE 3D (format liste)
t = 0;m = "";r=[]
for i in lmsg2:
    if t == 1:
        m += i
        r.append(m)
        t=0
        m = ""
    else :
        m += i
        t += 1
while len(r) < 8 :
    r.append("00")
#convertir la liste de la longueur en nombre puis en binaire :
result = []
for i in r :
    nb = hexa_to_number(i)
    b = number_to_bits(nb)
    while len(b) < 8 :
        b = "0" + b
    result.append(b)
print(result)
msg_len_binary = "".join(result) #Taille du message en binaire

tour = ((len(msg)*8)//448) + 1

print(msg)

#Initialisation des groupes
bloc_message = []
for i in range(0,tour):
    if len(msg) >= 64 :
        print('Not Padding')
        message = msg[0:64]
        binary = text_to_octet(message)
        bloc_message.append(binary)
        msg = msg[64:]
    else :
        print('Padding')
        message = msg
        message = text_to_octet(message)
        t = 0
        while len(message)<448:
            if t == 0 :
                t = 1
                message += "1"
            else:
                message += "0"
        message += msg_len_binary
        bloc_message.append(message)   
print(bloc_message)

A = "1100111010001010010001100000001"
B = "11101111110011011010101110001001"
C = "10011000101110101101110011111110"
D = "10000001100100101010001110110"

for bloc in bloc_message :
    
    #Couper le message en 16 blocs de 32 bits version little endina (mot)
    mot = []
    for i in range(0,16):
        bit = bloc[i*32:(i+1)*32]
        ls = []
        for tt in range(0,4):
            octet = bit[tt*8:(tt+1)*8]
            val = bits_to_number(octet)
            hexaval = number_to_hexa(val)
            ls.append(hexaval)
        re = little_endian(ls)
        bit = number_to_bits(re)
        while len(bit) < 32 :
            bit = '0' + bit
        mot.append(bit)

    #Boucles principales
    for i in range(0,64): # 16 + 16 + 16 + 16 (16 itération avec la fonction F, puis G, puis H, puis I)
        if i <= 15 : #16 Première iterations
            f = F(B,C,D)
            word = i #word est utilisé pour désigner le mot utilisé 
        elif i >= 16 and i <= 31 :
            f = G(B,C,D)
            word = (5*i +1)%16
        elif i >= 32 and i <= 47 :
            f = H(B,C,D)
            word = (3*i + 5)%16
        elif i >= 48 :
            f = I(B,C,D)
            word = (7*i)%16
        a_ = bits_to_number(A) 
        f_ = bits_to_number(f) 
        k_ = k_constante[i] #Constante
        w_ = bits_to_number(mot[word]) # Message
        addition = (int(a_) + int(f_) + int(k_) + int(w_))%(2**32)
        bit = number_to_bits(addition)
        while len(bit) < 32 :
            bit = "0" + bit
        rotate = LEFT_ROTATE(bit,s_rotation[i])
        final = number_to_bits(int(bits_to_number(rotate)) + int(bits_to_number(B)))
        A = D
        D = C
        C = B
        B = final
    A = number_to_bits(int(bits_to_number(A) + 1732584193)%(2**32))
    B = number_to_bits(int(bits_to_number(B) + 4023233417)%(2**32))
    C = number_to_bits(int(bits_to_number(C) + 2562383102)%(2**32))
    D = number_to_bits(int(bits_to_number(D) + 271733878)%(2**32))

a_ = str(number_to_hexa(bits_to_number(A)))
b_ = number_to_hexa(bits_to_number(B))
c_ = number_to_hexa(bits_to_number(C))
d_ = number_to_hexa(bits_to_number(D))
final_result = ""
for variable in [a_,b_,c_,d_]:
    while len(variable)<8:
        variable = "0" + variable
    t = 0
    hexa_list = []
    r = ''
    for c in str(variable):
        if t == 1 :
            r += c
            hexa_list.append(r)
            r = ''
            t = 0
        else :
            r += c
            t += 1
    print(hexa_list)
    result = little_endian(hexa_list)
    final_result += number_to_hexa(result).lower()
print(final_result)