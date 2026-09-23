import os


# ==========================================================
# FUNGSI CLEAR SCREEN
# ==========================================================

def clear():
    os.system("cls" if os.name == "nt" else "clear")


# ==========================================================
# CLASS PELANGGAN
# ==========================================================

class Pelanggan:
    nama_aplikasi = "Drone Rental"
    total_pelanggan = 0
    status_default = "Aktif"

    def __init__(self, id_pelanggan, nama, nomor_hp, saldo):
        self.id_pelanggan = id_pelanggan
        self.nama = nama
        self.nomor_hp = nomor_hp
        self.status = Pelanggan.status_default
        self.__saldo = saldo
        Pelanggan.total_pelanggan += 1

    # Getter
    @property
    def saldo(self):
        return self.__saldo

    # Setter
    @saldo.setter
    def saldo(self, saldo_baru):
        if saldo_baru < 0:
            print("Saldo tidak boleh negatif.")
        else:
            self.__saldo = saldo_baru

    # Instance Method
    def tampilkan_data(self):
        print("\n--- DATA PELANGGAN ---")
        print("ID Pelanggan :", self.id_pelanggan)
        print("Nama         :", self.nama)
        print("Nomor HP     :", self.nomor_hp)
        print("Saldo        :", self.saldo)
        print("Status       :", self.status)

    def top_up(self, jumlah):
        if jumlah > 0:
            self.saldo = self.saldo + jumlah
            print("Top up berhasil.")
            print("Saldo sekarang :", self.saldo)
        else:
            print("Jumlah top up harus lebih dari 0.")

    # Class Method
    @classmethod
    def ubah_status_default(cls, status_baru):
        cls.status_default = status_baru

    # Static Method
    @staticmethod
    def validasi_nomor_hp(nomor_hp):
        if nomor_hp.isdigit() and len(nomor_hp) >= 10:
            return True
        return False


# ==========================================================
# CLASS DRONE
# ==========================================================

class Drone:
    nama_perusahaan = "Drone Rental"
    total_drone = 0
    status_default = "Tersedia"

    def __init__(self, id_drone, model, jenis, harga_sewa):
        self.id_drone = id_drone
        self.model = model
        self.jenis = jenis
        self.status = Drone.status_default
        self.__harga_sewa = harga_sewa
        Drone.total_drone += 1

    # Getter
    @property
    def harga_sewa(self):
        return self.__harga_sewa

    # Setter
    @harga_sewa.setter
    def harga_sewa(self, harga_baru):
        if harga_baru < 0:
            print("Harga sewa tidak boleh negatif.")
        else:
            self.__harga_sewa = harga_baru

    # Instance Method
    def tampilkan_data(self):
        print("\n--- DATA DRONE ---")
        print("ID Drone     :", self.id_drone)
        print("Model        :", self.model)
        print("Jenis        :", self.jenis)
        print("Harga Sewa   :", self.harga_sewa)
        print("Status       :", self.status)

    def ubah_status(self, status_baru):
        if status_baru == "Tersedia":
            self.status = status_baru
        elif status_baru == "Disewa":
            self.status = status_baru
        elif status_baru == "Perawatan":
            self.status = status_baru
        else:
            print("Status drone tidak valid.")

    # Class Method
    @classmethod
    def ubah_status_default(cls, status_baru):
        cls.status_default = status_baru

    # Static Method
    @staticmethod
    def validasi_jenis(jenis):
        if jenis == "Kamera":
            return True
        elif jenis == "Balap":
            return True
        elif jenis == "Profesional":
            return True
        else:
            return False


# ==========================================================
# CLASS PENYEWAAN
# ==========================================================

class Penyewaan:
    nama_layanan = "Penyewaan Drone"
    total_penyewaan = 0
    pajak = 0.10

    def __init__(self, id_penyewaan, pelanggan, drone, durasi):
        self.id_penyewaan = id_penyewaan
        self.pelanggan = pelanggan
        self.drone = drone
        self.durasi = durasi
        self.status = "Belum Dibayar"
        Penyewaan.total_penyewaan += 1

    # Instance Method
    def hitung_total(self):
        harga = self.drone.harga_sewa * self.durasi
        pajak = harga * Penyewaan.pajak

        return harga + pajak

    def tampilkan_data(self):
        print("\n--- DATA PENYEWAAN ---")
        print("ID Penyewaan :", self.id_penyewaan)
        print("Pelanggan    :", self.pelanggan.nama)
        print("Drone        :", self.drone.model)
        print("Durasi       :", self.durasi, "hari")
        print("Total        :", self.hitung_total())
        print("Status       :", self.status)

    def proses_penyewaan(self):
        total = self.hitung_total()

        if self.drone.status != "Tersedia":
            print("Drone tidak tersedia.")

        elif self.pelanggan.saldo < total:
            print("Saldo pelanggan tidak cukup.")

        else:
            self.pelanggan.saldo = self.pelanggan.saldo - total
            self.drone.status = "Disewa"
            self.status = "Sudah Dibayar"

            print("\nPenyewaan berhasil!")
            print("Pelanggan :", self.pelanggan.nama)
            print("Drone     :", self.drone.model)
            print("Durasi    :", self.durasi, "hari")
            print("Total     :", total)
            print("Sisa saldo:", self.pelanggan.saldo)

    # Class Method
    @classmethod
    def ubah_pajak(cls, pajak_baru):
        if pajak_baru >= 0 and pajak_baru <= 1:
            cls.pajak = pajak_baru

    # Static Method
    @staticmethod
    def hitung_diskon(harga, persen):
        if persen < 0 or persen > 100:
            return harga

        diskon = harga * persen / 100

        return harga - diskon


# ==========================================================
# OBJECT
# ==========================================================

pelanggan1 = Pelanggan(
    "P001",
    "Geo",
    "081234567890",
    1000000
)

pelanggan2 = Pelanggan(
    "P002",
    "Budi",
    "082345678901",
    750000
)

drone1 = Drone(
    "D001",
    "DJI Mini 4 Pro",
    "Kamera",
    250000
)

drone2 = Drone(
    "D002",
    "DJI Avata 2",
    "Balap",
    300000
)

penyewaan1 = Penyewaan(
    "S001",
    pelanggan1,
    drone1,
    2
)

penyewaan2 = Penyewaan(
    "S002",
    pelanggan2,
    drone2,
    1
)


# ==========================================================
# LOGIN
# ==========================================================

USERNAME = "geo"
PASSWORD = "121"

login_berhasil = False

while login_berhasil == False:

    clear()

    print("==============================================")
    print("              LOGIN DRONE RENTAL")
    print("==============================================")

    username = input("Username : ")
    password = input("Password : ")

    if username == USERNAME and password == PASSWORD:
        login_berhasil = True

        print("\nLogin berhasil!")
        input("Tekan ENTER untuk masuk...")

    else:
        print("\nUsername atau password salah!")
        input("Tekan ENTER untuk mencoba lagi...")


# ==========================================================
# MENU UTAMA
# ==========================================================

while True:

    clear()

    print("==============================================")
    print("       SISTEM PENGELOLAAN PENYEWAAN DRONE")
    print("==============================================")
    print("Selamat datang, Geo!")
    print("----------------------------------------------")
    print("1. Data Pelanggan")
    print("2. Data Drone")
    print("3. Data Penyewaan")
    print("4. Proses Penyewaan")
    print("5. Top Up Saldo")
    print("6. Keluar")
    print("==============================================")

    pilihan = input("Pilih menu: ")


    # ======================================================
    # MENU 1 - DATA PELANGGAN
    # ======================================================

    if pilihan == "1":

        clear()

        print("==============================================")
        print("               DATA PELANGGAN")
        print("==============================================")

        pelanggan1.tampilkan_data()
        pelanggan2.tampilkan_data()

        input("\nTekan ENTER untuk kembali...")


    # ======================================================
    # MENU 2 - DATA DRONE
    # ======================================================

    elif pilihan == "2":

        clear()

        print("==============================================")
        print("                  DATA DRONE")
        print("==============================================")

        drone1.tampilkan_data()
        drone2.tampilkan_data()

        input("\nTekan ENTER untuk kembali...")


    # ======================================================
    # MENU 3 - DATA PENYEWAAN
    # ======================================================

    elif pilihan == "3":

        clear()

        print("==============================================")
        print("              DATA PENYEWAAN")
        print("==============================================")

        penyewaan1.tampilkan_data()
        penyewaan2.tampilkan_data()

        input("\nTekan ENTER untuk kembali...")


    # ======================================================
    # MENU 4 - PROSES PENYEWAAN
    # ======================================================

    elif pilihan == "4":

        clear()

        print("==============================================")
        print("             PROSES PENYEWAAN")
        print("==============================================")
        print("1. Geo - DJI Mini 4 Pro")
        print("2. Budi - DJI Avata 2")
        print("3. Kembali")

        pilih = input("\nPilih: ")

        if pilih == "1":
            penyewaan1.proses_penyewaan()

        elif pilih == "2":
            penyewaan2.proses_penyewaan()

        elif pilih == "3":
            pass

        else:
            print("Pilihan tidak valid.")

        input("\nTekan ENTER untuk kembali...")


    # ======================================================
    # MENU 5 - TOP UP
    # ======================================================

    elif pilihan == "5":

        clear()

        print("==============================================")
        print("                TOP UP SALDO")
        print("==============================================")
        print("1. Geo")
        print("2. Budi")
        print("3. Kembali")

        pilih = input("\nPilih pelanggan: ")

        if pilih == "1":

            jumlah = int(input("Masukkan jumlah top up: "))
            pelanggan1.top_up(jumlah)

        elif pilih == "2":

            jumlah = int(input("Masukkan jumlah top up: "))
            pelanggan2.top_up(jumlah)

        elif pilih == "3":
            pass

        else:
            print("Pilihan tidak valid.")

        input("\nTekan ENTER untuk kembali...")


    # ======================================================
    # MENU 6 - KELUAR
    # ======================================================

    elif pilihan == "6":

        clear()

        print("==============================================")
        print("       TERIMA KASIH SUDAH MENGGUNAKAN")
        print("              DRONE RENTAL")
        print("==============================================")

        break


    else:

        print("\nPilihan tidak tersedia.")
        input("Tekan ENTER untuk kembali...")