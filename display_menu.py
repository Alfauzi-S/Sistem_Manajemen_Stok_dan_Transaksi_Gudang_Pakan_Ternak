from InquirerPy import inquirer
import tabulate as tb
import data_program as dpm
import Essential_tools as tool

def menu_awal():
    pilihan = [
        "Login",
        "Register",
        "Keluar"
    ]
    result = inquirer.select(
        message="Pilih Menu:",
        choices=pilihan,
        cycle=True
    ).execute()

    if result is None:
        return None
    return result


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
    result = inquirer.select(
        message="Pilih Menu Admin",
        choices=pilihan,
        cycle=True
    ).execute()

    if result is None:
        return None
    return result


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
    result = inquirer.select(
        message="Pilih Menu User",
        choices=pilihan,
        cycle=True
    ).execute()

    if result is None:
        return None
    return result

def menu_produk():
    table_data = []
    for key_id, velues in dpm.data_produk.items():
        table_data.append([
            key_id,
            velues["Nama Produk"],
            velues["Stok"],
            velues["Ukuran/per Stok"],
            f"Rp{velues['Harga']:,}",
            velues["Kadaluarsa"],
            velues["Tanggal Masuk"],
            velues["Kategori"]
        ])
    print(tb.tabulate(table_data, headers=["ID", "Nama Produk", "Stok", "Ukuran/Stok", "Harga", "Kadaluarsa", "Tanggal Masuk", "Kategori"], tablefmt="rounded_grid", colalign=("center", "left", "center", "center", "right", "center", "center", "left")))


def tabel_keranjang(keranjang_user):
    data_tabel = []
    for key_id, velues in keranjang_user.items():
        baris = [
            key_id,
            velues['nama_produk'],
            velues['jumlah'],
            f"Rp {velues['harga_satuan']:,}",
        ]
        data_tabel.append(baris)
    print(tb.tabulate(data_tabel, headers=["ID produk", "Nama Produk", "Jumlah", "Harga Satuan"], tablefmt="rounded_grid", colalign=("center", "left", "center", "right")))