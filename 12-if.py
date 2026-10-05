angka = int(input("Masukkan angka: "))

if angka > 0: 
    if angka % 2 == 0:
        print("Angka genap positif")
    else:
        print("Angka ganjil positif")
elif angka < 0:
    print("Angka negatif")
elif angka == 0:
    print("Angka 0")

