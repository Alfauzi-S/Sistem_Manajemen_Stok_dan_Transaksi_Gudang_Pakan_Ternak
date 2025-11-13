import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import data_program as dpm
import Essential_tools as tool
import Essential_hendling_error as ehr
import display_menu as dmn

def visualisasi_data():
    df = pd.read_csv("history_transaksi.csv")
    df_produk = pd.DataFrame([
        {
            "id_produk": k,
            "harga": v["Harga"], 
            "nama_produk": v["Nama Produk"]
        }
        for k, v in dpm.data_produk.items()
    ])
    df_gabung = df.merge(df_produk, on="id_produk", how="left")
    print("Kolom setelah merge:", df_gabung.columns.tolist())
    df_gabung["pendapatan"] = df_gabung["jumlah_yang_dibeli"] * df_gabung["harga"]

    rekap = df_gabung.groupby("id_produk").agg({
        "jumlah_yang_dibeli": "sum",
        "pendapatan": "sum",
        "nama_produk_y": "first"
    }).reset_index()

    while True :
        tool.clear()
        print(dmn.menu_visualisai)
        pilihan = ehr.input_menu("masukan (1/2/0): ")
        if pilihan == 1:
            rekap_populer = rekap.sort_values(by="jumlah_yang_dibeli", ascending=False)

            plt.figure(figsize=(10, 6))
            plt.bar(rekap_populer["nama_produk_y"], rekap_populer["jumlah_yang_dibeli"], color='lightgreen', edgecolor='darkgreen')
            plt.title("Produk Paling Populer (Jumlah Terjual)", fontsize=14, fontweight='bold')
            plt.xlabel("Nama Produk", fontsize=12)
            plt.ylabel("Jumlah Terjual", fontsize=12)
            plt.xticks(rotation=45, ha="right")
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()

        elif pilihan == 2:
            rekap_pendapatan = rekap.sort_values(by="pendapatan", ascending=False)

            plt.figure(figsize=(10, 6))
            plt.bar(rekap_pendapatan["nama_produk_y"], rekap_pendapatan["pendapatan"], color='skyblue', edgecolor='navy')
            plt.title("Pendapatan Total per Produk", fontsize=14, fontweight='bold')
            plt.xlabel("Nama Produk", fontsize=12)
            plt.ylabel("Total Pendapatan (Rp)", fontsize=12)
            plt.xticks(rotation=45, ha="right")
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}'.replace(',', '.')))
            plt.tight_layout()
            plt.show()
        
        elif pilihan == 0:
            break