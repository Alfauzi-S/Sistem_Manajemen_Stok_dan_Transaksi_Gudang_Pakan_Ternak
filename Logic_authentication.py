import Logic_menu as mn
import data_program as dpm
import Essential_tools as tool
import Essential_hendling_error as ehr

def login():
    while True:
        tool.clear()
        print((f'{'='*18}{'HALAMAN LOGIN'}{'='*18}'))
        username = ehr.tidak_kosong_capitalize('Masukkan Username: ')
        password = ehr.tidak_kosong('Masukkan Password: ')

        if username in dpm.data_users and dpm.data_users[username]['password'] == password:
            print((f'\n{'-'*18}{'Login berhasil'}{'-'*18}'))
            input('< Lanjutkan(enter) ')
            role = dpm.data_users[username]['peran']
            if role == "admin":
                mn.menu_admin(username)
            else:
                mn.menu_user(username)
            return username
        else:
            print((f'\n{'-'*19}{'Login gagal'}{'-'*19}'))
            input('< kembali(enter) ')
            break

def register():
    print("")