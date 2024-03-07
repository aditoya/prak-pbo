"""
Aditya Wahyu Suhendar
122140235
Praktikum PBO RB (Asal kelas RC)
Soal 1
Praktikum-2
"""

class Mahasiswa:
    def __init__(self, nim, nama, kelas_mahasiswa, isMahasiswa=True):
        self.__nim = nim
        self.__nama = nama
        self.__kelas_mahasiswa = kelas_mahasiswa
        self.__isMahasiswa = isMahasiswa

    # Getter & Setter untuk 'nama'
    def dapatkan_nama(self):
        return self.__nama

    def atur_nama(self, nama_baru):
        self.__nama = nama_baru

    # Getter & Setter untuk 'nim'
    def dapatkan_nim(self):
        return self.__nim

    def atur_nim(self, nim_baru):
        self.__nim = nim_baru

    def dapatkan_status_mahasiswa(self):
        return self.__isMahasiswa

    def daftar(self):
        if self.__isMahasiswa:
            return f"{self.__nama} telah mendaftar di kelas {self.__kelas_mahasiswa}."
        else:
            return f"{self.__nama} bukan mahasiswa."

    def kumpulkan_tugas(self):
        return f"{self.__nama} telah mengumpulkan tugas untuk kelas {self.__kelas_mahasiswa}."

    def ikuti_ujian(self):
        return f"{self.__nama} sedang mengikuti ujian untuk kelas {self.__kelas_mahasiswa}."


mahasiswa1 = Mahasiswa(nim="122140235", nama="Aditya Wahyu Suhendar", kelas_mahasiswa="RA")
mahasiswa2 = Mahasiswa(nim="122140236", nama="Rayhan Fadel Irwanto", kelas_mahasiswa="RB", isMahasiswa=False)

# Menggunakan getter dan setter untuk mengambil dan mengganti nilai
print(f"Sebelum menggunakan setter :\n- Nama : {mahasiswa1.dapatkan_nama()} \n- NIM  : {mahasiswa1.dapatkan_nim()}")
mahasiswa1.atur_nama("Jason Surya Padantya")
mahasiswa1.atur_nim("122140237")
print(f"Sesudah menggunakan setter :\n- Nama : {mahasiswa1.dapatkan_nama()} \n- NIM  : {mahasiswa1.dapatkan_nim()}\n")

print(mahasiswa1.daftar())
print(mahasiswa1.kumpulkan_tugas())
print(mahasiswa1.ikuti_ujian())

print("\n" + "=" * 75)

print(f"\nSebelum menggunakan setter :\n- Nama : {mahasiswa2.dapatkan_nama()} \n- NIM  : {mahasiswa2.dapatkan_nim()}")
print(f"Sesudah menggunakan setter :\n- Nama : {mahasiswa2.dapatkan_nama()} \n- NIM  : {mahasiswa2.dapatkan_nim()}\n")

print(mahasiswa2.daftar())
