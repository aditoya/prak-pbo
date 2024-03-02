"""
Aditya Wahyu Suhendar
122140235
Praktikum PBO RB (Asal kelas RC)
Soal 2 (Mencari Jumlah Bilangan Ganjil diantara Batas Bawah dan Batas Atas)
"""

def Ganjil(bawah, atas):
  if bawah < 0 or atas < 0:
    print("Batas bawah dan atas yang dimasukan tidak boleh di bawah Nol")
    return 0

  jumlahGanjil = 0 

  for i in range(bawah, atas + 1):
    if i % 2 == 1:
      jumlahGanjil += 1

  return jumlahGanjil

bawah = int(input("batas bawah : "))
atas = int(input("batas atas  : "))

jumlahGanjil = Ganjil(bawah, atas)

print(bawah)
print(atas)
print(f"Total : {jumlahGanjil}")