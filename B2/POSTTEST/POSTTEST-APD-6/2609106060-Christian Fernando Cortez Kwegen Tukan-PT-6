import os

users = {
    "Nando": {"sandi": "123", "peran": "Admin"},
    "Cortez": {"sandi": "123", "peran": "Pengguna"}
}
travel = {
    1: {"tujuan": "Samarinda-Balikpapan", "tanggal": "15-10-2026", "jam": "08:00", "harga": 150000},
    2: {"tujuan": "Samarinda-Bontang", "tanggal": "15-10-2026", "jam": "09:00", "harga": 100000}
}
cls = "cls" if os.name == "nt" else "clear"

while True:
    os.system(cls)
    print("===== SISTEM PENDATAAN TRAVEL =====")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    menu = input("Pilih menu: ")

    if menu == "1":
        nama = input("Username: ")
        sandi = input("Password: ")
        akun = users.get(nama)

        if akun is None or akun["sandi"] != sandi:
            print("Username atau password salah!")
            input("Tekan Enter untuk lanjut")
            continue

        while True:
            os.system(cls)
            print("===== SISTEM PENDATAAN TRAVEL =====")
            print("Login sebagai:", nama, "-", akun["peran"])
            print("1. Tambah Jadwal")
            print("2. Lihat Jadwal")
            print("3. Ubah Jadwal")
            print("4. Hapus Jadwal")
            print("5. Logout")
            pilih = input("Pilih menu: ")

            if pilih in ("1", "3", "4") and akun["peran"] != "Admin":
                print("Akses ditolak! Fitur Khusus Admin.")

            elif pilih in ("1", "3", "4"):
                data = None
                if pilih != "1":
                    id_data = input("Masukkan ID jadwal: ")
                    if id_data.isdigit() and int(id_data) in travel:
                        data = travel[int(id_data)]

                if pilih != "1" and data is None:
                    print("ID jadwal tidak ditemukan!")
                elif pilih == "4":
                    travel.pop(int(id_data))
                    print("Jadwal berhasil dihapus!")
                else:
                    tujuan = input("Tujuan perjalanan: ")
                    tanggal = input("Tanggal: ")
                    jam = input("Jam keberangkatan: ")
                    harga = input("Harga tiket: ")

                    if tujuan.strip() and tanggal.strip() and jam.strip() and harga.isdigit() and int(harga) > 0:
                        if pilih == "1":
                            nomor = max(travel, default=0) + 1
                            travel[nomor] = {"tujuan": tujuan, "tanggal": tanggal, "jam": jam, "harga": int(harga)}
                            print("Jadwal berhasil ditambahkan! ID:", nomor)
                        else:
                            data.update({"tujuan": tujuan, "tanggal": tanggal, "jam": jam, "harga": int(harga)})
                            print("Jadwal berhasil diubah!")
                    else:
                        print("Input tidak valid!")

            elif pilih == "2":
                print()
                print("======= DAFTAR JADWAL =======")
                if not travel:
                    print("Belum ada jadwal travel.")
                for id_t, t in travel.items():
                    print("ID:", id_t, "| Tujuan:", t["tujuan"])
                    print("Tanggal:", t["tanggal"], "| Jam:", t["jam"])
                    print("Harga: Rp", t["harga"])
                    print("-" * 30)

            elif pilih == "5":
                break

            else:
                print("Pilihan tidak valid!")

            input("Tekan Enter untuk lanjut")

    elif menu == "2":
        nama = input("Username baru: ")
        sandi = input("Password baru: ")

        if not nama.strip() or not sandi.strip():
            print("Username dan password tidak boleh kosong!")
        elif nama in users:
            print("Username sudah dipakai!")
        else:
            users[nama] = {"sandi": sandi, "peran": "Pengguna"}
            print("Registrasi berhasil! Silakan login.")

        input("Tekan Enter untuk lanjut")

    elif menu == "3":
        print("Terima kasih telah menggunakan layanan ini.")
        break

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk lanjut")