# Implementasi Kriptografi Homofonik dengan Bahasa Python

Oleh Mohamad Rizky Irfianto & Rahmat Nur Azzis
       
Kriptografi homofonik adalah bagian dari kriptografi substitusi yang termasuk algoritma klasik. Disebut kriptografi *one-to-many* karena setiap huruf dalam *plainteks* akan dienkripsi menjadi *digram* atau lebih yang akan dibangun secara random dan dipilih secara random pula pada saat enkripsi. 

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
Plaintext = "KRIPTOGRAFI"
Ciphertext = ""
```

######Dekripsi
Untuk setiap  dua huruf(*digram*) di *ciphertext* disubtitusi dengan huruf sesuai dengan letak *digram* itu berada di tabel.
```
Contoh
Ciphertext = 
Plaintext = "KRIPTOGRAFI"
```

##Implementasi dengan bahasa python

Implementasi dibuat berdasarkan algoritma di atas. Tabel key dibuat menggunakan list dengan banyak elemen 26 yang didalamnya berisi array. Array tersebut akan diisi dengan dua huruf secara *random*. Untuk simbol dan huruf yang digunakan diatur pada *string* **huruf**. 

```python
huruf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Matrix = []
for i in range(26*4) : 
	a = random.choice(huruf) + random.choice(huruf)
	while(Matrix.__contains__(a) == True) : 
		a = random.choice(huruf) + random.choice(huruf)
	Matrix.append(a)

MatrixList = []
MatrixList = [Matrix[i:i+4] for i in range(0, len(Matrix), 4)]
```
Tabel key juga bisa dibuat sendiri dengan membuat *list* sebanyak 26 yang masing-masing berisi *array* yang isinya adalah *digram/polygram* tujuan. Kode *python* di bawah mendeskripsikan substitusi huruf A, B, dan C ke beberapa *digram*

```python
key = [["AB", "RR", "AP", "CM"], ["AS", "CV"], ["VD", "PO", "MK"]]
```

Pada saat enkripsi 


