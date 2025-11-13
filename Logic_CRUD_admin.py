import pandas as pd
import tabulate as tb
import data_program as dpm
import display_menu as dmn
import Essential_tools as tool
import Essential_hendling_error as ehr

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
    id_ubah = ehr.tidak_kosong('Masukkan ID produk yang ingin diubah: ').upper()
    
    if id_ubah not in dpm.data_produk:
        print(f'ID Produk {id_ubah} tidak ditemukan.')
    else:
        print(f"--- Mengubah Data ID: {id_ubah} ---")
        print("(Kosongi jika tidak ingin diubah)")
        produk_lama = dpm.data_produk[id_ubah]
        
        nama = ehr.input_string_kosong(f"Nama ({produk_lama['nama produk']}): ", produk_lama['nama produk'])
        stok = ehr.input_angka_kosong(f"Stok ({produk_lama['stok']}): ", produk_lama['stok'])
        ukuran = ehr.input_string_kosong(f"Ukuran ({produk_lama['ukuran/per stok']}): ", produk_lama['ukuran/per stok'])
        harga = ehr.input_angka_kosong(f"Harga (Rp{produk_lama['harga']:,}): ", produk_lama['harga'])
        kategori = ehr.input_kategori(f"Kategori ({produk_lama['kategori']}): ", bisa_kosong=True)
        tgl_masuk = ehr.input_tanggal(f"Tgl masuk ({produk_lama['tanggal masuk']}): ", bisa_kosong=True)
        kadaluarsa = ehr.input_tanggal(f"Kadaluarsa ({produk_lama['kadaluarsa']}): ", bisa_kosong=True)

        #updatenya
        dpm.data_produk[id_ubah] = {
            "nama produk": nama,
            "stok": stok,
            "ukuran/per stok": ukuran,
            "harga": harga,
            "kadaluarsa": kadaluarsa if kadaluarsa else produk_lama['kadaluarsa'],
            "tanggal masuk": tgl_masuk if tgl_masuk else produk_lama['tanggal masuk'],
            "kategori": kategori if kategori else produk_lama['kategori']
        }
        print('Data pakan berhasil diubah!')
    input('< kembali(0) ')

def delate():
    print("")

def history():
    tool.clear()
    try:
        print(f"┌{'─'*123}┐")
        print(f"│{'HISTORY TRANSAKSI':^123}│")
        print(f"└{'─'*123}┘")
        history = pd.read_csv("history_transaksi.csv")
        headers = ["ID Transaksi", "Nama Pembeli", "Tanggal Pembelian", "Total Bayar", "ID Produk", "Nama Produk", "Jumlah yang dibeli"]
        print(tb.tabulate(history, headers=headers, tablefmt="simple", showindex=False))
        print('─'*125)

    except FileNotFoundError:
        print("File 'history_transaksi.csv' tidak ditemukan.")

    except Exception as e:
        print(f"erjadi kesalahan: {e}")

    input('< kembali(enter) ')