import random  # untuk menghasilkan angka acak

# Input jumlah bilangan
n = int(input("Masukkan jumlah n: "))

i = 0  # penghitung jumlah bilangan yang sudah dicetak
while i < n:
    bil = random.random()  # menghasilkan bilangan acak antara 0.0 - 1.0
    if bil < 0.5:          # hanya cetak jika < 0.5
        print(bil)
        i += 1             # tambahkan penghitung bila angka valid

