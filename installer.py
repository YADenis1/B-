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
main_font = 'TkCaptionFont'
def create_msg_in_lbl(text):
    for widget in lbl.winfo_children():
        widget.destroy()
    msg = tk.Label(lbl,text=text)
    msg.config(font=("Courier", 22),fg='#4A7A8C')
    msg.pack(fill="both")

def delete_msg(parrent_widget):
    for widget in parrent_widget.winfo_children():
        widget.destroy()


def choose_folder():
    global folder_selected, lbl
    folder_selected = filedialog.askdirectory()
    create_msg_in_lbl("Выбери путь становления Русовъ \n Выбранный путь >> " + folder_selected)
    
def change_background():
    global page, image_font, font, root, lbl, button, folder_selected, button2
    if folder_selected == "":
        return 0
    page+=1
    delete_msg(lbl)
    if page == 1:
        create_msg_in_lbl("Для сражения требуется установленный ящеръ!\n Убедись что ящеръ установленъ!")
        button2.place_forget()
    if page == 2:
        button.configure(text="Завершить")
        create_msg_in_lbl("Помоги славянамъ\n одолеть злыхъ ящеровъ съ силой В++")
    if page == 3:
        for i in onlyfiles:
            print(pathload+"\\"+i, folder_selected)
            shutil.copyfile(pathload+"\\"+i, folder_selected+"\\"+i)
        call("pip.exe install subprocess.run")
        call("pip.exe install pyinstaller")
        print("pyinstaller.exe --icon=program.ico -F " + folder_selected+"\\"+"translator.py")
        call("pyinstaller.exe --icon=program.ico -F " + folder_selected+"\\"+"translator.py")
        exit(0)
    font = tk.PhotoImage(file=str(page)+'.png')
    image_font.configure(image=font, compound=tk.CENTER) 


root = tk.Tk()
root.geometry('800x600')
root.resizable (width=False, height=False)

font = tk.PhotoImage(file=str(page)+'.png')
image_font = tk.Label(root, image=font, compound=tk.CENTER) 
image_font.place(x=0, y=0)

lbl = tk.Frame(root)
# lbl.insert(1.0, " Выбери путь становления Русовъ")
lbl.config(background = 'white')
lbl.place(anchor = "nw", x = 0, y = 400, width = 800, height = 200)
create_msg_in_lbl("Выбери путь становления Русовъ")
# lbl.tag_add("text_styles", "1.0", "end")
# lbl.tag_configure("text_styles", font = main_font, )

button2 = tk.Button(root, text='Выбрать путь', command=choose_folder, width=50)
button2.place(x=215,y=575)

button = tk.Button(root, text='Далее', command=change_background, width=30)
button.place(x=580,y=575)

root.mainloop()
