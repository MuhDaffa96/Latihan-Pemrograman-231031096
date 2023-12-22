biodata = {"nama"   : "Muh.Daffa Nashwan Rasya",
           "nim"    : 231031096,
           "prodi"  : "Sistem Informasi C",
           "umur"   : 17,
           "hobi"   : {"hobi1" : "Bermain Game",
                       "hobi2" : "Makan Tidur"},
           "asal"   : "Parepare",
           "alamat" : "Jln.Jend.Ahmad Yani Km.6"
           }

print(f"""
Nama Saya  : {biodata['nama']}
Dengan NIM : {biodata['nim']}
Dari Prodi : {biodata['prodi']}
Hobi Saya  : {biodata['hobi']["hobi2"]}
""")