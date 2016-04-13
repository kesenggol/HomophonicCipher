# Implementasi Kriptografi Homofonik dengan Python

Oleh Mohamad Rizky Irfianto & Rahmat Nur Azzis
       
Kriptografi homofonik adalah bagian dari kriptografi subtitusi yang termasuk algoritma klasik. Disebut kriptografi *one-to-many* karena setiap huruf dalam *plainteks* akan dienkripsi menjadi **digram** atau lebih yang akan digenerasi secara random dan dipilih secara random juga pada saat enkripsi. 

NOTE : Pada implementasi homofonik ini, kami hanya menggunakan **digram**(dua huruf)

##Latar Belakang

Subtitusi cipher alfabet tunggal dan alfabet majemuk mempunyai kelemahan di frekuensi karakter, dimana *plaintext* yang sama memiliki *ciphertext* yang sama pula. Dengan cipher homofonik kejadian tersebut dapat dihindari, *plaintext* yang sama memiliki *ciphertext* yang berbeda.

##Algoritma

########Key
Key digambarkan sebagai tabel yang memetakan setiap huruf dengan **digram**. Setiap digram harus berbeda satu sama lain untuk menghindari **collision**.

```
Key :
A | DF BC LO PE
B | OF MC WK RL
C | AF CC PQ DE
.
.
Z | MM CF AZ RE
```

########Enkripsi
Untuk setiap huruf di **plaintext disubtitusi dengan **digram** yang dipilih secara **random**.
```
