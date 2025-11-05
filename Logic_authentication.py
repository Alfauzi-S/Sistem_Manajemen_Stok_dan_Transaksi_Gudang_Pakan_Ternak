import Logic_menu as mn

def login():
    if peran == "admin":
        mn.menu_admin()
    else:
        mn.menu_user()
        
def register():
    print("")