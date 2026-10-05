def app_tebak_angka():
    import random

    angka_acak = random.randint(1, 10)
    maximal_tebakan = 3
    tebakan = 0

    print("\n=== Tebak Angka ===")
    print(f"Tebak angka 1-10. Kamu punya {maximal_tebakan} kesempatan.\n")

    while tebakan < maximal_tebakan:
        tebakan += 1

        angka_user = int(input(f"Tebakan {tebakan}/{maximal_tebakan}: "))

        if angka_user > angka_acak:
            print("Angka terlalu besar.\n")
        elif angka_user < angka_acak:
            print("Angka terlalu kecil.\n")
        else:
            print(f"Benar! Angkanya adalah {angka_acak}.")
            print(f"Kamu berhasil dalam {tebakan} tebakan.\n")
            break

    else:
        print(f"Kesempatan habis. Angka yang benar adalah {angka_acak}.\n")

    input("Tekan Enter untuk kembali ke menu...")


def app_menu():

    while True:
        print("\n=== Program Tebak Angka ===")
        print("1. Tebak Angka")
        print("2. Keluar")

        pilihan = int(input("Pilih menu: "))

        if pilihan == 1:
            app_tebak_angka()

        elif pilihan == 2:
            print("\nProgram selesai. Terima kasih!")
            break

        else:
            print("Pilihan tidak valid.")


app_menu()
