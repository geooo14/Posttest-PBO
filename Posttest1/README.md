# Sistem Pengelolaan Penyewaan Drone

## Deskripsi

Sistem Pengelolaan Penyewaan Drone adalah program berbasis Python yang digunakan untuk mengelola data pelanggan, data drone, dan proses penyewaan drone.

Program dibuat menggunakan konsep Object-Oriented Programming (OOP) dengan menerapkan materi Class & Object, Atribut & Method, serta Encapsulation & Property.

Program juga memiliki fitur login, clear screen, top up saldo, proses penyewaan, dan menu utama.

## Fitur Program

1. **Login**
   - Username: `geo`
   - Password: `121`

2. **Data Pelanggan**
   - Menampilkan ID pelanggan, nama, nomor HP, saldo, dan status.

3. **Data Drone**
   - Menampilkan ID drone, model, jenis, harga sewa, dan status.

4. **Data Penyewaan**
   - Menampilkan data penyewaan dan total biaya.

5. **Proses Penyewaan**
   - Mengecek ketersediaan drone.
   - Mengecek saldo pelanggan.
   - Mengurangi saldo sesuai total biaya.
   - Mengubah status drone menjadi `Disewa`.

6. **Top Up Saldo**
   - Menambah saldo pelanggan sesuai jumlah yang dimasukkan.

7. **Clear Screen**
   - Membersihkan tampilan terminal agar program lebih rapi.

## Struktur Class

### 1. Class `Pelanggan`

Digunakan untuk mengelola data pelanggan.

Atribut utama:
- `id_pelanggan`
- `nama`
- `nomor_hp`
- `saldo`
- `status`

Private attribute:
- `__saldo`

Method:
- `tampilkan_data()`
- `top_up()`
- `ubah_status_default()`
- `validasi_nomor_hp()`

### 2. Class `Drone`

Digunakan untuk mengelola data drone.

Atribut utama:
- `id_drone`
- `model`
- `jenis`
- `harga_sewa`
- `status`

Private attribute:
- `__harga_sewa`

Method:
- `tampilkan_data()`
- `ubah_status()`
- `ubah_status_default()`
- `validasi_jenis()`

### 3. Class `Penyewaan`

Digunakan untuk mengelola proses penyewaan drone.

Atribut utama:
- `id_penyewaan`
- `pelanggan`
- `drone`
- `durasi`
- `status`

Method:
- `hitung_total()`
- `tampilkan_data()`
- `proses_penyewaan()`
- `ubah_pajak()`
- `hitung_diskon()`

## Konsep OOP yang Digunakan

### Class dan Object

Program menggunakan tiga class utama:
- `Pelanggan`
- `Drone`
- `Penyewaan`

Dari setiap class dibuat object untuk digunakan dalam program.

### Atribut Instance

Atribut instance dibuat di dalam `__init__()` menggunakan `self`.

Contoh:

```python
self.nama = nama
self.nomor_hp = nomor_hp
self.id_pelanggan = id_pelanggan
```

### Atribut Class

Atribut class digunakan bersama oleh object dalam class yang sama.

Contoh:

```python
total_pelanggan = 0
status_default = "Aktif"
```

### Instance Method

Instance method menggunakan parameter `self`.

### Class Method

Class method menggunakan decorator `@classmethod` dan parameter `cls`.

### Static Method

Static method menggunakan decorator `@staticmethod` tanpa `self` atau `cls`.

### Encapsulation

Encapsulation diterapkan menggunakan private attribute, contohnya:

```python
self.__saldo = saldo
```

### Getter dan Setter

Getter dan setter digunakan untuk mengakses dan mengubah private attribute.

Contoh getter:

```python
@property
def saldo(self):
    return self.__saldo
```

Contoh setter:

```python
@saldo.setter
def saldo(self, saldo_baru):
    if saldo_baru < 0:
        print("Saldo tidak boleh negatif.")
    else:
        self.__saldo = saldo_baru
```

## Data Awal

### Pelanggan

| ID | Nama | Nomor HP | Saldo |
|---|---|---|---:|
| P001 | Geo | 081234567890 | Rp1.000.000 |
| P002 | Budi | 082345678901 | Rp750.000 |

### Drone

| ID | Model | Jenis | Harga Sewa |
|---|---|---|---:|
| D001 | DJI Mini 4 Pro | Kamera | Rp250.000/hari |
| D002 | DJI Avata 2 | Balap | Rp300.000/hari |

## Alur Program

```text
Mulai
  ↓
Login
  ↓
Username & Password Benar?
  ↓
Menu Utama
  ├── Data Pelanggan
  ├── Data Drone
  ├── Data Penyewaan
  ├── Proses Penyewaan
  ├── Top Up Saldo
  └── Keluar
  ↓
Selesai
```

## Cara Menjalankan Program

Pastikan Python sudah terinstall.

Jalankan melalui terminal:

```bash
python nama_file.py
```

Kemudian login menggunakan:

```text
Username : geo
Password : 121
```

## Teknologi yang Digunakan

- Bahasa pemrograman: Python
- Konsep: Object-Oriented Programming (OOP)
- Materi: Class & Object, Atribut & Method, Encapsulation & Property
- Database: Tidak menggunakan database
- Library tambahan: Tidak digunakan
