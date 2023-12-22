nama_karyawan = input("Masukkan Nama Karyawan :")
pendapatan_pekerjaan = input("Masukkan pendapatan :")

pendapatan = int (pendapatan_pekerjaan)

print ("Nama Karyawan:", nama_karyawan)
print ("Pendapatan:", pendapatan)

if pendapatan >= 1000:
    print ("Status : Anda Berhak")
else:
    print ("Status : Tidak Berhak")