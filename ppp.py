kucing = { 
  "nama": "kuro",   
  "umur": 2 ,
  "ras": "persian",
"jantan": "true",
"hobi": ["makan", "tidur"]
}

print(len(kucing))

kucing = { 
  "nama": "kuro",   
  "umur": 2 ,
  "ras": "persian",
"jantan": "true",
"hobi": ["makan", "tidur"]
}

kucing.update({"umur": 4, "ras": "kampung"}) 
print(kucing)

kucing.update({"warna": ["putih", "hitam"]})

kucing = { 
  "nama": "kuro",   
  "umur": 2 ,
  "ras": "persian",
"jantan": "true",
"hobi": ["makan", "tidur"]
}

kucing.pop("jantan")
print(kucing)