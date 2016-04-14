# Implementasi Kriptografi Homofonik dengan Bahasa Python

Oleh Mohamad Rizky Irfianto & Rahmat Nur Azzis
       
Kriptografi homofonik adalah bagian dari kriptografi substitusi yang termasuk algoritma klasik. Disebut kriptografi *one-to-many* karena setiap huruf dalam *plaintext* akan dienkripsi menjadi *digram* atau lebih yang akan dibangun secara acak dan dipilih secara acak pula pada saat enkripsi. 

NOTE : Pada implementasi homofonik ini, kami hanya menggunakan **digram** dari huruf kapital

##Latar Belakang

Substitusi *cipher* alfabet tunggal dan alfabet majemuk mempunyai kelemahan di frekuensi karakter, dimana *plaintext* yang sama memiliki *ciphertext* yang sama pula. Dengan cipher homofonik kejadian tersebut dapat dihindari, *plaintext* yang sama memiliki *ciphertext* yang berbeda.

##Algoritma

######Key
Key digambarkan sebagai tabel yang memetakan setiap huruf dengan **digram**. Setiap digram harus berbeda satu sama lain untuk menghindari kesalahan pada saat dekripsi.

```
Key :
A | DF BC LO PE
B | OF MC WK RL
C | AF CC PQ DE
.
.
Z | MM CF AZ RE
```

######Enkripsi
Untuk setiap huruf di *plaintext* disubtitusi dengan *digram* yang dipilih secara ***random***.
```
Contoh
Key:
A| KI VU KB FA
B| TS OC HR YN
C| NZ TL ON LB
D| UY ES IE WV
E| TJ YW NC UE
F| SV RX KC LZ
G| DF RY BD HH
H| BJ DO QU XJ
I| ZG MH EC FE
J| SA OU NB HF
K| VH UI OD DJ
L| RN XW ST OY
M| LL JO XV PC
N| QW HO PA WB
O| EQ OZ PK MX
P| GV MM FR PR
Q| RU KV SY CP
R| CQ TC MK KP
S| VS MB CV MI
T| VC ZS KY LG
U| JZ BC JC QG
V| CD QT TT MZ
W| LY AC CJ AE
X| DT OF XH OW
Y| MT AU VD LO
Z| YX OS ZC UX
PLAINTEXT = KRIPTOGRAFIILMUKOMPUTER
CIPHERTEXT = DJTCMHGVLGPKRYCQKBLZECECXWLLJCUIPKLLFRJZKYTJCQ
```

######Dekripsi
Untuk setiap  dua huruf(*digram*) di *ciphertext* disubtitusi dengan huruf sesuai dengan letak *digram* itu berada di tabel.
```
Contoh
CIPHERTEXT = DJTCMHGVLGPKRYCQKBLZECECXWLLJCUIPKLLFRJZKYTJCQ
	-> Untuk setiap 2 huruf, cari di tabel key di baris mana ia berada. Lalu substitusikan menjadi huruf yang berkorespondensi.
	('DJ', 'TC', 'MH', 'GV', 'LG', 'PK', 'RY', 'CQ', 'KB', 'LZ', 'EC', 'EC', 'XW', 'LL', 'JC', 'UI', 'PK', 'LL', 'FR', 'JZ', 'KY', 'TJ', 'CQ')
	-> Substitusikan
	('K', 'R', 'I', 'P', 'T', 'O', 'G', 'R', 'A', 'F', 'I', 'I', 'L', 'M', 'U', 'K', 'O', 'M', 'P', 'U', 'T', 'E', 'R')

PLAINTEXT = KRIPTOGRAFIILMUKOMPUTER
```

##Implementasi dengan bahasa python

Implementasi dibuat berdasarkan algoritma di atas. Tabel key dibuat menggunakan list dengan banyak elemen 26 yang didalamnya berisi array. Array tersebut akan diisi dengan dua huruf secara *random*. Untuk simbol dan huruf yang digunakan diatur pada *string* **huruf**.  Hasil dari kode di bawah adalah *list* dengan 26 elemen (index ke-0 artinya huruf "A", index ke-25 huruf "Z") yang berisi *array*. 

```python
huruf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = []
for i in range(26*4) : 
	a = random.choice(huruf) + random.choice(huruf)
	while(key.__contains__(a) == True) : 
		a = random.choice(huruf) + random.choice(huruf)
	key.append(a)

keyList = []
keyList = [key[i:i+4] for i in range(0, len(key), 4)]
```
Tabel key juga bisa dibuat sendiri dengan membuat *list* sebanyak 26 yang masing-masing berisi *array* yang isinya adalah *digram/polygram* tujuan. Kode *python* di bawah mendeskripsikan substitusi huruf A, B, dan C ke beberapa *digram*

```python
key = [["AB", "RR", "AP", "CM"], ["AS", "CV"], ["VD", "PO", "MK"]]
```

Pada saat enkripsi, untuk setiap karakter di *plaintext* akan diubah menjadi *digram* yang sesuai dengan cara acak. Pemilihan secara random menggunakan *library random* dan menggunkan fungsi *random.choice* menggunakan *seed default*.

```python
for a in plaintext : 
	ciphertext += random.choice(keyList[ord(a)-65])
```

Untuk dekripsi hal yang pertama dilakukan adalah membagi string plainteks menjadi *digram* ke dalam suatu *list*. Lalu untuk setiap elemen *digram* di list tersebut akan dicari apakah *digram* tersebut ada pada suatu elemen di keyList , jika ada maka substitusikan sesuai dengan index elemen ditambah 65 (*ascii*).

```python
dPlaintext = ""
cipherList = []
[cipherList.append(ciphertext[i:i+2]) for i in range(0, len(ciphertext), 2)]
print cipherList

for i in cipherList :
	for x in range(26):
		if keyList[x].__contains__(i) == True : 
			dPlaintext += chr(x+65)
			
print dPlaintext
```

######Contoh Run
![alt tag](https://github.com/kesenggol/HomophonicCipher/raw/master/run.jpg)


