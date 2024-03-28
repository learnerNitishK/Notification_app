import customtkinter as ctk
import threading
import notifications as nf
from tkinter import messagebox
import json

#  Saving the notes file to  be uses to save the notes.
notes = "notes.json"

#  Creating a notes dictonary to saperately save the notes.
notes_dict = {}

#  Message box to confirm on quitting.
def on_closing():
    if messagebox.askyesno(title='Quit?', message='Do you really want to quit?'):
        window.destroy()

#  Creating function to clear the display frame to change the ui.
def clear_frame():
    for widget in display.winfo_children():
        widget.destroy()
        
#  Function for the Notification button.
def open_notification():
    clear_frame()
    notification_label = ctk.CTkLabel(display, text="Notifications", font=('Arial', 18))
    notification_label.place(x=237.5, y=20)

#  Function for the to-do list button.
def open_todo_list():
    clear_frame()
    todo_label = ctk.CTkLabel(display, text="To-Do List", font=('Arial', 18))
    todo_label.place(x=237.5, y=20)

#  Creating ui for the add notification button and functionality. 
def add_notification():
    clear_frame()
    todo_label = ctk.CTkLabel(display, text="Add new Notificaton", font=('Arial', 18))
    todo_label.place(x=237.5, y=20)
    text_add = ctk.CTkTextbox(display, height=400, width=550, font=('Areal', 16), corner_radius=30)
    text_add.place(x=10, y=60)
    addbtn = ctk.CTkButton(display, text='Add Notification',  height=40, width=100, font=('Areal', 12))
    addbtn.place(x=237.5, y=500)

#  UI and functionality for the add to-do list.
def add_to_do():
    clear_frame()
    add_todo_label = ctk.CTkLabel(display, text="Add To Do Task", font=('Arial', 18))
    add_todo_label.place(x=237.5, y=20)
    text_add_todo = ctk.CTkTextbox(display, height=400, width=550, font=('Areal', 16), corner_radius=30)
    text_add_todo.place(x=10, y=60)
    add_todobtn = ctk.CTkButton(display, text='Add Task',  height=40, width=100, font=('Areal', 12))
    add_todobtn.place(x=237.5, y=500)

#  Notes button functionality
def notes_list():
    clear_frame()
    notes_lable_label = ctk.CTkLabel(display, text="Notes", font=('Arial', 16))
    notes_lable_label.place(x=237.5, y=10)
    all_notes = ctk.CTkButton(display, text='All Notes', height=40, width=100, font=('Areal', 12), command=allnotebtn)
    all_notes.place(x=10,y=36)
    new_note = ctk.CTkButton(display, text='New Note', height=40, width=100, font=('Areal', 12), command=new_note1)
    new_note.place(x=10,y=86)

#  Functionality for the all notes button.
def allnotebtn():
    clear_frame()
    allnotes_lable_label = ctk.CTkLabel(display, text="All Notes", font=('Arial', 16))
    allnotes_lable_label.place(x=237.5, y=10)

#  Defining functionality for the New Note button.
def new_note1():
    clear_frame()
    new_note_lable = ctk.CTkLabel(display, text="Add New Notes", font=('Arial', 16))
    new_note_lable.place(x=237.5, y=10)
    newnote_text = ctk.CTkTextbox(display, height=400, width=550, font=('Areal', 16), corner_radius=30)
    newnote_text.place(x=10, y=60)
    savebtn = ctk.CTkButton(display, text='Save', height=40, width=100, font=('Areal', 12), command=save_notes)
    savebtn.place(x=237.5, y=500)

#  Saving the notes from the dictonary to the notes file.
def save_notes():
    with open(notes, "w") as f:
        json.dump(notes_dict, f)   

#  Main window ui.
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

window = ctk.CTk()
window.geometry("800x600")
window.maxsize(820, 620)
window.title("Notification Centre")

#  Saperate frame for the buttons in menu.
frame_menu = ctk.CTkFrame(window, width=200, height=550)
frame_menu.place(x=10, y=40)

#  Saperate frame for the display and button functionality.
display = ctk.CTkFrame(window, width=575, height=550)
display.place(x=220, y=40)

lable = ctk.CTkLabel(window, text='Notification Centre', font=('Areal', 18))
lable.pack(pady=10, padx=20)

note_lable = ctk.CTkLabel(display, text='Create Note', width=100, font=('Areal', 20))
note_lable.place(x=237.5, y=20)

text1 = ctk.CTkTextbox(display, height=400, width=550, font=('Areal', 12), corner_radius=30)
text1.place(x=10, y=60)

save_notes =ctk.CTkButton(display, text='Save Note', height=40, width=100, font=('Areal', 12))
save_notes.place(x=237.5, y=500)

frame_lable = ctk.CTkLabel(frame_menu, text='MENU', font=('Areal', 16))
frame_lable.place(x=70, y=10)

notf_button = ctk.CTkButton(frame_menu, width=150, height= 50, text='Notifications', font=('Areal', 12), command=open_notification)
notf_button.place(x=25, y=40)

add_notif = ctk.CTkButton(frame_menu, text='Add Notification', width=150, height= 50, font=('Areal', 12), command=add_notification)
add_notif.place(x=25, y=100)

todo = ctk.CTkButton(frame_menu, text='To-Do List', width=150, height= 50, font=('Areal', 12), command=open_todo_list)
todo.place(x=25, y=160)

add_todo = ctk.CTkButton(frame_menu, text='Add To-Do Task', width=150, height= 50, font=('Areal', 12), command=add_to_do)
add_todo.place(x=25, y=220)

notes = ctk.CTkButton(frame_menu, text='Notes', width=150, height=50, font=('Areal', 12), command=notes_list)
notes.place(x=25, y=280)

window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()