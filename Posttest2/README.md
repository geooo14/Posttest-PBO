# Sistem Pengelolaan Penyewaan Drone

## Deskripsi Program

Program **Sistem Pengelolaan Penyewaan Drone** merupakan aplikasi berbasis Python yang digunakan untuk mengelola proses penyewaan drone. Program memiliki fitur login pelanggan, melihat data pelanggan, melihat daftar drone, melakukan penyewaan, memproses pembayaran, dan melakukan top up saldo.

Program dibuat menggunakan konsep **Object-Oriented Programming (OOP)** sesuai materi yang dipelajari, yaitu Class & Object, Atribut & Method, Encapsulation & Property, serta konsep tambahan berupa Inheritance dan Relasi UML.

---

## Fitur Program

Program memiliki beberapa fitur utama:

1. **Login**

   * Pelanggan dapat masuk menggunakan username dan password.
   * Data pengguna yang tersedia:

     * Username: `geo`
     * Password: `121`
     * Username: `budi`
     * Password: `123`

2. **Data Pelanggan**

   * Menampilkan ID pelanggan.
   * Menampilkan nama pelanggan.
   * Menampilkan username.
   * Menampilkan saldo.

3. **Data Drone**

   * Menampilkan daftar drone yang tersedia.
   * Menampilkan harga sewa.
   * Menampilkan status drone.
   * Menampilkan informasi khusus berdasarkan jenis drone.

4. **Penyewaan Drone**

   * Pelanggan dapat memilih drone.
   * Pelanggan dapat menentukan durasi penyewaan.
   * Sistem menghitung subtotal dan pajak.

5. **Proses Penyewaan**

   * Sistem memeriksa saldo pelanggan.
   * Jika saldo mencukupi, pembayaran diproses.
   * Saldo pelanggan akan berkurang.
   * Status drone berubah menjadi `Disewa`.

6. **Top Up Saldo**

   * Pelanggan dapat menambahkan saldo.
   * Saldo akan diperbarui setelah proses top up.

7. **Keluar**

   * Pengguna dapat keluar dari program melalui menu utama.

---

## Struktur Class

Program menggunakan beberapa class utama:

### 1. Class `Pelanggan`

Digunakan untuk menyimpan data pelanggan seperti:

* ID pelanggan
* Nama
* Username
* Password
* Saldo

Class ini juga menerapkan **Encapsulation dan Property**.

### 2. Class `Drone`

Merupakan **Superclass** yang menyimpan atribut dasar drone:

* ID drone
* Nama drone
* Harga sewa
* Status drone

### 3. Class `DroneKamera`

Merupakan **Subclass** dari class `Drone`.

Class ini memiliki atribut tambahan berupa resolusi kamera dan melakukan **method overriding** pada `tampilkan_data()`.

### 4. Class `DroneBalap`

Merupakan **Subclass** dari class `Drone`.

Class ini memiliki atribut tambahan berupa kecepatan dan melakukan **method overriding** pada `tampilkan_data()`.

### 5. Class `DetailPenyewaan`

Digunakan untuk menyimpan detail penyewaan seperti:

* Drone yang disewa
* Durasi penyewaan
* Subtotal penyewaan

Class ini digunakan dalam hubungan **Composition** dengan `Penyewaan`.

### 6. Class `Penyewaan`

Digunakan untuk mengatur proses penyewaan drone dan pembayaran.

Class ini berhubungan dengan:

* `Pelanggan`
* `Drone`
* `DetailPenyewaan`

### 7. Class `ArmadaDrone`

Digunakan untuk mengelola kumpulan drone yang tersedia.

Class ini menerapkan konsep **Aggregation** terhadap objek `Drone`.

---

## Penerapan Konsep OOP

### 1. Encapsulation

Encapsulation diterapkan menggunakan atribut protected-style dan private.

Contohnya:

```python
self._nama
```

dan:

```python
self.__harga_sewa
```

Atribut `__harga_sewa` dibuat private sehingga tidak dapat diakses langsung dari luar class.

---

### 2. Property

Property digunakan untuk mengakses dan mengubah atribut tertentu secara terkontrol.

Contohnya:

```python
@property
def harga_sewa(self):
    return self.__harga_sewa
```

dan setter:

```python
@harga_sewa.setter
def harga_sewa(self, harga_baru):
    self.__harga_sewa = harga_baru
```

---

### 3. Inheritance

Inheritance diterapkan dengan membuat `Drone` sebagai superclass dan:

* `DroneKamera`
* `DroneBalap`

sebagai subclass.

Contohnya:

```python
class DroneKamera(Drone):
```

dan:

```python
class DroneBalap(Drone):
```

Subclass menggunakan:

```python
super().__init__()
```

untuk memanggil constructor dari superclass.

---

### 4. Method Overriding

Method `tampilkan_data()` pada class `DroneKamera` dan `DroneBalap` dibuat kembali dengan informasi tambahan sesuai jenis drone.

Hal tersebut merupakan penerapan **method overriding**.

---

## Relasi UML

Program menerapkan tiga jenis relasi UML yang diwajibkan.

### 1. Association

Association diterapkan antara class `Penyewaan` dan `Pelanggan`.

Objek `Penyewaan` membutuhkan objek `Pelanggan` untuk mengetahui siapa yang melakukan penyewaan.

```python
self.pelanggan = pelanggan
```

### 2. Aggregation

Aggregation diterapkan antara `ArmadaDrone` dengan `Drone`.

`ArmadaDrone` menyimpan beberapa objek drone, tetapi objek drone tetap dapat berdiri sendiri.

```python
self.daftar_drone = []
```

Kemudian drone dimasukkan ke dalam armada menggunakan:

```python
armada.tambah_drone(drone)
```

### 3. Composition

Composition diterapkan antara `Penyewaan` dan `DetailPenyewaan`.

`DetailPenyewaan` dibuat ketika proses penyewaan dilakukan:

```python
self.detail = DetailPenyewaan(drone, durasi)
```

Detail tersebut menjadi bagian dari proses penyewaan.

---

## Struktur Relasi Class

Secara sederhana hubungan antar-class pada program adalah:

```text
                 Drone
                /     \
               /       \
      DroneKamera     DroneBalap
              
Pelanggan -------- Penyewaan
                         |
                         |
                  DetailPenyewaan


ArmadaDrone ◇-------- Drone
```

Keterangan:

* `Drone` → Superclass
* `DroneKamera` → Subclass
* `DroneBalap` → Subclass
* `Pelanggan` ↔ `Penyewaan` → Association
* `ArmadaDrone` ◇→ `Drone` → Aggregation
* `Penyewaan` ◆→ `DetailPenyewaan` → Composition

---

## Cara Menjalankan Program

### 1. Pastikan Python sudah terinstall

Cek Python dengan perintah:

```bash
python --version
```

atau:

```bash
python3 --version
```

### 2. Masuk ke folder program

Buka terminal pada folder tempat file Python disimpan.

### 3. Jalankan program

Gunakan:

```bash
python main.py
```

Jika menggunakan Linux atau sistem yang menggunakan `python3`:

```bash
python3 main.py
```

---

## Pengujian Program

### Pengujian Login

Gunakan salah satu akun:

```text
Username : geo
Password : 121
```

atau:

```text
Username : budi
Password : 123
```

Jika username dan password benar, program akan masuk ke menu utama.

### Pengujian Penyewaan

1. Login sebagai pelanggan.
2. Pilih menu **Data Drone** untuk melihat drone.
3. Pilih menu **Penyewaan Drone**.
4. Pilih drone.
5. Masukkan durasi penyewaan.
6. Sistem menghitung subtotal dan pajak.
7. Pilih menu **Proses Penyewaan**.
8. Sistem memeriksa saldo.
9. Jika saldo mencukupi, pembayaran berhasil.
10. Status drone berubah menjadi `Disewa`.

### Pengujian Top Up

1. Pilih menu **Top Up Saldo**.
2. Masukkan jumlah saldo.
3. Sistem menambahkan saldo ke akun pelanggan.
4. Saldo terbaru ditampilkan.

---

## Kesimpulan

Program Sistem Pengelolaan Penyewaan Drone dibuat untuk menerapkan konsep dasar Object-Oriented Programming dalam sebuah sistem penyewaan. Program telah menggunakan **Class & Object, Atribut & Method, Encapsulation, Property, Inheritance, Superclass, Subclass, Method Overriding, Association, Aggregation, dan Composition**.

Dengan penerapan konsep tersebut, program tidak hanya dapat digunakan untuk melakukan proses penyewaan drone, tetapi juga menunjukkan penerapan konsep OOP dan relasi antar-class dalam sebuah studi kasus yang nyata.
