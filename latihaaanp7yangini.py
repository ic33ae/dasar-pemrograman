"""Nama: Ica Apriyanti Rahayu
NIM: 2408415
Kelas: RPL 1B"""

jumlah_barang =  int(input(f"Masukan jumlah barang: "))
harga_satu = 5000
harga_dua = 4000
harga_tiga = 2500
if (jumlah_barang < 100):
    print("Maka harga perbarang adalah Rp.", jumlah_barang*harga_satu)
elif (jumlah_barang >150):
    ("Maka harga perbarang adalah Rp.", jumlah_barang*harga_tiga)
elif (jumlah_barang >= 100):
    print ("Maka harga perbarang adalah Rp.", jumlah_barang*harga_dua)

