import Logic_CRUD_admin as ladm
import Logic_user as lusr
import display_menu as dmn
import Essential_tools as tool

def menu_admin():
    tool.clear
    print(dmn.menu_admin)
    while True:
        pilihan = input
        if pilihan == 1:
            ladm.create()
        elif pilihan == 2:
            ladm.read()
        elif pilihan == 3:
            ladm.update()
        elif pilihan == 4:
            ladm.delate()
        elif pilihan == 5:
            ladm.history()
        elif pilihan == 6:
            break
        else:
            print("")

def menu_user():
    tool.clear
    print(dmn.menu_user)
    while True:
        pilihan = input
        if pilihan == 1:
            lusr.belanja()
        elif pilihan == 2:
            lusr.keranjang()
        elif pilihan == 3:
            lusr.ubah_keranjang()
        elif pilihan == 4:
            lusr.topup()
        elif pilihan == 5:
            lusr.history()
        elif pilihan == 6:
            break
        else:
            print("")