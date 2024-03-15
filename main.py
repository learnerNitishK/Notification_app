import tkinter as tk

window = tk.Tk()
window.configure(bg="lightblue")
window.geometry("800x600")
window.title("Notification centre")

notification = tk.Button(window, text="Notification's", font=('Arial', 12))
notification.place(x=10, y=40)

lable = tk.Label(window, text="Home", font=('Arial', 18))
lable.pack(padx=5, pady=5)

text1 = tk.Text(window, height=5, font=('Arial', 12))
text1.pack(padx=5, pady=80)

save = tk.Button(window, text="Save Task", font=('Areal', 12))
save.pack(padx=5, pady=10)


window.mainloop()