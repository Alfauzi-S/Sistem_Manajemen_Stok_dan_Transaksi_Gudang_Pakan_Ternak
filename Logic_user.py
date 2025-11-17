import pandas as pd 
import tabulate as tb
import Essential_tools as tool 
import data_program as dpm
import Essential_hendling_error as ehr
import display_menu as dmn

def belanja(username):
    while True:
        tool.clear()
        print(f"{'='*56} BELANJA {'='*56}")
        dmn.menu_produk()
        konfirmasi = ehr.input_y_or_n("Apakah Anda ingin membeli produk? (y/n): ")
        if konfirmasi == 'y':
            id = ehr.harus_nomor("Masukkan ID produk yang ingin dibeli: ")
            if id in dpm.data_produk and dpm.data_produk[id]['Stok'] > 0:
                print(f"Anda memilih produk: {dpm.data_produk[id]['Nama Produk']}")
                print(f"Stok tersedia: {dpm.data_produk[id]['Stok']}")

                while True:
                    jumlah = ehr.harus_nomor("Masukkan jumlah yang ingin dibeli: ")
                    if jumlah <= dpm.data_produk[id]['Stok'] and dpm.data_produk[id]['Stok'] > 0:
                        while True:
                            konfirmasi = ehr.input_y_or_n(f"Apakah Anda yakin ingin membeli {jumlah} x {dpm.data_produk[id]['Nama Produk']}? (y/n): ")

                            if konfirmasi == 'y':
                                # Buat item keranjang
                                item_keranjang = dpm.data_users[username].setdefault('keranjang', {})
                                item_keranjang[id] = {
                                "nama_produk": dpm.data_produk[id]['Nama Produk'],
                                "jumlah": jumlah,
                                "harga_satuan": dpm.data_produk[id]['Harga']
                                }

                                # Tambahkan item ke keranjang user
                                if 'keranjang' not in dpm.data_users[username]:
                                    dpm.data_users[username]['keranjang'] = {}
                                    dpm.data_users[username]['keranjang'] = item_keranjang 
                                else:
                                    dpm.data_users[username]['keranjang'] = item_keranjang
                                print(f"{jumlah} x {dpm.data_produk[id]['Nama Produk']} telah ditambahkan ke keranjang Anda.")
                                input('< kembali(enter) ') 
                                return None
                            
                            elif konfirmasi == 'n':
                                print("Pembelian dibatalkan.")
                                input('< kembali(enter) ')
                                return None
                    else:
                        input('< Stok tidak mencukupi, coba lagi(enter) ')
            elif id in dpm.data_produk and dpm.data_produk[id]['Stok'] <= 0:
                print(f"Maaf, stok {dpm.data_produk[id]['Nama Produk']} sedang habis.")
                input('< kembali(enter) ')
                return None
            elif id not in dpm.data_produk:
                print(f"Produk dengan ID {id} tidak ditemukan.")
                input('< kembali(enter) ')
                return None
        elif konfirmasi == 'n':
            return None

def keranjang(username):
    while True:
        tool.clear()            
        print(f"{'='*27} KERANJANG {'='*27}")
        keranjang_user = dpm.data_users[username].get('keranjang', {})
        if keranjang_user:
            dmn.tabel_keranjang(keranjang_user)
            konfirmasi = ehr.input_y_or_n("Apakah Anda ingin melanjutkan ke checkout? (y/n): ")
            if konfirmasi == 'y':
                tool.clear()
                total_pembelian = 0
                data_struk = []
                for id_produk, item in keranjang_user.items():
                    subtotal = item['jumlah'] * item['harga_satuan']
                    total_pembelian += subtotal
                    struk_baris = [
                        id_produk,
                        item['nama_produk'],
                        item['jumlah'],
                        f"Rp {item['harga_satuan']:,}",
                        f"Rp {subtotal:,}"
                    ]
                    data_struk.append(struk_baris)
                data_struk.append(["", "", "", "Total:", f"Rp {total_pembelian:,}"])

                print("=== STRUK PEMBELIAN ===")
                struk_belanja = tb.tabulate(data_struk, headers=["ID produk", "Nama Produk", "Jumlah", "Harga Satuan","Subtotal"], tablefmt="rounded_grid", colalign=("center", "left", "center", "right", "right"))
                print(struk_belanja)
                print(f"saldo Anda: Rp {dpm.data_users[username]['saldo']:,}")
                print("========================")
                
                konfirmasi = ehr.input_y_or_n("Apakah Anda yakin ingin melakukan pembayaran? (y/n): ")
                if konfirmasi == 'y':
                    if dpm.data_users[username]['saldo'] >= total_pembelian:
                        while True:
                            password = ehr.tidak_kosong("Masukkan password Anda untuk konfirmasi: ")
                            if password == dpm.data_users[username]['password']:
                                for id_produk, item in keranjang_user.items():
                                    id = id_produk
                                    jumlah = item['jumlah']
                                    dpm.data_produk[id]['Stok'] -= jumlah

                                dpm.data_users[username]['saldo'] -= total_pembelian
                                tool.history_belanja(username, keranjang_user, total_pembelian)
                                dpm.data_users[username]['keranjang'] = {}
                                print("Pembayaran berhasil!")
                                print(f"Sisa saldo Anda: Rp {dpm.data_users[username]['saldo']:,}")
                                input("< kembali(enter) ")
                            
                                return None
                            else:
                                print("Password salah! Pembayaran dibatalkan.")
                                input("< kembali(enter) ")
                    else:
                        print("Saldo tidak mencukupi untuk melakukan pembayaran.")
                        print(f"Saldo Anda: Rp {dpm.data_users[username]['saldo']:,}, Total Belanja: Rp {total_pembelian:,}")
                        input('< kembali(enter) ')
                        return None

                elif konfirmasi == 'n':
                    input('< pembayaran dibatalkan(enter) ')
                    return None
                    
            elif konfirmasi == 'n':
                print("Checkout dibatalkan.")
                input('< kembali(enter) ')
                return None
        else:
            print("Keranjang Anda kosong.")
            input('< kembali(enter) ')
            return None
        

def ubah_keranjang(username):
    while True:
        tool.clear()
        print(f"{'='*56} BELANJA {'='*56}")
        keranjang_user = dpm.data_users[username].get('keranjang', [])

        if keranjang_user:
            dmn.tabel_keranjang(keranjang_user)
            konfirmasi = ehr.input_y_or_n("Apakah anda ingin mengubah item di keranjang? (y/n): ")

            if konfirmasi == 'y':
                id = ehr.harus_nomor("Masukkan ID produk yang ingin diubah: ")

                if id in dpm.data_produk:
                    print(f"Anda memilih produk: {dpm.data_produk[id]['Nama Produk']}")
                    print(f"Jumlah Produk keranjang: {dpm.data_users[username]['keranjang'][id]['jumlah']}")

                    while True:
                        jumlah_ubah = ehr.harus_nomor("Masukkan jumlah baru: ")
                        if jumlah_ubah <= dpm.data_produk[id]['Stok']:
                            while True:
                                konfirmasi = ehr.input_y_or_n(f"Apakah Anda yakin ingin mengubah {jumlah_ubah} x {dpm.data_produk[id]['Nama Produk']}? (y/n): ")

                                if konfirmasi == 'y':
                                    item_keranjang = {
                                    "id_produk": id,
                                    "nama_produk": dpm.data_produk[id]['Nama Produk'],
                                    "jumlah": jumlah_ubah,
                                    "harga_satuan": dpm.data_produk[id]['Harga']
                                    }

                                    dpm.data_users[username]['keranjang'][id] = item_keranjang
                                    print(f"{jumlah_ubah} x {dpm.data_produk[id]['Nama Produk']} telah diubah di keranjang Anda.")
                                    input('< kembali(enter) ') 
                                    return None
                                
                                elif konfirmasi == 'n':
                                    print("Membatalkan perubahan.")
                                    input('< kembali(enter) ')
                                    return None
                        else:
                            input('< Stok tidak mencukupi, coba lagi(enter) ')
                else:
                    print(f"Produk dengan ID {id} tidak ditemukan.")
                    input('< kembali(enter) ')
                    return None
            elif konfirmasi == 'n':
                return None
        else:
            print("Keranjang Anda kosong.")
            input('< kembali(enter) ')
            return None

def hapus_keranjang(username):
    while True:
        tool.clear()
        print(f"{'='*56} BELANJA {'='*56}")
        keranjang_user = dpm.data_users[username].get('keranjang', [])

        if keranjang_user:
            dmn.tabel_keranjang(keranjang_user)
            konfirmasi = ehr.input_y_or_n("Apakah anda ingin menghapus item di keranjang? (y/n): ")

            if konfirmasi == 'y':
                id = ehr.harus_nomor("Masukkan ID produk yang ingin diubah: ")

                if id in dpm.data_produk:
                    print(f"Anda memilih produk: {dpm.data_produk[id]['Nama Produk']}")
                    konfirmasi = ehr.input_y_or_n(f"Apakah Anda yakin ingin menghapus {dpm.data_produk[id]['Nama Produk']} dari keranjang? (y/n): ")
                    if konfirmasi == 'y':   
                        del dpm.data_users[username]['keranjang'][id]
                        print(f"{dpm.data_produk[id]['Nama Produk']} telah dihapus dari keranjang Anda.")
                        input('< kembali(enter) ') 
                        return None
                    elif konfirmasi == 'n':
                        print("Membatalkan penghapusan.")
                        input('< kembali(enter) ')
                        return None
                else:
                    print(f"Produk dengan ID {id} tidak ditemukan.")
                    input('< kembali(enter) ')
                    return None
            elif konfirmasi == 'n':
                return None
        else:
            print("Keranjang Anda kosong.")
            input('< kembali(enter) ')
            return None

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
                        return None

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
        data_user = data_history[data_history["nama_pembeli"].str.lower() == username.lower()]

        if data_user:
            data_user = data_user.copy()
            data_user = data_user.astype({"total_bayar": "object"})
            data_user.loc[:, "total_bayar"] = data_user["total_bayar"].apply(lambda x: f"Rp{x:,}")

            headers = ["ID Transaksi", "Nama Pembeli", "Tanggal Pembelian", "Total Bayar", "ID Produk", "Nama Produk", "Jumlah yang dibeli"]
            print(tb.tabulate(data_user, headers=headers, tablefmt="simple", showindex=False))
            print('─'*125)
        else:
            print(f"Tidak ada transaksi untuk pengguna '{username}'.")

    except FileNotFoundError:
        print("File 'history_transaksi.csv' tidak ditemukan.")
    except KeyError as e:
        print(f"Kolom tidak ditemukan di CSV: {e}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

    input('< kembali(enter) ')