print(f"TUGAS DICTIONARIES")
#Biodata Mahasiswa
biodata = {"nama"   : "Muh.Daffa Nashwan Rasya",
           "nim"    : 231031096,
           "jrusan" : "Sains",
           "prodi"  : "Sistem Informasi C",
           "semster": "Ganjil",
           "angktan": 2023,
           "umur"   : 18,
           "asal"   : "Parepare",
           "alamat" : "BUKIT PARE PERMAI BLOCK C2 NO.1",
           "warna"  : "Abu-abu",
           "hobi"   : {"hb1" : "Membuat Program",
                       "hb2" : "Bermain Game"}
            }

print(f"""
Nama          : {biodata['nama']}
Nim           : {biodata['nim']}
Jurusan       : {biodata['jrusan']}
Prodi         : {biodata['prodi']}
Semester      : {biodata['semster']}
Angkatan      : {biodata['angktan']}
Umur          : {biodata['umur']}
Asal          : {biodata['asal']}
Alamat        : {biodata['alamat']}
Hobi          : {biodata['hobi']["hb2"]}
Warna Favorit : {biodata['warna']}
""")