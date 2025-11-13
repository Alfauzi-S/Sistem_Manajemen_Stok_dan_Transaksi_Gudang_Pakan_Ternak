import pandas as pd 
import tabulate as tb
import Essential_tools as tool 

def belanja():
    print("belanja")

def keranjang():
    print("hghgghg")

def ubah_keranjang():
    print("dis")

def hapus_keranjang():
    print("")

def topup():
    print("")

def history(username):
    tool.clear()
    try:
        print(f"┌{'─'*123}┐")
        print(f"│{'HISTORY TRANSAKSI USER':^123}│")
        print(f"└{'─'*123}┘")
        data_history = pd.read_csv("history_transaksi.csv")
        data_user = data_history[data_history["nama_pembeli"].str.capitalize() == username.capitalize()]

        if data_user.empty:
            print(f"Tidak ada transaksi untuk pengguna '{username}'.")
        else:
            headers = ["ID Transaksi", "Nama Pembeli", "Tanggal Pembelian", "Total Bayar", "ID Produk", "Nama Produk", "Jumlah yang dibeli"]
            print(tb.tabulate(data_user, headers=headers, tablefmt="simple", showindex=False))
            print('─'*125)

    except FileNotFoundError:
        print("File 'history_transaksi.csv' tidak ditemukan.")

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

    input('< kembali(enter) ')