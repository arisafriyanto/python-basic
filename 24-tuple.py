# Tupple dengan berbagai tipe data

# tup1 = ("Fisika", "Kimia", 345, 321)
# tup2 = (1, 2, 3, 4, 5, 6)

# rgb_color = (255, 128, 64)

# print(tup1)
# print(tup1[1])
# print(tup2[-1])
# print(rgb_color)


point = (5, 10)
print(point[0])
print(point[1])

# Untuk data yang tidak berubah

tanggal_lahir = (17, 11, 2001)
print(type(tanggal_lahir))
print("Tanggal Lahir: ", tanggal_lahir)


# iterasi di tuple
for e in tanggal_lahir:
    print(e)


# iterasi di tuple dengan index
for i in range(len(tanggal_lahir)):
    print(str(i + 1), ".", tanggal_lahir[i])
