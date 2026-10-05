def app_penjumlahan():
    print("=== Program Penjumlahan ===")
    number1 = int(input("Angka 1: "))
    number2 = int(input("Angka 2: "))
    result = number1 + number2
    print(f"Hasil penjumlahan: {result}")
    print("=== Program penjumlahan berhasil! ===")


def app_pengurangan():
    print("=== Program Pengurangan ===")
    number1 = int(input("Angka 1: "))
    number2 = int(input("Angka 2: "))
    result = number1 - number2
    print(f"Hasil pengurangan: {result}")
    print("=== Program pengurangan berhasil! ===")


def app_perkalian():
    print("=== Program Perkalian ===")
    number1 = int(input("Angka 1: "))
    number2 = int(input("Angka 2: "))
    result = number1 * number2
    print(f"Hasil perkalian: {result}")
    print("=== Program perkalian berhasil! ===")


def app_pembagian():
    print("=== Program Pembagian ===")
    number1 = int(input("Angka 1: "))
    number2 = int(input("Angka 2: "))
    result = number1 / number2
    print(f"Hasil pembagian: {result}")
    print("=== Program pembagian berhasil! ===")


def app_menu():

    while True:
        print("\n=== Calculator ===")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Keluar")
        print("=== Calculator ===\n")

        try:
            pilihan = int(input("Pilihan: "))

            if pilihan == 1:
                app_penjumlahan()
            elif pilihan == 2:
                app_pengurangan()
            elif pilihan == 3:
                app_perkalian()
            elif pilihan == 4:
                app_pembagian()
            elif pilihan == 5:
                print("=== Sampai Jumpa Lagi ===")
                break

        except ValueError:
            print("Angka tidak valid!")
            continue


app_menu()
