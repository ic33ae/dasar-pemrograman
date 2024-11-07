x = 4
if ( x > 0): #bila true maka akn dui eksekusi print nya
    print("eksekusi perintah ini")
    
    
# pernyataan else untuk mengeksekusi pernyataan yang false
x  = 1
if ( x < 0 ): 
    print("Perintah ini tidak akn di eksekusi")
else print("eksekusi perintah")

umur = 16 
if (umur > 17):
    print ("Anda boleh membuat SIM")
elif (umur < 17):
    print ("anda belum bisa membuat SIM")
    
jumlah_barang =  int(input(f"Masukan jumlah barang"))

if (jumlah_barang < 100):
    print("Maka harga perbarang adalah Rp. 5000")
elif (jumlah_barang >= 100):
    print ("Maka harga perbarang adalah Rp. 4000")
elif (jumlah_barang >150):
    print ("Maka harga perbarang adalah Rp. 2.500")
    
#nexted if apaila ada statement if dalam statement if 
a = 10

if (a>0):
    print("Nilai a lebih besar dari 0")
    if (a>5): 
        print("Nilai a juga lebih besar dari 5")
    else: 
        print("Nilai a lrbih kecil dari 5")

