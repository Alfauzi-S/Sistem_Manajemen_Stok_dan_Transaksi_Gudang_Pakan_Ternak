import tabulate as tb
import data_program as dpm
import data_history as dhis

menu_awal = ()

menu_admin = ('menu')

menu_user = ()

def menu_produk():
    headers = ["ID", "Nama Produk", "Stok", "Ukuran/Stok", "Harga", "Kadaluarsa", "Tanggal Masuk", "Kategori"]
    table_data = []
    for ID, info in dpm.data_produk.items():
        table_data.append([
            ID,
            info["nama produk"],
            info["stok"],
            info["ukuran/per stok"],
            f"Rp{info['harga']:,}",
            info["kadaluarsa"],
            info["tanggal masuk"],
            info["kategori"]
        ])
    print(tb.tabulate(table_data, headers=headers, tablefmt="fancy_grid"))

def menu_history():
    for id_transaksi, info in dhis.data_history.items():
        print("=" * 42)
        print(f"ID Transaksi : {id_transaksi}")
        print(f"Nama Pembeli : {info['nama pembeli']}")
        print(f"Tanggal      : {info['tanggal pembelian']}")
        print("-" * 42)
        print("Daftar Produk:")

        produk_list = []
        for p in info["produk"]:
            produk_list.append([
                p["id_produk"],
                p["nama produk"],
                p["jumlah yang dibeli"]
            ])

        headers = ["ID Produk", "Nama Produk", "Jumlah Dibeli"]
        print(tb.tabulate(produk_list, headers=headers, tablefmt="fancy_grid"))
        print(f"Total Bayar : Rp{info['total bayar']:,}")
        print("=" * 42, "\n")