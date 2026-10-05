# print("=== Simpan Data Nilai ===")

# file = open("nilai-siswa.txt", "w")

# while True:
#     nama = input("Nama Siswa (enter untuk selesai): ")
#     if nama == "":
#         break

#     nilai = input("Nilai: ")

#     # Tulis ke file
#     file.write(nama + "," + nilai + "\n")
#     print("Data", nama, "Berhasil disimpan!")

# file.close()
# print("Semua data berhasil disimpan ke nilai-siswa.txt")


# print("=== Menampilkan Data Nilai ===")

# file = open("nilai-siswa.txt", "r")

# for line in file:
#     data = line.strip().split(",")
#     print(data[0], ":", data[1])

# file.close()

# print("=== Selesai ===")


# print("=== Menampilkan Data Nilai ===")

# with open("nilai-siswa.txt", "r") as file:
#     for line in file:
#         data = line.strip().split(",")
#         print(data[0], ":", data[1])

# print("=== Selesai ===")


### Error Handling untuk File

print("=== Menampilkan Data Nilai ===")

try:
    with open("nilai-siswa-1.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            print(data[0], ":", data[1])
except FileNotFoundError:
    print("File tidak ditemukan.")

print("=== Selesai ===")
