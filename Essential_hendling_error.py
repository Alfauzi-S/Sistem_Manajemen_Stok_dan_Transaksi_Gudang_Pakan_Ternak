from datetime import datetime

def tidak_kosong(p):
    while True:
        input_str = input(p).strip()
        if input_str:
            return input_str
        else:
            print("Input tidak boleh kosong.")

def tidak_kosong_capitalize(p):
    while True:
        input_str = input(p).strip().capitalize()
        if input_str:
            return input_str
        else:
            print("Input tidak boleh kosong.")

def harus_nomor(p):
    while True:
        input_str = tidak_kosong(p)
        try:
            angka = int(input_str)
            if angka > 0:
                return angka
            else:
                print("Harus lebih dari 0.")
        except ValueError:
            print("Input harus berupa angka.")

def input_menu(p):
    while True:
        input_str = tidak_kosong(p)
        try:
            angka = int(input_str)
            return angka
        except ValueError:
            print("Input harus berupa angka.")

def input_tanggal(p):
    while True:
        tgl_str = tidak_kosong(p).strip()
        try:
            datetime.strptime(tgl_str, '%Y-%m-%d')
            return tgl_str
        except ValueError:
            print("Format tanggal salah. (YYYY-MM-DD)")