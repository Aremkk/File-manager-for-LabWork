import os
from importlib.resources import files
from tkinter import *
from tkinter import ttk, messagebox, filedialog
import  shutil

from IPython.utils.openpy import source_to_unicode
from bokeh.layouts import column

root = Tk()
root.geometry("600x600")
root.title("ФАЙМЕН")

label = ttk.Label(text="Я ФАЙМЕН! И я помогу тебе разобраться с содержимым этой помойки!", font=("Arial", 12), background="#FFCDD2")
label.pack()

ttk.Style().configure("TButton", font="helvetica 13", foreground="#004D40", padding=8, background="#B2DFDB")

icon = PhotoImage(file = "22.png")
root.iconphoto(False, icon)


def open_folder():
    dirr  = filedialog.askdirectory()
    file = Frame(root)
    file.pack(padx=20)
    listbox = Listbox(file, width=40)
    listbox.pack()
    files = os.listdir(dirr)
    for name in files:
        listbox.insert('end', name)
    exit_btn = Button(file, text='закрыть', bg='black', fg='white', command=file.destroy)
    exit_btn.pack()

def create_folder():
    global name_entry, dirr, file
    dirr = filedialog.askdirectory()
    file = Frame(root, background="white")
    file.pack()
    Label(file, text="Впиши название каталога", bg='white', font="bold").pack(padx=10, pady=10)
    name_entry = Entry(file, bd= 5)
    name_entry.pack()
    Button(file, text='Создать каталог', font="bold", bg='black', fg='white', command=makefolder).pack(padx=10, pady=10)
    Button(file, text = "Закрыть", bg="black", fg="white", font="bold", command=file.destroy).pack()
    file.mainloop()
def makefolder():
    name = name_entry.get()
    os.chdir(dirr)
    os.makedirs(name)
    file.destroy()
    messagebox.showinfo( "Созданный каталог", "Ещё один каталог в куче!")

def rename_folder():
    global entr_name, file, path
    dirr = filedialog.askdirectory()
    path = os.path.abspath(dirr)
    file = Frame(root, bg="white")
    file.pack()
    Label(file, text="Впиши новое имя каталога", bg="white", font='bold').pack(pady=10, padx=5)
    entr_name = Entry(file, bd=5)
    entr_name.pack()
    Button(file, text='Изменить имя', font='bold', bg='black', fg='white', command=new_name_fold).pack(padx=10, pady=10)
    Button(file, text='Закрыть',bg="black", fg="white", font="bold", command=file.destroy).pack()
def new_name_fold():
    new_name = entr_name.get()
    dir1 = os.path.dirname(path)
    renamed = os.path.join(dir1, new_name)
    os.rename(path, renamed)
    file.destroy()
    messagebox.showinfo('Измененный каталог',path + " с новым именем! ура!")

def delete_folder():
    kill = filedialog.askdirectory()
    os.rmdir(kill)
    messagebox.showinfo('Удаление','Неужели до этого дошло? И вполне успешно.')


def open_file():
    file = filedialog.askopenfilename()
    os.startfile(file)
    messagebox.showinfo("Файл","Работаем.")

def kill_file():
    file = filedialog.askopenfilename()
    os.remove(file)
    messagebox.showinfo("Удаление","Устройство стало чище!(ненадолго)")

def rename_file():
    global entr_name, file, path
    ff = filedialog.askopenfilename()
    path = os.path.abspath(ff)
    file = Frame(root, bg="white")
    file.pack()
    Label(file, text="Впиши новое имя файла", bg="white", font='bold').pack(pady=10, padx=5)
    entr_name = Entry(file, bd=5)
    entr_name.pack()
    Button(file, text='Изменить имя', font='bold', bg='black', fg='white', command=new_name_file).pack(padx=10, pady=10)
    Button(file, text='Закрыть', bg="black", fg="white", font="bold", command=file.destroy).pack()

def new_name_file():
    new_name = entr_name.get()
    dir1 = os.path.dirname(path)
    renamed = os.path.join(dir1, new_name)
    os.rename(path, renamed)
    file.destroy()
    messagebox.showinfo('Измененный файл', path + " с новым именем! ура?..")

def copy_move_file():
    global sourceText, destinationText, destination_location, f1
    f1 = Frame(root, bg="white")
    f1.pack()

    sourceText = []
    destinationText = []
    source_location = StringVar()
    destination_location = StringVar()

    link_label = Label(f1, text="Выбери файл для копирования", font="bold", bg="white")
    link_label.pack()

    src_text = Entry(f1, textvariable= source_location, font="bold")
    src_text.pack()

    src_button = Button(f1, text="Обзор...", command=browser, bg="black", fg="white")
    src_button.pack(padx=100)

    dest_label = Label(f1, text="Выбери путь", bg="white", font="bold")
    dest_label.pack(pady=10)

    dest_text = Entry(f1, textvariable=destination_location, font="bold")
    dest_text.pack()

    dest_button = Button(f1, text="Обзор...", command=browser_dest, bg="black", fg="white")
    dest_button.pack()

    copy_button = Button(f1, text="Копи", command= copyf, font="bold",width=5)
    copy_button.pack()
    move_button = Button(f1, text="Перем", command=movef, font="bold", width=5)
    move_button.pack()
    can_button = Button(f1, text="Закр", command=f1.destroy, font="bold", width=5)
    can_button.pack()

def browser():
    global files_list
    files_list = list(filedialog.askopenfilename())
    sourceText.insert(1, files_list)

def browser_dest():
    dest_dir = filedialog.askdirectory()
    destinationText.insert(1, dest_dir)

def copyf():
    dest_loc = destination_location.get()
    for f in files_list:
        shutil.copy(f, dest_loc)
    messagebox.showinfo("Оно работает..","Отлично скопировано")
    f1.destroy()

def movef():
    dest_loc = destination_location.get()
    for file in files_list:
        shutil.move(file, dest_loc)
    messagebox.showinfo("Оно работает..","Перемещено!")
    f1.destroy()


open_fold = ttk.Button(text="Открыть каталог", command=open_folder, cursor="diamond_cross")
open_fold.place(x=40, y=220)

create_fold = ttk.Button(text="Создать каталог", command=create_folder, cursor="diamond_cross")
create_fold.place(x=200, y=220)

rename_fold = ttk.Button(text="Переименовать каталог", command=rename_folder, cursor="diamond_cross")
rename_fold.place(x=360, y=220)

del_fold = ttk.Button(text="Удалить каталог", command=delete_folder, cursor="diamond_cross")
del_fold.place(x=40, y=270)

op_file = ttk.Button(text="  Открыть файл ", command=open_file, cursor="diamond_cross")
op_file.place(x=200, y=270)

ren_file = ttk.Button(text="  Переименовать файл  ", command=rename_file, cursor="diamond_cross")
ren_file.place(x=360, y=270)

del_file = ttk.Button(text="  Удалить файл ", command=kill_file, cursor="diamond_cross")
del_file.place(x=40, y=320)

del_file = ttk.Button(text="Скопировать/переместить файл", command=copy_move_file, cursor="diamond_cross")
del_file.place(x=200, y=320)


root.mainloop()