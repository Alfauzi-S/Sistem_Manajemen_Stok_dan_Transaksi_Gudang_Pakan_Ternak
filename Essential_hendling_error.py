from datetime import datetime
from colorama import init, Fore, Style
init(autoreset=True)

def tidak_kosong(p):
    while True:
        input_str = input(p).strip()
        if input_str:
            return input_str
        else:
            print(Fore.RED + "Input tidak boleh kosong.")

def harus_nomor(p):
    while True:
        input_str = tidak_kosong(p)
        try:
            angka = int(input_str)
            if angka > 0:
                return angka
            else:
                print(Fore.RED + "Harus lebih dari 0.")
        except ValueError:
            print(Fore.RED + "Input harus berupa angka.")

def input_menu(p):
    while True:
        input_str = tidak_kosong(p)
        try:
            angka = int(input_str)
            return angka
        except ValueError:
            print(Fore.RED + "Input harus berupa angka.")

def input_tanggal(p):
    while True:
        tgl_str = tidak_kosong(p).strip()
        try:
            datetime.strptime(tgl_str, '%Y-%m-%d')
            return tgl_str
        except ValueError:
            print(Fore.RED + "Format tanggal salah. (YYYY-MM-DD)")

def input_y_or_n(p):
    while True:
        input_str = tidak_kosong(p).strip().lower()
        if input_str in ['y', 'n']:
            return input_str
        else:
            print(Fore.RED + "Input harus 'y' atau 'n'.")