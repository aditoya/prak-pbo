"""
Aditya Wahyu Suhendar
122140235
Praktikum PBO RB (Asal kelas RC)
Soal 2 (Mencari Luas & Keliling Lingkaran)
"""

from math import pi # mengimport pi untuk kebutuhan perhitungan lingkaran, phi = 3.14 atau 22/7

def Hitung(jari):    
    luas = pi * jari **2
    keliling = 2 * pi * jari 
    return luas, keliling

try:
    jari = float(input("jari-jari : "))
    
    if jari >= 0:
        luas, keliling = Hitung(jari)
        print(f"Luas: {luas:.2f}")
        print(f"Keliling: {keliling:.2f}")
    else:
        print("jari-jari lingkaran tidak boleh negatif")
except ValueError: # akan dijalankan jika inputan selain angka 
    print("Masukkan yang Anda berikan tidak valid, harap masukkan angka!")