import Logic_authentication as auth
import display_menu as dmn
import Essential_tools as tool
import Essential_hendling_error as ehr

def main():
    while True:
        tool.clear()
        print("selamat datang".center(50))
        print(dmn.menu_awal)
        pilihan = ehr.input_menu("Masukkan pilihan: ")

        if pilihan == 1:
            auth.login()
        elif pilihan == 2:
            auth.register()
        elif pilihan == 0:
            break
        else:
            print(input("< Pilihan tidak valid!(enter)"))

if __name__ == "__main__":
    main()