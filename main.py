import customtkinter as ctk
import threading
import notification as nf
from tkinter import messagebox

def on_closing():
    if messagebox.askyesno(title='Quit?', message='Do you really want to quit?'):
        window.destroy()

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

window = ctk.CTk()
window.geometry("800x600")
window.title("Notification Centre")

frame_menu = ctk.CTkFrame(window, width=200, height=550)
frame_menu.place(x=10, y=40)

display = ctk.CTkFrame(window, width=575, height=550)
display.place(x=220, y=40)

lable = ctk.CTkLabel(window, text='Notification Centre', font=('Areal', 18))
lable.pack(pady=10, padx=20)

text1 = ctk.CTkTextbox(display, height=400, width=550, font=('Areal', 12), corner_radius=30)
text1.place(x=10, y=10)

frame_lable = ctk.CTkLabel(frame_menu, text='MENU', font=('Areal', 16))
frame_lable.place(x=70, y=10)

notf_button = ctk.CTkButton(frame_menu, width=150, height= 50, text='Notifications', font=('Areal', 12))
notf_button.place(x=25, y=40)

add_notif = ctk.CTkButton(frame_menu, text='Add Notification', width=150, height= 50, font=('Areal', 12))
add_notif.place(x=25, y=100)

todo = ctk.CTkButton(frame_menu, text='To-Do List', width=150, height= 50, font=('Areal', 12))
todo.place(x=25, y=160)

add_todo = ctk.CTkButton(frame_menu, text='Add To-Do Task', width=150, height= 50, font=('Areal', 12))
add_todo.place(x=25, y=220)


window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()