import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import Tk, Frame, Checkbutton, BooleanVar, BOTH

j1 = 0  # spam yes/no


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

    q = entry1qw.get()
    r = entry1qqw.get()  # pass
    print(q, r)

    if q == 'worker' and r == '':
        notebook.add(f4, text='worker')
        entry1.delete(0, last=tk.END)

    elif q == 'admin' and r == '':

        notebook.add(f3, text='admin')
        entry1.delete(0, last=tk.END)

    elif q == 'add' and r == '':
        notebook.add(f5, text='add smt')
        entry1.delete(0, last=tk.END)

    else:
        if j1 % 2 == 0:
            w = str('yes')
            j2 = str(j2)
            cursor1.execute("insert into user values ('" + j2 + "','" + q + "','" + r + "','" + w + "')")

        else:

            w = str('no')
            j2 = str(j2)
            cursor1.execute("insert into user values ('" + j2 + "','" + q + "','" + r + "','" + w + "')")

        j2 = int(j2)
        j2 = j2 + 1
        entry1qw.delete(0, last=tk.END)
        entry1qqw.delete(0, last=tk.END)
        conn.commit()


def select():
    q = entry1.get()
    w = entry1q.get()
    sql = "select * from user WHERE username = '" + q + "' and passworld = '" + w + "'"
    cursor1.execute(sql)
    conn.commit()
    tmp = cursor1.fetchall()
    if tmp:
        text1w.configure(text='login completed')
    else:
        text1w.configure(text='login not  completed')

    entry1.delete(0, last=tk.END)
    entry1q.delete(0, last=tk.END)


def okwork():
    # j3 - id worker
    global j3

    j3 = str(j3)
    q1 = entry2.get()  # name
    q2 = entry3.get()  # surname
    q3 = entry4.get()  # midl name
    q4 = entry5.get()  # id post

    cursor1.execute("insert into workers values ('" + j3 + "','" + q1 + "','" + q2 + "','" + q3 + "','" + q4 + "')")
    cursor1.execute("insert into workers_post values ('" + j3 + "','" + q4 + "')")

    j3 = int(j3)
    j3 = j3 + 1

    entry2.delete(0, last=tk.END)
    entry3.delete(0, last=tk.END)
    entry4.delete(0, last=tk.END)
    entry5.delete(0, last=tk.END)
    conn.commit()


def okprod():
    # j4 - id prod
    global j4
    j4 = str(j4)
    w1 = entry6.get()  # name
    w2 = entry7.get()  # tid
    w3 = entry8.get()  # bid

    cursor1.execute("insert into products values ('" + j4 + "','" + w1 + "','" + w2 + "','" + w3 + "')")
    cursor1.execute("insert into type_name values ('" + w2 + "','" + j4 + "')")
    cursor1.execute("insert into brand_products values ('" + w3 + "','" + j4 + "')")

    j4 = int(j4)
    j4 = j4 + 1

    entry6.delete(0, last=tk.END)
    entry7.delete(0, last=tk.END)
    entry8.delete(0, last=tk.END)
    conn.commit()


def registr():
    notebook.add(f6, text='registr')


conn = sqlite3.connect('internetshop.db')
cursor1 = conn.cursor()

# create table~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

cursor1.execute("""CREATE TABLE IF NOT EXISTS brand(
    ID   STRING,
    name STRING);
""")

conn.commit()

cursor1.execute("""CREATE TABLE IF NOT EXISTS brand_products(
    IDbrand   STRING,
    IDproduct STRING);
""")

conn.commit()

cursor1.execute("""CREATE TABLE IF NOT EXISTS posts(
    ID     STRING,
    title  STRING,
    salary STRING);
""")

conn.commit()

cursor1.execute("""CREATE TABLE IF NOT EXISTS products(
    ID     STRING,
    name   STRING,
    typeID STRING,
    brand  STRING);
""")

conn.commit()

cursor1.execute("""CREATE TABLE IF NOT EXISTS type(
    ID   STRING,
    name STRING);
""")

conn.commit()

cursor1.execute("""CREATE TABLE IF NOT EXISTS type_name(
    IDtype    STRING,
    IDprodust STRING);
""")

conn.commit()

cursor1.execute("""CREATE TABLE IF NOT EXISTS user(
    ID        STRING,
    username  STRING,
    passworld STRING,
    spam      STRING);
""")

conn.commit()

cursor1.execute("""CREATE TABLE IF NOT EXISTS workers(
    ID          STRING,
    name        STRING,
    surname     STRING,
    midddlename STRING,
    postid      STRING);
""")

conn.commit()

cursor1.execute("""CREATE TABLE IF NOT EXISTS workers_post (
    Idworker STRING,
    IDpost   STRING);
""")

conn.commit()

cursor1.execute("""CREATE TABLE IF NOT EXISTS feddback(
    userid STRING,
    text STRING);
""")
conn.commit()

j15 = '0'
test = 'test'

sql = "select * from user WHERE ID = '" + j15 + "'"
cursor1.execute(sql)
conn.commit()
tmp = cursor1.fetchall()
if tmp:
    pass
else:
    cursor1.execute("insert into user values ('" + j15 + "','" + test + "','" + test + "','" + test + "')")
    print('test user add')

sql = "select * from user WHERE ID = '" + j15 + "'"
cursor1.execute(sql)
conn.commit()
tmp = cursor1.fetchall()
if tmp:
    pass
else:
    cursor1.execute(
        "insert into workers values ('" + j15 + "','" + test + "','" + test + "','" + test + "','" + test + "')")
    print('test worker add')

sql = "select * from workers WHERE ID = '" + j15 + "'"
cursor1.execute(sql)
conn.commit()
tmp = cursor1.fetchall()
if tmp:
    pass
else:
    cursor1.execute(
        "insert into workers values ('" + j15 + "','" + test + "','" + test + "','" + test + "','" + test + "')")
    print('test worker add')

sql = "select * from workers_post WHERE Idworker = '" + j15 + "'"
cursor1.execute(sql)
conn.commit()
tmp = cursor1.fetchall()
if tmp:
    pass
else:
    cursor1.execute("insert into workers_post values ('" + j15 + "','" + test + "')")
    print('test workers_post add')

sql = "select * from products WHERE ID = '" + j15 + "'"
cursor1.execute(sql)
conn.commit()
tmp = cursor1.fetchall()
if tmp:
    pass
else:
    cursor1.execute("insert into products values ('" + j15 + "','" + test + "','" + test + "','" + test + "')")
    print('test products add')

sql = "select * from type_name WHERE IDtype = '" + j15 + "'"
cursor1.execute(sql)
conn.commit()
tmp = cursor1.fetchall()
if tmp:
    pass
else:
    cursor1.execute("insert into type_name values ('" + j15 + "','" + test + "')")
    print('test type_name add')

sql = "select * from brand_products WHERE IDbrand = '" + j15 + "'"
cursor1.execute(sql)
conn.commit()
tmp = cursor1.fetchall()
if tmp:
    pass
else:
    cursor1.execute("insert into brand_products values ('" + j15 + "','" + test + "')")
    print('test brand_products add')
# cursor1.execute("insert into user values ('"+j15+"','"+test+"','"+test+"','"+test+"')")
# cursor1.execute("insert into workers values ('"+j15+"','"+test+"','"+test+"','"+test+"','"+test+"')")
# cursor1.execute("insert into workers_post values ('"+j15+"','"+test+"')")
# cursor1.execute("insert into products values ('"+j15+"','"+test+"','"+test+"','"+test+"')")
# cursor1.execute("insert into type_name values ('"+test+"','"+test+"')")
# cursor1.execute("insert into brand_products values ('"+test+"','"+test+"')")

char_list = []
cursor1.execute("SELECT ID FROM user")
for row in cursor1.fetchall():
    char_list.append(row)
    print(char_list)
string = char_list[-1]
for c in string:
    char_list.append(c)
j2 = char_list[-1]
j2 = j2 + 1
print(j2)

char_list = []
cursor1.execute("SELECT ID FROM products")
for row in cursor1.fetchall():
    char_list.append(row)
    print(char_list)
string = char_list[-1]
for c in string:
    char_list.append(c)
j4 = char_list[-1]
j4 = j4 + 1
print(j4)

char_list = []
cursor1.execute("SELECT ID FROM workers")
for row in cursor1.fetchall():
    char_list.append(row)
    print(char_list)
string = char_list[-1]
for c in string:
    char_list.append(c)
j3 = char_list[-1]
j3 = j3 + 1
print(j3)

window = tk.Tk()
window.geometry('1366x768')
window.title('internetShop')

style = ttk.Style(window)
style.configure('uptab.TNnotebook', tabposition='ws')

notebook = ttk.Notebook(window, style='lefttab.TNotebook')

f1 = tk.Frame(notebook, width=1366, height=768)
f2 = tk.Frame(notebook, width=1366, height=768)
f3 = tk.Frame(notebook, width=1366, height=768)
f4 = tk.Frame(notebook, width=1366, height=768)
f5 = tk.Frame(notebook, width=1366, height=768)
f6 = tk.Frame(notebook, width=1366, height=768)

notebook.add(f1, text='add')
notebook.add(f2, text='recomendet')
notebook.pack()

text1w = ttk.Label(f1, text="ENTER:", width=15)
text1w.pack(side=tk.TOP)
text1 = ttk.Label(f1, text="USerName:", width=15)
text1.pack(side=tk.TOP)

entry1 = ttk.Entry(f1, width=22)
entry1.pack(side=tk.TOP)

text1q = ttk.Label(f1, text="passworld:", width=15)
text1q.pack(side=tk.TOP)

entry1q = ttk.Entry(f1, width=22)
entry1q.pack(side=tk.TOP)

text1qqqq = ttk.Label(f1, text="help - efnqofepfjofek ;)", width=150)
text1qqqq.pack(side=tk.TOP)

but1 = ttk.Button(f1, text="enter", command=select)  # thiiiiis
but1.pack(side=tk.TOP)

but1q = ttk.Button(f1, text="registr", command=registr)
but1q.pack(side=tk.TOP)

but3 = ttk.Button(f3, text="delete", command=delete)
but3.grid(row=1, column=1)

lb = tk.Listbox(f4, width=50)
lb.insert(tk.END, '1-admin', '2-consultant', '3-proger', "4-veb-desiger", "5-photographer", "6-directer",
          "7-deputy", "8-Secretary")
lb.grid(row=1, column=0)

text2 = ttk.Label(f4, text="<--list of available types:", width=30)
text2.grid(row=1, column=1)

text3 = ttk.Label(f4, text="name:", width=10)
text3.grid(row=2, column=0)

entry2 = ttk.Entry(f4, width=22)
entry2.grid(row=3, column=1)

text4 = ttk.Label(f4, text="surname:", width=10)
text4.grid(row=4, column=0)

entry3 = ttk.Entry(f4, width=22)
entry3.grid(row=5, column=1)

text5 = ttk.Label(f4, text="middle mame:", width=10)
text5.grid(row=6, column=0)

entry4 = ttk.Entry(f4, width=22)
entry4.grid(row=7, column=1)

text6 = ttk.Label(f4, text="number your post", width=25)
text6.grid(row=8, column=0)

entry5 = ttk.Entry(f4, width=22)
entry5.grid(row=9, column=1)

but4 = ttk.Button(f4, text="OK", command=okwork)
but4.grid()

# F5 aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA


lb1 = tk.Listbox(f5, width=50)
lb1.insert(tk.END, '1-T-shirt', '2-shoes', '3-laptop', "4-candy", "5-pictures")
lb1.grid(row=1, column=0)

text7 = ttk.Label(f5, text="<--list of available types:", width=30)
text7.grid(row=1, column=1)

text8 = ttk.Label(f5, text="list of available brands-->", width=30)
text8.grid(row=2, column=1)

lb2 = tk.Listbox(f5, width=50)
lb2.insert(tk.END, '1-aser', '2-lacost', '3-anus', "4-nike", "5-Ufon")
lb2.grid(row=1, column=2)

text9 = ttk.Label(f5, text="name prod:", width=30)
text9.grid(row=3, column=1)

entry6 = ttk.Entry(f5, width=22)
entry6.grid(row=4, column=1)

text10 = ttk.Label(f5, text="typeid", width=30)
text10.grid(row=5, column=1)

entry7 = ttk.Entry(f5, width=22)
entry7.grid(row=6, column=1)

text11 = ttk.Label(f5, text="brandid", width=30)
text11.grid(row=7, column=1)

entry8 = ttk.Entry(f5, width=22)
entry8.grid(row=8, column=1)

but5 = ttk.Button(f5, text="OK", command=okprod)
but5.grid(row=9, column=1)

# f6

text1qw = ttk.Label(f6, text="USerName:", width=15)
text1qw.pack(side=tk.TOP)

entry1qw = ttk.Entry(f6, width=22)
entry1qw.pack(side=tk.TOP)

text1qqw = ttk.Label(f6, text="passworld:", width=15)
text1qqw.pack(side=tk.TOP)

entry1qqw = ttk.Entry(f6, width=22)
entry1qqw.pack(side=tk.TOP)

var = tk.BooleanVar()
cb = Checkbutton(f6, text='refuse to hear the words', variable=var, command=qw)
cb.pack(side=tk.TOP)

but5www = ttk.Button(f6, text="OK", command=ok)
but5www.pack(side=tk.TOP)

window.mainloop()

print(j1, j2, j3, j4)
print(type(j1))
print(type(j2))
print(type(j3))
print(type(j4))