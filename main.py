import Logic_authentication as auth
import display_menu as dmn
import Essential_tools as tool
import Essential_hendling_error as ehr
from colorama import init, Fore, Style
init(autoreset=True)

# status done
def main():
    while True:
        tool.clear()
        print("╭" + "─" * 50 + "╮")
        print("│" + Fore.YELLOW + "Sistem Manajemen Stok dan Transaksi".center(50) + Style.RESET_ALL + "│")
        print("│" + Fore.YELLOW + "Gudang Pakan Ternak".center(50) + Style.RESET_ALL + "│")
        print("╰" + "─" * 50 + "╯")
        pilihan = dmn.menu_awal()
        if pilihan == 'Login':
            auth.login()
        elif pilihan == 'Register':
            auth.register()
        elif pilihan == 'Keluar':
            konfirmasi = ehr.input_y_or_n("Apakah yakin keluar? (y/n): ")
            if konfirmasi == "y":
                print ("Terima Kasih sudah mengunakan program kami.")
                break
            elif konfirmasi == 'n':
                print ("Membatalkan keluar")
        elif pilihan is None:
            print(Fore.RED + "\nanda mengunakan ctrl + c, Keluar dari program." + Style.RESET_ALL)
            break
        else:
            print('pilihan tidak valid')

if __name__ == "__main__":
    main()