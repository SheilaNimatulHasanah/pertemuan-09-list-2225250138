# Pertemuan 09 - List dan Pengolahan Data Numerik

Nama: Sheila Ni'matul Hasanah
NIM: 2225250138
Kelas: 3B

## Tujuan
Mengolah kumpulan data numerik dengan list Python.

## Struktur Program
- **Folder `latihan/`**:
  - `01_buat_list.py`: Membuat list dan membaca banyak data.
  - `02_indeks_slicing.py`: Mengakses elemen dengan indeks positif, negatif, dan slicing.
  - `03_manipulasi_list.py`: Mengubah, menambah, menyisipkan, dan menghapus elemen list.
  - `04_agregasi_nilai.py`: Menghitung total, rata-rata, minimum, dan maksimum.
  - `05_filter_kelulusan.py`: Memfilter nilai yang memenuhi batas kelulusan.
  - `06_fungsi_statistik.py`: Menggunakan fungsi untuk menghitung rata-rata list.
- **Folder `praktik/`**:
  - `analisis_nilai_mahasiswa.py`: Program utama untuk menganalisis data nilai numerik mahasiswa.

## Cara Menjalankan
python3 praktik/analisis_nilai_mahasiswa.py

## Test Case
| Data | Hasil yang Diharapkan | Hasil Aktual | Status |
| :--- | :--- | :--- | :--- |
| `[60, 70, 80]` | Rata-rata = 70.00 | Rata-rata = 70.00 | Sesuai |
| `[60, 70, 80]` | Minimum = 60, Maksimum = 80 | Minimum = 60, Maksimum = 80 | Sesuai |
| `[60, 70, 80]` | Jumlah lulus = 3 | Jumlah lulus = 3 | Sesuai |
| `[59, 60, 61]` | Batas kelulusan (>=60): 2 lulus | Jumlah lulus = 2 | Sesuai |
| `[]` | List kosong: Rata-rata = 0 (tidak error) | Rata-rata = 0 | Sesuai |

## Refleksi
- **Pemahaman Indeks/List**: Indeks pada Python dimulai dari angka 0 dan indeks negatif (`-1`) berguna untuk mengambil elemen dari posisi paling belakang. Selain itu, batas akhir pada slicing (seperti `1:4`) bersifat eksklusif sehingga indeks ke-4 tidak ikut terambil.
- **Kesalahan yang Berhasil Diperbaiki**: Saat menghitung rata-rata dari list kosong, program sempat mengalami error `ZeroDivisionError`. Kesalahan ini diperbaiki dengan menambahkan pengecekan `if len(data) == 0:` pada fungsi agar mengembalikan nilai `0` secara aman.