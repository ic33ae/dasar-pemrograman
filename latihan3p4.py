"""Nama: Ica Apriyanti Rahayu
NIM: 2408415
Kelas: RPL 1B"""

student_info = {
    "Alice": {"age": 20, "major": "Teknik Komputer"},
    "Bob": {"age": 21, "major": "Matematika"},
    "Charlie": {"age": 19, "major": "Fisika"},
}


nama_mahasiswa = input("Masukkan nama mahasiswa: ")
umur = student_info[nama_mahasiswa]["age"]
prodi = student_info[nama_mahasiswa]["major"]

print(f"Umur {nama_mahasiswa} adalah {umur} dengam program studi {prodi}")