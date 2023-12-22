pendapatan_input = float(input("Masukkan pendapatan: "))

if pendapatan_input <= 1000:
    persentase_bonus = 0
elif 1001 <= pendapatan_input <= 2000:
    persentase_bonus = 10
elif 2001 <= pendapatan_input <= 3000:
    persentase_bonus = 20
elif 3001 <= pendapatan_input <= 4000:
    persentase_bonus = 30
elif 4001 <= pendapatan_input <= 5000:
    persentase_bonus = 40
else:
    persentase_bonus = 50

bonus = pendapatan_input * (persentase_bonus / 100)
total = pendapatan_input + bonus

print(f"Persentase Bonus: {persentase_bonus}%")
print(f"Jumlah Bonus: {bonus}")
print(f"Total: {total}")