import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
from os import listdir, getcwd
from os.path import isfile, join
from subprocess import call
import shutil
pathload = getcwd()
onlyfiles = [f for f in listdir(pathload) if isfile(join(pathload, f))]
page = 0
folder_selected = ""
def choose_folder():
    global folder_selected, lbl
    folder_selected = filedialog.askdirectory()
    lbl.delete(1.0, 'end')
    lbl.insert("end", " Выбери путь становления Русовъ \n Выбранный путь >> " + folder_selected)
def change_background():
    global page, image_font, font, root, lbl, button, folder_selected, button2
    if folder_selected == "":
        return 0
    page+=1
    lbl.delete(1.0, 'end')
    if page == 1:
        lbl.insert(1.0, " Для сражения требуется установленный ящеръ!\n Убедись что ящеръ установленъ!")
        button2.place_forget()
    if page == 2:
        button.configure(text="Завершить")
        lbl.insert(1.0, "Помоги славянамъ одолеть злыхъ ящеровъ съ силой В++")
    if page == 3:
        for i in onlyfiles:
            print(pathload+"\\"+i, folder_selected)
            shutil.copyfile(pathload+"\\"+i, folder_selected+"\\"+i)
        call("pip.exe install subprocess.run")
        call("pip.exe install pyinstaller")
        print("pyinstaller.exe --icon=program.ico -F " + folder_selected+"\\"+"translator.py")
        call("pyinstaller.exe --icon="+folder_selected+"\\program.ico -F " + folder_selected+"\\"+"translator.py --distpath "+folder_selected+"\\")
        call(folder_selected+"\\translator.exe программушка.B++")
        exit(0)
    font = tk.PhotoImage(file=str(page)+'.png')
    image_font.configure(image=font, compound=tk.CENTER) 
root = tk.Tk()
root.geometry('800x600')
root.resizable (width=False, height=False)

font = tk.PhotoImage(file=str(page)+'.png')
image_font = tk.Label(root, image=font, compound=tk.CENTER) 
image_font.place(x=0, y=0)

lbl = tk.Text(root, width = 100, height=5)
lbl.insert(1.0, " Выбери путь становления Русовъ")
lbl.place(x=0, y=492)

button2 = tk.Button(root, text='Выбрать путь', command=choose_folder, width=50)
button2.place(x=215,y=575)

button = tk.Button(root, text='Далее', command=change_background, width=30)
button.place(x=580,y=575)

root.mainloop()
