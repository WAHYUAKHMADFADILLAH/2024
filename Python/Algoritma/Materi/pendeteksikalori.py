def hitung_kalori(aktifitas, durasi, BB):
    cal_per_min = {
"mancing": 3,"ngoding": 20,"jalan": 3,"lari": 10,"bersepeda": 8,"overthinking": 100,
    }
    if aktifitas not in cal_per_min:
        print("Aktifitas belum didukung atau tidak ditemukan dalam database kalori.")
        return
    cal_per_min_akt = cal_per_min[aktifitas]
    total_cal = cal_per_min_akt * durasi
    print(f"Anda telah membakar sekitar {total_cal*BB:,.0f} kalori selama melakukan {aktifitas}.")

def main():
    hitung_kalori(input("Jenis Aktifitas yang dilakukan: ").lower(), int(input("Durasi Melakukanya (dalam menit): ")), float(input("Berat badan Anda (kg): ")))

main()