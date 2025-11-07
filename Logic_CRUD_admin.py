import data_program as dpm
import display_menu as dmn
import Essential_tools as tool
import Essential_hendling_error as err

def create():
    tool.clear()
    print(f"{'='*18}{'TAMBAH PRODUK BARU'}{'='*18}")
    
    id_baru = err.tidak_kosong("Masukkan ID Produk baru (cth: A7): ").upper() 
    
    #cek id
    if id_baru in dpm.data_produk:
        print(f"\nID {id_baru} sudah ada.")
    else:
        #tersedia
        print(f"ID {id_baru} tersedia. Silakan masukkan detail produk:")
        
        nama = err.tidak_kosong("Nama Produk        : ")
        stok = err.harus_nomor("Stok Awal          : ")
        ukuran = err.tidak_kosong("Ukuran/per stok             : ")
        harga = err.harus_nomor("Harga              : ")
        kategori = err.input_kategori("Kategori           : ")
        tgl_masuk = err.input_tanggal("Tanggal Masuk (YYYY-MM-DD: ")
        kadaluarsa = err.input_tanggal("Kadaluarsa (YYYY-MM-DD): ")
        
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
    
    input('kembali ke menu admin...')

def read():
    print("")

def update():
    print("")

def delate():
    print("")

def history():
    print("")