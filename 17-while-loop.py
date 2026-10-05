# Mencetak angka 1 sampai 5

# number = 1
# while number <= 5:
#     print(number)
#     number += 1


# Input sampai benar

password = ""

while password != "123456":
    password = input("Masukkan password: ")
    if password != "123456":
        print("Password salah, silakan coba lagi!")
print("Password benar!")
