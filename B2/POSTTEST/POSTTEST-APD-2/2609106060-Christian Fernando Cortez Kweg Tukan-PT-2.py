#1.Data/List harga produk skincare
skincare_1 = 35000
skincare_2 = 42000
skincare_3 = 50000
skincare_4 = 55000
skincare_5 = 68000
skincare_6 = 70000

#2.Total pengeluaran
ongkos_kirim = 12000
total_pengeluaran = (skincare_1 + skincare_2 + skincare_3 +
                      skincare_4 + skincare_5 + skincare_6 +
                      ongkos_kirim)

#3.Rata-rata (pakai len())
daftar_skincare = [skincare_1, skincare_2, skincare_3,
                    skincare_4, skincare_5, skincare_6]
rata_rata = total_pengeluaran / len(daftar_skincare)

#4.Variabel NIM
nim = 60

#5.Variabel bolean
bolean = nim < rata_rata

#6.Menampilkan semua variabel
print("Harga skincare_1     :", skincare_1)
print("Harga skincare_2     :", skincare_2)
print("Harga skincare_3     :", skincare_3)
print("Harga skincare_4     :", skincare_4)
print("Harga skincare_5     :", skincare_5)
print("Harga skincare_6     :", skincare_6)
print("Ongkos kirim         :", ongkos_kirim)
print("Total pengeluaran    :", total_pengeluaran)
print("Rata-rata            :", rata_rata)
print("nim                  :", nim)
print("bolean (nim<rata rata)   :", bolean)