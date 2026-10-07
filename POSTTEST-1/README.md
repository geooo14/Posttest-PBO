# Sistem Pengelolaan Penyewaan Drone

## Deskripsi Program

Program ini merupakan aplikasi sederhana berbasis Python untuk mengelola penyewaan drone. Program dibuat menggunakan konsep Object-Oriented Programming (OOP), yaitu class, object, atribut, method, encapsulation, dan property.

Program ini memiliki fitur login, melihat data pelanggan, melihat data drone, melihat data penyewaan, memproses penyewaan, dan melakukan top up saldo.

## Fitur Program

1. Login menggunakan username dan password.
2. Menampilkan data pelanggan.
3. Menampilkan data drone.
4. Menampilkan data penyewaan.
5. Memproses penyewaan drone.
6. Menghitung total biaya penyewaan dan pajak.
7. Mengurangi saldo pelanggan setelah penyewaan berhasil.
8. Melakukan top up saldo pelanggan.
9. Mengubah status drone menjadi "Disewa".
10. Validasi saldo dan harga agar tidak bernilai negatif.

## Struktur Class

### 1. Class Pelanggan

Class `Pelanggan` digunakan untuk menyimpan data pelanggan yang melakukan penyewaan drone.

Atribut yang digunakan:

- `id_pelanggan`
- `nama`
- `nomor_hp`
- `status`
- `__saldo`

Method yang digunakan:

- `tampilkan_data()` untuk menampilkan data pelanggan.
- `top_up()` untuk menambahkan saldo.
- `ubah_status_default()` sebagai class method untuk mengubah status default pelanggan.
- `validasi_nomor_hp()` sebagai static method untuk memvalidasi nomor HP.
- `saldo` sebagai property untuk mengambil dan mengubah saldo.

Atribut `__saldo` dibuat private agar data saldo tidak diakses secara langsung dari luar class.

### 2. Class Drone

Class `Drone` digunakan untuk menyimpan data drone yang disewakan.

Atribut yang digunakan:

- `id_drone`
- `model`
- `jenis`
- `status`
- `__harga_sewa`

Method yang digunakan:

- `tampilkan_data()` untuk menampilkan data drone.
- `ubah_status()` untuk mengubah status drone.
- `ubah_status_default()` sebagai class method untuk mengubah status default drone.
- `validasi_jenis()` sebagai static method untuk memvalidasi jenis drone.
- `harga_sewa` sebagai property untuk mengambil dan mengubah harga sewa.

Atribut `__harga_sewa` dibuat private dan hanya dapat diakses melalui property.

### 3. Class Penyewaan

Class `Penyewaan` digunakan untuk mengelola proses penyewaan drone.

Atribut yang digunakan:

- `id_penyewaan`
- `pelanggan`
- `drone`
- `durasi`
- `status`

Method yang digunakan:

- `hitung_total()` untuk menghitung total biaya penyewaan.
- `tampilkan_data()` untuk menampilkan data penyewaan.
- `proses_penyewaan()` untuk memproses pembayaran dan penyewaan drone.
- `ubah_pajak()` sebagai class method untuk mengubah nilai pajak.
- `hitung_diskon()` sebagai static method untuk menghitung harga setelah diskon.

## Konsep OOP yang Digunakan

### Class dan Object

Class digunakan sebagai cetak biru atau rancangan objek. Object merupakan hasil pembuatan dari class tersebut.

Contoh object yang dibuat:

- `pelanggan1`
- `pelanggan2`
- `drone1`
- `drone2`
- `penyewaan1`
- `penyewaan2`

### Atribut Instance

Atribut instance merupakan atribut yang dimiliki oleh setiap object dan dibuat di dalam method `__init__()` menggunakan `self`.

Contohnya adalah:

```python
self.nama = nama
self.model = model
self.durasi = durasi
```

### Atribut Class

Atribut class merupakan atribut yang dimiliki bersama oleh semua object dalam class.

Contohnya:

```python
nama_aplikasi = "Drone Rental"
total_pelanggan = 0
status_default = "Aktif"
```

### Instance Method

Instance method merupakan method yang menggunakan parameter `self` dan dipanggil melalui object.

Contohnya:

```python
pelanggan1.tampilkan_data()
drone1.tampilkan_data()
penyewaan1.proses_penyewaan()
```

### Class Method

Class method menggunakan decorator `@classmethod` dan parameter `cls`. Method ini digunakan untuk mengakses atau mengubah atribut class.

Contohnya:

```python
@classmethod
def ubah_status_default(cls, status_baru):
    cls.status_default = status_baru
```

### Static Method

Static method menggunakan decorator `@staticmethod` dan tidak membutuhkan parameter `self` maupun `cls`.

Contohnya:

```python
@staticmethod
def validasi_nomor_hp(nomor_hp):
    if nomor_hp.isdigit() and len(nomor_hp) >= 10:
        return True
    return False
```

### Encapsulation

Encapsulation digunakan untuk melindungi data tertentu agar tidak diakses secara langsung dari luar class.

Contoh atribut private dalam program:

```python
self.__saldo = saldo
self.__harga_sewa = harga_sewa
```

### Property

Property digunakan untuk mengakses dan mengubah atribut private melalui getter dan setter.

Contohnya:

```python
@property
def saldo(self):
    return self.__saldo

@saldo.setter
def saldo(self, saldo_baru):
    if saldo_baru < 0:
        print("Saldo tidak boleh negatif.")
    else:
        self.__saldo = saldo_baru
```

Setter digunakan untuk melakukan validasi agar saldo tidak bernilai negatif.

## Data Awal Program

### Data Pelanggan

| ID | Nama | Nomor HP | Saldo |
|---|---|---|---:|
| P001 | Geo | 081234567890 | 1000000 |
| P002 | Budi | 082345678901 | 750000 |

### Data Drone

| ID | Model | Jenis | Harga Sewa |
|---|---|---|---:|
| D001 | DJI Mini 4 Pro | Kamera | 250000 |
| D002 | DJI Avata 2 | Balap | 300000 |

### Data Penyewaan

| ID | Pelanggan | Drone | Durasi |
|---|---|---|---:|
| S001 | Geo | DJI Mini 4 Pro | 2 hari |
| S002 | Budi | DJI Avata 2 | 1 hari |

Pajak penyewaan yang digunakan adalah 10%.

## Alur Program

1. Program menampilkan halaman login.
2. Pengguna memasukkan username dan password.
3. Jika data login benar, pengguna masuk ke menu utama.
4. Pengguna dapat melihat data pelanggan, drone, dan penyewaan.
5. Pengguna dapat memilih penyewaan yang ingin diproses.
6. Program memeriksa ketersediaan drone dan saldo pelanggan.
7. Jika memenuhi syarat, saldo pelanggan akan dikurangi.
8. Status drone berubah menjadi "Disewa".
9. Program menampilkan hasil penyewaan.
10. Pengguna dapat melakukan top up saldo atau keluar dari program.

## Panduan Menjalankan Program

1. Buka file program menggunakan Visual Studio Code.
2. Jalankan program melalui terminal dengan perintah:

```bash
python nama_file.py
```

3. Masukkan username dan password berikut:

```text
Username : geo
Password : 121
```

4. Jika login berhasil, program akan masuk ke menu utama.

## Panduan Pengujian

### 1. Pengujian Login

Masukkan username `geo` dan password `121`. Jika benar, program akan masuk ke menu utama. Jika salah, program akan meminta pengguna mencoba kembali.

### 2. Pengujian Data Pelanggan

Pilih menu `1. Data Pelanggan` untuk melihat data pelanggan Geo dan Budi.

### 3. Pengujian Data Drone

Pilih menu `2. Data Drone` untuk melihat data drone yang tersedia.

### 4. Pengujian Data Penyewaan

Pilih menu `3. Data Penyewaan` untuk melihat data penyewaan, durasi, total biaya, dan status.

### 5. Pengujian Proses Penyewaan

Pilih menu `4. Proses Penyewaan`, kemudian pilih penyewaan. Jika drone tersedia dan saldo mencukupi, penyewaan berhasil dan saldo pelanggan berkurang.

### 6. Pengujian Drone Tidak Tersedia

Coba menyewa drone yang statusnya sudah `Disewa`. Program akan menampilkan pesan `Drone tidak tersedia.`.

### 7. Pengujian Saldo Tidak Cukup

Coba melakukan penyewaan ketika saldo pelanggan kurang dari total biaya. Program akan menampilkan pesan `Saldo pelanggan tidak cukup.`.

### 8. Pengujian Top Up

Pilih menu `5. Top Up Saldo`, pilih pelanggan, lalu masukkan jumlah top up. Saldo akan bertambah sesuai jumlah yang dimasukkan.

### 9. Pengujian Input Tidak Valid

Masukkan jumlah top up 0 atau kurang dari 0. Program akan menampilkan pesan `Jumlah top up harus lebih dari 0.` dan saldo tidak berubah.

## Data Login

| Username | Password |
|---|---|
| geo | 121 |

## Teknologi yang Digunakan

- Bahasa pemrograman: Python
- Konsep: Object-Oriented Programming (OOP)
- Editor: Visual Studio Code
- Modul: `os` untuk membersihkan tampilan terminal
