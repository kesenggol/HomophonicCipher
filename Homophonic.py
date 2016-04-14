###Implementasi Homophonic Cipher###

#Menggunakan Python 2.75
#Input berupa String, tidak boleh menggunakan special karakter kecuali 'spasi'
#Dibuat oleh : Mohamad Rizky Irfianto dan Rahmat Nur Azzis

import random

##Random Key##
huruf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
key = []
for i in range(26*4) : 
	a = random.choice(huruf) + random.choice(huruf)
	while(key.__contains__(a) == True) : 
		a = random.choice(huruf) + random.choice(huruf)
	key.append(a)

keyList = []
keyList = [key[i:i+4] for i in range(0, len(key), 4)]

##Print Key##
print "Library KEY Homofonik Cipher"
print "--------------------------------------------------------------"
for i in range(26):
	print chr(i+65) + " : " + str(keyList[i])
print "--------------------------------------------------------------"

##Encryption##
def encryption(plain):
        dCiphertext = ""
        for a in plain : 
                dCiphertext += random.choice(keyList[ord(a)-65])
        return dCiphertext

##Decryption##
def decryption(cipher):
        dPlaintext = ""
        cipherList = []
        [cipherList.append(cipher[i:i+2]) for i in range(0, len(cipher), 2)]

        for i in cipherList :
                for x in range(26):
                        if keyList[x].__contains__(i) == True : 
                                dPlaintext += chr(x+65)
        return dPlaintext

##Set Plaintext##
while 1:
        plaint = raw_input("Masukkan Plaintext : ")
        plaintext = plaint.upper().replace(" ","")
        print "Plaintext : " + plaintext
        ciphertext = encryption(plaintext)
        print "--------------------------------------------------------------"
        print "Hasil Encryption : " + ciphertext
        print "Hasil Decryption : " + decryption(ciphertext)      

