import pandas as pd
import tabulate as tb
import data_program as dpm
import display_menu as dmn
import Essential_tools as tool
import Essential_handling_error as ehr
from colorama import init, Fore, Style
init(autoreset=True)

# File ini berisi logika untuk pengguna dengan role admin dan Fungsi-fungsi untuk CRUD produk dan history transaksi.
# reate() – Menambah produk baru ke data produk.
# ead() – Menampilkan daftar produk.
# pdate() – Mengubah data produk yang sudah ada.
# elete() – Menghapus produk dari data produk.
# istory() – Menampilkan riwayat transaksi dari file CSV.

def create():
    tool.clear()
    print(Fore.YELLOW + f"{" TAMBAH PRODUK BARU ":=^50}")
    
    konfirmasi = ehr.input_y_or_n("Apakah anda ingin tambah produk baru?")
    if konfirmasi: # jika true
        id_baru = ehr.harus_nomor("Masukkan ID Produk baru   : ")
        if id_baru not in dpm.data_produk: # jika id tersedia
            produk = ehr.tidak_kosong("Nama Produk               : ")
            stok = ehr.harus_nomor("Stok Awal                 : ")
            ukuran = ehr.harus_nomor("Ukuran/per stok (Kg)      : ")
            harga = ehr.harus_nomor("Harga                     : ")
            tgl_masuk = ehr.input_tanggal("Tanggal Masuk (YYYY-MM-DD): ")

            while True:
                kadaluarsa = ehr.input_tanggal("Kadaluarsa (YYYY-MM-DD)   : ")
                if kadaluarsa > tgl_masuk: # jika kadaluarsa lebih besar dari tanggal masuk
                    break #keluar dari perulangan
                else:
                    print(Fore.RED + "Tanggal kadaluarsa harus lebih besar dari tanggal masuk.")
            
            print("\nkatagori: 1.Ruminansia 2.Unggas 3.Perikanan 4.Hewan Peliharaan" )
            while True:
                pilihan = ehr.input_menu("pilih kategori (1/2/3/4)  : ")
                if pilihan in [1, 2, 3, 4]: #  Jika input dalam rentang 1-4
                    # Nested ternary operator untuk menentukan kategori
                    kategori = 'Ruminansia' if pilihan == 1 else 'Unggas' if pilihan == 2 else 'Perikanan' if pilihan == 3 else 'Hewan Peliharaan' 
                    break # keluar dari perulangan
                else: 
                    print(Fore.RED + 'Pilihan tidak valid!.')

            konfirmasi = ehr.input_y_or_n("Tambah Produk?")
            if konfirmasi: # jika true
                # tambah data baru ke data_produk
                dpm.data_produk[id_baru] = {
                    "Nama Produk": produk,
                    "Stok": stok,
                    "Ukuran/per Stok": str(ukuran) + " Kg",
                    "Harga": harga,
                    "Kadaluarsa": kadaluarsa,
                    "Tanggal Masuk": tgl_masuk,
                    "Kategori": kategori
                }
                print(Fore.CYAN + f"\nData Pakan '{produk}' (ID: {id_baru}) berhasil ditambahkan!")
            else: # jika false
                print("Membatalkan")
        else: # id sudah ada
            print(Fore.RED + f"\nID {id_baru} sudah ada.")
    else: 
        print("keluar dari menu tambah produk baru ")
    input('< kembali(enter) ')


def read():
    tool.clear()
    print(Fore.YELLOW + f"{" LIHAT DAFTAR PRODUK ":=^121}")
    dmn.menu_produk() # tampilkan produk
    input('< kembali(enter) ')


def update():
    tool.clear()
    print(Fore.YELLOW + f"{" UBAH DATA PRODUK ":=^121}")
    dmn.menu_produk() # tampilkan produk

    konfirmasi = ehr.input_y_or_n('Apakah anda ingin mengubah Produk?')
    if konfirmasi: # jika true
        id = ehr.harus_nomor('Masukkan ID produk yang ingin diubah : ')
        if id in dpm.data_produk: # jika id ada di data_produk
            print(Fore.YELLOW + f"{f" Mengubah Data ID: {id} ":-^121}")

            produk_lama = dpm.data_produk[id] # ambil key dari data_produk
            nama = input(f"Nama Produk ({produk_lama['Nama Produk']}) kosongkan untuk tetap : ").strip()
            stock = ehr.harus_nomor_boleh_kosong(f"Stok ({produk_lama['Stok']}) kosongkan untuk tetap : ")
            ukuran = ehr.harus_nomor_boleh_kosong(f"Ukuran/per Stok ({produk_lama['Ukuran/per Stok']}) kosongkan untuk tetap : ")
            harga = ehr.harus_nomor_boleh_kosong(f"Harga (Rp{produk_lama['Harga']}) kosongkan untuk tetap : ")
            tgl_masuk = ehr.input_tanggal_boleh_kosong(f"Tgl Masuk ({produk_lama['Tanggal Masuk']}) kosongkan untuk tetap : ")
            tgl_masuk_akhir = produk_lama['Tanggal Masuk'] if tgl_masuk is None else tgl_masuk # # jika kosong gunakan nilai lama
            
            while True:
                kadaluarsa = ehr.input_tanggal_boleh_kosong(f"Kadaluarsa ({produk_lama['Kadaluarsa']}) kosongkan untuk tetap : ")
                if kadaluarsa is None: # jika kosong
                    break
                if kadaluarsa > tgl_masuk_akhir: # jika kadaluarsa lebih besar dari tanggal masuk
                    break #keluar dari perulangan
                else:
                    print(Fore.RED + "Tanggal kadaluarsa harus lebih besar dari tanggal masuk.")
            

            print(f"Kategori ({produk_lama['Kategori']})")
            print("\nkatagori: 1.Ruminansia 2.Unggas 3.Perikanan 4.Hewan Peliharaan" )
            while True:
                pilihan = ehr.input_menu_boleh_kosong( f"Kategori ({produk_lama['Kategori']}), pilih kategori (1/2/3/4) kosongkan untuk tetap : ")
                if pilihan is None: # jika kosong
                    break
                if pilihan in [1, 2, 3, 4]: #  Jika input dalam rentang 1-4
                    # Nested ternary operator untuk menentukan kategori
                    kategori = 'Ruminansia' if pilihan == 1 else 'Unggas' if pilihan == 2 else 'Perikanan' if pilihan == 3 else 'Hewan Peliharaan' 
                    break # keluar dari perulangan
                else: 
                    print(Fore.RED + 'Pilihan tidak valid!.')

            konfirmasi = ehr.input_y_or_n("Ubah Produk")
            if konfirmasi: # jika true
                # ubah Produk
                dpm.data_produk[id] = {
                    "Nama Produk": produk_lama['Nama Produk'] if not nama else nama, # jika kosong gunakan nilai lama
                    "Stok": produk_lama['Stok'] if stock is None else stock, # jika kosong gunakan nilai lamar
                    "Ukuran/per Stok": produk_lama['Ukuran/per Stok'] if ukuran is None else str(ukuran) + " Kg", # jika kosong gunakan nilai lama
                    "Harga": produk_lama['Harga'] if harga is None else harga, # jika kosong gunakan nilai lama
                    "Kadaluarsa": produk_lama['Kadaluarsa'] if kadaluarsa is None else kadaluarsa, # jika kosong gunakan nilai lama
                    "Tanggal Masuk": tgl_masuk_akhir, # jika kosong gunakan nilai lama
                    "Kategori": produk_lama['Kategori'] if pilihan is None else kategori # jika kosong gunakan nilai lama
                }
                print(Fore.CYAN + 'Data produk berhasil diubah!')
            else:
                print("Membatalkan perubahan.")
        else:
            print(Fore.RED + f'ID Produk {id} tidak ditemukan.')
    else:
        print('keluar menu ubah produk')
    input('< kembali(Enter) ')


def delete():
    tool.clear()
    print(Fore.YELLOW + f'{" HAPUS DATA PRODUK ":=^121}')
    dmn.menu_produk()

    pilihan = ehr.input_y_or_n('Apakah mau hapus produk?')
    if pilihan: # jika true
        id_produk = ehr.harus_nomor("Masukkan ID produk yang mau dihapus: ")
        if id_produk in dpm.data_produk: # jika id ada di data_produk
            konfirmasi = ehr.input_y_or_n('Hapus produk?')
            if konfirmasi: # jika true
                del dpm.data_produk[id_produk] # hapus produk
                print(Fore.CYAN + "Produk berhasil dihapus!")
            else: # jika false
                print("Penghapusan dibatalkan.")
        else: 
            print(Fore.RED + "ID produk tidak ditemukan!")
    else: # jika false
        print('Keluar dari menu delete.')
    input('< kembali (enter) >')


def history():
    tool.clear()
    try:
        print(f"┌{'─'*96}┐")
        print(f"│" + Fore.YELLOW + 'HISTORY TRANSAKSI USER'.center(96) + Style.RESET_ALL + "│")
        print(f"└{'─'*96}┘")

        df = pd.read_csv("history_transaksi.csv") # baca file CSV
        
        if not df.empty:
            print(df.to_string(index=False)) # tampilkan data history tanpa index
        else:
            print(Fore.RED + 'Tidak ada data History')

    except FileNotFoundError: # Error jika file tidak ditemukan
        print(Fore.RED + "File 'history_transaksi.csv' tidak ditemukan.")
    except KeyError as e: # Error jika kolom tidak ditemukan
        print(Fore.RED + f"Kolom tidak ditemukan di CSV: {e}")
    except Exception as e: # Error umum lainnya
        print(Fore.RED + f"Terjadi kesalahan: {e}")
    finally:
        print('─'*98)
        input('< kembali(enter) ')