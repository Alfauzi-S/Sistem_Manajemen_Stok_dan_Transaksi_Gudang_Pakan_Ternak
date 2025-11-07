import Logic_menu as mn
import data_program as dpm
import Essential_tools as tool

def login():
    while True:
        tool.clear()
        print((f'{'='*18}{'HALAMAN LOGIN'}{'='*18}'))
        username = input('Masukkan Username: ')
        password = input('Masukkan Password: ')

        if username in dpm.data_users and dpm.data_users[username]['password'] == password:
            print((f'\n{'-'*18}{'Login berhasil'}{'-'*18}'))
            input('Tekan Enter untuk melanjutkan...')
            role = dpm.data_users[username]['peran']
            if role == "admin":
                mn.menu_admin()
                break
            else:
                mn.menu_user()
                break
        else:
            print((f'\n{'-'*19}{'Login gagal'}{'-'*19}'))
            input('Tekan Enter untuk kembali...')
            break

def register():
    print("")