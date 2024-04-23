import customtkinter as ctk
import threading
import notifications as nf
from tkinter import messagebox
import os


# Checking the notes file to  be uses to save the notes.
notes_file = "Notes.txt"
if not os.path.exists(notes_file):
    with open(notes_file, 'w') as file:
        pass

# Checking file for to-do list.
todo_file = "to_do_list.txt"
if not os.path.exists(todo_file):
    with open(todo_file, 'w') as todo:
        pass

# Checking Notification file.
daily_notif = "DailyNotify.txt"
regular_notif = "RegularNotif.txt"
if not os.path.exists(daily_notif):
    with open(daily_notif, 'w') as daily:
        pass
if not os.path.exists(regular_notif):
    with open(regular_notif, 'w') as daily:
        pass

# Message box to confirm on quitting.
def on_closing():
    if messagebox.askyesno(title='Quit?', message='Do you really want to quit?'):
        window.destroy()

# Function to clear the display frame to change the ui.
def clear_frame():
    for widget in display.winfo_children():
        widget.destroy()
        
# Function for the Notification button.
def open_notification():
    clear_frame()
    notification_label = ctk.CTkLabel(display, text="All Notifications", font=('Arial', 18))
    notification_label.place(x=237.5, y=20)
    text_lable = ctk.CTkLabel(display, text="No Notifications Yet!", font=('Arial', 50), text_color='#B1B3B4')
    text_lable.place(relx=0.5, rely=0.5, anchor="center")

# Function for the to-do list button.
def display_todo_list():
    clear_frame()
    todo_label = ctk.CTkLabel(display, text="To-Do List", font=('Arial', 18))
    todo_label.place(x=237.5, y=20)
    with open(todo_file, "r") as file:
        content = file.read()

        with open(todo_file, "r") as file:
            content = file.read()

        todo_content = [todo.strip() for todo in content.split("\n\n") if todo.strip()]

    back = ctk.CTkButton(display, text= '\u2190 Back', width=50, height=20, font=('Arial', 12), command=add_to_do)
    back.place(x=10, y=5)
    if todo_content:
        for index, todo in enumerate(todo_content):
            todo_preview = todo[:20]

            todo_btn = ctk.CTkButton(display, text=f"List {index + 1}: {todo_preview}...", width=150, height=40, font=('Arial', 12), command= lambda t=todo: open_todo(t))
            todo_btn.place(x=50, y=index* 50 + 50)
            del_btn = ctk.CTkButton(display, text="Delete.", font=('Arial', 10), command= lambda id=index: del_todo(id))
            del_btn.place(x=300, y=index* 50 + 50)
            
    else:
        empty_lable =  ctk.CTkLabel(display, text="No List Created!", font=('Arial', 50), text_color='#B1B3B4')
        empty_lable.place(relx=0.5, rely=0.5, anchor="center")

# Creating Function to open to-do list from the all list.
def open_todo(todo_content):
    clear_frame()
    todo_lable = ctk.CTkLabel(display, text="To-Do list", font=('Arial', 18))
    todo_lable.place(x=237.5, y=20)
    todo_text = ctk.CTkLabel(display, text=todo_content,height=400, width=550, font=('Arial', 16), wraplength=500)
    todo_text.place(x=10, y=60)
   
# Function to Delete the to-do list.
def del_todo(index):
    with open(todo_file, 'r') as file:
        all_list = file.read().strip().split("\n\n")
        del all_list[index]
    with open(todo_file, 'w') as file:
        if all_list:
            file.write("\n\n".join(all_list))
        else:
            file.write("")
    display_todo_list()

# GUI for the add notification button and functionality. 
def add_notification():
    clear_frame()
    global interval_label
    todo_label = ctk.CTkLabel(display, text="Add New Notificaton", font=('Arial', 18))
    todo_label.place(x=237.5, y=20)
    title_lable = ctk.CTkLabel(display, text="Title :- ", font=('Arial',16))
    title_lable.place(x=15, y=78)
    title = ctk.CTkEntry(display, width=200, height=20, placeholder_text="Enter title for the Notification")
    title.place(x=100 , y=80)
    interval = ctk.CTkSlider(display, width=300, height=20, from_=1, to=60, number_of_steps=59, button_hover_color="Green", command=update_interval)
    interval.place(x=100, y= 150)
    interval_label = ctk.CTkLabel(display, text=f"Repeat: {interval.get()} min's.", font=('Arial', 16), text_color="#4EAD51")
    interval_label.place(x=440, y=148)
    daily = ctk.StringVar(value="Regular")
    radio1 = ctk.CTkRadioButton(display, text="Daily", border_width_checked=5, border_width_unchecked=2, variable=daily, value="Daily")
    radio1.place(x=100, y= 200)
    radio2 = ctk.CTkRadioButton(display, text="Regular Interval", border_width_checked=5, border_width_unchecked=2, variable=daily, value="Regular")
    radio2.place(x=200, y=200)
    body = ctk.CTkLabel(display, text="Notification\nMessage: ", font=('Arial', 16))
    body.place(x=15, y=334)
    noti_body = ctk.CTkTextbox(display, width=300, height=200, corner_radius=30)
    noti_body.place(x=100, y=250)
    save_notification = ctk.CTkButton(display, text="Save!", height=40, width=100, font=('Arial', 12), command=lambda: save_notify(title.get(),noti_body.get("1.0", "end-1c"),daily.get(),interval.get() if daily=="Regular" else None))
    save_notification.place(x=215, y=500)
    
# Updating notification timer interval.
def update_interval(value):
    interval_label.configure(text=f"Repeat: {int(value)} min's.")

# Saving New Notifications.
def save_notify(title,message,daily,interval):
    if daily == "Daily":
        with open(daily_notif, 'a') as daily:
            daily.write(f"{title} | {message}\n")
        clear_frame()
        add_notification()
        messagebox.showinfo(title="Saved!", message="Notification Saved!")

    elif daily == "Regular":
        with open(regular_notif, 'a') as regular:
            regular.write(f"{title} | {interval} | {message}\n")
        clear_frame()
        add_notification()
        messagebox.showinfo(title="Saved!", message="Notification Saved!")
    


# UI and functionality for the add to-do list.
def add_to_do():
    global text_add_todo
    clear_frame()
    add_todo_label = ctk.CTkLabel(display, text="Add To Do Task", font=('Arial', 18))
    add_todo_label.place(x=237.5, y=20)
    text_add_todo = ctk.CTkTextbox(display, height=400, width=550, font=('Arial', 16), corner_radius=30)
    text_add_todo.place(x=10, y=60)
    add_todobtn = ctk.CTkButton(display, text='Add Task',  height=40, width=100, font=('Arial', 12), command=save_todo)
    add_todobtn.place(x=237.5, y=500)

# Notes button functionality
def notes_list():
    clear_frame()
    notes_lable_label = ctk.CTkLabel(display, text="Notes", font=('Arial', 16))
    notes_lable_label.place(x=237.5, y=10)
    all_notes = ctk.CTkButton(display, text='All Notes', height=40, width=100, font=('Arial', 12), command=display_notes)
    all_notes.place(x=10,y=36)
    new_note = ctk.CTkButton(display, text='New Note', height=40, width=100, font=('Arial', 12), command=new_note1)
    new_note.place(x=10,y=86)

# Defining functionality for the New Note button.
def new_note1():
    global newnote_text
    clear_frame()
    back = ctk.CTkButton(display, text= '\u2190 Back', width=50, height=20, font=('Arial', 12), command=notes_list)
    back.place(x=10, y=5)
    new_note_lable = ctk.CTkLabel(display, text="Add New Notes", font=('Arial', 16))
    new_note_lable.place(x=237.5, y=10)
    newnote_text = ctk.CTkTextbox(display, height=400, width=550, font=('Arial', 16), corner_radius=30)
    newnote_text.place(x=10, y=60)
    savebtn = ctk.CTkButton(display, text='Save', height=40, width=100, font=('Arial', 12), command=save_notes)
    savebtn.place(x=237.5, y=500)

# Saving the notes to the notes file.
def save_notes():
    global newnote_text
    note_text= newnote_text.get("1.0", "end-1c")
    if note_text:
        with open(notes_file, "a") as file:
            file.write(note_text + "\n\n")
            clear_frame()
            messagebox.showinfo(title="Done", message="Your note is saved")
            new_note1()
    if not note_text:
        messagebox.showerror(title="Empty!", message="Please type something to save.")

# For the home page save note button.
def save_note_h():
    note1 = text1.get("1.0", "end-1c")
    if note1:
        with open(notes_file, "a") as file:
            file.write(note1 + "\n\n")
            clear_frame()
            new_note1()
            messagebox.showinfo(title="Done", message="Saved!")

    if not note1:
        messagebox.showinfo(title="Empty!", message="Nothing to save, please type something.")

# Displaying notes in the display frame.
def display_notes():
    clear_frame()
    with open(notes_file, "r") as file:
        content = file.read()
        notes = content.split("\n\n")

        # Removeing any leading or trailing whitespace from each note and filter out empty notes
        all_notes = [note.strip() for note in notes if note.strip()]

    back = ctk.CTkButton(display, text= '\u2190 Back', width=50, height=20, font=('Arial', 12), command=notes_list)
    back.place(x=10, y=5)
    
    if all_notes:
        for index, note in enumerate(all_notes):
            # The length of note for display.
            note_preview = note[:20]
             
            # Displaying the note on the button.
            note_button = ctk.CTkButton(display, text=f"Note {index+1}: {note_preview}...", width=150, height=40,
                                         font=('Arial', 12), command=lambda n=note: open_note(n))
            note_button.place(x=50, y=index * 50 + 50)
            delete_button = ctk.CTkButton(display, text="Delete!", width=50, height=30, font=('Arial', 10), command=lambda id=index: delete_note(id))
            delete_button.place(x=300, y= index * 50 + 60)
    else:
        clear_frame()
        notes_label = ctk.CTkLabel(display, text="No Notes Saved", font=('Arial', 50), text_color="#B1B3B4")
        notes_label.place(relx=0.5, rely=0.5, anchor="center")


# Defining a function to open the note on display.
def open_note(note_content):
    clear_frame()
    note_label = ctk.CTkLabel(display, text="Note Content", font=('Arial', 18))
    note_label.place(x=237.5, y=20)
    note_text = ctk.CTkLabel(display, text=note_content, height=400, width=550, font=('Arial', 16), wraplength=500)
    note_text.place(x=10, y=60)

# Deleting a note.
def delete_note(index):
    with open(notes_file, "r") as file:
        all_notes = file.read().strip().split("\n\n")
    del all_notes[index]
    with open(notes_file, "w") as file:
        if all_notes:
            file.write("\n\n".join(all_notes))
        else:
            file.write("")
    display_notes()

# Save to-do list.
def save_todo():
    global text_add_todo
    todo_text = text_add_todo.get("1.0", "end-1c")
    if todo_text:
        with open(todo_file, "a") as file:
            file.write(todo_text + "\n\n")
            clear_frame()
            add_to_do()
            messagebox.showinfo(title="Done!", message="Saved!")
    else:
        messagebox.showerror(title="Empty", message="Nothing to save!")

# Main window ui.
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

window = ctk.CTk()
window.geometry("800x600")
window.maxsize(800, 600)
window.title("Utility Centre")


# Saperate frame for the buttons in menu.
frame_menu = ctk.CTkFrame(window, width=200, height=550)
frame_menu.place(x=10, y=40)

# Saperate frame for the display and button functionality.
display = ctk.CTkFrame(window, width=575, height=550)
display.place(x=220, y=40)

lable = ctk.CTkLabel(window, text='Utility Centre', font=('Arial', 18), text_color='#24A91C')
lable.pack(pady=10, padx=20)

note_lable = ctk.CTkLabel(display, text='Create Note', width=100, font=('Arial', 20))
note_lable.place(x=237.5, y=20)

text1 = ctk.CTkTextbox(display, height=400, width=550, font=('Arial', 12), corner_radius=30)
text1.place(x=10, y=60)

save_note =ctk.CTkButton(display, text='Save Note', height=40, width=100, font=('Arial', 12), command= save_note_h)
save_note.place(x=237.5, y=500)

frame_lable = ctk.CTkLabel(frame_menu, text='MENU', font=('Arial', 16))
frame_lable.place(x=70, y=10)

notf_button = ctk.CTkButton(frame_menu, width=150, height= 50, text='Notifications', font=('Arial', 12), command=open_notification)
notf_button.place(x=25, y=40)

add_notif = ctk.CTkButton(frame_menu, text='Add Notification', width=150, height= 50, font=('Arial', 12), command=add_notification)
add_notif.place(x=25, y=100)

todo = ctk.CTkButton(frame_menu, text='To-Do List', width=150, height= 50, font=('Arial', 12), command=display_todo_list)
todo.place(x=25, y=160)

add_todo = ctk.CTkButton(frame_menu, text='Add To-Do Task', width=150, height= 50, font=('Arial', 12), command=add_to_do)
add_todo.place(x=25, y=220)

notes = ctk.CTkButton(frame_menu, text='Notes', width=150, height=50, font=('Arial', 12), command=notes_list)
notes.place(x=25, y=280)

window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()