import tkinter as tk
from tkinter import filedialog
from tkinter import Frame
from tkinter import ttk
import pandas as pd

data = pd.DataFrame()

def browseFiles():
    file_path = filedialog.askopenfilename()
    if file_path:
        global data
        data = pd.read_csv(file_path)
        tree['columns'] = list(data.columns)
        tree['show'] = "headings"
        for i, col in enumerate(data.columns):
            tree.heading(i, text=col)
            for j, item in enumerate(data[col]):
                tree.insert('', 'end', values=list(data.iloc[j,:]))

root = tk.Tk()
root.title("CSV Data Viewer")
root.geometry('1100x400+200+200')

browseButton = tk.Button(root, text="Browse CSV Files", command=browseFiles, width=60, height=2, font=30, fg="white", bg="#0078d7")
browseButton.pack(pady=25)

frame = tk.Frame(root)
frame.pack(pady=25)

#treeview
tree = ttk.Treeview(frame, columns=[], show="headings")
tree.pack()

root.mainloop()
