"""
Aditya Wahyu Suhendar
122140235
Praktikum PBO RB (Asal kelas RC)
Soal 2 (Mencari Luas & Keliling Lingkaran)
"""

from math import pi # mengimport pi untuk kebutuhan perhitungan lingkaran, phi = 3.14 atau 22/7

def Hitung(jari): # fungsi bernama Hitung dengan parameter jari    
    luas = pi * jari **2  # mencari luas lingkaran 
    keliling = 2 * pi * jari  # mencari  keliling lingkaran
    return luas, keliling # mengembalikan nilai luas dan keliling lingkaran

try: # digunakan untuk menjalankan blok kode dan menangkap error yang mungkin terjadi.
    jari = float(input("Inputkan jari-jari : ")) # user menginputkan jari-jari
    
    if jari >= 0: # jika jari-jari yang dinputkan user lebih dari sama dengan 0, maka
        luas, keliling = Hitung(jari) # jari-jari yang diinputkan user akan dihitung dengan memanggil fungsi  Hitung()
        print(f"Luas: {luas:.2f}") # 2f berfungsi agar maksimal 2 angka dibelakang koma
        print(f"Keliling: {keliling:.2f}") # 2f berfungsi agar maksimal 2 angka dibelakang koma
    else: # jika tidak
        print("jari-jari lingkaran tidak boleh negatif")
except ValueError: # akan dijalankan jika inputan selain angka 
    print("Masukkan yang Anda berikan tidak valid, harap masukkan angka!")
