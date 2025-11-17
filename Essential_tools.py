import os
import csv
from datetime import datetime    
def clear():
    os.system('cls || clear')

def generate_id(id_produk):
    tanggal_pembelian = datetime.now().strftime('%Y-%m-%d')
    tanggal = tanggal_pembelian.split('-')[2] 
    id_transaksi = tanggal + str(id_produk)
    return id_transaksi

def history_belanja(username, keranjang_user, total_pembelian):
    tanggal_pembelian = datetime.now().strftime('%Y-%m-%d')
    file_exists = False
    try:
        with open('history_transaksi.csv', 'r', newline='') as f:
            file_exists = True
    except FileNotFoundError:
        pass

    with open('history_transaksi.csv', 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id_transaksi', 'nama_pembeli', 'tanggal_pembelian', 'total_bayar', 'id_produk', 'nama_produk', 'jumlah_yang_dibeli']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)

        if not file_exists:
            writer.writeheader()

        for id_produk, item in keranjang_user.items():
            id_transaksi_per_item = generate_id(id_produk)
            nama_produk_bersih = item['nama_produk'].strip()
            nama_pembeli_bersih = username.strip()

            writer.writerow({
                'id_transaksi': id_transaksi_per_item,
                'nama_pembeli': nama_pembeli_bersih,
                'tanggal_pembelian': tanggal_pembelian,
                'total_bayar': total_pembelian,
                'id_produk': id_produk,
                'nama_produk': nama_produk_bersih,
                'jumlah_yang_dibeli': item['jumlah']
            })