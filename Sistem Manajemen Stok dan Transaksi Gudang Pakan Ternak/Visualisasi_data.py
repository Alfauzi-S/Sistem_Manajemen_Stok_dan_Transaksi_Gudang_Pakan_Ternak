import matplotlib.pyplot as plt
import pandas as pd

def visualisasi_data():
    try :
        df = pd.read_csv(r"D:\Kuliah\praktikum\Projek-Akhir\Sistem Manajemen Stok dan Transaksi Gudang Pakan Ternak\history_transaksi.csv") # baca file CSV

        # Group data berdasarkan 'nama_produk' dan jumlahkan(sum) nilai 'jumlah_yang_dibeli' untuk setiap grup
        # Hasilnya adalah DataFrame baru dengan kolom 'nama_produk' dan 'jumlah_yang_dibeli'
        # .reset_index() digunakan agar 'nama_produk' yang tadinya menjadi indeks grup, kembali menjadi kolom biasa
        data_produk = df.groupby('nama_produk')['jumlah_yang_dibeli'].sum().reset_index()
        Produk = data_produk['nama_produk'] # ambil data nama produk dari dataframe
        jumlah = data_produk['jumlah_yang_dibeli'] # ambil data jumlah yang di beli dari data frame

        plt.figure(figsize=(10, 6))
        plt.bar(Produk, jumlah) #buat char sumbu produk sebagai sumbu x dan jumlah sebagi sumbu y
        plt.xlabel("Nama Produk")
        plt.ylabel("Jumlah Terjual")
        plt.title("Perbandingan Jumlah Penjualan Produk")
        plt.xticks(rotation=45) # putar label agar mudah di baca
        plt.grid(axis="y", alpha=0.5, linestyle="--") # buat line untuk membudahkan membaca grafik
        plt.tight_layout() # mencegah elemen grafik (judul, label) tidak terpotong
        plt.show() # menampilkan grafik
    except FileNotFoundError:
        print("tidak ada file history_transaksi.csv")