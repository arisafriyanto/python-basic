# def nama_function():
#     print("Hello dari function")


# nama_function()
# nama_function()
# nama_function()


# def sayHello(name = "John"):
#     print("Hello, ", name)
#     print("Nice to meet you!")


# sayHello("Alice")
# sayHello("Bob")


# def hitung_luas_persegi(radius):
#     pi = 314159
#     luas = pi * radius * radius

#     return luas


# luas1 = hitung_luas_persegi(5)
# luas2 = hitung_luas_persegi(10)

# print(f"Luas lingkarang radius 5:", luas1)
# print(f"Luas lingkarang radius 10:", luas2)
# print("Total luas:", luas1 + luas2)


# Keyword Argument

# def greeting(name, age, city):
#     print("Name: ", name.title())
#     print("Age: ", age)
#     print("City: ", city)
#     print(15 * "-")


# greeting("Alice", 20, "Jakarta")
# greeting(age=23, name="John", city="Surabaya")
# greeting(age=21, city="Tangerang", name="Hendri")


# Global variable

# nama_global = "Alice"


# def tampilkan_nama():
#     print("Nama: ", nama_global)


# def ubah_nama():
#     global nama_global
#     nama_global = "Bob"


# tampilkan_nama()
# ubah_nama()
# tampilkan_nama()


# Parameter Dinamis


def cetak_list(*list):
    for i in list:
        print(i)


cetak_list(1, 2, 3, 4, 5)


def cetak_dict(**dict):
    for key, value in dict.items():
        print(f"{key} : {value}")


cetak_dict(name="Aris", age=24, city="Bandung")
