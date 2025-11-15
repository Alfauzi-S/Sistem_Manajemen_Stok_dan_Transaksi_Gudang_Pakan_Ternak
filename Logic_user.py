import pandas as pd 
import tabulate as tb
import Essential_tools as tool 
import data_program as dpm
import Essential_hendling_error as ehr

def belanja():
    print("belanja")

def keranjang():
    print("hghgghg")

def ubah_keranjang():
    print("dis")

def hapus_keranjang():
    print("")

def topup(username):
    tool.clear()
    print(f"{'='*18}{'ISI SALDO'}{'='*18}")
    saldo_sekarang = dpm.data_users[username].get('saldo', 0)
    print(f'Username: {username}')
    print(f'Saldo Anda saat ini: Rp{saldo_sekarang:,}')
    print('-' * 42)

    while True:
        konfirmasi = ehr.input_y_or_n('Apakah anda ingin top up? (y/n): ')
        if konfirmasi == 'y':
            while True:
                print('Masukkan password Anda')
                password_input = ehr.tidak_kosong('Masukkan Password: ')

                if password_input == dpm.data_users[username]['password']:
                    jumlah_topup = ehr.harus_nomor('Masukkan jumlah top up (Rp): ')
                    if 'saldo' not in dpm.data_users[username]:
                        dpm.data_users[username]['saldo'] = 0

                    dpm.data_users[username]['saldo'] += jumlah_topup
                    saldo_baru = dpm.data_users[username]['saldo']
                    print(f'Top up berhasil!')
                    print(f'Saldo Anda sekarang: Rp{saldo_baru:,}')
                    input('< kembali(enter) ')
                    break

                else :
                    print('Password salah!.')
                    cobalagi = ehr.input_y_or_n('Coba lagi? (y/n): ')
                    if cobalagi == 'y':
                        continue
                    elif cobalagi == 'n':
                        input('< kembali(enter) ')
                        return

        elif konfirmasi == 'n':
            input('< kembali(enter) ')
            break

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
            history["total_bayar"] = history["total_bayar"].apply(lambda x: f"Rp{x:,}")
            headers = ["ID Transaksi", "Nama Pembeli", "Tanggal Pembelian", "Total Bayar", "ID Produk", "Nama Produk", "Jumlah yang dibeli"]
            print(tb.tabulate(data_user, headers=headers, tablefmt="simple", showindex=False))
            print('─'*125)

    except FileNotFoundError:
        print("File 'history_transaksi.csv' tidak ditemukan.")

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

    input('< kembali(enter) ')