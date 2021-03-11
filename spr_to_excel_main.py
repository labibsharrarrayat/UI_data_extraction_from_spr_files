import os
import sys
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import spr_folder
import spr_file

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Python Tkinter Dialog Widget")
        self.minsize(940, 400)

        self.labelFrame = ttk.LabelFrame(self, text="OPEN AND PROCESS FILE")
        self.labelFrame.grid(column=0, row=1, padx=1, pady=20)
        self.labelFrame.pack(fill="both", expand="yes")

        self.button()

        self.select_folder()
        self.convert_button()
        self.convert_file_button()


    def button(self):
        self.button = ttk.Button(self.labelFrame, text="Browse A File", command=self.fileDialog)
        self.button.grid(column=1, row=1,padx=10, pady=10)

    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype=(("spr files", "*.spr"), ("all files", "*.*")))
        self.folder = " "
        self.label = ttk.Label(self.labelFrame, text="")
        self.label.grid(column=2, row=1)
        self.label.configure(text=self.filename)

    def folderDialog(self):
        self.filename = " "
        self.folder = filedialog.askdirectory()
        self.label = ttk.Label(self.labelFrame, text="")
        self.label.grid(column=1, row=12)
        self.label.configure(text=self.folder)


    def select_folder(self):
        self.button = ttk.Button(self.labelFrame, text="Browse .spr Folder", command=self.folderDialog)
        self.button.grid(column=1, row=10)

    def convert_folder(self):
        print("FILE: ",self.filename)
        print("FOLDER: ",self.folder)
        try:
            spr_folder.main_process(self.folder)

        except ValueError:
            messagebox.showerror('ERROR','No .spr files found in folder. Please be sure to select a fodler with .spr files')

        print(self.folder)

    def convert_spr_file(self):
        try:
            spr_file.main_process(self.filename)
        except ValueError:
            messagebox.showerror('ERROR','File does not match the require .spr format')

    def convert_button(self):
        self.button = ttk.Button(self.labelFrame, text="Convert .spr Folder", command=self.convert_folder)
        self.button.grid(column=1, row=15,padx=10, pady=10)

    def convert_file_button(self):
        self.button = ttk.Button(self.labelFrame, text="Convert .spr File", command=self.convert_spr_file)
        self.button.grid(column=2, row=15,padx=10, pady=10)

root = Root()
root.mainloop()