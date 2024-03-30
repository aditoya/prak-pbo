"""
Aditya Wahyu Suhendar
122140235
Praktikum PBO RB (Asal kelas RC)
Soal 1
Modul 4
"""

class Hewan:
    def __init__(self, nama, jenis_kelamin):
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin

    def bersuara(self):
        raise NotImplementedError

    def makan(self):
        print(f"{self.__class__.__name__} {self.nama} sedang makan: tulang")

    def minum(self):
        print(f"{self.__class__.__name__} {self.nama} sedang minum: air")

class Kucing(Hewan):
    def bersuara(self):
        print(f"{self.__class__.__name__} {self.nama} bersuara: Meong!")

class Anjing(Hewan):
    def bersuara(self):
        print(f"{self.__class__.__name__} {self.nama} bersuara: Guk Guk!")

hewan1 = Kucing("Kiki", "Betina")
hewan2 = Anjing("Ichi", "Jantan")

print(hewan1.nama) 
print(hewan2.nama)

hewan1.bersuara() 
hewan1.makan() 
hewan2.bersuara() 
hewan2.makan() 