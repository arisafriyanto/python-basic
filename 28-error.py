## Try-Except

# print(6 * "=", " Kalkulator ", 6 * "=")

# try:
#     a = int(input("Masukkan angka pertama: "))  # tanpa int() default str()
#     b = int(input("Masukkan angka kedua: "))
#     result = a / b
#     print("Hasil: ", result)

# except ValueError:
#     print("Mohon masukkan angka yang valid!")
# except ZeroDivisionError:
#     print("Tidak bisa dibagi dengan noll!")
# except:
#     print("Terjadi error dalam perhitungan!")


## Try-Except-Else (Bagian else dijalankan jika tidak ada error pada try-except)

# try:
#     number = int(input("Masukkan angka: "))
# except:
#     print("Input tidak valid!")
# else:
#     print("Angka yang anda masukkan: ", number)
#     if number > 0:
#         print("Angka positif")
#     elif number < 0:
#         print("Angka negatif")
#     else:
#         print("Angka noll")


## Try-Except-Finnaly (finally selalu dijalankan, baik ada error atau tidak)

try:
    number = int(input("Masukkan angka: "))
    print(f"Angka yang anda masukkan: {number}")
except ValueError:
    print("Input tidak valid!")
finally:
    print("Progam selesai dijalankan!")
