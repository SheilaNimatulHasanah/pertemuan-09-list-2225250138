# Input: List nilai mahasiswa dengan batas kelulusan 60
# Proses: Melakukan iterasi dan seleksi nilai yang memenuhi syarat lulus
# Output: Daftar nilai yang lulus dan jumlah totalnya

nilai = [75, 55, 80, 60, 45, 90]
lulus = []
for x in nilai:
  if x >= 60:
    lulus.append(x)

print(f"Nilai lulus = {lulus}")
print(f"Jumlah lulus = {len(lulus)}")