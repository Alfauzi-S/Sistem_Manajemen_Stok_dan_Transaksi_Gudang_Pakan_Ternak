import pandas as pd
import tabulate as tb
import data_program as dpm
import display_menu as dmn
import Essential_tools as tool
import Essential_hendling_error as ehr
from colorama import init, Fore, Style
init(autoreset=True)

# status done
def create():
    tool.clear()
    print(Fore.YELLOW + f"{" TAMBAH PRODUK BARU ":=^50}")
    id_baru = ehr.harus_nomor("Masukkan ID Produk baru   : ")
    if id_baru not in dpm.data_produk:
        produk = ehr.tidak_kosong_capitalize("Nama Produk               : ")
        stok = ehr.harus_nomor("Stok Awal                 : ")
        ukuran = ehr.harus_nomor("Ukuran/per stok (Kg)      : ")
        harga = ehr.harus_nomor("Harga                     : ")
        tgl_masuk = ehr.input_tanggal("Tanggal Masuk (YYYY-MM-DD): ")

        while True:
            kadaluarsa = ehr.input_tanggal("Kadaluarsa (YYYY-MM-DD)   : ")
            if kadaluarsa > tgl_masuk:
                break
            else:
                print(Fore.RED + "Tanggal kadaluarsa harus lebih besar dari tanggal masuk.")
        
        print("\nkatagori: 1.Ruminansia 2.Unggas 3.Perikanan 4.Hewan Peliharaan" )
        while True:
            pilihan = ehr.input_menu("pilih kategori (1/2/3/4)  :")
            if pilihan in [1, 2, 3, 4]:
                kategori = 'Ruminansia' if pilihan == 1 else 'Unggas' if pilihan == 2 else 'Perikanan' if pilihan == 3 else 'Hewan Peliharaan'
                break
            else: 
                print(Fore.RED + 'Pilihan tidak valid!.')

        data_baru = {
            "Nama Produk": produk,
            "Stok": stok,
            "Ukuran/per Stok": str(ukuran) + " Kg",
            "Harga": harga,
            "Kadaluarsa": kadaluarsa,
            "Tanggal Masuk": tgl_masuk,
            "Kategori": kategori
        }
        dpm.data_produk[id_baru] = data_baru
        print(Fore.CYAN + f"\nData Pakan '{produk}' (ID: {id_baru}) berhasil ditambahkan!")
    else:
        print(Fore.RED + f"\nID {id_baru} sudah ada.")
    input('< kembali(enter) ')

# status done
def read():
    tool.clear()
    print(Fore.YELLOW + f"{" LIHAT DAFTAR PRODUK ":=^121}")
    dmn.menu_produk()
    input('< kembali(enter) ')

# status done
def update():
    tool.clear()
    print(Fore.YELLOW + f"{" UBAH DATA PRODUK ":=^121}")
    dmn.menu_produk()
    
    konfirmasi = ehr.input_y_or_n('Apakah anda ingin mengubah Produk? (y/n): ')
    if konfirmasi == 'y':
        id = ehr.harus_nomor('Masukkan ID produk yang ingin diubah    : ')
        if id in dpm.data_produk:
            print(Fore.YELLOW + f"{f" Mengubah Data ID: {id} ":-^121}")
            produk_lama = dpm.data_produk[id]
            nama = ehr.tidak_kosong_capitalize(f"'Nama ({produk_lama['Nama Produk']})': ")
            stok = ehr.harus_nomor(f"Stok ({produk_lama['Stok']}): ")
            ukuran = ehr.harus_nomor(f"Ukuran/per Stok ({produk_lama['Ukuran/per Stok']}: ")
            harga = ehr.harus_nomor(f"Harga (Rp{produk_lama['Harga']}: ")
            tgl_masuk = ehr.input_tanggal(f"Tgl Masuk ({produk_lama['Tanggal Masuk']}): ")

            while True:
                kadaluarsa = ehr.input_tanggal(f"Kadaluarsa ({produk_lama['Kadaluarsa']}): ")
                if kadaluarsa > tgl_masuk:
                    break
                else:
                    print(Fore.RED + "Tanggal kadaluarsa harus lebih besar dari tanggal masuk.")
            while True:
                print(f"Kategori ({produk_lama['Kategori']}): ")
                print("\nkatagori: 1.Ruminansia 2.Unggas 3.Perikanan 4.Hewan Peliharaan")
                pilihan = ehr.input_menu("pilih kategori (1/2/3/4): ")
                if pilihan in [1, 2, 3, 4]:
                    kategori = 'Ruminansia' if pilihan == 1 else 'Unggas' if pilihan == 2 else 'Perikanan' if pilihan == 3 else 'Hewan Peliharaan'
                    break
                else:
                    print(Fore.RED + 'Pilihan tidak valid!.')

            dpm.data_produk[id] = {
                "Nama Produk": nama,
                "Stok": stok,
                "Ukuran/per Stok": str(ukuran) + "Kg",
                "Harga": harga,
                "Kadaluarsa": kadaluarsa,
                "Tanggal Masuk": tgl_masuk,
                "Kategori": kategori
            }
            print(Fore.CYAN + 'Data pakan berhasil diubah!')

        else:
            print(Fore.RED + f'ID Produk {id} tidak ditemukan.')
    elif konfirmasi == 'n':
        print('keluar menu ubah produk')
    input('< kembali(Enter) ')

# status done
def delate():
    tool.clear()
    print(Fore.YELLOW + f'{" HAPUS DATA PRODUK ":=^121}')
    dmn.menu_produk()

    pilihan = ehr.input_y_or_n('Apakah mau hapus produk? (y/n): ')
    if pilihan == 'y':
        id_produk = ehr.harus_nomor("Masukkan ID produk yang mau dihapus: ")
        if id_produk in dpm.data_produk:
            konfirmasi = ehr.input_y_or_n('Hapus produk? (y/n): ')
            if konfirmasi == 'y':
                del dpm.data_produk[id_produk]
                print(Fore.CYAN + "Produk berhasil dihapus!")
            else:
                print("Penghapusan dibatalkan.")
        else:
            print(Fore.RED + "ID produk tidak ditemukan!")
    elif pilihan == 'n':
        print('Keluar dari menu delete.')
    input('< kembali (enter) >')

# status done
def history():
    tool.clear()
    try:
        print(f"┌{'─'*96}┐")
        print(f"│" + Fore.YELLOW + 'HISTORY TRANSAKSI USER'.center(96) + Style.RESET_ALL + "│")
        print(f"└{'─'*96}┘")

        df = pd.read_csv("history_transaksi.csv")
        
        if not df.empty:
            print(df.to_string(index=False)) 
        else:
            print(Fore.RED + 'Tidak ada data History')

    except FileNotFoundError:
        print(Fore.RED + "File 'history_transaksi.csv' tidak ditemukan.")
    except KeyError as e:
        print(Fore.RED + f"Kolom tidak ditemukan di CSV: {e}")
    except Exception as e:
        print(Fore.RED + f"Terjadi kesalahan: {e}")
    finally:
        print('─'*98)
        input('< kembali(enter) ')