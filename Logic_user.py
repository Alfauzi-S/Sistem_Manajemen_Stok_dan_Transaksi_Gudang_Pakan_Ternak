import pandas as pd 
import tabulate as tb
import Essential_tools as tool 
import data_program as dpm
import Essential_hendling_error as ehr
import display_menu as dmn
from colorama import init, Fore, Style
init(autoreset=True)

# status Done
def belanja(username):
    tool.clear()
    print(Fore.YELLOW + f"{" BELANJA ":=^121}")
    dmn.menu_produk()
    konfirmasi = ehr.input_y_or_n("Apakah Anda ingin membeli produk? (y/n): ")
    if konfirmasi == 'y':
        id = ehr.harus_nomor("Masukkan ID produk yang ingin dibeli: ")
        if id in dpm.data_produk and dpm.data_produk[id]['Stok'] > 0:
            print(f"Anda memilih produk: {dpm.data_produk[id]['Nama Produk']}")
            print(f"Stok tersedia: {dpm.data_produk[id]['Stok']}")
            jumlah = ehr.harus_nomor("Masukkan jumlah yang ingin dibeli: ")
            if jumlah <= dpm.data_produk[id]['Stok'] and dpm.data_produk[id]['Stok'] > 0:
                konfirmasi = ehr.input_y_or_n(f"Apakah Anda yakin ingin membeli {jumlah} x {dpm.data_produk[id]['Nama Produk']}? (y/n): ")
                if konfirmasi == 'y':
                    # .setdefult untuk memastikan bahwa setiap user memiliki key 'keranjang'
                    item_keranjang = dpm.data_users[username].setdefault('keranjang', {})
                    # menambahkan
                    item_keranjang[id] = {
                    "nama_produk": dpm.data_produk[id]['Nama Produk'],
                    "jumlah": jumlah,
                    "harga_satuan": dpm.data_produk[id]['Harga']
                    }
                    print(Fore.CYAN + f"{jumlah} x {dpm.data_produk[id]['Nama Produk']} telah ditambahkan ke keranjang Anda.")
                elif konfirmasi == 'n':
                    print("Pembelian dibatalkan.")
            else:
                print(Fore.RED + "Stok tidak mencukupi.")
        elif id in dpm.data_produk and dpm.data_produk[id]['Stok'] <= 0:
            print(Fore.RED + f"Maaf, stok {dpm.data_produk[id]['Nama Produk']} sedang habis.")
        else:
            print(Fore.RED + f"Produk dengan ID {id} tidak ditemukan.")
    elif konfirmasi == 'n':
        print('keluar menu pembelian')
    input('< kembali(enter) ')

# status Done tapi History
def keranjang(username):
    tool.clear()
    print(Fore.YELLOW + f"{" KERANJANG ":=^64}")
    keranjang_user = dpm.data_users[username].get('keranjang', {})
    if keranjang_user:
        dmn.tabel_keranjang(keranjang_user)
        konfirmasi = ehr.input_y_or_n("Apakah Anda ingin melanjutkan ke checkout? (y/n): ")
        if konfirmasi == 'y':
            tool.clear()
            total_pembelian = 0
            data_struk = []
            for key_id, velues in keranjang_user.items():
                subtotal = velues['jumlah'] * velues['harga_satuan']
                total_pembelian += subtotal
                struk_baris = [
                    key_id,
                    velues['nama_produk'],
                    velues['jumlah'],
                    f"Rp {velues['harga_satuan']:,}",
                    f"Rp {subtotal:,}"
                ]
                data_struk.append(struk_baris)
                
            data_struk.append(["", "", "", "Total:", f"Rp {total_pembelian:,}"])

            print(Fore.YELLOW + f"{" STRUK PEMBELIAN ":=^80}")
            struk_belanja = tb.tabulate(data_struk, headers=["ID produk", "Nama Produk", "Jumlah", "Harga Satuan","Subtotal"], tablefmt="rounded_grid", colalign=("center", "left", "center", "right", "right"))
            print(struk_belanja)
            saldo = dpm.data_users[username].setdefault('saldo', 0)
            print(f"saldo Anda: Rp {saldo:,}")
            print("="*80)
            
            konfirmasi = ehr.input_y_or_n("Apakah Anda yakin ingin melakukan pembayaran? (y/n): ")
            if konfirmasi == 'y':
                if dpm.data_users[username]['saldo'] >= total_pembelian:
                    password = ehr.tidak_kosong("Masukkan password Anda untuk konfirmasi: ")
                    if password == dpm.data_users[username]['password']:
                        for key_id, velues in keranjang_user.items():
                            id = key_id
                            jumlah = velues['jumlah']
                            dpm.data_produk[id]['Stok'] -= jumlah
                        dpm.data_users[username]['saldo'] -= total_pembelian
                        tool.history_belanja(username, keranjang_user, total_pembelian)
                        dpm.data_users[username]['keranjang'] = {}
                        print(Fore.CYAN + "Pembayaran berhasil!")
                        print(f"Sisa saldo Anda: Rp {dpm.data_users[username]['saldo']:,}")
                    else:
                        print(Fore.RED + "Password salah! Pembayaran dibatalkan.")
                else:
                    print(Fore.RED + "Saldo tidak mencukupi untuk melakukan pembayaran.")
                    print(f"Saldo Anda: Rp {dpm.data_users[username]['saldo']:,}, Total Belanja: Rp {total_pembelian:,}")
            elif konfirmasi == 'n':
                print("Pembayaran dibatalkan.")
        elif konfirmasi == 'n':
            print('keluar menu keranjang')
    else:
        print(Fore.RED + "Keranjang Anda kosong.")
    input('< kembali(enter) ')

# status done
def ubah_keranjang(username):
    tool.clear()
    print(Fore.YELLOW + f"{" UBAH KERANJANG ":=^64}")
    keranjang_user = dpm.data_users[username].get('keranjang', {})
    if keranjang_user:
        dmn.tabel_keranjang(keranjang_user)
        konfirmasi = ehr.input_y_or_n("Apakah anda ingin mengubah item di keranjang? (y/n): ")
        if konfirmasi == 'y':
            id = ehr.harus_nomor("Masukkan ID produk yang ingin diubah: ")
            if id in keranjang_user:
                print(f"Anda memilih produk: {keranjang_user[id]['nama_produk']}")
                print(f"Jumlah Produk keranjang: {keranjang_user[id]['jumlah']}")
                print(f"Jumlah Stock Gudang: {dpm.data_produk[id]['Stok']}")
                jumlah_ubah = ehr.harus_nomor("Masukkan jumlah baru: ")
                if jumlah_ubah <= dpm.data_produk[id]['Stok']:
                    konfirmasi = ehr.input_y_or_n(f"Apakah Anda yakin ingin mengubah {jumlah_ubah} x {dpm.data_produk[id]['Nama Produk']}? (y/n): ")
                    if konfirmasi == 'y':
                        keranjang_user[id]['jumlah'] = jumlah_ubah
                        print(Fore.CYAN + f"{jumlah_ubah} x {keranjang_user[id]['nama_produk']} telah diubah di keranjang Anda.")
                    elif konfirmasi == 'n':
                        print(Fore.RED + "Membatalkan perubahan.")
                else:
                    input(Fore.RED + '< Stok tidak mencukupi, coba lagi(enter) ' + Style.RESET_ALL)
            else:
                print(Fore.RED + f"Produk dengan ID {id} tidak ditemukan.")
        elif konfirmasi == 'n':
                print('keluar menu ubah keranjang')
    else:
        print(Fore.RED + "Keranjang Anda kosong.")
    input('< kembali(enter) ')

# status done
def hapus_keranjang(username):
    tool.clear()
    print(Fore.YELLOW + f"{" HAPUS KERANJANG ":=^64}")
    keranjang_user = dpm.data_users[username].get('keranjang', {})
    if keranjang_user:
        dmn.tabel_keranjang(keranjang_user)
        konfirmasi = ehr.input_y_or_n("Apakah anda ingin menghapus item di keranjang? (y/n): ")
        if konfirmasi == 'y':
            id = ehr.harus_nomor("Masukkan ID produk yang ingin diubah: ")
            if id in keranjang_user:
                print(f"Anda memilih produk: {keranjang_user[id]['nama_produk']}")
                konfirmasi = ehr.input_y_or_n(f"Apakah Anda yakin ingin menghapus {keranjang_user[id]['nama_produk']} dari keranjang? (y/n): ")
                if konfirmasi == 'y':   
                    del keranjang_user[id]
                    print(Fore.CYAN + "Produk dihapus dari keranjang Anda.")
                elif konfirmasi == 'n':
                    print("Membatalkan penghapusan.")
            else:
                print(Fore.RED + f"Produk dengan ID {id} tidak ditemukan.")
        elif konfirmasi == 'n':
            print('keluar dari menu hapus keranjang')
    else:
        print(Fore.RED + "Keranjang Anda kosong.")
    input('< kembali(enter) ')

# status done
def topup(username):
    tool.clear()
    print(Fore.YELLOW + f"{" ISI SALDO ":=^50}")
    saldo_sekarang = dpm.data_users[username].setdefault('saldo', 0)
    print(f'Username: {username}')
    print(f'Saldo Anda saat ini: Rp{saldo_sekarang:,}')
    print('-' * 50)

    konfirmasi = ehr.input_y_or_n('Apakah anda ingin top up? (y/n): ')
    if konfirmasi == 'y':
        password_input = ehr.tidak_kosong('Masukkan Password: ')
        if password_input == dpm.data_users[username]['password']:
            jumlah_topup = ehr.harus_nomor('Masukkan jumlah top up (Rp): ')
            saldo_sekarang += jumlah_topup
            dpm.data_users[username]['saldo'] = saldo_sekarang
            print(Fore.CYAN + f'Top up berhasil!')
            print(f'Saldo Anda sekarang: Rp{saldo_sekarang:,}')
        else :
            print(Fore.RED + 'Password salah!.')
    elif konfirmasi == 'n':
        print('keluar dari menu top up')
    input('< kembali(enter) ')

# status done
def history(username):
    tool.clear()
    try:
        print(f"┌{'─'*96}┐")
        print(f"│" + Fore.YELLOW + 'HISTORY TRANSAKSI USER'.center(96) + Style.RESET_ALL + "│")
        print(f"└{'─'*96}┘")

        df = pd.read_csv("history_transaksi.csv")
        data = df[df["nama_pembeli"].str.lower() == username.lower()]
        
        if not data.empty:
            print(data.to_string(index=False)) 
        else:
            print(f"Tidak ada transaksi untuk user '{username}'.")

    except FileNotFoundError:
        print("File 'history_transaksi.csv' tidak ditemukan.")
    except KeyError as e:
        print(f"Kolom tidak ditemukan di CSV: {e}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        print('─'*98)
        input('< kembali(enter) ')
