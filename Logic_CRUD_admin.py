import data_program as dpm
import display_menu as dmn
import Essential_tools as tool
import Essential_hendling_error as ehr

def create():
    tool.clear()
    print(f"{'='*18}{'TAMBAH PRODUK BARU'}{'='*18}")
    id_baru = ehr.tidak_kosong("Masukkan ID Produk baru (cth: A7): ").upper() 
    
    #cek id
    if id_baru in dpm.data_produk:
        print(f"\nID {id_baru} sudah ada.")
    else:
        #tersedia
        print(f"ID {id_baru} tersedia. Silakan masukkan detail produk:")
        nama = ehr.tidak_kosong("Nama Produk        : ")
        stok = ehr.harus_nomor("Stok Awal          : ")
        ukuran = ehr.tidak_kosong("Ukuran/per stok             : ")
        harga = ehr.harus_nomor("Harga              : ")
        kategori = ehr.input_kategori("Kategori           : ")
        tgl_masuk = ehr.input_tanggal("Tanggal Masuk (YYYY-MM-DD: ")
        kadaluarsa = ehr.input_tanggal("Kadaluarsa (YYYY-MM-DD): ")
        
        data_baru = {
            "nama produk": nama,
            "stok": stok,
            "ukuran/per stok": ukuran,
            "harga": harga,
            "kadaluarsa": kadaluarsa,
            "tanggal masuk": tgl_masuk,
            "kategori": kategori
        }
        dpm.data_produk[id_baru] = data_baru
            
        print(f"\nData Pakan '{nama}' (ID: {id_baru}) berhasil ditambahkan!")
    
    input('< kembali(0) ')

def read():
    tool.clear()
    print(f"{'='*18}{'LIHAT DAFTAR GUDANG'}{'='*18}")
    dmn.menu_produk
    input('< kembali(0) ')

def update():
    tool.clear()
    print(f"{'='*18}{'UBAH DATA GUDANG'}{'='*18}")
    dmn.menu_produk()
    id_ubah = ehr.tidak_kosong('Masukkan ID produk yang ingin diubah: ').upper()
    
    if id_ubah not in dpm.data_produk:
        print(f'ID Produk {id_ubah} tidak ditemukan.')
    else:
        print(f"--- Mengubah Data ID: {id_ubah} ---")
        print("(Kosongi jika tidak ingin diubah)")
        produk_lama = dpm.data_produk[id_ubah]
        
        nama = ehr.input_string_kosong(f"Nama ({produk_lama['nama produk']}): ", produk_lama['nama produk'])
        stok = ehr.input_angka_kosong(f"Stok ({produk_lama['stok']}): ", produk_lama['stok'])
        ukuran = ehr.input_string_kosong(f"Ukuran ({produk_lama['ukuran/per stok']}): ", produk_lama['ukuran/per stok'])
        harga = ehr.input_angka_kosong(f"Harga (Rp{produk_lama['harga']:,}): ", produk_lama['harga'])
        kategori = ehr.input_kategori(f"Kategori ({produk_lama['kategori']}): ", bisa_kosong=True)
        tgl_masuk = ehr.input_tanggal(f"Tgl masuk ({produk_lama['tanggal masuk']}): ", bisa_kosong=True)
        kadaluarsa = ehr.input_tanggal(f"Kadaluarsa ({produk_lama['kadaluarsa']}): ", bisa_kosong=True)

        #updatenya
        dpm.data_produk[id_ubah] = {
            "nama produk": nama,
            "stok": stok,
            "ukuran/per stok": ukuran,
            "harga": harga,
            "kadaluarsa": kadaluarsa if kadaluarsa else produk_lama['kadaluarsa'],
            "tanggal masuk": tgl_masuk if tgl_masuk else produk_lama['tanggal masuk'],
            "kategori": kategori if kategori else produk_lama['kategori']
        }
        print('Data pakan berhasil diubah!')
    input('< kembali(0) ')

def delate():
    print("")

def history():
    print("")