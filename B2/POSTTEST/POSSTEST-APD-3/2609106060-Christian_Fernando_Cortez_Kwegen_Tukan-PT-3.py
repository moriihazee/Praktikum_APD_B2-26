Nama = "Nando"
NIM = "60"

username = input("Masukkan Username: ")
password = input("Masukkan Password: ")

login_berhasil = False

if username == Nama:
    if password == NIM:
        login_berhasil = True
    else:
        print("Password Salah!")
else:
    print("Username Salah!")

if login_berhasil:
    print("Login Berhasil! Selamat Datang,", username)

    total_point = int(input("Masukkan Total Point: "))

    if total_point < 0:
        print("Error: Point Tidak Bisa Lebih Rendah Dari 0!")
    else:
        if total_point < 100:
            rank = "Rookie"
            next_rank = "Warrior"
            sisa = 100 - total_point
        elif total_point < 300:
            rank = "Warrior"
            next_rank = "Master"
            sisa = 300 - total_point
        elif total_point < 1000:
            rank = "Master"
            next_rank = "Grand Master"
            sisa = 1000 - total_point
        elif total_point < 5000:
            rank = "Grand Master"
            next_rank = "Legend"
            sisa = 5000 - total_point
        else:
            rank = "Legend"
            next_rank = None
            sisa = 0

        print(f"Rank kamu: {rank}")
        if next_rank:
            print(f"Butuh {sisa} poin lagi untuk naik ke rank '{next_rank}'")
        else:
            print("Selamat! Kamu sudah di rank tertinggi!")
        print("=" * 70)
else:
    print("Program berhenti karena login gagal.")