from datetime import datetime

def tidak_kosong(prompt):
    """Memastikan input string tidak boleh kosong."""
    while True:
        input_str = input(prompt).strip()
        if input_str:
            return input_str
        else:
            print("Input tidak boleh kosong.")

def harus_nomor(prompt):
    """Memastikan input adalah angka positif."""
    while True:
        input_str = input(prompt).strip()
        try:
            angka = int(input_str)
            if angka > 0:
                return angka
            else:
                print("Input harus berupa angka (lebih dari 0).")
        except ValueError:
            print("Input harus berupa angka.")

def input_tanggal(prompt, bisa_kosong=False):
    """Memvalidasi input tanggal format YYYY-MM-DD."""
    while True:
        tgl_str = input(prompt).strip()
        
        if tgl_str.lower() == 'today' and not bisa_kosong:
            return datetime.now().strftime('%Y-%m-%d')
        
        if bisa_kosong and tgl_str == "":
            return ""
            
        if not tgl_str and not bisa_kosong:
            print("Tanggal tidak boleh kosong. (Ketik 'today' untuk hari ini)")
            continue
        try:
            datetime.strptime(tgl_str, '%Y-%m-%d')
            return tgl_str
        except ValueError:
            print("Format tanggal salah. (YYYY-MM-DD)")

def input_kategori(prompt, bisa_kosong=False):
    """Memvalidasi input kategori."""
    kategori_valid = ['ruminansia', 'unggas', 'perikanan', 'hewan peliharaan']
    print(f"Pilihan Kategori: {', '.join(kategori_valid)}")
    
    while True:
        kategori_str = input(prompt).strip().lower()
        if bisa_kosong and kategori_str == "":
            return ""
        
        if kategori_str in kategori_valid:
            return kategori_str.replace(" ", "_").title().replace("_", " ")
        else:
            print(f"Kategori tidak valid. Pilih dari: {', '.join(kategori_valid)}")

def input_string_kosong(prompt, default_value):
    """Untuk update: Mengembalikan nilai baru, atau nilai lama jika dikosongi."""
    input_str = input(prompt).strip()
    return input_str if input_str else default_value

def input_angka_kosong(prompt, default_value):
    """Untuk update: Mengembalikan angka baru, atau nilai lama jika dikosongi."""
    input_str = input(prompt).strip()
    if not input_str:
        return default_value
    try:
        angka = int(input_str)
        if angka > 0:
            return angka
        else:
            print("Input harus angka > 0.")
            return default_value
    except ValueError:
        print("Input tidak valid (harus angka).")
        return default_value