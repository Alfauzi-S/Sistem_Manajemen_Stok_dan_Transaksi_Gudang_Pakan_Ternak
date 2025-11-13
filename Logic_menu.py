import Logic_CRUD_admin as ladm
import Logic_user as lusr
import display_menu as dmn
import Essential_tools as tool
import Essential_hendling_error as ehr
import Visualisasi_data as vs

def menu_admin(username):
    while True:
        tool.clear()
        print(f"selamat datang, {username}".center(50))
        print(dmn.menu_admin)
        pilihan = ehr.input_menu('masukan pilihan: ')
        if pilihan == 1:
            ladm.read()
        elif pilihan == 2:
            ladm.create()
        elif pilihan == 3:
            ladm.update()
        elif pilihan == 4:
            ladm.delate()
        elif pilihan == 5:
            ladm.history()
        elif pilihan == 6:
            vs.visualisasi_data()
        elif pilihan == 0:
            break
        else:
            print(input("< Pilihan tidak valid!(enter)"))

def menu_user(username):
    while True:
        tool.clear()
        print(f"selamat datang, {username}".center(50))
        print(dmn.menu_user)
        pilihan = ehr.input_menu('masukan pilihan: ')
        if pilihan == 1:
            lusr.belanja()
        elif pilihan == 2:
            lusr.keranjang()
        elif pilihan == 3:
            lusr.ubah_keranjang()
        elif pilihan == 4:
            lusr.hapus_keranjang()
        elif pilihan == 5:
            lusr.topup()
        elif pilihan == 6:
            lusr.history(username)
        elif pilihan == 0:
            break
        else:
            print(input("< Pilihan tidak valid!(enter)"))