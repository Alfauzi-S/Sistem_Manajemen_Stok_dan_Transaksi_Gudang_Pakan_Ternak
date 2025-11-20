import inquirer
import tabulate as tb
import data_program as dpm
import colorama as colorama
from colorama import Fore, Style

def menu_awal():
    pilihan = [
        "Login",
        "Register",
        "Keluar"
    ]
    questions = [
        inquirer.List(
            'pilihan',
            message="Pilih Menu:",
            choices=pilihan,
            carousel=True
        ),
    ]
    answers = inquirer.prompt(questions)
    if answers is None:
        return None
    return answers['pilihan']


def menu_admin():
    pilihan = [
        "Lihat Data Gudang",
        "Tambah Produk Baru",
        "Update Data Produk",
        "Hapus Produk",
        "Lihat History Transaksi",
        "Visualisasi Data",
        "Logout"
    ]
    questions = [
        inquirer.List(
            'pilihan',
            message="Pilih Menu Admin",
            choices=pilihan,
            carousel=True
        ),
    ]
    answers = inquirer.prompt(questions)
    if answers is None:
        return None
    return answers['pilihan']


def menu_user():
    pilihan = [
        "Beli Produk",
        "Keranjang dan Checkout",
        "Ubah Produk di Keranjang",
        "Hapus Produk di Keranjang",
        "Top Up Saldo",
        "History Transaksi",
        "Logout"
    ]
    questions = [
        inquirer.List(
            'pilihan',
            message="Pilih Menu User",
            choices=pilihan,
            carousel=True
        ),
    ]
    answers = inquirer.prompt(questions)
    if answers is None:
        return None
    return answers['pilihan']


def menu_visualisasi():
    pilihan = [
        "Produk Populer",
        "Pendapatan Per Produk",
        "Keluar"
    ]
    questions = [
        inquirer.List(
            'pilihan',
            message="Pilih Menu Visualisasi Data",
            choices=pilihan,
            carousel=True
        ),
    ]
    answers = inquirer.prompt(questions)
    if answers is None:
        return None
    return answers['pilihan']


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