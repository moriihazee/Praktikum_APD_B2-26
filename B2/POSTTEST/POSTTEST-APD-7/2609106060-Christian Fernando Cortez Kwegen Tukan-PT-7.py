import os
from datetime import datetime

users = {
    "Nando": {"sandi": "123", "peran": "Admin"},
    "Cortez": {"sandi": "123", "peran": "Pengguna"}
}
travel = {
    1: {"tujuan": "Samarinda-Balikpapan", "tanggal": "15-10-2026", "jam": "08:00", "harga": 150000},
    2: {"tujuan": "Samarinda-Bontang", "tanggal": "15-10-2026", "jam": "09:00", "harga": 100000}
}
cls = "cls" if os.name == "nt" else "clear"

def ambil_id_baru():
    nomor = max(travel, default=0) + 1
    return nomor

def input_data_jadwal():
    tujuan = input("Tujuan perjalanan: ")
    tanggal = input("Tanggal: ")
    jam = input("Jam keberangkatan: ")
    harga = input("Harga tiket: ")
    return tujuan, tanggal, jam, harga

# ===== FUNGSI DENGAN PARAMETER =====
def cek_login(nama, sandi):
    try:
        akun = users[nama]
    except KeyError:
        return None
    else:
        if akun["sandi"] == sandi:
            return akun
        return None

def cari_jadwal(id_data):
    try:
        nomor = int(id_data)
        travel[nomor]
    except (ValueError, KeyError):
        return None
    else:
        return nomor

def validasi_tanggal(tanggal):
    try:
        datetime.strptime(tanggal, "%d-%m-%Y")
    except ValueError:
        return False
    else:
        return len(tanggal) == 10

def validasi_jam(jam):
    try:
        datetime.strptime(jam, "%H:%M")
    except ValueError:
        return False
    else:
        return len(jam) == 5

def validasi_jadwal(tujuan, tanggal, jam, harga):
    try:
        harga_angka = int(harga)
    except ValueError:
        return None
    else:
        if tujuan.strip() and tanggal.strip() and jam.strip() and harga_angka > 0:
            return harga_angka
        return None

def lihat_jadwal():
    print()
    print("======= DAFTAR JADWAL =======")
    if not travel:
        print("Belum ada jadwal travel.")
    for id_t, t in travel.items():
        print("ID:", id_t, "| Tujuan:", t["tujuan"])
        print("Tanggal:", t["tanggal"], "| Jam:", t["jam"])
        print("Harga: Rp", t["harga"])
        print("-" * 30)

def kelola_jadwal(pilih):
    if pilih != "1":
        lihat_jadwal()
        print()
        nomor = cari_jadwal(input("Masukkan ID jadwal: "))
        if nomor is None:
            print("ID jadwal tidak ditemukan!")
            return

    if pilih == "4":
        travel.pop(nomor)
        print("Jadwal berhasil dihapus!")
    else:
        tujuan, tanggal, jam, harga = input_data_jadwal()
        if not validasi_tanggal(tanggal):
            print("Format tanggal tidak valid! Gunakan format DD-MM-YYYY")
        elif not validasi_jam(jam):
            print("Format jam tidak valid! Gunakan format HH:MM (00:00 - 23:59")
        else:
            harga_angka = validasi_jadwal(tujuan, tanggal, jam, harga)
            if harga_angka is None:
                print("Input tidak valid!")
            else:
                data_baru = {"tujuan": tujuan, "tanggal": tanggal, "jam": jam, "harga": harga_angka}
                if pilih == "1":
                    nomor = ambil_id_baru()
                    travel[nomor] = data_baru
                    print("Jadwal berhasil ditambahkan! ID:", nomor)
                else:
                    travel[nomor].update(data_baru)
                    print("Jadwal berhasil diubah!")

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
        akun = cek_login(nama, sandi)
        if akun is None:
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
                kelola_jadwal(pilih)
            elif pilih == "2":
                lihat_jadwal()
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
        else:
            try:
                users[nama]
            except KeyError:
                users[nama] = {"sandi": sandi, "peran": "Pengguna"}
                print("Registrasi berhasil! Silakan login.")
            else:
                print("Username sudah dipakai!")
        input("Tekan Enter untuk lanjut")

    elif menu == "3":
        print("Terima kasih telah menggunakan layanan ini.")
        break
    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk lanjut")
