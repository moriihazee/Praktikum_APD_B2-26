import pwinput
from tampilan import sukses, error

users = {
    "Nando": {"sandi": "123", "peran": "Admin"},
    "Cortez": {"sandi": "123", "peran": "Pengguna"}
}


def cek_login(nama, sandi):
    try:
        akun = users[nama]
    except KeyError:
        return None
    else:
        if akun["sandi"] == sandi:
            return akun
        return None


def proses_login():
    """Mengembalikan (nama, akun) jika berhasil, None jika gagal."""
    nama = input("Username: ")
    sandi = pwinput.pwinput("Password: ", mask="*")
    akun = cek_login(nama, sandi)
    if akun is None:
        error("Username atau password salah!")
        return None
    return nama, akun


def proses_register():
    nama = input("Username baru: ")
    sandi = pwinput.pwinput("Password baru: ", mask="*")
    if not nama.strip() or not sandi.strip():
        error("Username dan password tidak boleh kosong!")
        return
    try:
        users[nama]
    except KeyError:
        users[nama] = {"sandi": sandi, "peran": "Pengguna"}
        sukses("Registrasi berhasil! Silakan login.")
    else:
        error("Username sudah dipakai!")