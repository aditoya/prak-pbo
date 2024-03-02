"""
Aditya Wahyu Suhendar
122140235
Praktikum PBO RB (Asal kelas RC)
Soal 2 (Mencari Jumlah Bilangan Ganjil diantara Batas Bawah dan Batas Atas)
"""

def Ganjil(bawah, atas): # fungsi bernama Ganjil dengan argumen bawah dan atas
  if bawah < 0 or atas < 0: # percabangan untuk mengecek apakah batas bawah atau batas atas dibawah 0
    print("Batas bawah dan atas yang dimasukan tidak boleh di bawah Nol")
    return 0 # mengembalikan nilai 0 jika  salah satu dari batas bawah atau batas atas adalah dibawah nol

  jumlahGanjil = 0 # men-set nilai 0 agar nanti bertambah seiring  proses looping

  for i in range(bawah, atas + 1): # melakukan looping dengan kondisi awal "bawa"
    if i % 2 == 1: # ketika i dibagi 2 sisa 1 maka  ganjil
      jumlahGanjil += 1 #  jika ganjil maka nilai jumlahGanjil akan bertambah 1 setiap perulangannya

  return jumlahGanjil # mengembalikan nilai  jumlah bilangan ganjil

bawah = int(input("Inputkan batas bawah : ")) # user menginputkan batas bawah dengan tipe data integer
atas = int(input("Inputkan batas atas  : ")) # user menginputkan batas atas dengan tipe data integer

jumlahGanjil = Ganjil(bawah, atas) # membuat variabel jumlahGanjil dengan memanggil fungsi Ganjil() disertai paramter bawah dan atas

print(bawah) # untuk mencetak batas bawah
print(atas) # untuk mencetak batas atas
print(f"Total : {jumlahGanjil}") # untuk menampilkan jumlah bilangan ganjil dari interval batas bawah s.d batas atas
