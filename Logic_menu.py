import Logic_CRUD_admin as ladm
import Logic_user as lusr
import display_menu as dmn
import Essential_tools as tool
import Essential_handling_error as ehr
import Visualisasi_data as vs
from colorama import init, Fore, Style
init(autoreset=True)

# file ini untuk menu admin dan menu user
# menu_admin() fitur CRUD produk, riwayat transaksi, dan visualisasi data
# menu_user() fitur belanja, keranjang, top-up saldo, dan riwayat transaksi.

def menu_admin(username):
    while True:
        tool.clear()
        print("╭" + "─" * 50 + "╮")
        print("│" + Fore.YELLOW + f"Selamat Datang {username}".center(50) + Style.RESET_ALL + "│")
        print("│" + Fore.YELLOW + "Menu Admin ".center(50) + Style.RESET_ALL + "│")
        print("╰" + "─" * 50 + "╯")

        pilihan = dmn.menu_admin() # menampilkan menu admin dan mendapatkan input pengguna
        if pilihan == "Lihat Data Gudang":
            ladm.read() # menampilkan data produk
        elif pilihan == "Tambah Produk Baru":
            ladm.create() # membuat produk baru
        elif pilihan == "Update Data Produk":
            ladm.update() # mengubah produk
        elif pilihan == "Hapus Produk":
            ladm.delete() # menghapus produk
        elif pilihan == "Lihat History Transaksi":
            ladm.history() # menampilkan history
        elif pilihan == "Visualisasi Data":
            vs.visualisasi_data() # menampilkan grafik
        elif pilihan == "Logout":
            konfirmasi = ehr.input_y_or_n("Apakah yakin Logout?") 
            if konfirmasi:  # Jika True
                print("anda telah logout.")
                break
            else:  # Jika False
                print("Membatalkan logout")
        elif pilihan is None: # jika user mengunakan ctrl + c
            print(Fore.RED + "\nanda mengunakan ctrl + c." + Style.RESET_ALL)
            input('< (enter)')
            break
        else:
            print('pilihan tidak valid')


def menu_user(username):
    while True:
        tool.clear()
        print("╭" + "─" * 50 + "╮")
        print("│" + Fore.YELLOW + f"Selamat Datang {username}".center(50) + Style.RESET_ALL + "│")
        print("│" + Fore.YELLOW + "Menu User ".center(50) + Style.RESET_ALL + "│")
        print("╰" + "─" * 50 + "╯")

        pilihan = dmn.menu_user() # menampilkan menu user dan mendapatkan input pengguna
        if pilihan == "Beli Produk":
            lusr.belanja(username) # menjalakan proses belanja
        elif pilihan == "Keranjang dan Checkout":
            lusr.keranjang(username) # menjalakan proses checkout
        elif pilihan == "Ubah Produk di Keranjang":
            lusr.ubah_keranjang(username) # menjalakan proses ubah keranjang
        elif pilihan == "Hapus Produk di Keranjang":
            lusr.hapus_keranjang(username)
        elif pilihan == "Top Up Saldo": 
            lusr.topup(username) # menjalakan proses topup
        elif pilihan == "History Transaksi":
            lusr.history(username) # menampilkanan history pembelian user
        elif pilihan == "Logout":
            konfirmasi = ehr.input_y_or_n("Apakah yakin Logout?") 
            if konfirmasi:  # Jika True
                print("anda telah logout.")
                break
            else:  # Jika False
                print("Membatalkan logout")
        elif pilihan is None: # jika user mengunakan ctrl + c
            print(Fore.RED + "\nanda mengunakan ctrl + c." + Style.RESET_ALL)
            input('< (enter)')
            break
        else:
            print('pilihan tidak valid')