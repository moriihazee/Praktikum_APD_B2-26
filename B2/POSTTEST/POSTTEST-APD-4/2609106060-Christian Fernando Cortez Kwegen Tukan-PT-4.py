print("========== Los Pollos Hermanos ==========")

USERNAME = "Nando"
PASSWORD = "60"

percobaan = 0
berhasil = False

while percobaan < 3 and not berhasil:
    user = input("Username: ").strip()
    pswd = input("Password: ").strip()

    if user == USERNAME and pswd == PASSWORD:
        berhasil = True
    else:
        percobaan += 1
        if user != USERNAME and pswd != PASSWORD:
            print("Username dan password salah.")
        elif user != USERNAME:
            print("Username salah.")
        else:
            print("Password salah.")

if not berhasil:
    print("Login gagal 3 kali. Program berhenti.")
else:
    print("Login berhasil! Halo,", USERNAME)

    while True:
        print("========== MENU DISTRIBUSI PAKET ==========")
        print("1. Paket Reguler  (1 porsi)")
        print("2. Paket Anak     (1 porsi)")
        print("3. Paket Keluarga (4 porsi)")
        print("4. Keluar")

        while True:
            pilihan = input("Pilih menu (1-4): ").strip()
            if pilihan in ("1", "2", "3", "4"):
                break
            print("Opsi tidak valid")

        if pilihan == "4":
            print("Terima kasih, sampai jumpa!")
            break

        if pilihan == "1":
            nama = "Paket Reguler"
            porsi_per_paket = 1
        elif pilihan == "2":
            nama = "Paket Anak"
            porsi_per_paket = 1
        else:
            nama = "Paket Keluarga"
            porsi_per_paket = 4

        while True:
            teks = input("Jumlah paket yang dibagikan: ").strip()
            if teks == "":
                print("Input tidak boleh kosong.")
            elif not teks.isdigit():
                print("Input harus berupa angka.")
            elif int(teks) < 1:
                print("Jumlah paket minimal 1.")
            else:
                jumlah = int(teks)
                break

        total_porsi = 0
        for i in range(jumlah):
            total_porsi += porsi_per_paket

        if total_porsi >= 20:
            bonus = "5 paket buah"
        elif total_porsi >= 10:
            bonus = "3 botol susu"
        elif total_porsi >= 5:
            bonus = "1 paket vitamin"
        else:
            bonus = "Tidak ada bonus"

        print("--- HASIL DISTRIBUSI ---")
        print("Jenis paket       :", nama)
        print("Jumlah paket      :", jumlah)
        print("Total porsi       :", total_porsi, "porsi")
        print("Penerima manfaat  :", total_porsi, "orang")
        print("Bonus             :", bonus)