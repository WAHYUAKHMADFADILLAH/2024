def hitung_rata_rata(nilai):
    return sum(nilai) / len(nilai)

def main():
    jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))

    nilai_mahasiswa = []
    for i in range(jumlah_mahasiswa):
        nilai = float(input(f"Masukkan nilai siswa ke-{i + 1}: "))
        nilai_mahasiswa.append(nilai)

    rata_rata_kelas = hitung_rata_rata(nilai_mahasiswa)

    nilai_tertinggi = max(nilai_mahasiswa)
    nilai_terendah = min(nilai_mahasiswa)

    jumlah_di_atas_rata_rata = sum(1 for nilai in nilai_mahasiswa if nilai > rata_rata_kelas)

    print(f"Nilai rata-rata kelas: {rata_rata_kelas:.2f}")
    print(f"Nilai tertinggi: {nilai_tertinggi}")
    print(f"Nilai terendah: {nilai_terendah}")
    print(f"Jumlah siswa di atas rata-rata: {jumlah_di_atas_rata_rata}")

main()
