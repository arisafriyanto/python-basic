# nama = "Budi"
# nama = "Budi"
# umur = 25

# # pesan = "Nama saya " + nama + ", Umur " + umur    # Error
# pesan = "Nama saya " + nama + ", Umur " + str(umur)

# print(pesan)
# print(len(nama))

# word = "Pyhton"

# print(word[0])
# print(word[1])

# print(word[-1])
# print(word[-2])


# # Indexing start : jumlah karakter

# print(word[0:3])
# print(word[2:5])

# print(word[:3])
# print(word[3:])
# print(word[:])



## String Methods (Fungsi String)

# nama = "Alice"
# nama_upper = nama.upper()
# print(nama_upper)

# nama_lower = nama.lower()
# print(nama_lower)


# nama2 = "John Doe"
# nama_title = nama2.title()
# print(nama_title)

# nama_capitalize = nama2.capitalize()
# print(nama_capitalize)


# nama3 = "   Alice   "
# nama_strip = nama3.strip()
# print(nama_strip)


# sentence = "I love Java"
# new_sentence = sentence.replace("Java", "Bandung")
# print(new_sentence)

# nama4 = "Mississipisii"
# countS = nama4.count('s')
# print(countS)

# sentence2 = "Python Programming"
# position = sentence2.find("Programming")
# print(position)



### String Interpolation

# nama = "Alice"
# umur = 25
# kota = "Jakarta"

# # Menggunakan f-string
# profil = f"Halo, nama saya {nama}, umur {umur} tahun, tinggal di {kota}"
# print(profil)

# # Concatenation (lebih ribet)
# profil_lama = "Halo, nama saya " + nama + ", umur " + str(umur) + " tahun, tinggal di " + kota
# print(profil_lama)



### f-strings dengan Expressions

harga = 100000
jumlah = 3

# Operasi matematika dalam f-string
total = f"Total : Rp {harga * jumlah:,}"
print(total)

# Method calls dalam f-string
nama = "john doe"
salam = f"Halo {nama.title()}!"
print(salam)