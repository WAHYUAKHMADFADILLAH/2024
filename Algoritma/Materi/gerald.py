nama = input("Masukan Nama: ")
jabatan = input("Masukan Jabatan [Design/Programmer/Resource]: ").title()
status = input("Status Perkawinan [Y/T]: ").upper()
gp = 5000000 if jabatan == "Design" or jabatan == "Resource" else 10000000 if jabatan == "Programmer" else 0
gk = gp*1.2 if status == "Y" else gp if status == "T" else 0
gb = gk*0.9
print("="*15+f"\nNama: {nama}\nJabatan: {jabatan}\nStatus Kawin: {status}\nGaji Kotor: Rp. {gk:,}\nPajak: Rp. {(gk-gb):,}\nTotal Pendapatan: Rp. {gb:,}" if gb > 0 else "Data jabatan yang anda masukan invalid" if gk <  else "Data kawin yang anda masukan invalid")