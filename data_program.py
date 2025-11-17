# nested Dictionary
data_users = {
    "admin" : {"password" : "123", "peran" : "admin"},
    "juragan" : {"password" : "piton", "peran" : "admin"},
    "peternak" : {"password" : "pembeli", "peran" : "user", "saldo": 500000},
    "siti" : {"password" : "user", "peran" : "user", "saldo": 300000},
    "user" : {"password" : "user", "peran" : "user", "saldo": 9999999999, "keranjang" : {1 : {"nama_produk" : "Pakan Sapi Potong", "jumlah" : 10, "harga_satuan" : 150000}, 2 : {"nama_produk" : "Pakan Ayam Broiler", "jumlah" : 5, "harga_satuan" : 95000}}}
    }

# nested Dictionary
data_produk = {
    1: {
        "Nama Produk": "Pakan Sapi Potong",
        "Stok": 110,
        "Ukuran/per Stok": "50 kg",
        "Harga": 150000,
        "Kadaluarsa": "2026-08-15",
        "Tanggal Masuk": "2025-11-01",
        "Kategori": "Ruminansia"
    },
    2: {
        "Nama Produk": "Pakan Sapi Perah",
        "Stok": 100,
        "Ukuran/per Stok": "50 kg",
        "Harga": 160000,
        "Kadaluarsa": "2026-09-10",
        "Tanggal Masuk": "2025-11-02",
        "Kategori": "Ruminansia"
    },
    3: {
        "Nama Produk": "Pakan Ayam Broiler",
        "Stok": 200,
        "Ukuran/per Stok": "25 kg",
        "Harga": 95000,
        "Kadaluarsa": "2026-05-20",
        "Tanggal Masuk": "2025-11-03",
        "Kategori": "Unggas"
    },
    4: {
        "Nama Produk": "Pakan Ayam Layer",
        "Stok": 180,
        "Ukuran/per Stok": "25 kg",
        "Harga": 90000,
        "Kadaluarsa": "2026-06-05",
        "Tanggal Masuk": "2025-11-04",
        "Kategori": "Unggas"
    },
    5: {
        "Nama Produk": "Pakan Ikan Lele",
        "Stok": 300,
        "Ukuran/per Stok": "20 kg",
        "Harga": 70000,
        "Kadaluarsa": "2026-10-12",
        "Tanggal Masuk": "2025-11-05",
        "Kategori": "Perikanan"
    },
    6: {
        "Nama Produk": "Pakan Bebek Pedaging",
        "Stok": 90,
        "Ukuran/per Stok": "25 kg",
        "Harga": 85000,
        "Kadaluarsa": "2026-07-25",
        "Tanggal Masuk": "2025-11-06",
        "Kategori": "Unggas"
    },

    7: {
        "Nama Produk": "Pakan Burung Lovebird",
        "Stok": 50,
        "Ukuran/per Stok": "5 kg",
        "Harga": 45000,
        "Kadaluarsa": "2026-04-30",
        "Tanggal Masuk": "2025-11-07",
        "Kategori": "Hewan Peliharaan"
    },
    8: {
        "Nama Produk": "Pakan Kelinci",
        "Stok": 60,
        "Ukuran/per Stok": "10 kg",
        "Harga": 50000,
        "Kadaluarsa": "2026-05-15",
        "Tanggal Masuk": "2025-11-08",
        "Kategori": "Hewan Peliharaan"
    },
    9: {
        "Nama Produk": "Pakan Hamster",
        "Stok": 40,
        "Ukuran/per Stok": "5 kg",
        "Harga": 40000,
        "Kadaluarsa": "2026-06-20",
        "Tanggal Masuk": "2025-11-09",
        "Kategori": "Hewan Peliharaan"
    },
    10: {
        "Nama Produk": "Pakan Ikan Hias",
        "Stok": 0,
        "Ukuran/per Stok": "20 kg",
        "Harga": 55000,
        "Kadaluarsa": "2026-08-05",
        "Tanggal Masuk": "2025-11-10",
        "Kategori": "Hewan Peliharaan"
    }
}