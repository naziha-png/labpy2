# Program mengurutkan data
print("Program mengurutkan data")
# Input minimal 3 bilangan
a = int(input("Bilangan ke-1: "))
b = int(input("Bilangan ke-2: "))
c = int(input("Bilangan ke-3: "))
# Masukkan ke dalam list
data = [a, b, c]
# Urutkan data
data.sort()
# Tampilkan hasil
print("Urutan bilangan:", data[0], data[1], data[2])