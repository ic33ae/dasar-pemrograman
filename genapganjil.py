"""Nama: Ica Apriyanti Rahayu
NIM: 2408415
Kelas: RPL 1B"""

a = int(input("Masukan bilangan"))
if (a > 0):
    print(" Angka positif")
    if (a % 2) == 0:
        print(" Angka adalah genap")
    else:
        print("Angka adalah ganjil")
        
elif (a < 0):
    print(" Angka adalah negatif")
    if (a % 2) == 0:
        print("Angka adalah genap")
    else:
        print("Angka adalah ganjil")
        
print(pow(3,3 ))

tahun = 2024
presiden = "prabowo"
wapres = "gibran"
informasi = "Tahun {} ini terpilih {} sebagai presiden dan {} sebagai wakil presiden"
print(informasi. format(tahun, presiden, wapres))