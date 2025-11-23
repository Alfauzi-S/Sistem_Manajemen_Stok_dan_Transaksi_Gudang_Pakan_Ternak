import os
import csv
import pandas as pd
from datetime import datetime

def clear():
    os.system('cls || clear')


def history_belanja(username, keranjang_user, total_pembelian):
    nama_file = 'history_transaksi.csv'
    kolom = ['nama_pembeli', 'tanggal_pembelian', 'total_bayar', 'id_produk', 'nama_produk', 'jumlah_yang_dibeli']

    try:
        df_history = pd.read_csv(nama_file)
        data_baru_list = []
        tgl = datetime.now().strftime('%Y-%m-%d')

        for key_id, values in keranjang_user.items(): 
            data_baris = {
                'nama_pembeli': username,
                'tanggal_pembelian': tgl,
                'total_bayar': total_pembelian,
                'id_produk': key_id,
                'nama_produk': values['nama_produk'],
                'jumlah_yang_dibeli': values['jumlah']
            }
            data_baru_list.append(data_baris)

        df_baru = pd.DataFrame(data_baru_list, columns=kolom)

        # Gabungkan DataFrame lama dan baru
        df_gabungan = pd.concat([df_history, df_baru], ignore_index=True)

        # Tulis kembali DataFrame gabungan ke file CSV
        df_gabungan.to_csv(nama_file, index=False)
    except FileNotFoundError:
        df_history = pd.DataFrame(columns=kolom)
