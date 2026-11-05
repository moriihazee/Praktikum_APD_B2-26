from auth import proses_login, proses_register
from data_travel import (cari_jadwal, cek_input, tambah_jadwal,
                         ubah_jadwal, hapus_jadwal)
from tampilan import (bersihkan_layar, judul, sukses, error, tunggu,
                      lihat_jadwal, input_data_jadwal)


def kelola_jadwal(pilih):
    """pilih: '1' = tambah, '3' = ubah, '4' = hapus"""
    if pilih != "1":
        lihat_jadwal()
        print()
        nomor = cari_jadwal(input("Masukkan ID jadwal: "))
        if nomor is None:
            error("ID jadwal tidak ditemukan!")
            return

    if pilih == "4":
        hapus_jadwal(nomor)
        sukses("Jadwal berhasil dihapus!")
        return

    data_baru, pesan_error = cek_input(*input_data_jadwal())
    if data_baru is None:
        error(pesan_error)
    elif pilih == "1":
        sukses(f"Jadwal berhasil ditambahkan! ID: {tambah_jadwal(data_baru)}")
    else:
        ubah_jadwal(nomor, data_baru)
        sukses("Jadwal berhasil diubah!")


def menu_akun(nama, akun):
    while True:
        bersihkan_layar()
        judul("===== SISTEM PENDATAAN TRAVEL =====")
        print("Login sebagai:", nama, "-", akun["peran"])
        print("1. Tambah Jadwal")
        print("2. Lihat Jadwal")
        print("3. Ubah Jadwal")
        print("4. Hapus Jadwal")
        print("5. Logout")
        pilih = input("Pilih menu: ")

        if pilih in ("1", "3", "4") and akun["peran"] != "Admin":
            error("Akses ditolak! Fitur Khusus Admin.")
        elif pilih in ("1", "3", "4"):
            kelola_jadwal(pilih)
        elif pilih == "2":
            lihat_jadwal()
        elif pilih == "5":
            break
        else:
            error("Pilihan tidak valid!")
        tunggu()


def main():
    while True:
        bersihkan_layar()
        judul("===== SISTEM PENDATAAN TRAVEL =====")
        print("1. Login")
        print("2. Register")
        print("3. Keluar")
        menu = input("Pilih menu: ")

        if menu == "1":
            hasil = proses_login()
            if hasil is None:
                tunggu()
                continue
            menu_akun(*hasil)
        elif menu == "2":
            proses_register()
            tunggu()
        elif menu == "3":
            print("Terima kasih telah menggunakan layanan ini.")
            break
        else:
            error("Pilihan tidak valid!")
            tunggu()


if __name__ == "__main__":
    main()