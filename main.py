import Logic_authentication as auth
import display_menu as dmn
import Essential_tools as tool

def main():
    while True:
        tool.clear
        print(dmn.menu_awal)
        pilihan = input

        if pilihan == 1:
            auth.login()
        elif pilihan == 2:
            auth.register()
        elif pilihan == 3:
            break
        else:
            print("")

if __name__ == "_main_":
    main()