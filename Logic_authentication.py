import Logic_menu as mn
import data_program as dpm
import Essential_tools as tool
import Essential_hendling_error as ehr
from colorama import init, Fore, Style
init(autoreset=True)

# status done
def login():
    tool.clear()
    print(Fore.YELLOW + (f"{" HALAMAN LOGIN ":=^50}"))
    username = ehr.tidak_kosong('Masukkan Username: ').lower()
    password = ehr.tidak_kosong('Masukkan Password: ')
    if username in dpm.data_users and dpm.data_users[username]['password'] == password:
        print(Fore.CYAN + (f"{" Login berhasil ":-^50}"))
        input('< Lanjutkan(enter) ')
        role = dpm.data_users[username]['peran']
        if role == "admin":
            mn.menu_admin(username)
        else:
            mn.menu_user(username)
        return username
    else:
        print(Fore.RED + (f"{" Login gagal ":-^50}"))
    input('< kembali(enter) ')

# risda
def register():
    print("")