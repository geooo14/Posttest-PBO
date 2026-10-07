import os


# =========================================================
# CLEAR TERMINAL
# =========================================================
def clear():
    os.system("cls" if os.name == "nt" else "clear")


# =========================================================
# CLASS PELANGGAN
# =========================================================
class Pelanggan:
    def __init__(self, id_pelanggan, nama, username, password, saldo=0):
        self.id_pelanggan = id_pelanggan
        self._nama = nama
        self.username = username
        self.password = password
        self.saldo = saldo

    @property
    def nama(self):
        return self._nama

    @nama.setter
    def nama(self, nama_baru):
        self._nama = nama_baru

    def tampilkan_data(self):
        print(f"ID       : {self.id_pelanggan}")
        print(f"Nama     : {self.nama}")
        print(f"Username : {self.username}")
        print(f"Saldo    : Rp{self.saldo:,}")


# =========================================================
# SUPERCLASS DRONE
# =========================================================
class Drone:
    def __init__(self, id_drone, nama, harga_sewa):
        self.id_drone = id_drone
        self._nama = nama
        self.__harga_sewa = harga_sewa
        self.status = "Tersedia"

    @property
    def nama(self):
        return self._nama

    @nama.setter
    def nama(self, nama_baru):
        self._nama = nama_baru

    @property
    def harga_sewa(self):
        return self.__harga_sewa

    @harga_sewa.setter
    def harga_sewa(self, harga_baru):
        self.__harga_sewa = harga_baru

    def tampilkan_data(self):
        print(f"ID Drone  : {self.id_drone}")
        print(f"Nama      : {self.nama}")
        print(f"Harga     : Rp{self.harga_sewa:,}")
        print(f"Status    : {self.status}")


# =========================================================
# SUBCLASS DRONE KAMERA
# INHERITANCE DARI CLASS DRONE
# =========================================================
class DroneKamera(Drone):
    def __init__(self, id_drone, nama, harga_sewa, resolusi):
        super().__init__(id_drone, nama, harga_sewa)
        self.resolusi = resolusi

    # OVERRIDING
    def tampilkan_data(self):
        print(f"ID Drone  : {self.id_drone}")
        print(f"Nama      : {self.nama}")
        print(f"Harga     : Rp{self.harga_sewa:,}")
        print(f"Resolusi  : {self.resolusi}")
        print(f"Status    : {self.status}")


# =========================================================
# SUBCLASS DRONE BALAP
# INHERITANCE DARI CLASS DRONE
# =========================================================
class DroneBalap(Drone):
    def __init__(self, id_drone, nama, harga_sewa, kecepatan):
        super().__init__(id_drone, nama, harga_sewa)
        self.kecepatan = kecepatan

    # OVERRIDING
    def tampilkan_data(self):
        print(f"ID Drone  : {self.id_drone}")
        print(f"Nama      : {self.nama}")
        print(f"Harga     : Rp{self.harga_sewa:,}")
        print(f"Kecepatan : {self.kecepatan}")
        print(f"Status    : {self.status}")


# =========================================================
# COMPOSITION
# DETAIL PENYEWAAN
# =========================================================
class DetailPenyewaan:
    def __init__(self, drone, durasi):
        self.drone = drone
        self.durasi = durasi
        self.subtotal = drone.harga_sewa * durasi

    def tampilkan_detail(self):
        print(f"Drone     : {self.drone.nama}")
        print(f"Durasi    : {self.durasi} hari")
        print(f"Subtotal  : Rp{self.subtotal:,}")


# =========================================================
# ASSOCIATION + COMPOSITION
# CLASS PENYEWAAN
# =========================================================
class Penyewaan:
    def __init__(self, pelanggan):
        self.pelanggan = pelanggan
        self.detail = None
        self.pajak = 10
        self.total = 0
        self.status = "Belum Diproses"

    def buat_penyewaan(self, drone, durasi):
        # COMPOSITION
        self.detail = DetailPenyewaan(drone, durasi)

        pajak = self.detail.subtotal * self.pajak / 100
        self.total = self.detail.subtotal + pajak

        return self.total

    def proses(self):
        if self.detail is None:
            print("Belum ada data penyewaan.")
            return False

        if self.pelanggan.saldo < self.total:
            print("Saldo tidak mencukupi.")
            return False

        self.pelanggan.saldo -= self.total
        self.detail.drone.status = "Disewa"
        self.status = "Selesai"

        return True

    def tampilkan_data(self):
        print("\n===== DATA PENYEWAAN =====")
        print(f"Pelanggan : {self.pelanggan.nama}")

        if self.detail:
            self.detail.tampilkan_detail()

            pajak = self.detail.subtotal * self.pajak / 100

            print(f"Pajak 10% : Rp{pajak:,.0f}")
            print(f"Total     : Rp{self.total:,.0f}")

        print(f"Status    : {self.status}")


# =========================================================
# AGGREGATION
# ARMADA DRONE
# Drone tetap dapat berdiri sendiri walaupun ArmadaDrone
# dihapus.
# =========================================================
class ArmadaDrone:
    def __init__(self):
        self.daftar_drone = []

    def tambah_drone(self, drone):
        self.daftar_drone.append(drone)

    def tampilkan_semua(self):
        print("\n===== DATA DRONE =====")

        for drone in self.daftar_drone:
            print("----------------------------")
            drone.tampilkan_data()


# =========================================================
# DATA AWAL
# =========================================================

pelanggan_list = [
    Pelanggan(
        "P001",
        "Geo",
        "geo",
        "121",
        500000
    ),
    Pelanggan(
        "P002",
        "Budi",
        "budi",
        "123",
        300000
    )
]


# Drone lama tetap ada
drone1 = DroneKamera(
    "D001",
    "DJI Mini 4 Pro",
    150000,
    "4K"
)

drone2 = DroneBalap(
    "D002",
    "DJI Avata 2",
    200000,
    "97 km/jam"
)


# AGGREGATION
armada = ArmadaDrone()
armada.tambah_drone(drone1)
armada.tambah_drone(drone2)


# =========================================================
# LOGIN
# =========================================================
def login():
    clear()

    print("===================================")
    print("     SISTEM PENYEWAAN DRONE")
    print("===================================")

    username = input("Username : ")
    password = input("Password : ")

    for pelanggan in pelanggan_list:
        if pelanggan.username == username and pelanggan.password == password:
            print("\nLogin berhasil!")
            print(f"Selamat datang, {pelanggan.nama}.")
            input("\nTekan ENTER untuk melanjutkan...")
            return pelanggan

    print("\nUsername atau password salah.")
    input("\nTekan ENTER untuk kembali...")
    return None


# =========================================================
# DATA PELANGGAN
# =========================================================
def menu_pelanggan(pelanggan):
    clear()

    print("===== DATA PELANGGAN =====")
    pelanggan.tampilkan_data()

    input("\nTekan ENTER untuk kembali...")


# =========================================================
# DATA DRONE
# =========================================================
def menu_drone():
    clear()

    armada.tampilkan_semua()

    input("\nTekan ENTER untuk kembali...")


# =========================================================
# PENYEWAAN DRONE
# =========================================================
def menu_penyewaan(pelanggan):
    clear()

    print("===== PENYEWAAN DRONE =====")

    print("\nPilihan Drone:")

    for i, drone in enumerate(armada.daftar_drone, start=1):
        print(
            f"{i}. {drone.nama} - "
            f"Rp{drone.harga_sewa:,}/hari - "
            f"{drone.status}"
        )

    pilihan = input("\nPilih drone (1/2): ")

    if pilihan == "1":
        drone = drone1

    elif pilihan == "2":
        drone = drone2

    else:
        print("Pilihan tidak valid.")
        input("\nTekan ENTER...")
        return None

    if drone.status != "Tersedia":
        print("\nDrone sedang tidak tersedia.")
        input("\nTekan ENTER...")
        return None

    durasi = int(input("Durasi sewa (hari): "))

    if durasi <= 0:
        print("Durasi tidak valid.")
        input("\nTekan ENTER...")
        return None

    # ASSOCIATION
    penyewaan = Penyewaan(pelanggan)

    # COMPOSITION
    total = penyewaan.buat_penyewaan(drone, durasi)

    clear()

    print("===== DETAIL PENYEWAAN =====")
    penyewaan.tampilkan_data()

    print("\nPenyewaan berhasil dibuat.")

    input("\nTekan ENTER untuk kembali...")

    return penyewaan


# =========================================================
# PROSES PENYEWAAN
# =========================================================
def menu_proses(penyewaan):
    clear()

    print("===== PROSES PENYEWAAN =====")

    if penyewaan is None:
        print("Belum ada penyewaan.")
        input("\nTekan ENTER untuk kembali...")
        return None

    penyewaan.tampilkan_data()

    if penyewaan.status == "Selesai":
        print("\nPenyewaan sudah diproses.")
        input("\nTekan ENTER...")
        return penyewaan

    print("\nSaldo pelanggan:")
    print(f"Rp{penyewaan.pelanggan.saldo:,}")

    konfirmasi = input("\nProses pembayaran? (y/n): ")

    if konfirmasi.lower() == "y":

        if penyewaan.proses():
            print("\nPembayaran berhasil!")
            print("Penyewaan berhasil diproses.")
        else:
            print("\nPembayaran gagal karena saldo tidak mencukupi.")

    else:
        print("\nProses dibatalkan.")

    input("\nTekan ENTER untuk kembali...")

    return penyewaan


# =========================================================
# TOP UP SALDO
# =========================================================
def menu_topup(pelanggan):
    clear()

    print("===== TOP UP SALDO =====")
    print(f"Saldo saat ini : Rp{pelanggan.saldo:,}")

    jumlah = int(input("\nMasukkan jumlah top up: Rp"))

    if jumlah <= 0:
        print("Jumlah top up tidak valid.")

    else:
        pelanggan.saldo += jumlah

        print("\nTop up berhasil!")
        print(f"Saldo sekarang : Rp{pelanggan.saldo:,}")

    input("\nTekan ENTER untuk kembali...")


# =========================================================
# MENU UTAMA
# =========================================================
def menu_utama(pelanggan):

    penyewaan_aktif = None

    while True:

        clear()

        print("===================================")
        print("     SISTEM PENGELOLAAN DRONE")
        print("===================================")
        print(f"Login sebagai : {pelanggan.nama}")
        print(f"Saldo         : Rp{pelanggan.saldo:,}")

        print("\n===== MENU =====")
        print("1. Data Pelanggan")
        print("2. Data Drone")
        print("3. Penyewaan Drone")
        print("4. Proses Penyewaan")
        print("5. Top Up Saldo")
        print("6. Keluar")

        pilihan = input("\nPilih menu: ")

        if pilihan == "1":
            menu_pelanggan(pelanggan)

        elif pilihan == "2":
            menu_drone()

        elif pilihan == "3":
            hasil = menu_penyewaan(pelanggan)

            if hasil is not None:
                penyewaan_aktif = hasil

        elif pilihan == "4":
            penyewaan_aktif = menu_proses(penyewaan_aktif)

        elif pilihan == "5":
            menu_topup(pelanggan)

        elif pilihan == "6":
            clear()
            print("===================================")
            print("       TERIMA KASIH")
            print("===================================")
            print("Program selesai.")
            break

        else:
            print("\nPilihan tidak valid.")
            input("\nTekan ENTER...")


# =========================================================
# PROGRAM UTAMA
# =========================================================
def main():

    pelanggan_login = login()

    if pelanggan_login is not None:
        menu_utama(pelanggan_login)


# =========================================================
# MENJALANKAN PROGRAM
# =========================================================
if __name__ == "__main__":
    main()