import pandas as pd
import tabulate as tb
import data_program as dpm
import display_menu as dmn
import Essential_tools as tool
import Essential_hendling_error as ehr
from colorama import init, Fore, Style
init(autoreset=True)

def create():
    tool.clear()
    print(f"{'='*18}{'TAMBAH PRODUK BARU'}{'='*18}")
    id_baru = ehr.harus_nomor("Masukkan ID Produk baru   : ")
    
    #cek id
    if id_baru in dpm.data_produk:
        print(f"\nID {id_baru} sudah ada.")
    else:
        #tersedia
        print(f"ID {id_baru} tersedia. Silakan masukkan detail produk:")
        produk = ehr.tidak_kosong_capitalize("Nama Produk               : ")
        stok = ehr.harus_nomor("Stok Awal                 : ")
        ukuran = ehr.harus_nomor("Ukuran/per stok (Kg)      : ")
        harga = ehr.harus_nomor("Harga                     : ")
        tgl_masuk = ehr.input_tanggal("Tanggal Masuk (YYYY-MM-DD): ")
        while True:
            kadaluarsa = ehr.input_tanggal("Kadaluarsa (YYYY-MM-DD)   : ")
            if kadaluarsa > tgl_masuk :
                break
            else:
                print("Tanggal kadaluarsa harus lebih besar dari tanggal masuk.")
        while True:
            print("\nkatagori: 1.Ruminansia 2.Unggas 3.Perikanan 4.Hewan Peliharaan" )
            pilihan = ehr.input_menu("pilih kategori (1/2/3/4)  :")
            if pilihan in [1, 2, 3, 4]:
                kategori = 'Ruminansia' if pilihan == 1 else 'Unggas' if pilihan == 2 else 'Perikanan' if pilihan == 3 else 'Hewan Peliharaan'
                break
            else: 
                print('Pilihan tidak valid!.')

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
            
        print(f"\nData Pakan '{produk}' (ID: {id_baru}) berhasil ditambahkan!")
    
    input('< kembali(enter) ')

def read():
    tool.clear()
    print(f"{'='*51}{'LIHAT DAFTAR GUDANG'}{'='*51}")
    dmn.menu_produk()
    input('< kembali(enter) ')

def update():
    tool.clear()
    print(f"{'='*18}{'UBAH DATA GUDANG'}{'='*18}")
    dmn.menu_produk()
    
    id_ubah= ehr.harus_nomor('Masukkan ID produk yang ingin diubah (atau ketik "x" untuk kembali): ')

    if id_ubah not in dpm.data_produk:
        print(f'ID Produk {id_ubah} tidak ditemukan.')
    else:
        print(f"--- Mengubah Data ID: {id_ubah} ---")
        print("(Kosongi jika tidak ingin diubah)")
        produk_lama = dpm.data_produk[id_ubah]

        nama = ehr.tidak_kosong_capitalize(f"Nama ({produk_lama['Nama Produk']}): ")
        stok = ehr.harus_nomor(f"Stok ({produk_lama['Stok']}): ")
        ukuran = ehr.harus_nomor(f"Ukuran ({produk_lama['Ukuran/per Stok']}): ")
        harga = ehr.harus_nomor(f"Harga (Rp{produk_lama['Harga']:,}): ")
        tgl_masuk = ehr.input_tanggal(f"Tgl masuk ({produk_lama['Tanggal Masuk']}): ")
        while True:
            kadaluarsa = ehr.input_tanggal(f"Kadaluarsa ({produk_lama['Kadaluarsa']}): ")
            if kadaluarsa > tgl_masuk:
                break
            else:
                print("Tanggal kadaluarsa harus lebih besar dari tanggal masuk.")
        while True:
            print(f"Kategori ({produk_lama['Kategori']}): ")
            print("\nkatagori: 1.Ruminansia 2.Unggas 3.Perikanan 4.Hewan Peliharaan")
            pilihan = ehr.input_menu("pilih kategori (1/2/3/4)  :")
            if pilihan in [1, 2, 3, 4]:
                kategori = 'Ruminansia' if pilihan == 1 else 'Unggas' if pilihan == 2 else 'Perikanan' if pilihan == 3 else 'Hewan Peliharaan'
                break
            else:
                print('Pilihan tidak valid!.')

        # Update
        dpm.data_produk[id_ubah] = {
            "Nama Produk": nama,
            "Stok": stok,
            "Ukuran/per Stok": str(ukuran) + "Kg",
            "Harga": harga,
            "Kadaluarsa": kadaluarsa if kadaluarsa else produk_lama['kadaluarsa'],
            "Tanggal Masuk": tgl_masuk if tgl_masuk else produk_lama['tanggal masuk'],
            "Kategori": kategori if kategori else produk_lama['kategori']
        }
        print('Data pakan berhasil diubah!')

    input('< kembali(Enter) ')

def delate():
    dmn.menu_produk()
    
    id_produk = input("Masukkan ID produk yang mau dihapus: ")

    if id_produk not in dpm.data_produk:
        print("ID tidak ada.")
        return
    
    konfirmasi = input("Hapus produk? (y/n): ").lower()
    if konfirmasi == 'y':
        del dpm.data_produk[id_produk]
        print("Produk berhasil dihapus!")
    else:
        print("Penghapusan dibatalkan.")

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