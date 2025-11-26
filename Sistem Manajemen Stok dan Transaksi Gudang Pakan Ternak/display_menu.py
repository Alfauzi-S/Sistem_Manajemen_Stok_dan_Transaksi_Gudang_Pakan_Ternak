import questionary as qs
import tabulate as tb
import data_program as dpm

# File ini berisi fungsi-fungsi untuk menampilkan menu interaktif dan tabel menggunakan questionary dan tabulate.
# menu_awal() – Menampilkan menu awal (Login, Register, Keluar).
# menu_admin() – Menampilkan menu admin.
# menu_user() – Menampilkan menu user.
# menu_produk() – Menampilkan daftar produk dalam bentuk tabel.
# tabel_keranjang(keranjang_user) – Menampilkan isi keranjang belanja dalam bentuk tabel.

custom_style = qs.Style([
    ('pointer', 'fg:yellow'),  # Warna panah ">"
    ('highlighted', 'fg:cyan'),  # Warna item yang disorot
    ('answer', 'fg:green'),  # Warna jawaban akhir
    ('text', 'fg:white'),  # Warna teks biasa
])

def menu_awal():
    pilihan = [
        "Login",
        "Register",
        "Keluar"
    ]
    result = qs.select(
        message="Pilih Menu:",
        choices=pilihan,
        use_shortcuts=True, # apa ini?
        style=custom_style, # style
        pointer="> " # kustom pointer
    ).ask()

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
    result = qs.select(
        message="Pilih Menu Admin",
        choices=pilihan,
        use_shortcuts=True,
        style=custom_style,
        pointer="> "
    ).ask()

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
    result = qs.select(
        message="Pilih Menu User",
        choices=pilihan,
        use_shortcuts=True,
        style=custom_style,
        pointer="> "
    ).ask()

    if result is None:
        return None
    return result

def menu_produk():
    table_data = []
    for key_id, velues in dpm.data_produk.items(): # perulangan ambil item dari data produk
        table_data.append([
            key_id,
            velues["Nama Produk"],
            velues["Stok"],
            velues["Ukuran/per Stok"],
            f"Rp{velues['Harga']:,}", # format ke rupiah
            velues["Kadaluarsa"],
            velues["Tanggal Masuk"],
            velues["Kategori"]
        ])
    print(tb.tabulate(table_data, headers=["ID", "Nama Produk", "Stok", "Ukuran/Stok", "Harga", "Kadaluarsa", "Tanggal Masuk", "Kategori"], tablefmt="rounded_grid", colalign=("center", "left", "center", "center", "right", "center", "center", "left")))


def tabel_keranjang(keranjang_user):
    data_tabel = []
    for key_id, velues in keranjang_user.items():# perulangan ambil item dari keranjang user
        # simpan di varibel baris
        baris = [
            key_id,
            velues['nama_produk'],
            velues['jumlah'],
            f"Rp {velues['harga_satuan']:,}", # format ke rupiah
        ]
        data_tabel.append(baris) # tambahkan baris di variabel data_tabel
    print(tb.tabulate(data_tabel, headers=["ID produk", "Nama Produk", "Jumlah", "Harga Satuan"], tablefmt="rounded_grid", colalign=("center", "left", "center", "right")))