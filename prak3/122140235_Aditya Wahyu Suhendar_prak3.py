"""
Aditya Wahyu Suhendar
122140235
Praktikum PBO RB (Asal kelas RC)
Soal 2
Modul 3
"""

class Dagangan:
    jumlah_barang = 0
    barang = []

    def __init__(self, nama, stok, harga):
        self.__nama = nama
        self.__stok = stok
        self.__harga = harga

        Dagangan.jumlah_barang += 1
        Dagangan.barang.append((nama, stok, harga))

    @classmethod
    def lihat_barang(cls):
        print(f"Jumlah barang dagangan pada toko: {cls.jumlah_barang} buah")
        for i, barang in enumerate(cls.barang, start=1):
            print(f"{i}. {barang[0]} seharga Rp {barang[2]} (stok: {barang[1]})")

    def __del__(self):
        Dagangan.jumlah_barang -= 1
        for barang in Dagangan.barang:
            if barang[0] == self.__nama:
                print(f"\n{self.__nama} dihapus dari toko!\n")
                Dagangan.barang.remove(barang)
                break

    def __str__(self):
        return f"{self.__nama} seharga Rp {self.__harga} (stok: {self.__stok})"


# Contoh penggunaan
Dagangan1 = Dagangan("Galon Aqua 19L", 32, 17000)
Dagangan2 = Dagangan("Gas LPG 5 kg", 22, 88000)
Dagangan3 = Dagangan("Beras Ramos 5 kg", 13, 68000)
Dagangan.lihat_barang()

del Dagangan1
Dagangan.lihat_barang()
