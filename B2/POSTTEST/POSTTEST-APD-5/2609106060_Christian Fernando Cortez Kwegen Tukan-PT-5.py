import os

users = [["Nando", "123", "Admin"], ["Cortez", "123", "Pengguna"]]
travel = [
    [1, "Samarinda-Balikpapan", "15-10-2026", "08:00", 150000],
    [2, "Samarinda-Bontang", "15-10-2026", "09:00", 100000]
]
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
        akun = next((u for u in users if u[0] == nama and u[1] == sandi), None)

        if akun is None:
            print("Username atau password salah!")
            input("Tekan Enter untuk lanjut")
            continue

        while True:
            os.system(cls)
            print("===== SISTEM PENDATAAN TRAVEL =====")
            print("Login sebagai:", akun[0], "-", akun[2])
            print("1. Tambah Jadwal")
            print("2. Lihat Jadwal")
            print("3. Ubah Jadwal")
            print("4. Hapus Jadwal")
            print("5. Logout")
            pilih = input("Pilih menu: ")

            if pilih in ("1", "3", "4") and akun[2] != "Admin":
                print("Akses ditolak! Fitur Khusus Admin.")

            elif pilih in ("1", "3", "4"):
                data = None
                if pilih != "1":
                    id_data = input("Masukkan ID jadwal: ")
                    data = next((t for t in travel if id_data.isdigit() and t[0] == int(id_data)), None)

                if pilih != "1" and data is None:
                    print("ID jadwal tidak ditemukan!")
                elif pilih == "4":
                    travel.remove(data)
                    print("Jadwal berhasil dihapus!")
                else:
                    tujuan = input("Tujuan perjalanan: ")
                    tanggal = input("Tanggal: ")
                    jam = input("Jam keberangkatan: ")
                    harga = input("Harga tiket: ")

                    if tujuan.strip() and tanggal.strip() and jam.strip() and harga.isdigit() and int(harga) > 0:
                        if pilih == "1":
                            nomor = max([t[0] for t in travel], default=0) + 1
                            travel.append([nomor, tujuan, tanggal, jam, int(harga)])
                            print("Jadwal berhasil ditambahkan! ID:", nomor)
                        else:
                            data[1:] = [tujuan, tanggal, jam, int(harga)]
                            print("Jadwal berhasil diubah!")
                    else:
                        print("Input tidak valid!")

            elif pilih == "2":
                print()
                print("======= DAFTAR JADWAL =======")
                if not travel:
                    print("Belum ada jadwal travel.")
                for t in travel:
                    print("ID:", t[0], "| Tujuan:", t[1])
                    print("Tanggal:", t[2], "| Jam:", t[3])
                    print("Harga: Rp", t[4])
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
        elif any(u[0] == nama for u in users):
            print("Username sudah dipakai!")
        else:
            users.append([nama, sandi, "Pengguna"])
            print("Registrasi berhasil! Silakan login.")

        input("Tekan Enter untuk lanjut")

    elif menu == "3":
        print("Terima kasih telah menggunakan layanan ini.")
        break

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk lanjut")