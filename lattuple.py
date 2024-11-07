"""Nama: Ica Apriyanti Rahayu
NIM: 2408415
Kelas: RPL 1B"""

a = ["Meja", "Kursi", "Papan tulis", "Pintu"]
x = list (a)
x[2] = "Jendela"
a = tuple(x)
print(a)

a = ["Ayah", "Ibu", "Paman", "Kakek"]
y = list (a)
y.insert(0, "Nenek")
a = tuple(y)
print(a)

a = ["Ayah", "Ibu", "Paman", "Kakek"]
z = list(a)
z.append("Bibi")
a = tuple(z)
print(a)

a = ["Ayah", "Ibu", "Paman", "Kakek"]
s = list(a)
s.pop(2)
a = tuple(s)
print(a)
