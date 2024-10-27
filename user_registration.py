"""
este archivo contiene funciones para:
verificar usuarios (cuando se registra uno nuevo)
verificar inicio de sesión
"""
import user_repository, customtkinter, constantesmp, json
def check_user(username, password, window):
    """
    esta funcion revisa que un nombre de usuario esté o no creado en el archivo json
    para definir si el usuario se crea o no
    """
    global users
    with open(user_repository.JSON_PATH, "r") as f:
        users = json.load(f)

    if username in users:
        error_label1 = customtkinter.CTkLabel(master= window, text = "Este usuario ya existe", 
                                              text_color= constantesmp.COLOR_RED)
        error_label1.place(relx=0.5, rely=0.8, anchor="center")
    
    elif username not in users:
        create_user(username, password, window)
        return True
        

def create_user(username, password, window):
    """
    Funcion que crea un usuario
    """
    users[username] = {"password": password}
    with open(user_repository.JSON_PATH, "w") as f:
        json.dump(users, f, indent=4)
    success_label = customtkinter.CTkLabel(master=window, text="Usuario creado exitosamente", 
                                           text_color=constantesmp.COLOR_GREY)
    success_label.place(relx=0.5, rely=0.8, anchor="center")


def check_user_login(username, password):
    """
    Verifica si el usuario y la contraseña son correctos 
    a la hora de iniciar sesion
    """
    if username in users:
        if users[username]['password'] == password:
            return True  
        else:
            return False  
    else:
        return False  





