"""
Aditya Wahyu Suhendar
122140235
Praktikum PBO RB (Asal kelas RC)
Soal 2
Praktikum-2
"""

def panggilMethod(func):
    def wrapper(*args, **kwargs):
        print(f"\nMemanggil metode: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Metode {func.__name__} selesai.")
        return result
    return wrapper

class Router:
    def __init__(self, model, mac_address, ip_address):
        self.model = model
        self.mac_address = mac_address
        self.ip_address = ip_address
        print(f"\nRouter {self.model} diinisialisasi.\nAlamat MAC: {self.mac_address}\nAlamat IP: {self.ip_address}")

    @panggilMethod
    def configure(self, settings):
        print(f"\nMengonfigurasi router {self.model} dengan pengaturan: {settings}")

    def __del__(self):
        print(f"\nRouter {self.model} sedang dimatikan.\nAlamat MAC: {self.mac_address}\nAlamat IP: {self.ip_address}")

if __name__ == "__main__":
    cisco = Router(model="Cisco", mac_address="00:11:22:33:44:55", ip_address="192.168.1.1")
    mikrotik = Router(model="MikroTik", mac_address="AA:BB:CC:DD:EE:FF", ip_address="192.168.1.2")

    cisco.configure(settings={"SSID": "CiscoNetwork", "Password": "CiscoSecurePassword"})
    mikrotik.configure(settings={"SSID": "MikroTikNetwork", "Password": "MikroTikSecurePassword"})

    del cisco
    del mikrotik
