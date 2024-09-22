m = [88, 75, 63, 97, 82, 74, 91, 80, 81, 63]

# cari nilai max dan minimum
max_val = max(m)
min_val = min(m)

# hitung rata-rata
total = sum(m)
length = len(m)
mean = total/length

print(f"Angka maksimum       : {max_val}")
print(f"Angka minimum        : {min_val}")
print(f"Rata-rata            : {mean}")

m.sort()
m.reverse()
print(f"Angka terbesar kedua : {m[1]}")
