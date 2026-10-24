# Input: Fungsi yang menerima parameter list dan data list uji
# Proses: Menghitung rata-rata dengan penanganan list kosong
# Output: Hasil perhitungan rata-rata dengan format 2 desimal


def rata_rata(data):
  if len(data) == 0:
    return 0
  return sum(data) / len(data)


nilai = [75, 80, 65, 90, 88]
print(f"Rata-rata = {rata_rata(nilai):.2f}")