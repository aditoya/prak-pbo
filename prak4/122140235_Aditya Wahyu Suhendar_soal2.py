"""
Aditya Wahyu Suhendar
122140235
Praktikum PBO RB (Asal kelas RC)
Soal 2
Modul 4
"""

from math import pi

class BangunDatar:
    def hitungLuas(self):
        raise NotImplementedError

class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi

    def hitungLuas(self):
        return self.sisi ** 2

class Lingkaran(BangunDatar):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def hitungLuas(self):
        return pi * (self.jari_jari ** 2)

persegi = Persegi(int(input("Inputkan sisi persegi\t\t: ")))
lingkaran = Lingkaran(int(input("Inputkan jari-jari lingkaran\t: ")))

print(f"\nLuas Persegi\t: {persegi.hitungLuas()}") 
print(f"Luas Lingkaran\t: {lingkaran.hitungLuas()}") 