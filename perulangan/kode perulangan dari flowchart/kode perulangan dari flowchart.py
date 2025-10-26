# Program pengendali suhu dan kelembapan otomatis
# Berdasarkan nilai standar dan toleransi

# Nilai standar dan batas toleransi
standar_suhu = 30
TSmin = 25
TSmax = 35

standar_kelembaban = 50
TKmin = 45
TKmax = 55

while True:  # perulangan terus menerus
    print("\n=== PEMBACAAN SENSOR ===")

    # Input suhu & kelembapan (simulasi sensor)
    S = float(input("Masukkan suhu saat ini (°C): "))
    K = float(input("Masukkan kelembapan saat ini (%): "))

    print("\n--- HASIL PEMERIKSAAN ---")

    # --- Cek suhu ---
    if S > TSmax:
        print(f"Suhu {S}°C > {TSmax}°C →  Terlalu panas! Nyalakan pendingin.")
    elif S < TSmin:
        print(f"Suhu {S}°C < {TSmin}°C →  Terlalu dingin! Nyalakan pemanas.")
    else:
        print(f"Suhu {S}°C dalam batas normal ({TSmin}°C - {TSmax}°C). ✅")

    # --- Cek kelembapan ---
    if K > TKmax:
        print(f"Kelembapan {K}% > {TKmax}% → Terlalu lembap! Nyalakan pengering.")
    elif K < TKmin:
        print(f"Kelembapan {K}% < {TKmin}% → Terlalu kering! Nyalakan pelembab.")
    else:
        print(f"Kelembapan {K}% dalam batas normal ({TKmin}% - {TKmax}%). ✅")

    # Tanya apakah ingin lanjutkan loop
    ulang = input("\nBaca sensor lagi? (y/n): ")
    if ulang.lower() != 'y':
        print("\nProgram selesai. Semua sistem stabil ")
        break