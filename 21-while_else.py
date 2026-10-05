password_benar = "python123"
percobaan = 0
max_percobaan = 3

while percobaan < max_percobaan:
    password = input("Masukkan password anda: ")
    percobaan += 1

    if password == password_benar:
        print("Selamat! Login anda berhasil!")
        break
    else:
        print("Password salah. Sisa percobaan: ", max_percobaan - percobaan)
else:
    print("Terlalu banyak percobaan gagal. Akses ditolak!")
