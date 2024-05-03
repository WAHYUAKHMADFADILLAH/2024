def nama():
    nama = input('masukan nama : ')
    return nama

def jam_kerja():
    jam_kerja = int(input('jam kerja   : '))
    return jam_kerja

def tarif_perjam():
    tarif_perjam = 30000
    return tarif_perjam

def login_system():
    nim = input('masukan NIM anda : ')
    password = input('masukan password anda (NIM) : ')

    if nim == '12345678' and password == '12345678':
        print(f'Selamat datang, {nama()}!')
    else:
        print('Maaf, NIM atau password anda salah. Silakan coba lagi.')
nim = ''
password = ''
login_system()