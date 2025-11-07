import Logic_CRUD_admin as ladm
import Logic_user as lusr
import display_menu as dmn
import Essential_tools as tool
import Visualisasi_data as vs

def menu_admin():
    while True:
        tool.clear()
        print("selamat datang".center(50))
        print(dmn.menu_admin)
        pilihan = input('masukan pilihan: ')
        if pilihan == '1':
            ladm.read()
        elif pilihan == '2':
            ladm.create()
        elif pilihan == '3':
            ladm.update()
        elif pilihan == '4':
            ladm.delate()
        elif pilihan == '5':
            ladm.history()
        elif pilihan == '6':
            vs.visualisasi_data()
        elif pilihan == '0':
            break
        else:
            print("tidak valid")

def menu_user():
    while True:
        tool.clear()
        print("selamat datang".center(50))
        print(dmn.menu_user)
        pilihan = input('masukan pilihan: ')
        if pilihan == '1':
            lusr.belanja()
        elif pilihan == '2':
            lusr.keranjang()
        elif pilihan == '3':
            lusr.ubah_keranjang()
        elif pilihan == '4':
            lusr.topup()
        elif pilihan == '5':
            lusr.history()
        elif pilihan == '0':
            break
        else:
            print("tidak valid")