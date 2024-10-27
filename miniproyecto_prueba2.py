import customtkinter
from PIL import Image

import constantesmp
from user_registration import check_user


#variables iniciales
previous_mode = None
points = 0

window = customtkinter.CTk()
window.geometry("600x1000")
window.title("fitness app")
window.iconbitmap("imagenes/app_logo.ico")
window.config(bg = constantesmp.COLOR_WHITE)

#imagenes:
#customtkinter.CTkImage(light_image= Image.open("imagenes/"), dark_image= Image.open("imagenes/"), size = ())
train_select = customtkinter.CTkImage(light_image= Image.open("imagenes/train_select.png"), dark_image= Image.open("imagenes/train_select.png"), size = (590,160))
back_button_img = customtkinter.CTkImage(light_image= Image.open("imagenes/back_button.png"), dark_image=Image.open("imagenes/back_button.png"), size= (40,40))
chest_exercise1 = customtkinter.CTkImage(light_image= Image.open("imagenes/chest_exercise1.png"), dark_image=Image.open("imagenes/chest_exercise1.png"), size= (400,300))
pause_button_img = customtkinter.CTkImage(light_image=Image.open("imagenes/pause_button.png") , dark_image= Image.open("imagenes/pause_button.png"), size=(40,40))
chest_exercise2 = customtkinter.CTkImage(light_image=Image.open("imagenes/chest_exercise2.png") , dark_image=Image.open("imagenes/chest_exercise2.png") , size=(400,300))
chest_exercise3 = customtkinter.CTkImage(light_image=Image.open("imagenes/chest_exercise3.png") , dark_image=Image.open("imagenes/chest_exercise3.png") , size=(400,300))
chest_exercise4_1 = customtkinter.CTkImage(light_image=Image.open("imagenes/chest_exercise4_1.png") , dark_image=Image.open("imagenes/chest_exercise4_1.png") , size=(250,300))
chest_exercise4_2 = customtkinter.CTkImage(light_image=Image.open("imagenes/chest_exercise4_2.png") , dark_image=Image.open("imagenes/chest_exercise4_2.png") , size=(250,250))
chest_exercise5_1 = customtkinter.CTkImage(light_image=Image.open("imagenes/chest_exercise5_1.png") , dark_image=Image.open("imagenes/chest_exercise5_1.png") , size=(250,300))
chest_exercise5_2 = customtkinter.CTkImage(light_image=Image.open("imagenes/chest_exercise5_2.png") , dark_image=Image.open("imagenes/chest_exercise5_2.png") , size=(250,250))
chest_exercise6 = customtkinter.CTkImage(light_image=Image.open("imagenes/chest_exercise6.png") , dark_image=Image.open("imagenes/chest_exercise6.png") , size=(400,300))
chest_exercise7 = customtkinter.CTkImage(light_image=Image.open("imagenes/chest_exercise7.png") , dark_image=Image.open("imagenes/chest_exercise7.png") , size=(400,300))
congratulations_img = customtkinter.CTkImage(light_image=Image.open("imagenes/congratulations.png") , dark_image=Image.open("imagenes/congratulations.png") , size=(300,300))
back_exercise1 = customtkinter.CTkImage(light_image= Image.open("imagenes/back_exercise1.png"), dark_image= Image.open("imagenes/back_exercise1.png"), size = (400,300))
back_exercise2 = customtkinter.CTkImage(light_image= Image.open("imagenes/back_exercise2.png"), dark_image= Image.open("imagenes/back_exercise2.png"), size = (400,300))
back_exercise3 = customtkinter.CTkImage(light_image= Image.open("imagenes/back_exercise3.png"), dark_image= Image.open("imagenes/back_exercise3.png"), size = (400,300))
back_exercise4 = customtkinter.CTkImage(light_image= Image.open("imagenes/back_exercise4.png"), dark_image= Image.open("imagenes/back_exercise4.png"), size = (400,300))
back_exercise5 = customtkinter.CTkImage(light_image= Image.open("imagenes/back_exercise5.png"), dark_image= Image.open("imagenes/back_exercise5.png"), size = (400,300))
back_exercise6 = customtkinter.CTkImage(light_image= Image.open("imagenes/back_exercise6.png"), dark_image= Image.open("imagenes/back_exercise6.png"), size = (400,300))
back_exercise7 = customtkinter.CTkImage(light_image= Image.open("imagenes/back_exercise7.png"), dark_image= Image.open("imagenes/back_exercise7.png"), size = (400,300))
arm_exercise1 = customtkinter.CTkImage(light_image= Image.open("imagenes/arm_exercise1.png"), dark_image= Image.open("imagenes/arm_exercise1.png"), size = (400,300))
arm_exercise2 = customtkinter.CTkImage(light_image= Image.open("imagenes/arm_exercise2.png"), dark_image= Image.open("imagenes/arm_exercise2.png"), size = (400,300))
arm_exercise3 = customtkinter.CTkImage(light_image= Image.open("imagenes/arm_exercise3.png"), dark_image= Image.open("imagenes/arm_exercise3.png"), size = (400,300))
arm_exercise4 = customtkinter.CTkImage(light_image= Image.open("imagenes/arm_exercise4.jpeg"), dark_image= Image.open("imagenes/arm_exercise4.jpeg"), size = (400,300))
arm_exercise5 = customtkinter.CTkImage(light_image= Image.open("imagenes/arm_exercise5.jpeg"), dark_image= Image.open("imagenes/arm_exercise5.jpeg"), size = (400,300))
arm_exercise6 = customtkinter.CTkImage(light_image= Image.open("imagenes/arm_exercise6.jpeg"), dark_image= Image.open("imagenes/arm_exercise6.jpeg"), size = (400,300))
arm_exercise7 = customtkinter.CTkImage(light_image= Image.open("imagenes/arm_exercise7.jpeg"), dark_image= Image.open("imagenes/arm_exercise7.jpeg"), size = (400,300))
leg_exercise1 = customtkinter.CTkImage(light_image= Image.open("imagenes/leg_exercise1.jpeg"), dark_image= Image.open("imagenes/leg_exercise1.jpeg"), size = (400,300))
leg_exercise2 = customtkinter.CTkImage(light_image= Image.open("imagenes/leg_exercise2.png"), dark_image= Image.open("imagenes/leg_exercise2.png"), size = (400,300))
leg_exercise3 = customtkinter.CTkImage(light_image= Image.open("imagenes/leg_exercise3.jpg"), dark_image= Image.open("imagenes/leg_exercise3.jpg"), size = (400,300))
leg_exercise4 = customtkinter.CTkImage(light_image= Image.open("imagenes/leg_exercise4.jpg"), dark_image= Image.open("imagenes/leg_exercise4.jpg"), size = (400,300))
leg_exercise5 = customtkinter.CTkImage(light_image= Image.open("imagenes/leg_exercise5.jpeg"), dark_image= Image.open("imagenes/leg_exercise5.jpeg"), size = (400,300))
leg_exercise6 = customtkinter.CTkImage(light_image= Image.open("imagenes/leg_exercise6.jpeg"), dark_image= Image.open("imagenes/leg_exercise6.jpeg"), size = (400,300))
leg_exercise7 = customtkinter.CTkImage(light_image= Image.open("imagenes/leg_exercise7.jpeg"), dark_image= Image.open("imagenes/leg_exercise7.jpeg"), size = (400,300))


def clean_window():
    #esta funcion es para borrar los widgets, se ejecutará al cambiar de menú
    for widget in window.winfo_children():
        widget.destroy()


def from_pause_to_mode(previous_mode):
    if previous_mode == "start":
        start()
    elif previous_mode == "chest_train1":
        chest_train1()
    elif previous_mode == "chest_train2":
        chest_train2()
    elif previous_mode  == "chest_train3":
        chest_train3()
    elif previous_mode == "chest_train4":
        chest_train4()
    elif previous_mode == "chest_train5":
        chest_train5()
    elif previous_mode == "chest_train6":
        chest_train6()
    elif previous_mode == "chest_train7":
        chest_train7()
    elif previous_mode == "back_train1":
        back_train1()
    elif previous_mode == "back_train2":
        back_train2()
    elif previous_mode == "back_train3":
        back_train3()
    elif previous_mode == "back_train4":
        back_train4()
    elif previous_mode == "back_train5":
        back_train5()
    elif previous_mode == "back_train6":
        back_train6()
    elif previous_mode == "back_train7":
        back_train7()
    elif previous_mode == "arm_train1":
        arm_train1()
    elif previous_mode == "arm_train2":
        arm_train2()
    elif previous_mode == "arm_train3":
        arm_train3()
    elif previous_mode == "arm_train4":
        arm_train4()
    elif previous_mode == "arm_train5":
        arm_train5()
    elif previous_mode == "arm_train6":
        arm_train6()
    elif previous_mode == "arm_train7":
        arm_train7()
    elif previous_mode == "leg_train1":
        leg_train1()
    elif previous_mode == "leg_train2":
        leg_train2()
    elif previous_mode == "leg_train3":
        leg_train3()
    elif previous_mode == "leg_train4":
        leg_train4()
    elif previous_mode == "leg_train5":
        leg_train5()
    elif previous_mode == "leg_train6":
        leg_train6()
    elif previous_mode == "leg_train7":
        leg_train7()

def login_screen():
    clean_window()
    global login_username, login_password

    login_screen_label1 = customtkinter.CTkLabel(master=window, text="Inicio de sesión", text_color=constantesmp.COLOR_BLACK,
                                                  fg_color=constantesmp.COLOR_WHITE, bg_color=constantesmp.COLOR_WHITE, font=("", 20))
    login_screen_label1.place(relx=0.5, rely=0.1, anchor="center")

    login_screen_label2 = customtkinter.CTkLabel(master=window, text="Nombre de usuario", text_color=constantesmp.COLOR_BLACK,
                                                  fg_color=constantesmp.COLOR_WHITE, bg_color=constantesmp.COLOR_WHITE, font=("", 20))
    login_screen_label2.place(relx=0.5, rely=0.35, anchor="center")

    login_username = customtkinter.CTkEntry(master=window, text_color=constantesmp.COLOR_BLACK,
                                                  fg_color=constantesmp.COLOR_WHITE, bg_color=constantesmp.COLOR_GREY, font=("", 20))
    login_username.place(relx=0.5, rely=0.4, anchor="center")

    login_screen_label3 = customtkinter.CTkLabel(master=window, text="Contraseña", text_color=constantesmp.COLOR_BLACK,
                                                  fg_color=constantesmp.COLOR_WHITE, bg_color=constantesmp.COLOR_WHITE, font=("", 20))
    login_screen_label3.place(relx=0.5, rely=0.55, anchor="center")

    login_password = customtkinter.CTkEntry(master=window, show="*", text_color=constantesmp.COLOR_BLACK,
                                                  fg_color=constantesmp.COLOR_WHITE, bg_color=constantesmp.COLOR_GREY, font=("", 20))
    login_password.place(relx=0.5, rely=0.6, anchor="center")

    login_button = customtkinter.CTkButton(master=window, text="Iniciar sesión", command=click_verify_login)
    login_button.place(relx=0.5, rely=0.7, anchor="center")
    login_button2 = customtkinter.CTkButton(master=window, text="registro de nuevo usuario", command= register_screen)
    login_button2.place(relx=0.5, rely=0.8, anchor="center")

def click_verify_login():
    from user_registration import check_user_login
    username = login_username.get()
    password = login_password.get()

    if check_user_login(username, password):
        start()
    else:
        error_label = customtkinter.CTkLabel(master=window, text="Usuario o contraseña incorrectos", text_color=constantesmp.COLOR_RED)
        error_label.place(relx=0.5, rely=0.8, anchor="center")



def register_screen():
    clean_window()
    global register_password, register_username
    register_screen_label1 = customtkinter.CTkLabel(master = window, text = "Registro de usuario", text_color= constantesmp.COLOR_BLACK,
                                                    fg_color=constantesmp.COLOR_WHITE, bg_color=constantesmp.COLOR_WHITE, font=("", 20))
    register_screen_label1.place(relx = 0.5, rely = 0.1, anchor = "center")
    register_screen_label2 = customtkinter.CTkLabel(master = window, text = "Nombre de usuario", text_color= constantesmp.COLOR_BLACK,
                                                    fg_color=constantesmp.COLOR_WHITE, bg_color=constantesmp.COLOR_WHITE, font=("", 20))
    register_screen_label2.place(relx = 0.5, rely = 0.35, anchor = "center")
    register_username = customtkinter.CTkEntry(master = window, text_color= constantesmp.COLOR_BLACK,
                                                    fg_color=constantesmp.COLOR_WHITE, bg_color=constantesmp.COLOR_GREY, font=("", 20))
    register_username.place(relx = 0.5, rely = 0.4, anchor = "center")
    register_screen_label3 = customtkinter.CTkLabel(master = window, text = "Contraseña", text_color= constantesmp.COLOR_BLACK,
                                                    fg_color=constantesmp.COLOR_WHITE, bg_color=constantesmp.COLOR_WHITE, font=("", 20))
    register_screen_label3.place(relx = 0.5, rely = 0.55, anchor = "center")
    register_password= customtkinter.CTkEntry(master = window, text_color= constantesmp.COLOR_BLACK,
                                                    fg_color=constantesmp.COLOR_WHITE, bg_color=constantesmp.COLOR_GREY, font=("", 20))
    register_password.place(relx = 0.5, rely = 0.6, anchor = "center")

    register_button = customtkinter.CTkButton(master = window, text = "registrarse", command =click_check_user)
    register_button.place(relx = 0.5, rely = 0.7, anchor = "center")
    register_button2 = customtkinter.CTkButton(master=window, text="inicio de sesion", command= login_screen)
    register_button2.place(relx=0.5, rely=0.8, anchor="center")

def click_check_user():
    new_username = register_username.get()
    new_pasword = register_password.get()

    user_created = check_user(new_username, new_pasword, window)
    if user_created:
        start()

def start():
    clean_window()
    button1 = customtkinter.CTkButton(master= window, text = "Pecho",
                                      text_color= constantesmp.COLOR_BLACK,
                                      corner_radius= 10,
                                      fg_color= constantesmp.COLOR_WHITE,
                                      hover_color= constantesmp.COLOR_GREY,
                                      border_color=constantesmp.COLOR_BLACK ,
                                      border_width=2,  width=250, height= 100,
                                      font= ("Helvetica", 65),
                                      command = chest_train1)
    button1.place(relx = 0.5, rely = 0.25, anchor = "center")
    label1 = customtkinter.CTkLabel(master=window, text = "",
                                    image = train_select)
    label1.place(relx = 0.5, rely = 0.06, anchor = "center")
    button2 = customtkinter.CTkButton(master=window, text="Espalda",
                                      text_color=constantesmp.COLOR_BLACK,
                                      corner_radius=10,
                                      fg_color=constantesmp.COLOR_WHITE,
                                      hover_color=constantesmp.COLOR_GREY,
                                      border_color=constantesmp.COLOR_BLACK,
                                      border_width=2,
                                      width=250, height=100,
                                      font=("Special_Elite", 65),
                                      command= back_train1)
    button2.place(relx = 0.5, rely = 0.4, anchor = "center")

    button3 = customtkinter.CTkButton(master=window, text="Brazo",
                                      text_color=constantesmp.COLOR_BLACK,
                                      corner_radius=10,
                                      fg_color=constantesmp.COLOR_WHITE,
                                      hover_color=constantesmp.COLOR_GREY,
                                      border_color=constantesmp.COLOR_BLACK,
                                      border_width=2,
                                      width=250,
                                      height=100,
                                      font=("Special_Elite", 65),
                                      command= arm_train1)
    button3.place(relx = 0.5, rely = 0.55, anchor = "center")

    button4 = customtkinter.CTkButton(master=window, text="Pierna",
                                      text_color=constantesmp.COLOR_BLACK,
                                      corner_radius=10,
                                      fg_color=constantesmp.COLOR_WHITE,
                                      hover_color=constantesmp.COLOR_GREY,
                                      border_color=constantesmp.COLOR_BLACK,
                                      border_width=2,
                                      width=250,
                                      height=100,
                                      font=("Special_Elite", 65),
                                      command=leg_train1)
    button4.place(relx = 0.5, rely = 0.7, anchor = "center")
    label2 = customtkinter.CTkLabel(master= window,
                                    text= "Puntos acomulados:",
                                    text_color=constantesmp.COLOR_BLACK,
                                    corner_radius=10,
                                    fg_color=constantesmp.COLOR_WHITE,
                                    bg_color=constantesmp.COLOR_WHITE,
                                    font= ("", 20))
    label2.place(relx = 0.15, rely = 0.97, anchor = "center")
    label3 = customtkinter.CTkLabel(master=window, text = str(points),
                                    text_color=constantesmp.COLOR_BLACK,
                                    corner_radius=10,
                                    fg_color=constantesmp.COLOR_WHITE,
                                    bg_color=constantesmp.COLOR_WHITE,
                                    font= ("", 20))
    label3.place(relx=0.35, rely=0.97, anchor="center")
    button4 = customtkinter.CTkButton(master=window, text="Tienda (coming soon...)",
                                      text_color=constantesmp.COLOR_BLACK,
                                      corner_radius=10,
                                      fg_color=constantesmp.COLOR_WHITE,
                                      hover_color=constantesmp.COLOR_GREY,
                                      border_color=constantesmp.COLOR_BLACK,
                                      border_width=2,
                                      width=100,
                                      height=100,
                                      font=("Special_Elite", 20))
    button4.place(relx = 0.8, rely = 0.95, anchor = "center")


def pause_menu():
    clean_window()
    pause_menu_label1 = customtkinter.CTkLabel(master = window, 
                                               text = "Menú de pausa", 
                                               text_color= constantesmp.COLOR_BLACK,
                                               corner_radius= 10, 
                                               fg_color= constantesmp.COLOR_WHITE,
                                               bg_color= constantesmp.COLOR_WHITE,
                                               width = 50, font= ("", 40))
    pause_menu_label1.place(relx = 0.5 , rely=0.2 , anchor = "center")
    pause_menu_button_continue = customtkinter.CTkButton(master= window, 
                                                         text = "salir", 
                                                         command = start)
    pause_menu_button_continue.place(relx = 0.5, rely = 0.6, anchor = "center")
    continue_button = customtkinter.CTkButton(master=window, text="continuar",
                                          corner_radius=0, 
                                          hover_color=constantesmp.COLOR_GREY, 
                                          command=lambda: from_pause_to_mode(previous_mode))
    continue_button.place(relx=0.5, rely=0.5, anchor="center")


def train_completed():
    global points
    clean_window()
    train_completed_label1 = customtkinter.CTkLabel(master=window, text = "¡FELICIDADES!", 
                                                    text_color= constantesmp.COLOR_BLACK, 
                                                    corner_radius= 10, 
                                                    fg_color= constantesmp.COLOR_WHITE, 
                                                    bg_color= constantesmp.COLOR_WHITE,
                                                    width = 50, font= ("", 40))
    train_completed_label1.place(relx = 0.5, rely = 0.2, anchor = "center")
    train_completed_label2 = customtkinter.CTkLabel(master= window, text= "", 
                                                    image= congratulations_img, 
                                                    fg_color= constantesmp.COLOR_WHITE)
    train_completed_label2.place(relx = 0.5, rely = 0.5, anchor = "center")
    train_completed_label3 = customtkinter.CTkLabel(master=window, text="Completaste el entrenamiento",
                                                    text_color=constantesmp.COLOR_BLACK, corner_radius=10,
                                                    fg_color=constantesmp.COLOR_WHITE,
                                                    bg_color=constantesmp.COLOR_WHITE,
                                                    width=50, font=("", 40))
    train_completed_label3.place(relx = 0.5, rely = 0.3, anchor = "center")
    train_completed_button = customtkinter.CTkButton(master = window, 
                                                    text= "Regresar al menú", 
                                                    command= start, 
                                                    width= 100, 
                                                    height=50)
    train_completed_button.place(relx =0.5 , rely=0.8 , anchor = "center")
    points += 7


def chest_train1():
    global previous_mode
    clean_window()
    previous_mode = "chest_train1"
    chest_train1_label =  customtkinter.CTkLabel(master=window, 
                                                 text = "Ejercicio #1", 
                                                 text_color= constantesmp.COLOR_BLACK, 
                                                 corner_radius= 10, 
                                                 fg_color= constantesmp.COLOR_WHITE, 
                                                 bg_color= constantesmp.COLOR_WHITE,
                                                     width = 50, font= ("", 40))
    chest_train1_label2 = customtkinter.CTkLabel(master=window, 
                                                 text = "Descripción: en este "
                                                        "ejercicio deberás levantar "
                                                        "las pesas de la maquina com "
                                                        "ambas manos como se "
                                                        "ve en la imagen",
                                                 text_color= constantesmp.COLOR_BLACK, 
                                                 corner_radius= 10, 
                                                 fg_color= constantesmp.COLOR_WHITE, 
                                                 bg_color= constantesmp.COLOR_WHITE,
                                                 width = 50, font= ("", 10),
                                                 height= 50)
    chest_train1_label3 = customtkinter.CTkLabel(master=window, 
                                                 text = "Repeticiones: 10", 
                                                 text_color= constantesmp.COLOR_BLACK, 
                                                 corner_radius= 10, 
                                                 fg_color= constantesmp.COLOR_WHITE, 
                                                 bg_color= constantesmp.COLOR_WHITE,
                                                 width = 50, font= ("", 20))
    chest_train1_label4 = customtkinter.CTkLabel(master=window, 
                                                 text = "Series: 3", 
                                                 text_color= constantesmp.COLOR_BLACK, 
                                                 corner_radius= 10, 
                                                 fg_color= constantesmp.COLOR_WHITE, 
                                                 bg_color= constantesmp.COLOR_WHITE,
                                                 width = 50, font= ("", 20))
    chest_train1_label5 = customtkinter.CTkLabel(master=window, 
                                                 text = "Descanso entre series de 1 minuto", 
                                                 text_color= constantesmp.COLOR_BLACK, 
                                                 corner_radius= 10, 
                                                 fg_color= constantesmp.COLOR_WHITE, 
                                                 bg_color= constantesmp.COLOR_WHITE,
                                                 width = 50, font= ("", 20))
    chest_train1_label2.place(relx = 0.5, rely = 0.5, anchor = "center")
    chest_train1_label3.place(relx = 0.5, rely = 0.55, anchor = "center")
    chest_train1_label4.place(relx = 0.5, rely = 0.6, anchor = "center")
    chest_train1_label5.place(relx = 0.5, rely = 0.65, anchor = "center")
    chest_train1_label.place(relx = 0.5, rely = 0.1, anchor = "center")
    chest_train1_label2 = customtkinter.CTkLabel(master = window, 
                                                 text = "", 
                                                 image = chest_exercise1)
    chest_train1_label2.place(relx = 0.5, rely = 0.3, anchor = "center")
    pause_button = customtkinter.CTkButton(master = window, 
                                           text = "", 
                                           image = pause_button_img, 
                                           command = pause_menu, 
                                           width= 40, height= 40, 
                                           fg_color= constantesmp.COLOR_WHITE, 
                                           corner_radius= 0)
    pause_button.place(relx = 0.1, rely = 0.1, anchor = "center")
    chest_train1_button = customtkinter.CTkButton(master = window, 
                                                  text= "completado", 
                                                  command= chest_train2)
    chest_train1_button.place(relx =0.5 , rely=0.7 , anchor = "center")


def chest_train2():
    global previous_mode
    clean_window()
    previous_mode = "chest_train2"
    pause_button = customtkinter.CTkButton(master = window, 
                                           text = "", 
                                           image = pause_button_img, 
                                           command = pause_menu, 
                                           width= 40, height= 40, 
                                           fg_color= constantesmp.COLOR_WHITE, 
                                           corner_radius= 0)
    pause_button.place(relx = 0.1, rely = 0.1, anchor = "center")
    chest_train2_label1 = customtkinter.CTkLabel(master=window, 
                                                 text = "Ejercicio #2", 
                                                 text_color= constantesmp.COLOR_BLACK, 
                                                 corner_radius= 10, 
                                                 fg_color= constantesmp.COLOR_WHITE, 
                                                 bg_color= constantesmp.COLOR_WHITE,
                                                 width = 50, font= ("", 40))
    chest_train2_label2 = customtkinter.CTkLabel(master=window, 
                                                 text = "Descripción: este ejercicio "
                                                        "es similar al anterior,"
                                                        "con la diferencia de que "
                                                        "será inclinado y "
                                                        "con mancuernas",
                                                 text_color= constantesmp.COLOR_BLACK, 
                                                 corner_radius= 10, 
                                                 fg_color= constantesmp.COLOR_WHITE, 
                                                 bg_color= constantesmp.COLOR_WHITE,
                                                 width = 50, font= ("", 10))
    chest_train2_label3 = customtkinter.CTkLabel(master=window, 
                                                 text = "Repeticiones: 10", 
                                                 text_color= constantesmp.COLOR_BLACK, 
                                                 corner_radius= 10, 
                                                 fg_color= constantesmp.COLOR_WHITE, 
                                                 bg_color= constantesmp.COLOR_WHITE,
                                                 width = 50, font= ("", 20))
    chest_train2_label4 = customtkinter.CTkLabel(master=window, 
                                                 text = "Series: 3", 
                                                 text_color= constantesmp.COLOR_BLACK, 
                                                 corner_radius= 10, 
                                                 fg_color= constantesmp.COLOR_WHITE, 
                                                 bg_color= constantesmp.COLOR_WHITE,
                                                 width = 50, font= ("", 20))
    chest_train2_label5 = customtkinter.CTkLabel(master=window, 
                                                 text = "Descanso entre series de 1 minuto", 
                                                 text_color= constantesmp.COLOR_BLACK, 
                                                 corner_radius= 10, 
                                                 fg_color= constantesmp.COLOR_WHITE, 
                                                 bg_color= constantesmp.COLOR_WHITE,
                                                 width = 50, font= ("", 20))
    chest_train2_label2.place(relx = 0.5, rely = 0.5, anchor = "center")
    chest_train2_label3.place(relx = 0.5, rely = 0.55, anchor = "center")
    chest_train2_label4.place(relx = 0.5, rely = 0.6, anchor = "center")
    chest_train2_label5.place(relx = 0.5, rely = 0.65, anchor = "center")
    chest_train2_label1.place(relx = 0.5, rely = 0.1, anchor = "center")
    chest_train2_label2 = customtkinter.CTkLabel(master = window, 
                                                 text = "", 
                                                 image = chest_exercise2)
    chest_train2_label2.place(relx = 0.5, rely = 0.3, anchor = "center")
    chest_train2_button = customtkinter.CTkButton(master = window, 
                                                  text= "Completado", 
                                                  command= chest_train3)
    chest_train2_button.place(relx =0.5 , rely=0.7 , anchor = "center")
    chest_train2_button2 = customtkinter.CTkButton(master = window, 
                                                   text= "Anterior", 
                                                   command= chest_train1)
    chest_train2_button2.place(relx =0.5 , rely=0.8 , anchor = "center")


def chest_train3():
    global previous_mode
    clean_window()
    previous_mode = "chest_train3"
    pause_button = customtkinter.CTkButton(master = window, text = "", 
                                           image = pause_button_img, 
                                           command = pause_menu, 
                                           width= 40, height= 40, 
                                           fg_color= constantesmp.COLOR_WHITE, 
                                           corner_radius= 0)
    pause_button.place(relx = 0.1, rely = 0.1, anchor = "center")
    chest_train3_label1 = customtkinter.CTkLabel(master=window, 
                                                 text = "Ejercicio #3", 
                                                 text_color= constantesmp.COLOR_BLACK, 
                                                 corner_radius= 10, 
                                                 fg_color= constantesmp.COLOR_WHITE, 
                                                 bg_color= constantesmp.COLOR_WHITE,
                                                 width = 50, font= ("", 40))
    chest_train3_label2 = customtkinter.CTkLabel(master=window, 
                                                 text = "En este "
                                                        "ejercicio deberás halar "
                                                        "las poleas desde arriba "
                                                        "hacia abajo,"
                                                        "como si las estuvieras "
                                                        "cruzando como se ve "
                                                        "en la imagen",
                                                 text_color= constantesmp.COLOR_BLACK, 
                                                 corner_radius= 10, 
                                                 fg_color= constantesmp.COLOR_WHITE, 
                                                 bg_color= constantesmp.COLOR_WHITE,
                                                 width = 50, font= ("", 10))
    chest_train3_label3 = customtkinter.CTkLabel(master=window, 
                                                 text = "Repeticiones: 10 ", 
                                                 text_color= constantesmp.COLOR_BLACK, 
                                                 corner_radius= 10, 
                                                 fg_color= constantesmp.COLOR_WHITE, 
                                                 bg_color= constantesmp.COLOR_WHITE,
                                                 width = 50, font= ("", 20))
    chest_train3_label4 = customtkinter.CTkLabel(master=window, 
                                                 text = "Series:  3 ", 
                                                 text_color= constantesmp.COLOR_BLACK, 
                                                 corner_radius= 10, 
                                                 fg_color= constantesmp.COLOR_WHITE, 
                                                 bg_color= constantesmp.COLOR_WHITE,
                                                 width = 50, font= ("", 20))
    chest_train3_label5 = customtkinter.CTkLabel(master=window, 
                                                 text = "Descanso entre series de 1 minuto", 
                                                 text_color= constantesmp.COLOR_BLACK, 
                                                 corner_radius= 10, 
                                                 fg_color= constantesmp.COLOR_WHITE, 
                                                 bg_color= constantesmp.COLOR_WHITE,
                                                 width = 50, font= ("", 20))
    chest_train3_label2.place(relx = 0.5, rely = 0.5, anchor = "center")
    chest_train3_label3.place(relx = 0.5, rely = 0.55, anchor = "center")
    chest_train3_label4.place(relx = 0.5, rely = 0.6, anchor = "center")
    chest_train3_label5.place(relx = 0.5, rely = 0.65, anchor = "center")
    chest_train3_label1.place(relx = 0.5, rely = 0.1, anchor = "center")
    chest_train3_label2 = customtkinter.CTkLabel(master = window, text = "", 
                                                 image = chest_exercise3)
    chest_train3_label2.place(relx = 0.5, rely = 0.3, anchor = "center")
    chest_train3_button = customtkinter.CTkButton(master = window, 
                                                  text= "Completado", 
                                                  command= chest_train4)
    chest_train3_button.place(relx =0.5 , rely=0.7 , anchor = "center")
    chest_train3_button2 = customtkinter.CTkButton(master = window, 
                                                   text= "Anterior", 
                                                   command= chest_train2)
    chest_train3_button2.place(relx =0.5 , rely=0.8 , anchor = "center")


def chest_train4():
    global previous_mode
    clean_window()
    previous_mode = "chest_train4"
    pause_button = customtkinter.CTkButton(master = window, 
                                           text = "", 
                                           image = pause_button_img, 
                                           command = pause_menu, 
                                           width= 40, height= 40, 
                                           fg_color= constantesmp.COLOR_WHITE, 
                                           corner_radius= 0)
    pause_button.place(relx = 0.1, rely = 0.1, anchor = "center")
    chest_train4_label1 = customtkinter.CTkLabel(master=window, 
                                                 text = "Ejercicio #4", 
                                                 text_color= constantesmp.COLOR_BLACK, 
                                                 corner_radius= 10, 
                                                 fg_color= constantesmp.COLOR_WHITE, 
                                                 bg_color= constantesmp.COLOR_WHITE,
                                                 width = 50, font= ("", 40))
    chest_train4_label2 = customtkinter.CTkLabel(master=window, 
                                                 text = "Descripción: este "
                                                        "ejercicio es similar al"
                                                        " anterior, pero en vez "
                                                        "de halar la polea hacia "
                                                        "abajo, la halas hasta el "
                                                        "centro",
                                                 text_color= constantesmp.COLOR_BLACK, 
                                                 corner_radius= 10, 
                                                 fg_color= constantesmp.COLOR_WHITE, 
                                                 bg_color= constantesmp.COLOR_WHITE,
                                                 width = 50, font= ("", 10))
    chest_train4_label3 = customtkinter.CTkLabel(master=window, 
                                                 text = "Repeticiones: 10", 
                                                 text_color= constantesmp.COLOR_BLACK, 
                                                 corner_radius= 10, 
                                                 fg_color= constantesmp.COLOR_WHITE, 
                                                 bg_color= constantesmp.COLOR_WHITE,
                                                 width = 50, font= ("", 20))
    chest_train4_label4 = customtkinter.CTkLabel(master=window, text = "Series: 3 ", 
                                                 text_color= constantesmp.COLOR_BLACK, 
                                                 corner_radius= 10, 
                                                 fg_color= constantesmp.COLOR_WHITE, 
                                                 bg_color= constantesmp.COLOR_WHITE,
                                                 width = 50, font= ("", 20))
    chest_train4_label5 = customtkinter.CTkLabel(master=window, 
                                                 text = "Descanso entre series de 1 minuto", 
                                                 text_color= constantesmp.COLOR_BLACK, 
                                                 corner_radius= 10, 
                                                 fg_color= constantesmp.COLOR_WHITE, 
                                                 bg_color= constantesmp.COLOR_WHITE,
                                                 width = 50, font= ("", 20))
    chest_train4_label2.place(relx = 0.5, rely = 0.5, anchor = "center")
    chest_train4_label3.place(relx = 0.5, rely = 0.55, anchor = "center")
    chest_train4_label4.place(relx = 0.5, rely = 0.6, anchor = "center")
    chest_train4_label5.place(relx = 0.5, rely = 0.65, anchor = "center")
    chest_train4_label1.place(relx = 0.5, rely = 0.1, anchor = "center")
    chest_train4_label2 = customtkinter.CTkLabel(master = window, text = "", 
                                                 image = chest_exercise4_1)
    chest_train4_label2.place(relx = 0.3, rely = 0.3, anchor = "center")
    chest_train4_label3 = customtkinter.CTkLabel(master = window, text = "", 
                                                 image = chest_exercise4_2)
    chest_train4_label3.place(relx = 0.7, rely = 0.3, anchor = "center")
    chest_train4_button = customtkinter.CTkButton(master = window, 
                                                  text= "Completado", 
                                                  command= chest_train5)
    chest_train4_button.place(relx =0.5 , rely=0.7 , anchor = "center")
    chest_train4_button2 = customtkinter.CTkButton(master = window, 
                                                   text= "Anterior", 
                                                   command= chest_train3)
    chest_train4_button2.place(relx =0.5 , rely=0.8 , anchor = "center")


def chest_train5():
    global previous_mode
    clean_window()
    previous_mode = "chest_train5"
    pause_button = customtkinter.CTkButton(master = window, 
                                           text = "", 
                                           image = pause_button_img, 
                                           command = pause_menu, 
                                           width= 40, height= 40, 
                                           fg_color= constantesmp.COLOR_WHITE, 
                                           corner_radius= 0)
    pause_button.place(relx = 0.1, rely = 0.1, anchor = "center")
    chest_train5_label1 = customtkinter.CTkLabel(master=window, 
                                                 text = "Ejercicio #5", 
                                                 text_color= constantesmp.COLOR_BLACK, 
                                                 corner_radius= 10, 
                                                 fg_color= constantesmp.COLOR_WHITE, 
                                                 bg_color= constantesmp.COLOR_WHITE,
                                                 width = 50, font= ("", 40))
    chest_train5_label2 = customtkinter.CTkLabel(master=window, 
                                                 text = "Descripción: similar a los "
                                                        "anteriores, pero halando la "
                                                        "polea desde abajo hacia arriba",
                                                 text_color= constantesmp.COLOR_BLACK, 
                                                 corner_radius= 10, 
                                                 fg_color= constantesmp.COLOR_WHITE, 
                                                 bg_color= constantesmp.COLOR_WHITE,
                                                 width = 50, font= ("", 10))
    chest_train5_label3 = customtkinter.CTkLabel(master=window, 
                                                 text = "Repeticiones: 10", 
                                                 text_color= constantesmp.COLOR_BLACK, 
                                                 corner_radius= 10, 
                                                 fg_color= constantesmp.COLOR_WHITE, 
                                                 bg_color= constantesmp.COLOR_WHITE,
                                                 width = 50, font= ("", 20))
    chest_train5_label4 = customtkinter.CTkLabel(master=window, 
                                                 text = "Series: 3", 
                                                 text_color= constantesmp.COLOR_BLACK, 
                                                 corner_radius= 10, 
                                                 fg_color= constantesmp.COLOR_WHITE, 
                                                 bg_color= constantesmp.COLOR_WHITE,
                                                 width = 50, font= ("", 20))
    chest_train5_label5 = customtkinter.CTkLabel(master=window, 
                                                 text = "Descanso entre series de 1 minuto", 
                                                 text_color= constantesmp.COLOR_BLACK, 
                                                 corner_radius= 10, 
                                                 fg_color= constantesmp.COLOR_WHITE, 
                                                 bg_color= constantesmp.COLOR_WHITE,
                                                 width = 50, font= ("", 20))
    chest_train5_label2.place(relx = 0.5, rely = 0.5, anchor = "center")
    chest_train5_label3.place(relx = 0.5, rely = 0.55, anchor = "center")
    chest_train5_label4.place(relx = 0.5, rely = 0.6, anchor = "center")
    chest_train5_label5.place(relx = 0.5, rely = 0.65, anchor = "center")
    chest_train5_label1.place(relx = 0.5, rely = 0.1, anchor = "center")
    chest_train5_label2 = customtkinter.CTkLabel(master = window, 
                                                 text = "", image = chest_exercise5_1)
    chest_train5_label2.place(relx = 0.3, rely = 0.3, anchor = "center")
    chest_train5_label3 = customtkinter.CTkLabel(master = window, 
                                                 text = "", image = chest_exercise5_2)
    chest_train5_label3.place(relx = 0.7, rely = 0.3, anchor = "center")
    chest_train5_button = customtkinter.CTkButton(master = window, 
                                                  text= "Completado", 
                                                  command= chest_train6)
    chest_train5_button.place(relx =0.5 , rely=0.7 , anchor = "center")
    chest_train5_button2 = customtkinter.CTkButton(master = window, 
                                                   text= "Anterior", 
                                                   command= chest_train4)
    chest_train5_button2.place(relx =0.5 , rely=0.8 , anchor = "center")


def chest_train6():
    global previous_mode
    clean_window()
    previous_mode = "chest_train6"
    pause_button = customtkinter.CTkButton(master = window, 
                                           text = "", 
                                           image = pause_button_img, 
                                           command = pause_menu, 
                                           width= 40, height= 40, 
                                           fg_color= constantesmp.COLOR_WHITE, 
                                           corner_radius= 0)
    pause_button.place(relx = 0.1, rely = 0.1, anchor = "center")
    chest_train6_label1 = customtkinter.CTkLabel(master=window, 
                                                 text = "Ejercicio #6", 
                                                 text_color= constantesmp.COLOR_BLACK, 
                                                 corner_radius= 10, 
                                                 fg_color= constantesmp.COLOR_WHITE, 
                                                 bg_color= constantesmp.COLOR_WHITE,
                                                 width = 50, font= ("", 40))
    chest_train6_label2 = customtkinter.CTkLabel(master=window, 
                                                 text = "Mientras estés acostado "
                                                        "inclinado alzarás una barra, "
                                                        "luego la bajarás hasta que toque el pecho "
                                                        "y repites hasta culminar la serie",
                                                 text_color= constantesmp.COLOR_BLACK, 
                                                 corner_radius= 10, 
                                                 fg_color= constantesmp.COLOR_WHITE, 
                                                 bg_color= constantesmp.COLOR_WHITE,
                                                      width = 50, font= ("", 9.3))
    chest_train6_label3 = customtkinter.CTkLabel(master=window, 
                                                 text = "Repeticiones: 10", 
                                                 text_color= constantesmp.COLOR_BLACK, 
                                                 corner_radius= 10, 
                                                 fg_color= constantesmp.COLOR_WHITE, 
                                                 bg_color= constantesmp.COLOR_WHITE,
                                                 width = 50, font= ("", 20))
    chest_train6_label4 = customtkinter.CTkLabel(master=window, 
                                                 text = "Series: 3", 
                                                 text_color= constantesmp.COLOR_BLACK, 
                                                 corner_radius= 10, 
                                                 fg_color= constantesmp.COLOR_WHITE, 
                                                 bg_color= constantesmp.COLOR_WHITE,
                                                 width = 50, font= ("", 20))
    chest_train6_label5 = customtkinter.CTkLabel(master=window, 
                                                 text = "Descanso entre series de 1 minuto", 
                                                 text_color= constantesmp.COLOR_BLACK, 
                                                 corner_radius= 10, 
                                                 fg_color= constantesmp.COLOR_WHITE, 
                                                 bg_color= constantesmp.COLOR_WHITE,
                                                 width = 50, font= ("", 20))
    chest_train6_label2.place(relx = 0.5, rely = 0.5, anchor = "center")
    chest_train6_label3.place(relx = 0.5, rely = 0.55, anchor = "center")
    chest_train6_label4.place(relx = 0.5, rely = 0.6, anchor = "center")
    chest_train6_label5.place(relx = 0.5, rely = 0.65, anchor = "center")
    chest_train6_label1.place(relx = 0.5, rely = 0.1, anchor = "center")
    chest_train6_label6 = customtkinter.CTkLabel(master = window, 
                                                 text = "", 
                                                 image = chest_exercise6)
    chest_train6_label6.place(relx = 0.5, rely = 0.3, anchor = "center")
    chest_train6_button = customtkinter.CTkButton(master = window, 
                                                  text= "Completado", 
                                                  command= chest_train7)
    chest_train6_button.place(relx =0.5 , rely=0.7 , anchor = "center")
    chest_train6_button2 = customtkinter.CTkButton(master = window, 
                                                   text= "Anterior", 
                                                   command= chest_train5)
    chest_train6_button2.place(relx =0.5 , rely=0.8 , anchor = "center")


def chest_train7():
    global previous_mode
    clean_window()
    previous_mode = "chest_train7"
    pause_button = customtkinter.CTkButton(master = window, 
                                           text = "", 
                                           image = pause_button_img, 
                                           command = pause_menu, 
                                           width= 40, height= 40, 
                                           fg_color= constantesmp.COLOR_WHITE, 
                                           corner_radius= 0)
    pause_button.place(relx = 0.1, rely = 0.1, anchor = "center")
    chest_train7_label1 = customtkinter.CTkLabel(master=window, 
                                                 text = "Ejercicio #7", 
                                                 text_color= constantesmp.COLOR_BLACK, 
                                                 corner_radius= 10, 
                                                 fg_color= constantesmp.COLOR_WHITE, 
                                                 bg_color= constantesmp.COLOR_WHITE,
                                                 width = 50, font= ("", 40))
    chest_train7_label2 = customtkinter.CTkLabel(master=window, 
                                                 text = "Exactamente lo mismo que el ejercicio "
                                                        "anterior, con la diferencia de que "
                                                        "deberás estar acostado "
                                                        "horizontalmente y no inclinado.",
                                                 text_color= constantesmp.COLOR_BLACK, 
                                                 corner_radius= 10, 
                                                 fg_color= constantesmp.COLOR_WHITE, 
                                                 bg_color= constantesmp.COLOR_WHITE,
                                                 width = 50, font= ("", 10))
    chest_train7_label3 = customtkinter.CTkLabel(master=window, 
                                                 text = "Repeticiones: 10", 
                                                 text_color= constantesmp.COLOR_BLACK, 
                                                 corner_radius= 10, 
                                                 fg_color= constantesmp.COLOR_WHITE, 
                                                 bg_color= constantesmp.COLOR_WHITE,
                                                 width = 50, font= ("", 20))
    chest_train7_label4 = customtkinter.CTkLabel(master=window, 
                                                 text = "Series: 3", 
                                                 text_color= constantesmp.COLOR_BLACK, 
                                                 corner_radius= 10, 
                                                 fg_color= constantesmp.COLOR_WHITE, 
                                                 bg_color= constantesmp.COLOR_WHITE,
                                                 width = 50, font= ("", 20))
    chest_train7_label5 = customtkinter.CTkLabel(master=window, 
                                                 text = "Descanso entre series de 1 minuto", 
                                                 text_color= constantesmp.COLOR_BLACK, 
                                                 corner_radius= 10, 
                                                 fg_color= constantesmp.COLOR_WHITE, 
                                                 bg_color= constantesmp.COLOR_WHITE,
                                                 width = 50, font= ("", 20))
    chest_train7_label1.place(relx = 0.5, rely = 0.1, anchor = "center")
    chest_train7_label2.place(relx = 0.5, rely = 0.5, anchor = "center")
    chest_train7_label3.place(relx = 0.5, rely = 0.55, anchor = "center")
    chest_train7_label4.place(relx = 0.5, rely = 0.6, anchor = "center")
    chest_train7_label5.place(relx = 0.5, rely = 0.65, anchor = "center")
    chest_train7_label6 = customtkinter.CTkLabel(master = window, text = "", 
                                                 image = chest_exercise7)
    chest_train7_label6.place(relx = 0.5, rely = 0.3, anchor = "center")
    chest_train7_button = customtkinter.CTkButton(master = window, 
                                                  text= "Completado", 
                                                  command= train_completed)
    chest_train7_button.place(relx =0.5 , rely=0.7 , anchor = "center")
    chest_train7_button2 = customtkinter.CTkButton(master = window, 
                                                   text= "Anterior", 
                                                   command= chest_train6)
    chest_train7_button2.place(relx =0.5 , rely=0.8 , anchor = "center")


def back_train1():
    global previous_mode
    clean_window()
    previous_mode = "back_train1"
    back_train1_label =  customtkinter.CTkLabel(master=window, 
                                                text = "Ejercicio #1", 
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                     width = 50, font= ("", 40))
    back_train1_label2 = customtkinter.CTkLabel(master=window, 
                                                text = "inclina la columna y "
                                                       "lleva los brazos hacia "
                                                       "atrás mientras cargas peso",
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                      width = 50, font= ("", 10))
    back_train1_label3 = customtkinter.CTkLabel(master=window, 
                                                text = "Repeticiones: 20", 
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                      width = 50, font= ("", 20))
    back_train1_label4 = customtkinter.CTkLabel(master=window, 
                                                text = "Series: 5", 
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    back_train1_label5 = customtkinter.CTkLabel(master=window, 
                                                text = "Descanso entre series de 1 minuto", 
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    back_train1_label2.place(relx = 0.5, rely = 0.5, anchor = "center")
    back_train1_label3.place(relx = 0.5, rely = 0.55, anchor = "center")
    back_train1_label4.place(relx = 0.5, rely = 0.6, anchor = "center")
    back_train1_label5.place(relx = 0.5, rely = 0.65, anchor = "center")
    back_train1_label.place(relx = 0.5, rely = 0.1, anchor = "center")
    back_train1_label2 = customtkinter.CTkLabel(master = window, 
                                                text = "", 
                                                image = back_exercise1)
    back_train1_label2.place(relx = 0.5, rely = 0.3, anchor = "center")
    pause_button = customtkinter.CTkButton(master = window, 
                                           text = "", 
                                           image = pause_button_img, 
                                           command = pause_menu, 
                                           width= 40, height= 40, 
                                           fg_color= constantesmp.COLOR_WHITE, 
                                           corner_radius= 0)
    pause_button.place(relx = 0.1, rely = 0.1, anchor = "center")
    back_train1_button = customtkinter.CTkButton(master = window, 
                                                 text= "completado", 
                                                 command= back_train2)
    back_train1_button.place(relx =0.5 , rely=0.7 , anchor = "center")


def back_train2():
    global previous_mode
    clean_window()
    previous_mode = "back_train2"
    back_train2_label =  customtkinter.CTkLabel(master=window, text = "Ejercicio #2 ", 
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 40))
    back_train2_label2 = customtkinter.CTkLabel(master=window, 
                                                text = "Deberás llevar los brazos "
                                                       "desde alfrente hacia los lados "
                                                       "empujando el peso de la maquina",
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 10))
    back_train2_label3 = customtkinter.CTkLabel(master=window, 
                                                text = "Repeticiones: 10", 
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    back_train2_label4 = customtkinter.CTkLabel(master=window, 
                                                text = "Series: 3", 
                                                text_color= 
                                                constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    back_train2_label5 = customtkinter.CTkLabel(master=window, 
                                                text = "Descanso entre series de 1 minuto", 
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    back_train2_label2.place(relx = 0.5, rely = 0.5, anchor = "center")
    back_train2_label3.place(relx = 0.5, rely = 0.55, anchor = "center")
    back_train2_label4.place(relx = 0.5, rely = 0.6, anchor = "center")
    back_train2_label5.place(relx = 0.5, rely = 0.65, anchor = "center")
    back_train2_label.place(relx = 0.5, rely = 0.1, anchor = "center")
    back_train2_label2 = customtkinter.CTkLabel(master = window, 
                                                text = "", 
                                                image = back_exercise2)
    back_train2_label2.place(relx = 0.5, rely = 0.3, anchor = "center")
    pause_button = customtkinter.CTkButton(master = window, 
                                           text = "", 
                                           image = pause_button_img, 
                                           command = pause_menu, 
                                           width= 40, height= 40, 
                                           fg_color= constantesmp.COLOR_WHITE, 
                                           corner_radius= 0)
    pause_button.place(relx = 0.1, rely = 0.1, anchor = "center")
    back_train2_button = customtkinter.CTkButton(master = window, 
                                                 text= "completado", 
                                                 command= back_train3)
    back_train2_button.place(relx =0.5 , rely=0.7 , anchor = "center")
    back_train2_button2 = customtkinter.CTkButton(master = window, 
                                                  text= "Anterior", 
                                                  command= back_train1)
    back_train2_button2.place(relx =0.5 , rely=0.8 , anchor = "center")


def back_train3():
    global previous_mode
    clean_window()
    previous_mode = "back_train3"
    back_train3_label =  customtkinter.CTkLabel(master=window, text = "Ejercicio #3 ", 
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 40))
    back_train3_label2 = customtkinter.CTkLabel(master=window, 
                                                text = "Aqui deberás llevar la polea "
                                                       "hasta el centro del pecho",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 10))
    back_train3_label3 = customtkinter.CTkLabel(master=window, 
                                                text = "Repeticiones: 10", 
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    back_train3_label4 = customtkinter.CTkLabel(master=window, 
                                                text = "Series: 3", 
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                      width = 50, font= ("", 20))
    back_train3_label5 = customtkinter.CTkLabel(master=window, 
                                                text = "Descanso entre series de 1 minuto", 
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    back_train3_label2.place(relx = 0.5, rely = 0.5, anchor = "center")
    back_train3_label3.place(relx = 0.5, rely = 0.55, anchor = "center")
    back_train3_label4.place(relx = 0.5, rely = 0.6, anchor = "center")
    back_train3_label5.place(relx = 0.5, rely = 0.65, anchor = "center")
    back_train3_label.place(relx = 0.5, rely = 0.1, anchor = "center")
    back_train3_label2 = customtkinter.CTkLabel(master = window, 
                                                text = "",
                                                image = back_exercise3)
    back_train3_label2.place(relx = 0.5, rely = 0.3, anchor = "center")
    pause_button = customtkinter.CTkButton(master = window, 
                                           text = "", 
                                           image = pause_button_img, 
                                           command = pause_menu, 
                                           width= 40, height= 40, 
                                           fg_color= constantesmp.COLOR_WHITE, 
                                           corner_radius= 0)
    pause_button.place(relx = 0.1, rely = 0.1, anchor = "center")
    back_train3_button = customtkinter.CTkButton(master = window, 
                                                 text= "completado", 
                                                 command= back_train4)
    back_train3_button.place(relx =0.5 , rely=0.7 , anchor = "center")
    back_train3_button2 = customtkinter.CTkButton(master = window, 
                                                  text= "Anterior", 
                                                  command= back_train2)
    back_train3_button2.place(relx =0.5 , rely=0.8 , anchor = "center")


def back_train4():
    global previous_mode
    clean_window()
    previous_mode = "back_train4"
    back_train4_label =  customtkinter.CTkLabel(master=window, 
                                                text = "Ejercicio #4 ", 
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                     width = 50, font= ("", 40))
    back_train4_label2 = customtkinter.CTkLabel(master=window, 
                                                text = "Apoyado de un banquillo "
                                                       "usarás 1 brazo para subir peso "
                                                       "de una mancuerna, alterna los 2 brazos",
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                      width = 50, font= ("", 10))
    back_train4_label3 = customtkinter.CTkLabel(master=window, 
                                                text = "Repeticiones: 10", 
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    back_train4_label4 = customtkinter.CTkLabel(master=window, 
                                                text = "Series: 3", 
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    back_train4_label5 = customtkinter.CTkLabel(master=window, 
                                                text = "Descanso entre series de 1 minuto", 
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    back_train4_label2.place(relx = 0.5, rely = 0.5, anchor = "center")
    back_train4_label3.place(relx = 0.5, rely = 0.55, anchor = "center")
    back_train4_label4.place(relx = 0.5, rely = 0.6, anchor = "center")
    back_train4_label5.place(relx = 0.5, rely = 0.65, anchor = "center")
    back_train4_label.place(relx = 0.5, rely = 0.1, anchor = "center")
    back_train4_label2 = customtkinter.CTkLabel(master = window, 
                                                text = "", 
                                                image = back_exercise4)
    back_train4_label2.place(relx = 0.5, rely = 0.3, anchor = "center")
    pause_button = customtkinter.CTkButton(master = window, 
                                           text = "", 
                                           image = pause_button_img, 
                                           command = pause_menu, 
                                           width= 40, height= 40, 
                                           fg_color= constantesmp.COLOR_WHITE, 
                                           corner_radius= 0)
    pause_button.place(relx = 0.1, rely = 0.1, anchor = "center")
    back_train4_button = customtkinter.CTkButton(master = window, 
                                                 text= "completado", 
                                                 command= back_train5)
    back_train4_button.place(relx =0.5 , rely=0.7 , anchor = "center")
    back_train4_button2 = customtkinter.CTkButton(master = window, 
                                                  text= "Anterior", 
                                                  command= back_train3)
    back_train4_button2.place(relx =0.5 , rely=0.8 , anchor = "center")


def back_train5():
    global previous_mode
    clean_window()
    previous_mode = "back_train5"
    back_train5_label =  customtkinter.CTkLabel(master=window, 
                                                text = "Ejercicio #5 ", 
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 40))
    back_train5_label2 = customtkinter.CTkLabel(master=window, 
                                                text = "Con la columna recta, hala "
                                                       "hacia a ti la polea lo"
                                                       "que más puedas",
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,                                                                                                       
                                                width = 50, font= ("", 10))
    back_train5_label3 = customtkinter.CTkLabel(master=window, 
                                                text = "Repeticiones: 10", 
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    back_train5_label4 = customtkinter.CTkLabel(master=window, 
                                                text = "Series: 3", 
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    back_train5_label5 = customtkinter.CTkLabel(master=window, 
                                                text = "Descanso entre series de 1 minuto", 
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    back_train5_label2.place(relx = 0.5, rely = 0.5, anchor = "center")
    back_train5_label3.place(relx = 0.5, rely = 0.55, anchor = "center")
    back_train5_label4.place(relx = 0.5, rely = 0.6, anchor = "center")
    back_train5_label5.place(relx = 0.5, rely = 0.65, anchor = "center")
    back_train5_label.place(relx = 0.5, rely = 0.1, anchor = "center")
    back_train5_label2 = customtkinter.CTkLabel(master = window, 
                                                text = "", 
                                                image = back_exercise5)
    back_train5_label2.place(relx = 0.5, rely = 0.3, anchor = "center")
    pause_button = customtkinter.CTkButton(master = window, text = "", 
                                           image = pause_button_img, 
                                           command = pause_menu,
                                           width= 40, height= 40, 
                                           fg_color= constantesmp.COLOR_WHITE, 
                                           corner_radius= 0)
    pause_button.place(relx = 0.1, rely = 0.1, anchor = "center")
    back_train5_button = customtkinter.CTkButton(master = window, 
                                                 text= "completado", 
                                                 command= back_train6)
    back_train5_button.place(relx =0.5 , rely=0.7 , anchor = "center")
    back_train5_button2 = customtkinter.CTkButton(master = window, 
                                                  text= "Anterior", 
                                                  command= back_train4)
    back_train5_button2.place(relx =0.5 , rely=0.8 , anchor = "center")


def back_train6():
    global previous_mode
    clean_window()
    previous_mode = "back_train6"
    back_train6_label =  customtkinter.CTkLabel(master=window, 
                                                text = "Ejercicio #6 ", 
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 40))
    back_train6_label2 = customtkinter.CTkLabel(master=window, 
                                                text = "Curvea un poco la espalda "
                                                       "y levanta una pesa",
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 10))
    back_train6_label3 = customtkinter.CTkLabel(master=window, 
                                                text = "Repeticiones: 10", 
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    back_train6_label4 = customtkinter.CTkLabel(master=window, 
                                                text = "Series: 3", 
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    back_train6_label5 = customtkinter.CTkLabel(master=window, 
                                                text = "Descanso entre series de 1 minuto",
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    back_train6_label2.place(relx = 0.5, rely = 0.5, anchor = "center")
    back_train6_label3.place(relx = 0.5, rely = 0.55, anchor = "center")
    back_train6_label4.place(relx = 0.5, rely = 0.6, anchor = "center")
    back_train6_label5.place(relx = 0.5, rely = 0.65, anchor = "center")
    back_train6_label.place(relx = 0.5, rely = 0.1, anchor = "center")
    back_train6_label2 = customtkinter.CTkLabel(master = window, text = "", 
                                                image = back_exercise6)
    back_train6_label2.place(relx = 0.5, rely = 0.3, anchor = "center")
    pause_button = customtkinter.CTkButton(master = window, text = "", 
                                           image = pause_button_img, 
                                           command = pause_menu, 
                                           width= 40, height= 40, 
                                           fg_color= constantesmp.COLOR_WHITE, 
                                           corner_radius= 0)
    pause_button.place(relx = 0.1, rely = 0.1, anchor = "center")
    back_train6_button = customtkinter.CTkButton(master = window, 
                                                 text= "completado", 
                                                 command= back_train7)
    back_train6_button.place(relx =0.5 , rely=0.7 , anchor = "center")
    back_train6_button2 = customtkinter.CTkButton(master = window, 
                                                  text= "Anterior", 
                                                  command= back_train5)
    back_train6_button2.place(relx =0.5 , rely=0.8 , anchor = "center")


def back_train7():
    global previous_mode
    clean_window()
    previous_mode = "back_train7"
    back_train7_label =  customtkinter.CTkLabel(master=window,
                                                text = "Ejercicio #7 ",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 40))
    back_train7_label2 = customtkinter.CTkLabel(master=window,
                                                text = "hala la polea hacia ti lo "
                                                       "mas que puedas con la espalda "
                                                       "inclinada hacia atrás",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 10))
    back_train7_label3 = customtkinter.CTkLabel(master=window, 
                                                text = "Repeticiones: 10", 
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    back_train7_label4 = customtkinter.CTkLabel(master=window, text = "Series: 3", 
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    back_train7_label5 = customtkinter.CTkLabel(master=window, 
                                                text = "Descanso entre series de 1 minuto", 
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    back_train7_label2.place(relx = 0.5, rely = 0.5, anchor = "center")
    back_train7_label3.place(relx = 0.5, rely = 0.55, anchor = "center")
    back_train7_label4.place(relx = 0.5, rely = 0.6, anchor = "center")
    back_train7_label5.place(relx = 0.5, rely = 0.65, anchor = "center")
    back_train7_label.place(relx = 0.5, rely = 0.1, anchor = "center")
    back_train7_label2 = customtkinter.CTkLabel(master = window,
                                                text = "", 
                                                image = back_exercise7)
    back_train7_label2.place(relx = 0.5, rely = 0.3, anchor = "center")
    pause_button = customtkinter.CTkButton(master = window, 
                                           text = "", 
                                           image = pause_button_img, 
                                           command = pause_menu, 
                                           width= 40, height= 40, 
                                           fg_color= constantesmp.COLOR_WHITE, 
                                           corner_radius= 0)
    pause_button.place(relx = 0.1, rely = 0.1, anchor = "center")
    back_train7_button = customtkinter.CTkButton(master = window, 
                                                 text= "completado", 
                                                 command= train_completed)
    back_train7_button.place(relx =0.5 , rely=0.7 , anchor = "center")
    back_train7_button2 = customtkinter.CTkButton(master = window, 
                                                  text= "Anterior", 
                                                  command= back_train6)
    back_train7_button2.place(relx =0.5 , rely=0.8 , anchor = "center")


def arm_train1():
    global previous_mode
    clean_window()
    previous_mode = "arm_train1"
    arm_train1_label =  customtkinter.CTkLabel(master=window,
                                                text = "Ejercicio #1 ",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 40))
    arm_train1_label2 = customtkinter.CTkLabel(master=window,
                                                text = "Contrae ambos antebrazos "
                                                       "mientras cargas con el "
                                                       "peso de una barra, "
                                                       "como se ve en la imagen",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 10))
    arm_train1_label3 = customtkinter.CTkLabel(master=window, 
                                                text = "Repeticiones: 10", 
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    arm_train1_label4 = customtkinter.CTkLabel(master=window, 
                                                text = "Series: 3", 
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                      width = 50, font= ("", 20))
    arm_train1_label5 = customtkinter.CTkLabel(master=window, 
                                                text = "Descanso entre series de 1 minuto", 
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    arm_train1_label2.place(relx = 0.5, rely = 0.5, anchor = "center")
    arm_train1_label3.place(relx = 0.5, rely = 0.55, anchor = "center")
    arm_train1_label4.place(relx = 0.5, rely = 0.6, anchor = "center")
    arm_train1_label5.place(relx = 0.5, rely = 0.65, anchor = "center")
    arm_train1_label.place(relx = 0.5, rely = 0.1, anchor = "center")
    arm_train1_label6 = customtkinter.CTkLabel(master = window, 
                                                text = "", 
                                                image = arm_exercise1)
    arm_train1_label6.place(relx = 0.5, rely = 0.3, anchor = "center")
    pause_button = customtkinter.CTkButton(master = window, 
                                           text = "", 
                                           image = pause_button_img, 
                                           command = pause_menu, 
                                           width= 40, height= 40, 
                                           fg_color= constantesmp.COLOR_WHITE, 
                                           corner_radius= 0)
    pause_button.place(relx = 0.1, rely = 0.1, anchor = "center")
    arm_train1_button = customtkinter.CTkButton(master = window, 
                                                 text= "completado", 
                                                 command= arm_train2)
    arm_train1_button.place(relx =0.5 , rely=0.7 , anchor = "center")


def arm_train2():
    global previous_mode
    clean_window()
    previous_mode = "arm_train2"
    arm_train2_label1 =  customtkinter.CTkLabel(master=window,
                                                text = "Ejercicio #2 ",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 40))
    arm_train2_label2 = customtkinter.CTkLabel(master=window,
                                                text = "Coje la mancuerna con ambas "
                                                       "manos y haz que los codos apunten "
                                                       "hacia delante, "
                                                       "la espalda deberá estar recta.",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 10))
    arm_train2_label3 = customtkinter.CTkLabel(master=window, 
                                                text = "Repeticiones: 10", 
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    arm_train2_label4 = customtkinter.CTkLabel(master=window, 
                                                text = "Series: 3", 
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    arm_train2_label5 = customtkinter.CTkLabel(master=window, 
                                                text = "Descanso entre series de 1 minuto", 
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    arm_train2_label2.place(relx = 0.5, rely = 0.5, anchor = "center")
    arm_train2_label3.place(relx = 0.5, rely = 0.55, anchor = "center")
    arm_train2_label4.place(relx = 0.5, rely = 0.6, anchor = "center")
    arm_train2_label5.place(relx = 0.5, rely = 0.65, anchor = "center")
    arm_train2_label1.place(relx = 0.5, rely = 0.1, anchor = "center")
    arm_train2_label2 = customtkinter.CTkLabel(master = window, text = "", 
                                                image = arm_exercise2)
    arm_train2_label2.place(relx = 0.5, rely = 0.3, anchor = "center")
    pause_button = customtkinter.CTkButton(master = window, 
                                           text = "", 
                                           image = pause_button_img,
                                           command = pause_menu, 
                                           width= 40, height= 40, 
                                           fg_color= constantesmp.COLOR_WHITE, 
                                           corner_radius= 0)
    pause_button.place(relx = 0.1, rely = 0.1, anchor = "center")
    arm_train2_button = customtkinter.CTkButton(master = window, 
                                                 text= "completado", 
                                                 command= arm_train3)
    arm_train2_button.place(relx =0.5 , rely=0.7 , anchor = "center")
    arm_train2_button2 = customtkinter.CTkButton(master = window, 
                                                  text= "Anterior", 
                                                  command= arm_train1)
    arm_train2_button2.place(relx =0.5 , rely=0.8 , anchor = "center")


def arm_train3():
    global previous_mode
    clean_window()
    previous_mode = "arm_train3"
    arm_train3_label =  customtkinter.CTkLabel(master=window,
                                                text = "Ejercicio #3 ",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 40))
    arm_train3_label2 = customtkinter.CTkLabel(master=window,
                                                text = "Levanta las mancuernas de manera "
                                                       "vertical como en la imagen",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                      width = 50, font= ("", 10))
    arm_train3_label3 = customtkinter.CTkLabel(master=window, 
                                                text = "Repeticiones: 10", 
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    arm_train3_label4 = customtkinter.CTkLabel(master=window, 
                                                text = "Series: 3", 
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    arm_train3_label5 = customtkinter.CTkLabel(master=window, 
                                                text = "Descanso entre series de 1 minuto", 
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    arm_train3_label2.place(relx = 0.5, rely = 0.5, anchor = "center")
    arm_train3_label3.place(relx = 0.5, rely = 0.55, anchor = "center")
    arm_train3_label4.place(relx = 0.5, rely = 0.6, anchor = "center")
    arm_train3_label5.place(relx = 0.5, rely = 0.65, anchor = "center")
    arm_train3_label.place(relx = 0.5, rely = 0.1, anchor = "center")
    arm_train3_label2 = customtkinter.CTkLabel(master = window, text = "", 
                                                image = arm_exercise3)
    arm_train3_label2.place(relx = 0.5, rely = 0.3, anchor = "center")
    pause_button = customtkinter.CTkButton(master = 
                                           window, text = "", 
                                           image = pause_button_img, 
                                           command = pause_menu, 
                                           width= 40, height= 40, 
                                           fg_color= constantesmp.COLOR_WHITE, 
                                           corner_radius= 0)
    pause_button.place(relx = 0.1, rely = 0.1, anchor = "center")
    arm_train3_button = customtkinter.CTkButton(master = window, 
                                                 text= "completado", 
                                                 command= arm_train4)
    arm_train3_button.place(relx =0.5 , rely=0.7 , anchor = "center")
    arm_train3_button2 = customtkinter.CTkButton(master = window, 
                                                  text= "Anterior", 
                                                  command= arm_train2)
    arm_train3_button2.place(relx =0.5 , rely=0.8 , anchor = "center")


def arm_train4():
    global previous_mode
    clean_window()
    previous_mode = "arm_train4"
    arm_train4_label =  customtkinter.CTkLabel(master=window,
                                                text = "Ejercicio #4 ",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 40))
    arm_train4_label2 = customtkinter.CTkLabel(master=window,
                                                text = "Lenvanta las "
                                                       "mancuernas hacia los lados "
                                                       "con ambos brazos",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 10))
    arm_train4_label3 = customtkinter.CTkLabel(master=window, 
                                                text = "Repeticiones: 10", 
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    arm_train4_label4 = customtkinter.CTkLabel(master=window, 
                                                text = "Series: 3", 
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    arm_train4_label5 = customtkinter.CTkLabel(master=window, 
                                                text = "Descanso entre series de 1 minuto", 
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    arm_train4_label2.place(relx = 0.5, rely = 0.5, anchor = "center")
    arm_train4_label3.place(relx = 0.5, rely = 0.55, anchor = "center")
    arm_train4_label4.place(relx = 0.5, rely = 0.6, anchor = "center")
    arm_train4_label5.place(relx = 0.5, rely = 0.65, anchor = "center")
    arm_train4_label.place(relx = 0.5, rely = 0.1, anchor = "center")
    arm_train4_label2 = customtkinter.CTkLabel(master = window, 
                                                text = "", 
                                                image = arm_exercise4)
    arm_train4_label2.place(relx = 0.5, rely = 0.3, anchor = "center")
    pause_button = customtkinter.CTkButton(master = window, 
                                           text = "", 
                                           image = pause_button_img, 
                                           command = pause_menu,
                                            width= 40, height= 40, 
                                           fg_color= constantesmp.COLOR_WHITE, 
                                           corner_radius= 0)
    pause_button.place(relx = 0.1, rely = 0.1, anchor = "center")
    arm_train4_button = customtkinter.CTkButton(master = window, 
                                                 text= "completado", 
                                                 command= arm_train5)
    arm_train4_button.place(relx =0.5 , rely=0.7 , anchor = "center")
    arm_train4_button2 = customtkinter.CTkButton(master = window, 
                                                  text= "Anterior", 
                                                  command= arm_train3)
    arm_train4_button2.place(relx =0.5 , rely=0.8 , anchor = "center")


def arm_train5():
    global previous_mode
    clean_window()
    previous_mode = "arm_train5"
    arm_train5_label =  customtkinter.CTkLabel(master=window,
                                                text = "Ejercicio #5 ",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 40))
    arm_train5_label2 = customtkinter.CTkLabel(master=window,
                                                text = "Levanta las mancuernas "
                                                       "como indica en la imagen "
                                                       "mientras alternas los brazos",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 10))
    arm_train5_label3 = customtkinter.CTkLabel(master=window, 
                                                text = "Repeticiones: 10", 
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    arm_train5_label4 = customtkinter.CTkLabel(master=window, 
                                                text = "Series: 3", 
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    arm_train5_label5 = customtkinter.CTkLabel(master=window, 
                                                text = "Descanso entre series de 1 minuto", 
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    arm_train5_label2.place(relx = 0.5, rely = 0.5, anchor = "center")
    arm_train5_label3.place(relx = 0.5, rely = 0.55, anchor = "center")
    arm_train5_label4.place(relx = 0.5, rely = 0.6, anchor = "center")
    arm_train5_label5.place(relx = 0.5, rely = 0.65, anchor = "center")
    arm_train5_label.place(relx = 0.5, rely = 0.1, anchor = "center")
    arm_train5_label2 = customtkinter.CTkLabel(master = window, text = "", 
                                                image = arm_exercise5)
    arm_train5_label2.place(relx = 0.5, rely = 0.3, anchor = "center")
    pause_button = customtkinter.CTkButton(master = window, 
                                           text = "", 
                                           image = pause_button_img, 
                                           command = pause_menu, 
                                           width= 40, height= 40, 
                                           fg_color= constantesmp.COLOR_WHITE, 
                                           corner_radius= 0)
    pause_button.place(relx = 0.1, rely = 0.1, anchor = "center")
    arm_train5_button = customtkinter.CTkButton(master = window, 
                                                 text= "completado", 
                                                 command= arm_train6)
    arm_train5_button.place(relx =0.5 , rely=0.7 , anchor = "center")
    arm_train5_button2 = customtkinter.CTkButton(master = window, 
                                                  text= "Anterior", 
                                                  command= arm_train4)
    arm_train5_button2.place(relx =0.5 , rely=0.8 , anchor = "center")


def arm_train6():
    global previous_mode
    clean_window()
    previous_mode = "arm_train6"
    arm_train6_label =  customtkinter.CTkLabel(master=window,
                                                text = "Ejercicio #6 ",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 40))
    arm_train6_label2 = customtkinter.CTkLabel(master=window,
                                                text = "En este ejercicio concentrarás "
                                                       "la fuerza en 1 solo brazo para "
                                                       "levantar la mancuerna",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 10))
    arm_train6_label3 = customtkinter.CTkLabel(master=window, 
                                                text = "Repeticiones: 10", 
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    arm_train6_label4 = customtkinter.CTkLabel(master=window, 
                                                text = "Series: 3", 
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    arm_train6_label5 = customtkinter.CTkLabel(master=window, 
                                                text = "Descanso entre series de 1 minuto", 
                                                text_color= constantesmp.COLOR_BLACK, 
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE, 
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    arm_train6_label2.place(relx = 0.5, rely = 0.5, anchor = "center")
    arm_train6_label3.place(relx = 0.5, rely = 0.55, anchor = "center")
    arm_train6_label4.place(relx = 0.5, rely = 0.6, anchor = "center")
    arm_train6_label5.place(relx = 0.5, rely = 0.65, anchor = "center")
    arm_train6_label.place(relx = 0.5, rely = 0.1, anchor = "center")
    arm_train6_label2 = customtkinter.CTkLabel(master = window, text = "", 
                                                image = arm_exercise6)
    arm_train6_label2.place(relx = 0.5, rely = 0.3, anchor = "center")
    pause_button = customtkinter.CTkButton(master = window, text = "", 
                                           image = pause_button_img, 
                                           command = pause_menu, 
                                           width= 40, height= 40, 
                                           fg_color= constantesmp.COLOR_WHITE, 
                                           corner_radius= 0)
    pause_button.place(relx = 0.1, rely = 0.1, anchor = "center")
    arm_train6_button = customtkinter.CTkButton(master = window, 
                                                 text= "completado", 
                                                 command= arm_train7)
    arm_train6_button.place(relx =0.5 , rely=0.7 , anchor = "center")
    arm_train6_button2 = customtkinter.CTkButton(master = window, 
                                                  text= "Anterior", 
                                                  command= arm_train5)
    arm_train6_button2.place(relx =0.5 , rely=0.8 , anchor = "center")


def arm_train7():
    global previous_mode
    clean_window()
    previous_mode = "arm_train7"
    arm_train7_label =  customtkinter.CTkLabel(master=window,
                                                text = "Ejercicio #7 ",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 40))
    arm_train7_label2 = customtkinter.CTkLabel(master=window,
                                                text = "Aquí levantarás las mancuernas "
                                                       "al mismo tiempo.",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 10))
    arm_train7_label3 = customtkinter.CTkLabel(master=window,
                                                text = "Repeticiones: 10",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10, fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    arm_train7_label4 = customtkinter.CTkLabel(master=window,
                                                text = "Series: 3",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    arm_train7_label5 = customtkinter.CTkLabel(master=window,
                                                text = "Descanso entre series de 1 minuto",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    arm_train7_label2.place(relx = 0.5, rely = 0.5, anchor = "center")
    arm_train7_label3.place(relx = 0.5, rely = 0.55, anchor = "center")
    arm_train7_label4.place(relx = 0.5, rely = 0.6, anchor = "center")
    arm_train7_label5.place(relx = 0.5, rely = 0.65, anchor = "center")
    arm_train7_label.place(relx = 0.5, rely = 0.1, anchor = "center")
    arm_train7_label2 = customtkinter.CTkLabel(master = window, text = "",
                                                image = arm_exercise7)
    arm_train7_label2.place(relx = 0.5, rely = 0.3, anchor = "center")
    pause_button = customtkinter.CTkButton(master = window, text = "",
                                           image = pause_button_img,
                                           command = pause_menu,
                                           width= 40, height= 40,
                                           fg_color= constantesmp.COLOR_WHITE,
                                           corner_radius= 0)
    pause_button.place(relx = 0.1, rely = 0.1, anchor = "center")
    arm_train7_button = customtkinter.CTkButton(master = window,
                                                 text= "completado",
                                                 command= train_completed)
    arm_train7_button.place(relx =0.5 , rely=0.7 , anchor = "center")
    arm_train7_button2 = customtkinter.CTkButton(master = window,
                                                  text= "Anterior",
                                                  command= arm_train6)
    arm_train7_button2.place(relx =0.5 , rely=0.8 , anchor = "center")


def leg_train1():
    global previous_mode
    clean_window()
    previous_mode = "leg_train1"
    leg_train1_label =  customtkinter.CTkLabel(master=window,
                                                text = "Ejercicio #1 ",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 40))
    leg_train1_label2 = customtkinter.CTkLabel(master=window,
                                                text = "Hacer sentadillas "
                                                       "cargando con un "
                                                       "peso en brazos ",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 10))
    leg_train1_label3 = customtkinter.CTkLabel(master=window,
                                                text = "Repeticiones: 10",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10, fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    leg_train1_label4 = customtkinter.CTkLabel(master=window,
                                                text = "Series: 3",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    leg_train1_label5 = customtkinter.CTkLabel(master=window,
                                                text = "Descanso entre series de 1 minuto",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    leg_train1_label2.place(relx = 0.5, rely = 0.5, anchor = "center")
    leg_train1_label3.place(relx = 0.5, rely = 0.55, anchor = "center")
    leg_train1_label4.place(relx = 0.5, rely = 0.6, anchor = "center")
    leg_train1_label5.place(relx = 0.5, rely = 0.65, anchor = "center")
    leg_train1_label.place(relx = 0.5, rely = 0.1, anchor = "center")
    leg_train1_label2 = customtkinter.CTkLabel(master = window, text = "",
                                                image = leg_exercise1)
    leg_train1_label2.place(relx = 0.5, rely = 0.3, anchor = "center")
    pause_button = customtkinter.CTkButton(master = window, text = "",
                                           image = pause_button_img,
                                           command = pause_menu,
                                           width= 40, height= 40,
                                           fg_color= constantesmp.COLOR_WHITE,
                                           corner_radius= 0)
    pause_button.place(relx = 0.1, rely = 0.1, anchor = "center")
    leg_train1_button = customtkinter.CTkButton(master = window,
                                                 text= "completado",
                                                 command= leg_train2)
    leg_train1_button.place(relx =0.5 , rely=0.7 , anchor = "center")


def leg_train2():
    global previous_mode
    clean_window()
    previous_mode = "leg_train2"
    leg_train2_label =  customtkinter.CTkLabel(master=window,
                                                text = "Ejercicio #2 ",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 40))
    leg_train2_label2 = customtkinter.CTkLabel(master=window,
                                                text = "Este ejercicio es similar "
                                                       "a una sentadilla, pero "
                                                       "con un pie apoyado "
                                                       "en un soporte como "
                                                       "se muestra en la imagen",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 10))
    leg_train2_label3 = customtkinter.CTkLabel(master=window,
                                                text = "Repeticiones: 10",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10, fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    leg_train2_label4 = customtkinter.CTkLabel(master=window,
                                                text = "Series: 3",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    leg_train2_label5 = customtkinter.CTkLabel(master=window,
                                                text = "Descanso entre series de 1 minuto",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    leg_train2_label2.place(relx = 0.5, rely = 0.5, anchor = "center")
    leg_train2_label3.place(relx = 0.5, rely = 0.55, anchor = "center")
    leg_train2_label4.place(relx = 0.5, rely = 0.6, anchor = "center")
    leg_train2_label5.place(relx = 0.5, rely = 0.65, anchor = "center")
    leg_train2_label.place(relx = 0.5, rely = 0.1, anchor = "center")
    leg_train2_label2 = customtkinter.CTkLabel(master = window, text = "",
                                                image = leg_exercise2)
    leg_train2_label2.place(relx = 0.5, rely = 0.3, anchor = "center")
    pause_button = customtkinter.CTkButton(master = window, text = "",
                                           image = pause_button_img,
                                           command = pause_menu,
                                           width= 40, height= 40,
                                           fg_color= constantesmp.COLOR_WHITE,
                                           corner_radius= 0)
    pause_button.place(relx = 0.1, rely = 0.1, anchor = "center")
    leg_train2_button = customtkinter.CTkButton(master = window,
                                                 text= "completado",
                                                 command= leg_train3)
    leg_train2_button.place(relx =0.5 , rely=0.7 , anchor = "center")
    leg_train2_button2 = customtkinter.CTkButton(master = window,
                                                  text= "Anterior",
                                                  command= leg_train1)
    leg_train2_button2.place(relx =0.5 , rely=0.8 , anchor = "center")


def leg_train3():
    global previous_mode
    clean_window()
    previous_mode = "leg_train3"
    leg_train3_label =  customtkinter.CTkLabel(master=window,
                                                text = "Ejercicio #3 ",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 40))
    leg_train3_label2 = customtkinter.CTkLabel(master=window,
                                                text = "Con las piernas deberás "
                                                       "hacer fuerza para extenderlas "
                                                       "y empujar el peso que "
                                                       "evita que las extiendas",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 10))
    leg_train3_label3 = customtkinter.CTkLabel(master=window,
                                                text = "Repeticiones: 10",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    leg_train3_label4 = customtkinter.CTkLabel(master=window,
                                                text = "Series: 3",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    leg_train3_label5 = customtkinter.CTkLabel(master=window,
                                                text = "Descanso entre series de 1 minuto",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    leg_train3_label2.place(relx = 0.5, rely = 0.5, anchor = "center")
    leg_train3_label3.place(relx = 0.5, rely = 0.55, anchor = "center")
    leg_train3_label4.place(relx = 0.5, rely = 0.6, anchor = "center")
    leg_train3_label5.place(relx = 0.5, rely = 0.65, anchor = "center")
    leg_train3_label.place(relx = 0.5, rely = 0.1, anchor = "center")
    leg_train3_label2 = customtkinter.CTkLabel(master = window, text = "",
                                                image = leg_exercise3)
    leg_train3_label2.place(relx = 0.5, rely = 0.3, anchor = "center")
    pause_button = customtkinter.CTkButton(master = window, text = "",
                                           image = pause_button_img,
                                           command = pause_menu,
                                           width= 40, height= 40,
                                           fg_color= constantesmp.COLOR_WHITE,
                                           corner_radius= 0)
    pause_button.place(relx = 0.1, rely = 0.1, anchor = "center")
    leg_train3_button = customtkinter.CTkButton(master = window,
                                                 text= "completado",
                                                 command= leg_train4)
    leg_train3_button.place(relx =0.5 , rely=0.7 , anchor = "center")
    leg_train3_button2 = customtkinter.CTkButton(master = window,
                                                  text= "Anterior",
                                                  command= leg_train2)
    leg_train3_button2.place(relx =0.5 , rely=0.8 , anchor = "center")


def leg_train4():
    global previous_mode
    clean_window()
    previous_mode = "leg_train4"
    leg_train4_label =  customtkinter.CTkLabel(master=window,
                                                text = "Ejercicio #4 ",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 40))
    leg_train4_label2 = customtkinter.CTkLabel(master=window,
                                                text = "En este ejercicio deberás "
                                                       "empinarte mientras sostienes "
                                                       "peso para fortalecer las "
                                                       "pantorrillas",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 10))
    leg_train4_label3 = customtkinter.CTkLabel(master=window,
                                                text = "Repeticiones: 10",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    leg_train4_label4 = customtkinter.CTkLabel(master=window,
                                                text = "Series: 3",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    leg_train4_label5 = customtkinter.CTkLabel(master=window,
                                                text = "Descanso entre series de 1 minuto",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    leg_train4_label2.place(relx = 0.5, rely = 0.5, anchor = "center")
    leg_train4_label3.place(relx = 0.5, rely = 0.55, anchor = "center")
    leg_train4_label4.place(relx = 0.5, rely = 0.6, anchor = "center")
    leg_train4_label5.place(relx = 0.5, rely = 0.65, anchor = "center")
    leg_train4_label.place(relx = 0.5, rely = 0.1, anchor = "center")
    leg_train4_label2 = customtkinter.CTkLabel(master = window, text = "",
                                                image = leg_exercise4)
    leg_train4_label2.place(relx = 0.5, rely = 0.3, anchor = "center")
    pause_button = customtkinter.CTkButton(master = window, text = "",
                                           image = pause_button_img,
                                           command = pause_menu,
                                           width= 40, height= 40,
                                           fg_color= constantesmp.COLOR_WHITE,
                                           corner_radius= 0)
    pause_button.place(relx = 0.1, rely = 0.1, anchor = "center")
    leg_train4_button = customtkinter.CTkButton(master = window,
                                                 text= "completado",
                                                 command= leg_train5)
    leg_train4_button.place(relx =0.5 , rely=0.7 , anchor = "center")
    leg_train4_button2 = customtkinter.CTkButton(master = window,
                                                  text= "Anterior",
                                                  command= leg_train3)
    leg_train4_button2.place(relx =0.5 , rely=0.8 , anchor = "center")


def leg_train5():
    global previous_mode
    clean_window()
    previous_mode = "leg_train5"
    leg_train5_label =  customtkinter.CTkLabel(master=window,
                                                text = "Ejercicio #5 ",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 40))
    leg_train5_label2 = customtkinter.CTkLabel(master=window,
                                                text = "Haz fuerza con las piernas "
                                                       "hacia adentro para empujar "
                                                       "la maquina como se "
                                                       "muestra en la imagen.",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 10))
    leg_train5_label3 = customtkinter.CTkLabel(master=window,
                                                text = "Repeticiones: 10",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    leg_train5_label4 = customtkinter.CTkLabel(master=window,
                                                text = "Series: 3",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    leg_train5_label5 = customtkinter.CTkLabel(master=window,
                                                text = "Descanso entre series de 1 minuto",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    leg_train5_label2.place(relx = 0.5, rely = 0.5, anchor = "center")
    leg_train5_label3.place(relx = 0.5, rely = 0.55, anchor = "center")
    leg_train5_label4.place(relx = 0.5, rely = 0.6, anchor = "center")
    leg_train5_label5.place(relx = 0.5, rely = 0.65, anchor = "center")
    leg_train5_label.place(relx = 0.5, rely = 0.1, anchor = "center")
    leg_train5_label2 = customtkinter.CTkLabel(master = window, text = "",
                                                image = leg_exercise5)
    leg_train5_label2.place(relx = 0.5, rely = 0.3, anchor = "center")
    pause_button = customtkinter.CTkButton(master = window, text = "",
                                           image = pause_button_img,
                                           command = pause_menu,
                                           width= 40, height= 40,
                                           fg_color= constantesmp.COLOR_WHITE,
                                           corner_radius= 0)
    pause_button.place(relx = 0.1, rely = 0.1, anchor = "center")
    leg_train5_button = customtkinter.CTkButton(master = window,
                                                text= "completado",
                                                command= leg_train6)
    leg_train5_button.place(relx =0.5 , rely=0.7 , anchor = "center")
    leg_train5_button2 = customtkinter.CTkButton(master = window,
                                                text= "Anterior",
                                                command= leg_train4)
    leg_train5_button2.place(relx =0.5 , rely=0.8 , anchor = "center")


def leg_train6():
    global previous_mode
    clean_window()
    previous_mode = "leg_train6"
    leg_train6_label =  customtkinter.CTkLabel(master=window,
                                                text = "Ejercicio #6 ",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 40))
    leg_train6_label2 = customtkinter.CTkLabel(master=window,
                                                text = "en este ejercicio "
                                                       "estás acostado y tendrás "
                                                       "que contraer la  pierna "
                                                       "para cargar "
                                                       "el peso",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 10))
    leg_train6_label3 = customtkinter.CTkLabel(master=window,
                                                text = "Repeticiones: 10",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    leg_train6_label4 = customtkinter.CTkLabel(master=window,
                                                text = "Series: 3",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    leg_train6_label5 = customtkinter.CTkLabel(master=window,
                                                text = "Descanso entre series de 1 minuto",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    leg_train6_label2.place(relx = 0.5, rely = 0.5, anchor = "center")
    leg_train6_label3.place(relx = 0.5, rely = 0.55, anchor = "center")
    leg_train6_label4.place(relx = 0.5, rely = 0.6, anchor = "center")
    leg_train6_label5.place(relx = 0.5, rely = 0.65, anchor = "center")
    leg_train6_label.place(relx = 0.5, rely = 0.1, anchor = "center")
    leg_train6_label2 = customtkinter.CTkLabel(master = window, text = "",
                                                image = leg_exercise6)
    leg_train6_label2.place(relx = 0.5, rely = 0.3, anchor = "center")
    pause_button = customtkinter.CTkButton(master = window, text = "",
                                           image = pause_button_img,
                                           command = pause_menu,
                                           width= 40, height= 40,
                                           fg_color= constantesmp.COLOR_WHITE,
                                           corner_radius= 0)
    pause_button.place(relx = 0.1, rely = 0.1, anchor = "center")
    leg_train6_button = customtkinter.CTkButton(master = window,
                                                 text= "completado",
                                                 command= leg_train7)
    leg_train6_button.place(relx =0.5 , rely=0.7 , anchor = "center")
    leg_train6_button2 = customtkinter.CTkButton(master = window,
                                                  text= "Anterior",
                                                  command= leg_train5)
    leg_train6_button2.place(relx =0.5 , rely=0.8 , anchor = "center")


def leg_train7():
    global previous_mode
    clean_window()
    previous_mode = "leg_train7"
    leg_train7_label =  customtkinter.CTkLabel(master=window,
                                                text = "Ejercicio #7 ",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 40))
    leg_train7_label2 = customtkinter.CTkLabel(master=window,
                                                text = "Muy parecido a las sentadillas "
                                                       "con peso, aquí tienes que hacer "
                                                       "sentadilla cargando con una "
                                                       "barra en la espalda.",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 10))
    leg_train7_label3 = customtkinter.CTkLabel(master=window,
                                                text = "Repeticiones: 10",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10, 
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    leg_train7_label4 = customtkinter.CTkLabel(master=window,
                                                text = "Series: 3",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    leg_train7_label5 = customtkinter.CTkLabel(master=window,
                                                text = "Descanso entre series de 1 minuto",
                                                text_color= constantesmp.COLOR_BLACK,
                                                corner_radius= 10,
                                                fg_color= constantesmp.COLOR_WHITE,
                                                bg_color= constantesmp.COLOR_WHITE,
                                                width = 50, font= ("", 20))
    leg_train7_label2.place(relx = 0.5, rely = 0.5, anchor = "center")
    leg_train7_label3.place(relx = 0.5, rely = 0.55, anchor = "center")
    leg_train7_label4.place(relx = 0.5, rely = 0.6, anchor = "center")
    leg_train7_label5.place(relx = 0.5, rely = 0.65, anchor = "center")
    leg_train7_label.place(relx = 0.5, rely = 0.1, anchor = "center")
    leg_train7_label2 = customtkinter.CTkLabel(master = window, text = "",
                                                image = leg_exercise7)
    leg_train7_label2.place(relx = 0.5, rely = 0.3, anchor = "center")
    pause_button = customtkinter.CTkButton(master = window, text = "",
                                           image = pause_button_img,
                                           command = pause_menu,
                                           width= 40, height= 40,
                                           fg_color= constantesmp.COLOR_WHITE,
                                           corner_radius= 0)
    pause_button.place(relx = 0.1, rely = 0.1, anchor = "center")
    leg_train7_button = customtkinter.CTkButton(master = window,
                                                 text= "completado",
                                                 command= train_completed)
    leg_train7_button.place(relx =0.5 , rely=0.7 , anchor = "center")
    leg_train7_button2 = customtkinter.CTkButton(master = window,
                                                  text= "Anterior",
                                                  command= leg_train6)
    leg_train7_button2.place(relx =0.5 , rely=0.8 , anchor = "center")

register_screen()
window.mainloop()
