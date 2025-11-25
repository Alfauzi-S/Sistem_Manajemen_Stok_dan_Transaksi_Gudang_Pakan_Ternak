import pandas as pd 
import tabulate as tb
import Essential_tools as tool 
import data_program as dpm
import Essential_handling_error as ehr
import display_menu as dmn
from colorama import init, Fore, Style
init(autoreset=True)

# File ini berisi logika untuk pengguna dengan role user
# belanja() Memungkinkan user memilih dan menambahkan produk ke keranjang.
# keranjang() Menampilkan isi keranjang dan memproses checkout.
# ubah_keranjang() Mengubah jumlah produk di keranjang.
# hapus_keranjang() Menghapus produk dari keranjang.
# topup() Menambah saldo user.
# history() Menampilkan riwayat transaksi user dari file CSV.


def belanja(username):
    tool.clear()
    print(Fore.YELLOW + f"{" BELANJA ":=^121}")
    dmn.menu_produk()

    konfirmasi = ehr.input_y_or_n("Apakah Anda ingin membeli produk?")
    if konfirmasi: # jika true
        id = ehr.harus_nomor("Masukkan ID produk yang ingin dibeli : ") # input id produk
        if id in dpm.data_produk and dpm.data_produk[id]['Stok'] > 0:  # Jika ID ada dan stok > 0
            print(f"Anda memilih produk: {dpm.data_produk[id]['Nama Produk']}")
            print(f"Stok tersedia: {dpm.data_produk[id]['Stok']}")

            jumlah = ehr.harus_nomor("Masukkan jumlah yang ingin dibeli : ")
            if dpm.data_produk[id]['Stok'] >= jumlah: # Jika stock >= jumlah
                konfirmasi = ehr.input_y_or_n(f"Apakah Anda yakin ingin membeli {jumlah} x {dpm.data_produk[id]['Nama Produk']}?")  
                if konfirmasi: # jikar true
                    # .setdefult untuk memastikan bahwa setiap user memiliki key 'keranjang'
                    item_keranjang = dpm.data_users[username].setdefault('keranjang', {}) # Default data dict kosong
                    # membuat data baru dan menambahkan data baru
                    item_keranjang[id] = {
                    "nama_produk": dpm.data_produk[id]['Nama Produk'],
                    "jumlah": jumlah,
                    "harga_satuan": dpm.data_produk[id]['Harga']
                    }
                    print(Fore.CYAN + f"{jumlah} x {dpm.data_produk[id]['Nama Produk']} telah ditambahkan ke keranjang Anda.")
                else: #jika false
                    print("Pembelian dibatalkan.")
            else:
                print(Fore.RED + "Stok tidak mencukupi.")
        elif id in dpm. data_produk and dpm.data_produk[id]['Stok'] <= 0: # Jika stok <= 0
            print(Fore.RED + f"Maaf, stok {dpm.data_produk[id]['Nama Produk']} sedang habis.")
        else:
            print(Fore.RED + f"Produk dengan ID {id} tidak ditemukan.")
    else: #jika false
        print('keluar menu pembelian')
    input('< kembali(enter) ')


def keranjang(username):
    tool.clear()
    print(Fore.YELLOW + f"{" KERANJANG ":=^64}")

    keranjang_user = dpm.data_users[username].get('keranjang', {}) # cek keranjang ada atau tidak
    if keranjang_user: # Jika keranjang tidak kosong
        dmn.tabel_keranjang(keranjang_user) # tampilkan keranjang

        konfirmasi = ehr.input_y_or_n("Apakah Anda ingin melanjutkan ke checkout?")
        if konfirmasi:
            total_pembelian = 0 # Inisialisasi variabel total_pembelian
            data_struk = [] # Inisialisasi list untuk menyimpan data struk
            for key_id, velues in keranjang_user.items():  # Perulangan untuk mengambil item dari keranjang user
                subtotal = velues['jumlah'] * velues['harga_satuan'] # jumlah * harga produk
                total_pembelian += subtotal # Tambahkan ke total_pembelian
                # Membuat list untuk menyimpan data produk dalam struk
                struk_baris = [
                    key_id,
                    velues['nama_produk'],
                    velues['jumlah'],
                    f"Rp {velues['harga_satuan']:,}",
                    f"Rp {subtotal:,}"
                ]
                data_struk.append(struk_baris) # Tambahkan struk_baris ke data_struk
                
            data_struk.append(["", "", "", "Total:", f"Rp {total_pembelian:,}"]) # Tambahkan total pembelian ke data_struk
            
            tool.clear()
            print(Fore.YELLOW + f"{" STRUK PEMBELIAN ":=^80}")
            struk_belanja = tb.tabulate(data_struk, headers=["ID produk", "Nama Produk", "Jumlah", "Harga Satuan","Subtotal"], tablefmt="rounded_grid", colalign=("center", "left", "center", "right", "right"))
            print(struk_belanja) # Tampilkan struk belanja

            saldo = dpm.data_users[username].setdefault('saldo', 0) # .setdefult untuk memastikan bahwa setiap user memiliki key 'saldo'
            print(f"saldo Anda: Rp {saldo:,}")
            print("="*80)
            
            konfirmasi = ehr.input_y_or_n("Apakah Anda yakin ingin melakukan pembayaran?")
            if konfirmasi:
                if dpm.data_users[username]['saldo'] >= total_pembelian:# Cek apakah saldo >= total_pembelian
                    password = ehr.password("Masukkan password Anda untuk konfirmasi : ")
                    if username in dpm.data_users and dpm.data_users[username]['password'] == password: # cek apakah password benar
                        for key_id, velues in keranjang_user.items(): # Perulangan untuk mengambil item dari keranjang user
                            dpm.data_produk[key_id]['Stok'] -= velues['jumlah'] # Kurangi stok produk
                        dpm.data_users[username]['saldo'] -= total_pembelian  # Kurangi saldo user
                        tool.history_belanja(username, keranjang_user, total_pembelian) # simpan history transaksi di module tool
                        dpm.data_users[username]['keranjang'] = {} # kosongkan keranjang
                        print(Fore.CYAN + "Pembayaran berhasil!")
                        print(f"Sisa saldo Anda: Rp {dpm.data_users[username]['saldo']:,}")
                    else:
                        print(Fore.RED + "Password salah! Pembayaran dibatalkan.")
                else:
                    print(Fore.RED + "Saldo tidak mencukupi untuk melakukan pembayaran.")
                    print(f"Saldo Anda: Rp {dpm.data_users[username]['saldo']:,}, Total Belanja: Rp {total_pembelian:,}")
            else:
                print("Pembayaran dibatalkan.")
        else:
            print('keluar menu keranjang')
    else: # Jika keranjang kosong
        print(Fore.RED + "Keranjang Anda kosong.")
    input('< kembali(enter) ')


def ubah_keranjang(username):
    tool.clear()
    print(Fore.YELLOW + f"{" UBAH KERANJANG ":=^64}")

    keranjang_user = dpm.data_users[username].get('keranjang', {}) # ambil nilai keranjang
    if keranjang_user: # Jika keranjang tidak kosong
        dmn.tabel_keranjang(keranjang_user) # tampilkan keranjang
        konfirmasi = ehr.input_y_or_n("Apakah anda ingin mengubah item di keranjang?")
        if konfirmasi: # jika true
            id = ehr.harus_nomor("Masukkan ID produk yang ingin diubah : ")
            if id in keranjang_user: # Cek apakah ID ada di keranjang
                print(f"Anda memilih produk: {keranjang_user[id]['nama_produk']}")
                print(f"Jumlah Produk keranjang: {keranjang_user[id]['jumlah']}")
                print(f"Jumlah Stock Gudang: {dpm.data_produk[id]['Stok']}")

                jumlah_ubah = ehr.harus_nomor("Masukkan jumlah baru: ")
                if dpm.data_produk[id]['Stok'] >= jumlah_ubah: # jika stock >= jumlah_ubah
                    konfirmasi = ehr.input_y_or_n(f"Apakah Anda yakin ingin mengubah {jumlah_ubah} x {dpm.data_produk[id]['Nama Produk']}?")
                    if konfirmasi: # jika true
                        keranjang_user[id]['jumlah'] = jumlah_ubah # ubah nilai jumlah di keranjang
                        print(Fore.CYAN + f"{jumlah_ubah} x {keranjang_user[id]['nama_produk']} telah diubah di keranjang Anda.")
                    else: # jika false
                        print(Fore.RED + "Membatalkan perubahan.")
                else:
                    print(Fore.RED + 'Stok tidak mencukupi')
            else:
                print(Fore.RED + f"Produk dengan ID {id} tidak ditemukan.")
        else: # jika false
                print('keluar menu ubah keranjang')
    else: # jika keranjang kosong
        print(Fore.RED + "Keranjang Anda kosong.")
    input('< kembali(enter) ')


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


def topup(username):
    tool.clear()
    print(Fore.YELLOW + f"{" ISI SALDO ":=^50}")

    saldo_sekarang = dpm.data_users[username].setdefault('saldo', 0) # .setdefult untuk memastikan bahwa setiap user memiliki key 'saldo'
    print(f'Username: {username}')
    print(f'Saldo Anda saat ini: Rp{saldo_sekarang:,}')
    print('-' * 50)

    konfirmasi = ehr.input_y_or_n('Apakah anda ingin top up? ')
    if konfirmasi: # jika true
        password = ehr.tidak_kosong('Masukkan Password : ')
        if username in dpm.data_users and dpm.data_users[username]['password'] == password: # cek apakah password benar
            jumlah_topup = ehr.harus_nomor('Masukkan jumlah top up (Rp) : ')
            saldo_sekarang += jumlah_topup # tambah jumlah_topup ke saldo_sekarang
            dpm.data_users[username]['saldo'] = saldo_sekarang # masukan saldo_sekarang ke data user
            print(Fore.CYAN + f'Top up berhasil!')
            print(f'Saldo Anda sekarang: Rp{saldo_sekarang:,}')
        else :
            print(Fore.RED + 'Password salah!.')
    else: # jika false
        print('keluar dari menu top up')
    input('< kembali(enter) ')


def history(username):
    tool.clear()
    try:
        print(f"┌{'─'*96}┐")
        print(f"│" + Fore.YELLOW + 'HISTORY TRANSAKSI USER'.center(96) + Style.RESET_ALL + "│")
        print(f"└{'─'*96}┘")

        df = pd.read_csv("history_transaksi.csv") # baca file csv
        data = df[df["nama_pembeli"].str.lower() == username.lower()] # ambil data untuk user 
        
        if not data.empty:
            print(data.to_string(index=False)) # tampilkan data history tanpa index
        else:
            print(f"Tidak ada transaksi untuk user '{username}'.")

    except FileNotFoundError:  # Error jika file tidak ditemukan
        print("File 'history_transaksi.csv' tidak ditemukan.")
    except KeyError as e: # Error jika kolom tidak ditemukan
        print(f"Kolom tidak ditemukan di CSV: {e}")
    except Exception as e: # Error umum lainnya
        print(f"Terjadi kesalahan: {e}")
    finally:
        print('─'*98)
        input('< kembali(enter) ')
