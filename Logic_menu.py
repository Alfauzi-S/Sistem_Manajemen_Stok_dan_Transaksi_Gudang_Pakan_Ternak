import Logic_CRUD_admin as ladm
import Logic_user as lusr
import display_menu as dmn
import Essential_tools as tool
import Essential_hendling_error as ehr
import Visualisasi_data as vs
from colorama import init, Fore, Style
init(autoreset=True)

# status done
def menu_admin(username):
    while True:
        tool.clear()
        print("╭" + "─" * 50 + "╮")
        print("│" + Fore.YELLOW + f"Selamat Datang {username}".center(50) + Style.RESET_ALL + "│")
        print("│" + Fore.YELLOW + "Menu Admin ".center(50) + Style.RESET_ALL + "│")
        print("╰" + "─" * 50 + "╯")
        pilihan = dmn.menu_admin()
        if pilihan == "Lihat Data Gudang":
            ladm.read()
        elif pilihan == "Tambah Produk Baru":
            ladm.create()
        elif pilihan == "Update Data Produk":
            ladm.update()
        elif pilihan == "Hapus Produk":
            ladm.delate()
        elif pilihan == "Lihat History Transaksi":
            ladm.history()
        elif pilihan == "Visualisasi Data":
            vs.visualisasi_data()
        elif pilihan == "Logout":
            print('anda telah logout')
            input('< (enter)')
            break
        elif pilihan is None:
            print(Fore.RED + "\nanda mengunakan ctrl + c." + Style.RESET_ALL)
            input('< (enter)')
            break
        else:
            print('pilihan tidak valid')


# status done
def menu_user(username):
    while True:
        tool.clear()
        print("╭" + "─" * 50 + "╮")
        print("│" + Fore.YELLOW + f"Selamat Datang {username}".center(50) + Style.RESET_ALL + "│")
        print("│" + Fore.YELLOW + "Menu User ".center(50) + Style.RESET_ALL + "│")
        print("╰" + "─" * 50 + "╯")
        pilihan = dmn.menu_user()
        if pilihan == "Beli Produk":
            lusr.belanja(username)
        elif pilihan == "Keranjang dan Checkout":
            lusr.keranjang(username)
        elif pilihan == "Ubah Produk di Keranjang":
            lusr.ubah_keranjang(username)
        elif pilihan == "Hapus Produk di Keranjang":
            lusr.hapus_keranjang(username)
        elif pilihan == "Top Up Saldo":
            lusr.topup(username)
        elif pilihan == "History Transaksi":
            lusr.history(username)
        elif pilihan == "Logout":
            print('anda telah logout')
            input('< (enter)')
            break
        elif pilihan is None:
            print(Fore.RED + "\nanda mengunakan ctrl + c." + Style.RESET_ALL)
            input('< (enter)')
            break
        else:
            print('pilihan tidak valid')