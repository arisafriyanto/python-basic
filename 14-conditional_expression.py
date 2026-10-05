angka = int(input("Masukkan angka: "))

# with if-else biasa
if angka > 0:
    print("Positif")
else:
    print("Negatif")


# ternary operator
result = "Positif" if angka > 0 else "Negatif"
print(result)