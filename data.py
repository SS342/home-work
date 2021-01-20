import sqlite3
import tkinter as tk
from tkinter import ttk

conn = sqlite3.connect('работники.db')
cursor1 = conn.cursor()
def delete():
    cursor1.execute("DELETE FROM работники")

def ok():
    q = entry1.get()
    w = entry2.get()
    print(q,w)
    if q == 'admin' and w == '1254':
        notebook.add(f3, text = 'admin')
        
    else:
        
        cursor1.execute("insert into работники values ('"+q+"','"+w+"')")
        conn.commit()
        entry1.delete(0,last = tk.END)
        entry2.delete(0,last = tk.END)

def sql_fetch():

    cursor1.execute('SELECT * FROM работники')
    for row in cursor1.fetchall():
        data = str(row[0]) + ' ' + str(row[1])
        ttk.Label(f2,text = data).grid()

window = tk.Tk()
window.geometry('300x300+100+100')
window.title('123')

style = ttk.Style(window)
style.configure('uptab.TNnotebook', tabposition='ws')

notebook = ttk.Notebook(window, style ='lefttab.TNotebook')
f1 = tk.Frame(notebook,width = 200, height = 200)
f2 = tk.Frame(notebook,width = 200, height = 200)
f3 = tk.Frame(notebook,width = 200, height = 200)

notebook.add(f1, text = 'добавить')
notebook.add(f2, text = 'просмотр')
notebook.pack()

text1 = ttk.Label(f1,text="имя:") 
text1.grid(row=2, column=0)

entry1 = ttk.Entry(f1, width = 15)
entry1.grid(row=2, column=1)

text2 = ttk.Label(f1,text="фамилия:") 
text2.grid(row=3, column=0)

entry2 = ttk.Entry(f1, width = 15)
entry2.grid(row=3, column=1)

but1 = ttk.Button(f1, text="добавить",command = ok)
but1.grid(row=4, column=1)
but2 = ttk.Button(f2, text="загрузить", command = sql_fetch)
but2.grid(row=1, column=1)
but3 = ttk.Button(f3, text="delete", command = delete)
but3.grid(row=1, column=1)

window.mainloop()