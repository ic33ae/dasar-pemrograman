#numeric


"""absolut"""
x= abs(-20)
print(x)

y= pow(4,5)
print(y)

kali= 3*4*2
tambah= 5+22
bagi= 4/2
print(kali + bagi - bagi * bagi + kali)

#menghitung luas keliling
panjang= int(input("Masukan panjang dari persegi :"))
lebar= int(input("Masukan lebra dari persegi :"))
tinggi= int(input("Masukan tinggi dari persegi :"))
luas= (panjang * tinggi * lebar)
print(f"Hasil luas keliling dari persegi panjang adalah", luas)


panjang= int(input("Masukan panjang dari persegi :"))
lebar= int(input("Masukan lebra dari persegi :"))
tinggi= int(input("Masukan tinggi dari persegi :"))

print(f"Luas keliling dari persegi panjang adalah :", panjang * tinggi * lebar)

nama= " Ica Apriyanti Rahayu "
tahun_lahir= 2006
umur= 2024-tahun_lahir
rencana_menikah= umur + 5
kapan= "Nama saya {} di tahun ini saya berumur {} tahun, rencananya saya menikah di umur {}"
print(kapan.format(nama, umur, rencana_menikah))

nama= " Ica Apriyanti Rahayu "
tahun_lahir= 2006
umur= 2024-tahun_lahir
rencana_menikah= umur + 5
print(f"Nama saya {nama} di tahun ini saya berumur {umur} tahun, rencananya saya menikah di umur {rencana_menikah}")


print("Halo user! Isi registrasi dulu ya :)")
nama= input("Masukan nama lengkap: ")
print('Masukan tanggal, bulan, dan tahun lahir mu: ')
tanggal= int(input("Tanggal lahir: "))
bulan= input("Bulan lahir: ")
tahun= int(input("Tahun lahir: "))
tbt= tanggal, bulan, tahun
umur= 2024 - tahun
username= input("Masukan username kamu")

print(f"selamat bergabung {nama}, format lahir kamu {tbt} dan kamu berumur {umur}, apakah benar?" ) 

a= int(input("masukan angka: "))
b= int(input("masukan angka: "))
c= int(input("masukan angka: "))
hasil= a + b + c
print(f"Hasil dari penjumlahan {a} + {b} + {c} = {hasil}\n ")

#kecepatan
jarak= int(input("Masukan jarak: "))
waktu= int(input("Masukan waktu: "))
kecepatan= jarak * waktu
print(f"Maka kecepatannya adalah {kecepatan} m/s \n" ) 

#luas bola
print("Hitung luas bola 🎂")
r= int(input("Masukan jari-jari bola: "))
luas_bola= 4 * 22/7 * (r**2)
print(f"Maka luas bola adqlqh {luas_bola}  \n")

print("Hitung luas bola 🎂")
r= float(input("Masukan jari-jari bola: "))
luas_bola= 4 * 3,14 * (r**2)
print(f"Maka luas bola adqlqh {luas_bola} \n")

#luas balok

panjang= int(input('Masukan panjang balok: '))
lebar= int(input('Masukkan lebar balok: '))
tinggi= int(input('Masukkan tinggi balok: '))
luas= 2 * ((panjang*lebar) + (panjang*tinggi) + (tinggi*lebar))
print(f"Maka luas balok adalah = {luas}")


x= 2
y= 7
z= 4
operasi= x + y - z * x + (x*y)
print(operasi)


#liast
warna= ['merah', 'kuning', 'hijau', 'jingga', 'biru']
print(warna[0], "\n")
tambah_warna= input("Masukkan warna kesukaan mu ") 
index= int(input('Mau di masukkan ke index berapa: '))
warna.insert(index, tambah_warna)
print(warna)

warna.pop(0)
print(warna)

warna.append("cream")
print(warna)
warna_lain= ['burgundy', 'hazelnut', 'biscuit', 'mocca']
warna.extend(warna_lain)
print(warna)

warna.sort()
print(warna)

warna.reverse()
print(warna)

print(len(warna), "\n")

# List nilai mahasiswa
nilai_mahasiswa = [88, 75, 63, 97, 82, 74, 91, 80, 81, 63 ]

# Nilai maksimum, minimum, dan rata-rata nilai mahasiswa
nilai_maks = max(nilai_mahasiswa)
print("Nilai mahasiswa terbesar adalah: ", nilai_maks)

nilai_min = min(nilai_mahasiswa)
print("Nilai mahasiswa terkecil adalah: ", nilai_min)

rata_rata = sum(nilai_mahasiswa)/len(nilai_mahasiswa)
print("Rata-rata nilai mahasiswa adalah: ", rata_rata)

# Angka terbesar ke-dua
nilai_mahasiswa.sort()
print(nilai_mahasiswa)
nilai_terbesar_kedua = nilai_mahasiswa[-2] 
print("Nilai mahasiswa terbesar ke-dua adalah : ", nilai_terbesar_kedua, '\n')

# List koordinat lokasi
lokasi = (
    ("Jakarta", (-6.2088, 106.8456)),
    ("Bandung", (-6.9175, 107.6191)),
    ("Surabaya", (-7.2575, 112.7521)) )

# Koordinat lokasi Bandung
bandung_koordinat = lokasi [1][1]
print("Titik koordinat Bandung adalah: ", bandung_koordinat)

# Jumlah lokasi tersimpan
jumlah_lokasi = len(lokasi)
print("Jumlah lokasi tersimpan sebanyak:", jumlah_lokasi)

hewan= ("kuicng", 'jangkrik', 'harimau')
b= list(hewan)
b.insert(3, 'kuda')
hewan= tuple(b)
print(hewan)

b.pop(3)
hewan= tuple(b)
print(hewan)

b=list(hewan)
baru= input('Masukan nama hewan yang kamu inginkan: ')
b.append(baru)
hewan= tuple(b)
print(hewan)
jumlah_hewan= len(hewan)
print("Maka jumlah hewan seluruhnya adalah : ", jumlah_hewan)