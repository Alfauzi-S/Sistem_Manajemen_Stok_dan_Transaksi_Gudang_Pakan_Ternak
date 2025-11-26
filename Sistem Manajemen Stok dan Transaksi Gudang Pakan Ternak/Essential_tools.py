import os
import pandas as pd
from datetime import datetime

def clear(): 
    os.system('cls || clear') #  # Menjalankan perintah 'cls' di Windows atau 'clear' di Linux/Mac untuk membersihkan terminal

def history_belanja(username, keranjang_user, total_pembelian):
    kolom = ['nama_pembeli', 'tanggal_pembelian', 'total_bayar', 'id_produk', 'nama_produk', 'jumlah_yang_dibeli'] 
    try:
        df_history = pd.read_csv(r"D:\Kuliah\praktikum\Projek-Akhir\Sistem Manajemen Stok dan Transaksi Gudang Pakan Ternak\history_transaksi.csv") # baca file CSV
        
    except FileNotFoundError: 
        df_history = pd.DataFrame(columns=kolom) # jika file tidak ada buat baru dengan kolom yang ditentukan

    data_baru_list = [] # list kosong  
    tgl = datetime.now().strftime('%Y-%m-%d') # ambil tanggal hari ini dengan format YYYY-MM-DD

    for key_id, values in keranjang_user.items(): # Perulangan untuk setiap item di keranjang pengguna
        # dictionary untuk satu baris data pembelian item
        data_baris = {
            'nama_pembeli': username,
            'tanggal_pembelian': tgl,
            'total_bayar': total_pembelian,
            'id_produk': key_id,
            'nama_produk': values['nama_produk'],
            'jumlah_yang_dibeli': values['jumlah']
        }
        data_baru_list.append(data_baris) # masukan data_baris dict ke data_baru_list yang menjadi data list of dict 
    df_baru = pd.DataFrame(data_baru_list, columns=kolom) #buat dataframe dengan kolom di tentunkan
    df_gabungan = pd.concat([df_history, df_baru], ignore_index=True) # gabungkan df_history dengan df_baru
    df_gabungan.to_csv(r"D:\Kuliah\praktikum\Projek-Akhir\Sistem Manajemen Stok dan Transaksi Gudang Pakan Ternak\history_transaksi.csv", index=False) # tulis DataFrame gabungan ke file CSV 'history_transaksi.csv' dan tanpa index