import Logic_authentication as auth
import display_menu as dmn
import Essential_tools as tool
import Essential_handling_error as ehr
from colorama import init, Fore, Style
init(autoreset=True)

# file ini untuk menjalankan program dan menyediakan menu utama untuk login, register dan keluars

def main():
    while True:
        tool.clear() # memersihkan terminal
        print("╭" + "─" * 50 + "╮")
        print("│" + Fore.YELLOW + "Sistem Manajemen Stok dan Transaksi".center(50) + Style.RESET_ALL + "│")
        print("│" + Fore.YELLOW + "Gudang Pakan Ternak".center(50) + Style.RESET_ALL + "│")
        print("╰" + "─" * 50 + "╯")

        pilihan = dmn.menu_awal() # Menampilkan menu utama dan mendapatkan input pengguna
        if pilihan == 'Login':
            auth.login() # menjalakankan fungsi login
        elif pilihan == 'Register':
            auth.register() # menjalankan fungsi register
        elif pilihan == 'Keluar':
            konfirmasi = ehr.input_y_or_n("Apakah yakin keluar?") 
            if konfirmasi:  # Jika True
                print("Terima Kasih sudah menggunakan program kami.")
                break
            else:  # Jika False
                print("Membatalkan keluar")
        elif pilihan is None: # jika user mengunakan ctrl + c
            print(Fore.RED + "\nanda mengunakan ctrl + c, Keluar dari program.")
            break
        else:
            print('pilihan tidak valid')

# memastikan kode hany berjalan di file ini saja dan menjagah main() jalan di file lain
if __name__ == "__main__": 
    main()