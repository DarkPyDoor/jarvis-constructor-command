import customtkinter

phrases_list = []

customtkinter.set_default_color_theme("dark-blue")

def add_directory():
    global code_success
    code_success += f"os.startfile('{directory_entry.get()}')\n"

def add_site():
    global code_success
    code_success += f"os.system('{site_entry.get()}')\n"

def add_timer():
    global code_success
    code_success += f"time.sleep('{timergt_entry.get()}')\n"

def delete_command(command):
    global code_success
    code_success = code_success.replace(command, "")

def extract():
    command_text = f"""
- command:
    action: ahk
    exe_path: ahk/{name_file_entry.get()}.py
    exe_args:
  voice:
    sounds:
    - ok1
    - ok2
    - ok3
  phrases:
  - {phrase_entry.get()}
    """
    with open("C:\\Program Files\\jarvis-app\\commands\\constructor-commands\\command.yaml", "a") as file:
        file.write(command_text)
    with open(f"C:\\Program Files\\jarvis-app\\commands\\constructor-commands\\ahk\\{name_file_entry.get()}.py", "w") as py_file:
        py_file.write(code_success)
    messagebox.showinfo("Succes", "Команда успешно создана")

root = customtkinter.CTk()

name_file_label = customtkinter.CTkLabel(root, text="Имя команды (должно быть уникальным, на английском):")
name_file_entry = customtkinter.CTkEntry(root)
name_file_entry.insert(0, "Пример: run_firefox")

directory_label = customtkinter.CTkLabel(root, text="Директория дла запуска приложения")
directory_frame = customtkinter.CTkFrame(root)
directory_entry = customtkinter.CTkEntry(directory_frame)
directory_entry.insert(0, "Пример: C:\Program Files\Mozilla Firefox\firefox.exe")
directory_add_button = customtkinter.CTkButton(directory_frame, text="Add", width=5, command=add_directory)
directory_delete_button = customtkinter.CTkButton(directory_frame, text="X", width=3, command=lambda: delete_command(f"os.startfile({directory_entry.get()})\n"))

site_label = customtkinter.CTkLabel(root, text="Ссылку дла запуска сайта")
site_frame = customtkinter.CTkFrame(root)
site_entry = customtkinter.CTkEntry(site_frame)
site_entry.insert(0, "Пример: https://yandex.kz/")
site_add_button = customtkinter.CTkButton(site_frame, text="Add", width=5, command=add_site)
site_delete_button = customtkinter.CTkButton(site_frame, text="X", width=3, command=lambda: delete_command(f"os.system({site_entry.get()})\n"))

phrase_label = customtkinter.CTkLabel(root, text="Какое слово/фразу нужно сказать для запуска:")
phrase_entry = customtkinter.CTkEntry(root)
phrase_entry.insert(0, "Пример: Запуски браузер файерфокс")
phrase_add_button = customtkinter.CTkButton(root, text="Add", width=5, command=lambda: phrases_list.insert(len(phrases_list), phrase_entry.get()))
phrase_delete_button = customtkinter.CTkButton(root, text="X", width=3, command=lambda: phrases_list.remove(phrase_entry.get()))

timergt_label = customtkinter.CTkLabel(root, text="Timer - Время которое команда будет бездействовать.(в секундах)")
timergt_frame = customtkinter.CTkFrame(root)
timergt_entry = customtkinter.CTkEntry(timergt_frame)
timergt_entry.insert(0, "Пример: 5")
timergt_add_button = customtkinter.CTkButton(timergt_frame, text="Add", width=5, command=add_timer)
timergt_delete_button = customtkinter.CTkButton(timergt_frame, text="X", width=3, command=lambda: delete_command(f"time.sleep({timergt_entry.get()})\n"))

extract_button = customtkinter.CTkButton(root, text="Extract", command=extract)

name_file_label.pack()
name_file_entry.pack()

directory_label.pack()
directory_frame.pack()
directory_entry.pack()
directory_add_button.pack()
directory_delete_button.pack()

site_label.pack()
site_frame.pack()
site_entry.pack()
site_add_button.pack()
site_delete_button.pack()

phrase_label.pack()
phrase_entry.pack()
phrase_add_button.pack()
phrase_delete_button.pack()

timergt_label.pack()
timergt_frame.pack()
timergt_entry.pack()
timergt_add_button.pack()
timergt_delete_button.pack()

extract_button.pack()

code_success = "import os\nimport time\n\n"

root.mainloop()
