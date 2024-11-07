"""Nama: Ica Apriyanti Rahayu
NIM: 2408415
Kelas: RPL 1B"""

a = ["Apel", 'Jeruk', "Ceri", "Durian", "Apel"]
a[2] = "Cherry"
print(a)

nama_buah = input ("Masukan nama buah: ")
index_baru = int(input ("Masukan urutan Index: "))
a.insert(index_baru, nama_buah)
print(a)

a.sort()
print(a)