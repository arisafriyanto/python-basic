day = input("Masukkan nama hari: ").lower()

match day:
    case "senin" | "selasa" | "rabu" | "kamis" | "jumat":
        print("Hari kerja")
    case "sabtu" | "minggu":
        print("Hari Libur")
    case _:
        print("Nama hari tidak valid!")
