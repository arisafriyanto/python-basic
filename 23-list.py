# daftar_kosong = []

# angka = [1, 2, 3, 4, 5]
# print(angka)


# nama = ["Alice", "Bob", "Charlie"]
# print(nama)

# mix = ["Alice", 25, "Bob", 26]
# print(mix)


### Manipulasi List

# fruits = ["apple", "orange", "banana", "Mango"]
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])

# print(fruits[-1])


# colors = ["Red", "Blue", "Green"]
# print(colors)

# colors[1] = "Yellow"
# print(colors)


# append() - menambah di akhir
fruits = ["apple", "orange"]
fruits.append("banana")
print(type(fruits))
print(fruits)

# remove() - menghapus nilai tertentu yang ditemukan pertama kali
numbers = [1, 3, 2, 3, 4, 5, 6, 5]
numbers.remove(3)
print(numbers)

# pop() - menghapus element terakhir
numbers.pop()
print(numbers)

# del - menghapus berdasarkan index
del numbers[5]
print(numbers)

# len() - panjang list
print(len(fruits))

# menggabungkan list

list1 = [1, 2, 3]
list2 = [4, 5, 6]

merge = list1 + list2

print(merge)


# check apakah apple ada di fruits
print("Apple available!") if "aspple" in fruits else print("Not available")

# menggukana for loop
print("List Fruits: ")
for item in fruits:
    print("-", item)

# Dengan index
for i in range(len(fruits)):
    print(str(i + 1) + ".", fruits[i])
