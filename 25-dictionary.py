# Dictionary dengan data
siswa = {"nama": "Budi Santoso", "umur": 20, "kelas": "12C"}
print(siswa)

print(siswa["nama"])
print(siswa["umur"])
print(siswa["kelas"])

# Mengubah nilai
siswa["umur"] = 21
print(siswa)

# Menghapus key-value
del siswa["kelas"]
print(siswa)

# Mengiterasi keys
for key in siswa:
    print(key, ":", siswa[key])

# Mwngiterasi key-value pairs
for key, value in siswa.items():
    print(key, "=", value)
