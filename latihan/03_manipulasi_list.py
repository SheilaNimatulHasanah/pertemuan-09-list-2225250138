# Input: List awal [75, 80, 65]
# Proses: Mengubah elemen, menambah, menyisipkan, dan menghapus elemen
# Output: Hasil akhir list setelah manipulasi

nilai = [75, 80, 65]
nilai[1] = 82  # Mengubah elemen indeks 1 menjadi 82
nilai.append(90)  # Menambah 90 di akhir
nilai.insert(2, 70)  # Menyisipkan 70 pada indeks 2
nilai.remove(65)  # Menghapus nilai 65
print(nilai)