import Logic_menu as mn
import data_program as dpm
import Essential_tools as tool
import Essential_handling_error as ehr
from colorama import init, Fore
init(autoreset=True)

# file ini untuk fungsi login dan registers
# login() Memvalidasi username dan password pengguna, lalu mengarahkan ke menu berdasarkan peran.
# register() Mendaftarkan pengguna baru dengan role default user.

def login():
    tool.clear()
    print(Fore.YELLOW + f"{" HALAMAN LOGIN ":=^50}")

    username = ehr.tidak_kosong('Masukkan Username : ') # input username
    password = ehr.password('Masukkan Password : ') # input password mengunakan libery PWinput
    if username in dpm.data_users and dpm.data_users[username]['password'] == password: # cek apakah password benar
        print(Fore.CYAN + f"{" Login berhasil ":=^50}")
        input('< Lanjutkan(enter) ')
        role = dpm.data_users[username]['peran'] # mengambil velue role dari data_users
        if role == "admin":
            mn.menu_admin(username) # menjalankan menu admin
        else:
            mn.menu_user(username) # menjalankan menu user
    else: # jika password salah
        print(Fore.RED + f"{" Login gagal ":=^50}")
        input('< kembali(enter) ')

def register():
    tool.clear()
    print(Fore.YELLOW + f"{" HALAMAN REGISTER ":=^50}")

    username = ehr.tidak_kosong("Buat username : ") # input username
    if username not in dpm.data_users: # cek apakah username tersedia
        password = ehr.tidak_kosong("Buat password : ")  # input password
        # membuat data baru dan menambahkan data baru
        dpm.data_users[username] = {
            "password": password,
            "peran": "user"
        } 
        print(Fore.CYAN + "Register berhasil!")
    else: # jika input username ada di data user
        print(Fore.RED + "Username sudah ada, coba lagi!")
    input('< kembali(enter) ')