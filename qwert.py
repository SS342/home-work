import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import Tk,Frame,Checkbutton, BooleanVar,BOTH
j1 = 0  
j2 = 1
j3 = 1
j4 = 1
char_list = []


def qw():
    global j1
    j1 = j1 + 1

def delete():
    cursor1.execute("DELETE FROM user")
    cursor1.execute("DELETE FROM brand_products")
    cursor1.execute("DELETE FROM type_name")
    cursor1.execute("DELETE FROM workers")
    conn.commit()

def ok():

    global j1
    global j2

    q = entry1.get()
    
    if q == 'worker':
        notebook.add(f4, text = 'worker')
        entry1.delete(0,last = tk.END)

    elif q == 'admin':
        
        notebook.add(f3, text = 'admin')
        entry1.delete(0,last = tk.END)

    elif q == 'add':
        notebook.add(f5, text = 'add smt')
        entry1.delete(0,last = tk.END)

    else:
        if j1 % 2 == 0:
            w = str('yes')
            j2 = str(j2)
            cursor1.execute("insert into user values ('"+j2+"','"+q+"','"+w+"')")
           
        else:

            w = str('no')
            j2 = str(j2)
            cursor1.execute("insert into user values ('"+j2+"','"+q+"','"+w+"')")
            
        j2 = int(j2)
        j2 = j2 + 1
        entry1.delete(0,last = tk.END)
        conn.commit()

def okwork():

    #j3 - id worker
    global j3

    j3 = str(j3)
    q1 = entry2.get()#name
    q2 = entry3.get()#surname
    q3 = entry4.get()#midl name
    q4 = entry5.get()#id post

    cursor1.execute("insert into workers values ('"+j3+"','"+q1+"','"+q2+"','"+q3+"','"+q4+"')")
    cursor1.execute("insert into workers_post values ('"+j3+"','"+q4+"')")
    
    j3 = int(j3)
    j3 = j3 + 1

    entry2.delete(0,last = tk.END)
    entry3.delete(0,last = tk.END)
    entry4.delete(0,last = tk.END)
    entry5.delete(0,last = tk.END)
    conn.commit()

def okprod():
    #j4 - id prod
    global j4
    j4 = str(j4)
    w1 = entry6.get()#name
    w2 = entry7.get()#tid
    w3 = entry8.get()#bid

    cursor1.execute("insert into products values ('"+j4+"','"+w1+"','"+w2+"','"+w3+"')")
    cursor1.execute("insert into type_name values ('"+w2+"','"+j4+"')")
    cursor1.execute("insert into brand_products values ('"+w3+"','"+j4+"')")

    j4 = int(j4)
    j4 = j4 + 1

    entry6.delete(0,last = tk.END)
    entry7.delete(0,last = tk.END)
    entry8.delete(0,last = tk.END)
    conn.commit()

conn = sqlite3.connect('internetshop.db')
cursor1 = conn.cursor()

conn.commit()

window = tk.Tk()
window.geometry('1366x768')
window.title('internetShop')

style = ttk.Style(window)
style.configure('uptab.TNnotebook', tabposition='ws')

notebook = ttk.Notebook(window, style ='lefttab.TNotebook')

f1 = tk.Frame(notebook,width = 1366, height = 768)
f2 = tk.Frame(notebook,width = 1366, height = 768)
f3 = tk.Frame(notebook,width = 1366, height = 768)
f4 = tk.Frame(notebook,width = 1366, height = 768)
f5 = tk.Frame(notebook,width = 1366, height = 768)

notebook.add(f1, text = 'добавить')
notebook.add(f2, text = 'рекомендации')
notebook.pack()

text1 = ttk.Label(f1,text="USerName:", width = 15) 
text1.pack(side=tk.TOP)

entry1 = ttk.Entry(f1, width = 22)
entry1.pack(side=tk.TOP)
but1 = ttk.Button(f1, text="добавить",command = ok)
but1.pack(side=tk.TOP)

var = tk.BooleanVar()
cb = Checkbutton(f1,text = 'отказаться от рассылки', variable = var, command = qw)
cb.pack(side=tk.TOP)


but3 = ttk.Button(f3, text="delete", command = delete)
but3.grid(row=1, column=1)

lb = tk.Listbox(f4, width = 50)
lb.insert(tk.END, '1-админ','2-консультант','3-программист',"4-веб-дизайнер","5-фотограф","6-директор","7-заместитель","8-секретарь")
lb.grid(row = 1,column = 0)

text2 = ttk.Label(f4,text="<--список доступных должностей:", width = 30) 
text2.grid(row = 1, column = 1)

text3 = ttk.Label(f4,text="имя:", width = 10) 
text3.grid(row = 2, column = 0)

entry2 = ttk.Entry(f4, width = 22)
entry2.grid(row = 3, column = 1)

text4 = ttk.Label(f4,text="фамилия:", width = 10) 
text4.grid(row = 4, column = 0)

entry3 = ttk.Entry(f4, width = 22)
entry3.grid(row = 5, column = 1)

text5 = ttk.Label(f4,text="отчество:", width = 10) 
text5.grid(row = 6, column = 0)

entry4 = ttk.Entry(f4, width = 22)
entry4.grid(row = 7, column = 1)

text6 = ttk.Label(f4,text="номер вашей должности:", width = 25) 
text6.grid(row = 8, column = 0)

entry5 = ttk.Entry(f4, width = 22)
entry5.grid(row = 9, column = 1)

but4 = ttk.Button(f4, text="OK", command = okwork)
but4.grid()

#F5 aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA


lb1 = tk.Listbox(f5, width = 50)
lb1.insert(tk.END, '1-футболки','2-обувь','3-ноутбуки',"4-сладости","5-картины")
lb1.grid(row = 1,column = 0)

text7 = ttk.Label(f5,text="<--список доступных типов:", width = 30) 
text7.grid(row = 1, column = 1)

text8 = ttk.Label(f5,text="список доступных брендов-->", width = 30) 
text8.grid(row = 2, column = 1)

lb2 = tk.Listbox(f5, width = 50)
lb2.insert(tk.END, '1-aser','2-lacost','3-anus',"4-nike","5-Ufon")
lb2.grid(row = 1,column = 2)

text9 = ttk.Label(f5,text="name prod:", width = 30) 
text9.grid(row = 3, column = 1)

entry6 = ttk.Entry(f5, width = 22)
entry6.grid(row = 4, column = 1)

text10 = ttk.Label(f5,text="typeid", width = 30) 
text10.grid(row = 5, column = 1)

entry7 = ttk.Entry(f5, width = 22)
entry7.grid(row = 6, column = 1)

text11 = ttk.Label(f5,text="brandid", width = 30) 
text11.grid(row = 7, column = 1)

entry8 = ttk.Entry(f5, width = 22)
entry8.grid(row = 8, column = 1)

but5 = ttk.Button(f5, text="OK", command = okprod)
but5.grid(row = 9, column = 1)

window.mainloop()