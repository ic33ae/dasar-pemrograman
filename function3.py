"""Nama: Ica Apriyanti Rahayu
NIM: 2408415
Kelas: RPL 1B"""

def rata-rata (*angka):
    total = sum(angka)
    rata-rata = total / len(angka)
    return total, rata-rata

angka = []
while True:
    inp_angka = int(input("Masukan angka (ketik 'selesai' untuk berhenti): "))
    if inp_angka == "selesai":
        break
    angka.append(inp_angka)
    
total, rata-rata = rata-rata(*angka)
print("Nilai total: ", nilai_total)
print("Rata-rata: ", rata_rata)

    
