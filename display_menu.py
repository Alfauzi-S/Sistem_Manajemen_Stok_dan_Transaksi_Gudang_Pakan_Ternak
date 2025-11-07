import tabulate as tb
import data_program as dpm
import data_history as dhis

menu_awal_data = [
    ['1', 'Login'.ljust(33)],
    ['2', 'Register'.ljust(33)],
    ['0', 'Keluar'.ljust(33)]
]
menu_awal = tb.tabulate(menu_awal_data, headers=['Pilihan', 'Deskripsi'.ljust(33)], tablefmt='rounded_grid', colalign=("center", "left"))


menu_admin_data = [
    ['1', 'Read'.ljust(33)],
    ['2', 'Create'.ljust(33)],
    ['3', 'Update'.ljust(33)],
    ['4', 'Delete'.ljust(33)],
    ['5', 'History'.ljust(33)],
    ['6', 'Visualisasi'.ljust(33)],
    ['0', 'Logout'.ljust(33)]
]
menu_admin = tb.tabulate(menu_admin_data, headers=['Pilihan', 'Deskripsi'.ljust(33)], tablefmt='rounded_grid', colalign=("center", "left"))


menu_user_data = [
    ['1', 'Beli'.ljust(33)],
    ['2', 'Keranjang'.ljust(33)],
    ['3', 'Ubah'.ljust(33)],
    ['4', 'hapus'.ljust(33)],
    ['5', 'History'.ljust(33)],
    ['0', 'Logout'.ljust(33)]
]
menu_user = tb.tabulate(menu_user_data, headers=['Pilihan', 'Deskripsi'.ljust(33)], tablefmt='rounded_grid', colalign=("center", "left"))



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