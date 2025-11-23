import matplotlib.pyplot as plt
import pandas as pd

def visualisasi_data():
    df = pd.read_csv('history_transaksi.csv')

    data_produk = df.groupby('nama_produk')['jumlah_yang_dibeli'].sum().reset_index()

    Produk = data_produk['nama_produk']
    jumlah = data_produk['jumlah_yang_dibeli']

    plt.figure(figsize=(10, 6))
    plt.bar(Produk, jumlah)
    plt.xlabel("Nama Produk")
    plt.ylabel("Jumlah Terjual")
    plt.title("Perbandingan Jumlah Penjualan Produk")
    plt.xticks(rotation=45)
    plt.grid(axis="y", alpha=0.5, linestyle="--")
    plt.tight_layout()
    plt.show()