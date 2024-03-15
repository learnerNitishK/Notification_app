import tkinter as tk
import threading
import notification as nf
from tkinter import messagebox

def start_notification():
    threading.Thread(target=nf.notif).start()

def on_closing():
    if messagebox.askyesno(title='Quit?', message='Do you really want to quit?'):
        window.destroy()

window = tk.Tk()
window.configure(bg="lightblue")
window.geometry("800x600")
window.title("Notification centre")

notification = tk.Button(window, text="Notification's", font=('Arial', 12), command=start_notification)
notification.place(x=10, y=40)

lable = tk.Label(window, text="Home", font=('Arial', 18))
lable.pack(padx=5, pady=5)

text1 = tk.Text(window, height=5, font=('Arial', 12))
text1.pack(padx=5, pady=80)

save = tk.Button(window, text="Save Task", font=('Areal', 12))
save.pack(padx=5, pady=10)

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()