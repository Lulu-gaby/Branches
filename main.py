import tkinter as tk

def user_name():
    user_input = entry.get()
    label.config(text=f"Привет, {user_input}!")


root = tk.Tk()
root.title("Бла бла")

label = tk.Label(root,text = "Введите имя:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text = "Давай знакомиться!", command=user_name)
button.pack()


root.mainloop()
