from datetime import datetime

travel = {
    1: {"tujuan": "Samarinda-Balikpapan", "tanggal": "15-10-2026", "jam": "08:00", "harga": 150000},
    2: {"tujuan": "Samarinda-Bontang", "tanggal": "15-10-2026", "jam": "09:00", "harga": 100000}
}


# ===== VALIDASI =====
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


def cek_input(tujuan, tanggal, jam, harga):
    """Mengembalikan (data_jadwal, pesan_error). Salah satunya None."""
    if not validasi_tanggal(tanggal):
        return None, "Format tanggal tidak valid! Gunakan format DD-MM-YYYY"
    if not validasi_jam(jam):
        return None, "Format jam tidak valid! Gunakan format HH:MM (00:00 - 23:59)"
    harga_angka = validasi_jadwal(tujuan, tanggal, jam, harga)
    if harga_angka is None:
        return None, "Input tidak valid!"
    return {"tujuan": tujuan, "tanggal": tanggal, "jam": jam, "harga": harga_angka}, None


# ===== CRUD =====
def ambil_id_baru():
    return max(travel, default=0) + 1


def cari_jadwal(id_data):
    try:
        nomor = int(id_data)
        travel[nomor]
    except (ValueError, KeyError):
        return None
    else:
        return nomor


def tambah_jadwal(data_baru):
    nomor = ambil_id_baru()
    travel[nomor] = data_baru
    return nomor


def ubah_jadwal(nomor, data_baru):
    travel[nomor].update(data_baru)


def hapus_jadwal(nomor):
    travel.pop(nomor)