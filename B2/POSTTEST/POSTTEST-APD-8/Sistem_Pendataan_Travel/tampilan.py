import os
from colorama import Fore, Style, init
from prettytable import PrettyTable

init(autoreset=True)
cls = "cls" if os.name == "nt" else "clear"


def bersihkan_layar():
    os.system(cls)


def judul(teks):
    print(Fore.CYAN + Style.BRIGHT + teks)


def sukses(pesan):
    print(Fore.GREEN + pesan)


def error(pesan):
    print(Fore.RED + pesan)


def peringatan(pesan):
    print(Fore.YELLOW + pesan)


def tunggu():
    input("Tekan Enter untuk lanjut")


def format_rupiah(angka):
    return "Rp " + f"{angka:,}".replace(",", ".")


def input_data_jadwal():
    tujuan = input("Tujuan perjalanan: ")
    tanggal = input("Tanggal (DD-MM-YYYY): ")
    jam = input("Jam keberangkatan (HH:MM): ")
    harga = input("Harga tiket: ")
    return tujuan, tanggal, jam, harga


def lihat_jadwal():
    from data_travel import travel
    print()
    judul("======= DAFTAR JADWAL =======")
    if not travel:
        peringatan("Belum ada jadwal travel.")
        return

    tabel = PrettyTable()
    tabel.field_names = ["ID", "Tujuan", "Tanggal", "Jam", "Harga"]
    for id_t, t in travel.items():
        tabel.add_row([id_t, t["tujuan"], t["tanggal"], t["jam"], format_rupiah(t["harga"])])
    tabel.align["Tujuan"] = "l"
    tabel.align["Harga"] = "r"
    print(tabel)