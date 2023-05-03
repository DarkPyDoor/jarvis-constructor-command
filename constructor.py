import tkinter as tk

def extract_data():
    name_file = name_file_entry.get()
    directory = directory_entry.get()
    phrase1 = phrase1_entry.get()
    phrase2 = phrase2_entry.get()
    phrase3 = phrase3_entry.get()
    phrase4 = phrase4_entry.get()

    path = "C:/Program Files/jarvis-app/commands/constructor-commands"

    # create commands.yaml
    with open(f"{path}/command.yaml", "a+", encoding='utf-8') as file:
        file.write(f"""
\n
- command:
    action: ahk
    exe_path: ahk/{name_file}.bat
    exe_args:
  voice:
    sounds:
    - ok1
    - ok2
    - ok3
  phrases:
  - {phrase1}
  - {phrase2}
  - {phrase3}
  - {phrase4}

""")

    # create ahk folder
    import os
    try:
        os.mkdir(f"{path}/ahk")
    except:
        pass

    # create ahk file
    with open(f"{path}/ahk/{name_file}.bat", "w") as file:
        file.write(f"start {directory}")

    # show success message
    tk.messagebox.showinfo("Success", "Restart to Jarvis.")

# create main window
root = tk.Tk()
root.title("Constructor Jarvis")

# create label and text entry
name_file_label = tk.Label(root, text="Имя команды (должно быть уникальным, на английском):")
name_file_entry = tk.Entry(root)

directory_label = tk.Label(root, text="Директория/ссылка дла запуска приложения/сайта:")
directory_entry = tk.Entry(root)
directory2_label = tk.Label(root, text="Пример: C:\Program Files\Mozilla Firefox\firefox.exe")

phrase1_label = tk.Label(root, text="Какое слово/фразу нужно сказать для запуска:")
phrase1_entry = tk.Entry(root)

phrase2_label = tk.Label(root, text="Какое слово/фразу нужно сказать для запуска:")
phrase2_entry = tk.Entry(root)

phrase3_label = tk.Label(root, text="Какое слово/фразу нужно сказать для запуска:")
phrase3_entry = tk.Entry(root)

phrase4_label = tk.Label(root, text="Какое слово/фразу нужно сказать для запуска:")
phrase4_entry = tk.Entry(root)

# create extract button
extract_button = tk.Button(root, text="Extract", command=extract_data)

# add to window
name_file_label.grid(row=0, column=0)
name_file_entry.grid(row=0, column=1)

directory_label.grid(row=1, column=0)
directory_entry.grid(row=1, column=1)

phrase1_label.grid(row=2, column=0)
phrase1_entry.grid(row=2, column=1)

phrase2_label.grid(row=3, column=0)
phrase2_entry.grid(row=3, column=1)

phrase3_label.grid(row=4, column=0)
phrase3_entry.grid(row=4, column=1)

phrase4_label.grid(row=5, column=0)
phrase4_entry.grid(row=5, column=1)

extract_button.grid(row=6, column=1)

# run main loop
root.mainloop()