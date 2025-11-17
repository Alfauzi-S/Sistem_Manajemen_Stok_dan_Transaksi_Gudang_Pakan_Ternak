import tabulate as tb
import data_program as dpm

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
    ['4', 'Hapus'.ljust(33)],
    ['5', 'Top Up'.ljust(33)],
    ['6', 'History'.ljust(33)],
    ['0', 'Logout'.ljust(33)]
]
menu_user = tb.tabulate(menu_user_data, headers=['Pilihan', 'Deskripsi'.ljust(33)], tablefmt='rounded_grid', colalign=("center", "left"))


def menu_produk():
    table_data = []
    for ID, info in dpm.data_produk.items():
        table_data.append([
            ID,
            info["Nama Produk"],
            info["Stok"],
            info["Ukuran/per Stok"],
            f"Rp{info['Harga']:,}",
            info["Kadaluarsa"],
            info["Tanggal Masuk"],
            info["Kategori"]
        ])
    print(tb.tabulate(table_data, headers=["ID", "Nama Produk", "Stok", "Ukuran/Stok", "Harga", "Kadaluarsa", "Tanggal Masuk", "Kategori"], tablefmt="rounded_grid", colalign=("center", "left", "center", "center", "right", "center", "center", "left")))


def tabel_keranjang(keranjang_user):
    data_tabel = []
    for id_produk, item in keranjang_user.items():
        baris = [
            id_produk,
            item['nama_produk'],
            item['jumlah'],
            f"Rp {item['harga_satuan']:,}",
        ]
        data_tabel.append(baris)
    print(tb.tabulate(data_tabel, headers=["ID produk", "Nama Produk", "Jumlah", "Harga Satuan"], tablefmt="rounded_grid", colalign=("center", "left", "center", "right")))


menu_visualisai_data =[
    ['1', 'Produk Populer'.ljust(33)],
    ['2', 'Pendapatan Per Produk'.ljust(33)],
    ['0', 'Keluar'.ljust(33)]
]
menu_visualisai = tb.tabulate(menu_visualisai_data, headers=['Pilihan', 'Deskripsi'.ljust(33)], tablefmt='rounded_grid', colalign=("center", "left"))