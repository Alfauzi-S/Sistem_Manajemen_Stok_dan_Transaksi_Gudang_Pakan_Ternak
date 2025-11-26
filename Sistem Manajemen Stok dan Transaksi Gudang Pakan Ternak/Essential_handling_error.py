import pwinput as pw
import questionary as qs
from datetime import datetime
from colorama import init, Fore, Style
init(autoreset=True)

# Modul ini berisi fungsi-fungsi penanganan error dan validasi input dan Digunakan untuk memastikan input dari pengguna valid dan aman.
# tidak_kosong(pesan) – Memastikan input string tidak kosong.
# harus_nomor(pesan) – Memastikan input adalah angka positif.
# harus_nomor_boleh_kosong(pesan) – Memastikan input adalah angka atau None jika kosong.
# input_menu(pesan) – Memastikan input adalah angka untuk menu.
# input_menu_boleh_kosong(pesan) – Memastikan input adalah angka atau None jika kosong untuk menu.
# input_tanggal(pesan) – Memastikan input adalah tanggal dengan format YYYY-MM-DD.
# input_tanggal_boleh_kosong(pesan) – Memastikan input adalah tanggal atau None jika kosong.
# input_y_or_n(pesan) – Menampilkan konfirmasi interaktif (y/n).
# password(pesan) – Meminta input password tanpa menampilkan karakter.

def tidak_kosong(p):
    while True:
        input_str = input(p).strip() # Ambil input dan hapus spasi
        if input_str: # jika true
            return input_str 
        else:
            print(Fore.RED + "Input tidak boleh kosong.")

def harus_nomor(p):
    while True:
        input_str = tidak_kosong(p)
        try:
            angka = int(input_str) # ubah ke int
            if angka > 0: # harus lebih dari 0
                return angka 
            else:
                print(Fore.RED + "Harus lebih dari 0.")
        except ValueError: # error jika input_str bukan angka
            print(Fore.RED + "Input harus berupa angka.")

def harus_nomor_boleh_kosong(p):
    while True:
        input_str = input(p).strip() # Ambil input dan hapus spasi
        if not input_str: # Jika input kosong
            return None # Kembalikan None
        try:
            input_angka = int(input_str)
            if input_angka > 0: # harus lebih dari 0
                return input_angka 
            else:
                print(Fore.RED + "Harus lebih dari 0.")
        except ValueError:
            print(Fore.RED + "Input harus berupa angka.")

def input_menu(p):
    while True:
        input_str = tidak_kosong(p)
        try:
            angka = int(input_str) # ubah ke int
            return angka
        except ValueError: # error jika input_str bukan angka
            print(Fore.RED + "Input harus berupa angka.")

def input_menu_boleh_kosong(pesan):
    while True:
        input_str = input(pesan).strip() # Ambil input dan hapus spasi
        if not input_str: # Jika input kosong
            return None 
        try:
            angka = int(input_str)
            return angka # Kembalikan angka jika valid
        except ValueError:
            print(Fore.RED + "Input harus berupa angka.")

def input_tanggal(p):
    while True:
        tgl_str = tidak_kosong(p).strip() # Ambil input dan hapus spasi
        try:
            datetime.strptime(tgl_str, '%Y-%m-%d') # mengubah string menjadi objek tanggal dengan format (YYYY-MM-DD)
            return tgl_str
        except ValueError: # jika salah format
            print(Fore.RED + "Format tanggal salah. (YYYY-MM-DD)")

def input_tanggal_boleh_kosong(p):
    while True:
        tgl_str = input(p).strip() # Ambil input dan hapus spasi
        if not tgl_str: # Jika input kosong
            return None # Kembalikan None
        try:
            datetime.strptime(tgl_str, '%Y-%m-%d') # mengubah string menjadi objek tanggal dengan format (YYYY-MM-DD)
            return tgl_str
        except ValueError: # jika salah format
            print(Fore.RED + "Format tanggal salah. (YYYY-MM-DD)")

def input_y_or_n(p):
    konfirmasi = qs.confirm(
        message=p,
        style=qs.Style([('answer', 'fg:green')])

    ).ask()

    if konfirmasi is None:
        return None

    if konfirmasi:  # Jika true 
        return True
    else:  # Jika false 
        return False
    
def password(p):
    while True:
        password_input = pw.pwinput(prompt=p).strip()
        if password_input:
            return password_input
        else:
            print(Fore.RED + "Password tidak boleh kosong.")