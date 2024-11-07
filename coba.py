angka = int(input(f"Masukan bilangan yang akan di cek: "))

if (angka > 0):
    print("Maka bilangan positif")
    if (angka % 2 == 0):
        print("Bilangan adalah genap")
    else:
        print("Bilangan adalah ganjil")

if (angka < 0):
    print("Maka bilangan negatif")
    if (angka % 2 == 0):
        print("Bilangan adalah genap")
    else:
        print("Bilangan adalah ganjil")
