#  Praktikum 2
## **Pertemuan ke-6: Kondisional dan Perulangan**



**Nama:** Naziha Raiqi Aribino <br>
**Kelas:** TI.25.A2<br>
**NIM:** 312510232 <br>
**Mata Kuliah:** Pengantar Pemrograman <br>
**Dosen Pengampu:** Agung Nugroho, M.Kom <br>

---

##  Tujuan Praktikum

1. Memahami konsep **struktur kondisi** (`if`, `elif`, `else`) dalam Python.
2. Menerapkan **perulangan** (`for`, `while`) untuk menyelesaikan kasus logika.
3. Menggabungkan kondisi dan perulangan dalam satu program.
4. Membuat simulasi **kode loop flowchart** yang menggambarkan pembacaan sensor otomatis.



##  Dasar Teori

### Struktur Kondisi

Struktur kondisi memungkinkan program mengambil keputusan berdasarkan hasil evaluasi logika tertentu.
Contohnya:

```python
if x > 10:
    print("Nilai besar")
else:
    print("Nilai kecil")
```

### Struktur Perulangan

Perulangan digunakan untuk menjalankan perintah berulang kali.
Python mendukung dua jenis utama:

* **for loop** → perulangan berdasarkan urutan data atau range.
* **while loop** → perulangan selama kondisi masih bernilai benar.

---

##  Praktikum & Pembahasan

### **Lab 2 – Struktur Kondisi**

####  Latihan 1: Menentukan Bilangan Terbesar

**Tujuan:** Menentukan bilangan terbesar dari empat input menggunakan `if`.

**Penjelasan:**

* Program menerima empat angka dari pengguna.
* Menggunakan kondisi `if` dan `elif` untuk membandingkan setiap nilai.
* Nilai terbesar disimpan dan ditampilkan.

```python
a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
c = int(input("Masukkan bilangan ketiga: "))
d = int(input("Masukkan bilangan keempat: "))

terbesar = a
if b > terbesar:
    terbesar = b
if c > terbesar:
    terbesar = c
if d > terbesar:
    terbesar = d

print("Bilangan terbesar adalah:", terbesar)
```

**Output Contoh:**

```
Masukkan bilangan pertama: 17
Masukkan bilangan kedua: 25
Masukkan bilangan ketiga: 19
Masukkan bilangan keempat: 20
Bilangan terbesar adalah: 25
```

**Kesimpulan:**
Struktur kondisi `if` memudahkan pengambilan keputusan berdasarkan perbandingan antar nilai.



####  Latihan 2: Mengurutkan Data dari Terkecil ke Terbesar

**Tujuan:** Menggunakan list dan metode `sort()` untuk mengurutkan data.

**Penjelasan:**

* Pengguna menentukan jumlah data.
* Semua data disimpan dalam list.
* Fungsi `sort()` mengurutkan dari kecil ke besar.

```python
data = []
n = int(input("Masukkan jumlah data: "))

for i in range(n):
    angka = int(input(f"Masukkan data ke-{i+1}: "))
    data.append(angka)

data.sort()
print("Data setelah diurutkan:", data)
```

**Output Contoh:**

```
Masukkan jumlah data: 3
Masukkan data ke-1: 10
Masukkan data ke-2: 3
Masukkan data ke-3: 5
Data setelah diurutkan: [3,5, 10]
```

**Kesimpulan:**
Latihan ini melatih penggunaan list serta fungsi bawaan Python untuk mengolah dan mengurutkan data.



### **Lab 3 – Perulangan**

####  Latihan 1: Perulangan Bertingkat (Nested For)

**Tujuan:** Membuat pola segitiga menggunakan *nested loop*.

**Penjelasan:**

* Loop luar menentukan jumlah baris.
* Loop dalam mencetak simbol `*`.
* Program membentuk pola bertingkat.

```python
n = int(input("Masukkan jumlah baris: "))

for i in range(n):
    for j in range(i + 1):
        print("*", end="")
    print()
```

**Output Contoh:**

```
Masukkan jumlah baris: 5
*
**
***
****
*****
```

**Kesimpulan:**
Nested loop memungkinkan penciptaan pola visual berbasis logika berulang.



####  Latihan 2: Menampilkan n Bilangan Acak < 0.5

**Tujuan:** Menggunakan `random` untuk menghasilkan bilangan acak terbatas.

**Penjelasan:**

* Menghasilkan angka acak 0–1 dengan `random.random()`.
* Menampilkan hanya nilai yang < 0.5.
* Menggunakan `while` untuk mengatur jumlah bilangan yang ditampilkan.

```python
import random

n = int(input("Masukkan jumlah bilangan acak: "))
count = 0

while count < n:
    x = random.random()
    if x < 0.5:
        print(x)
        count += 1
```

**Output Contoh:**

```
Masukkan jumlah bilangan acak: 5
0.324564
0.278641
0.182945
0.492116
0.035842
```

**Kesimpulan:**
Kombinasi `while` dan `if` memungkinkan pengendalian hasil acak sesuai kondisi yang diinginkan.



##  Tambahan: Kode Loop Flowchart (Pembacaan Sensor)

**Tujuan:**
Mengimplementasikan konsep *loop* dan *kondisi* dalam simulasi sistem pembacaan sensor suhu dan kelembapan.

**Penjelasan:**

1. Program meminta input suhu dan kelembapan dari pengguna.
2. Menggunakan `if` untuk menentukan status suhu dan kelembapan.
3. Setelah hasil ditampilkan, pengguna diminta memilih apakah ingin membaca ulang sensor.
4. Jika menjawab “ya”, maka proses berulang dengan `while`.

```python
print("=== PEMBACAAN SENSOR ===")

ulang = "ya"
while ulang.lower() == "ya":
    suhu = float(input("Masukkan suhu saat ini (°C): "))
    kelembapan = float(input("Masukkan kelembapan saat ini (%): "))

    print("\n--- HASIL PEMERIKSAAN ---")

    if suhu < 25:
        print(f"Suhu {suhu}°C < 25°C → Terlalu dingin! Nyalakan pemanas.")
    elif suhu > 35:
        print(f"Suhu {suhu}°C > 35°C → Terlalu panas! Nyalakan pendingin.")
    else:
        print(f"Suhu {suhu}°C dalam batas normal (25°C - 35°C). ✅")

    if kelembapan < 45:
        print(f"Kelembapan {kelembapan}% < 45% → Terlalu kering! Aktifkan pelembap.")
    elif kelembapan > 55:
        print(f"Kelembapan {kelembapan}% > 55% → Terlalu lembap! Aktifkan ventilasi.")
    else:
        print(f"Kelembapan {kelembapan}% dalam batas normal (45% - 55%). ✅")

    ulang = input("\nBaca sensor lagi? (y/n): ")

print("\nProgram selesai. Semua sistem stabil.")
```

**Output Contoh:**

```
=== PEMBACAAN SENSOR ===
Masukkan suhu saat ini (°C): 20
Masukkan kelembapan saat ini (%): 50

--- HASIL PEMERIKSAAN ---
Suhu 20.0°C < 25°C → Terlalu dingin! Nyalakan pemanas.
Kelembapan 50.0% dalam batas normal (45% - 55%). ✅

Baca sensor lagi? (y/n): ya

Program selesai. Semua sistem stabil
```

**Kesimpulan:**
Program *kode loop flowchart* ini menunjukkan penerapan nyata kombinasi **perulangan dan kondisi** dalam sistem monitoring otomatis yang berjalan hingga pengguna memilih untuk berhenti.

---

##  Kesimpulan Keseluruhan

Dari seluruh latihan, diperoleh pemahaman bahwa:

* Struktur kondisi digunakan untuk **pengambilan keputusan**.
* Perulangan digunakan untuk **menjalankan tugas berulang**.
* Kombinasi keduanya menghasilkan program dinamis dan interaktif.
* *Kode loop flowchart* menjadi contoh penerapan praktis logika kontrol dalam simulasi sensor.

