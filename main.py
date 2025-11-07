import Logic_authentication as auth
import display_menu as dmn
import Essential_tools as tool

def main():
    while True:
        tool.clear()
        print("selamat datang".center(50))
        print(dmn.menu_awal)
        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            auth.login()
        elif pilihan == "2":
            auth.register()
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()