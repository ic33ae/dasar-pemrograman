#melihat jumlah iten dalam suatu list
a = ["apel", 'jeruk', "ceri", "durian", "apel"]
print(len(a))

#mengambil index tertentu dalam suatu list
a = ['apel', 'jeruk', 'ceri','durian', 'apel']
print(a[2])

#mengambil list dengan range tertentu
a = ["apel", 'jeruk', "ceri", "durian", "apel"]
print(a[1:5])

#menambah item di akhir list
a = ["apel", 'jeruk', "ceri", "durian", "apel"]
a.append("sirsak") 
print(a)

#mengganti index tertentu dalam suatu list
a = ["apel", 'jeruk', "ceri", "durian", "apel"]
a[3] = "manggis"
print(a)

#menambah item di list tertentu
a = ["apel", 'jeruk', "ceri", "durian", "apel"]
a.insert(3, 'semangka')
print(a)

#menghapus item d index tertentu menurut index
a = ["apel", 'jeruk', "ceri", "durian", "apel"]
a.pop(2)
print(a)

#menghapus item d index tertentu menurut list
a = ["apel", 'jeruk', "ceri", "durian", "apel"]
a.remove('durian')
print(a)

#menambah item di list dari list lainnya
a = ["apel", 'jeruk', "ceri", "durian", "apel"]
b = ['strawberry', 'bluberry" "\n']      
print(a) #a sebelum di extend
a.extend(b) 
print(a)

#memgurutkan item di list sesuai abjadnya
a = ["apel", 'jeruk', "ceri", "durian", "apel"]
a.sort()
print(a)

a = ["apel", 'jeruk', "ceri", "durian", "apel"]
a.count()
print(a)

b = ["Kucing", "Anjing"]
