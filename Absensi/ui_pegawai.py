from tkinter import *

def populate_list():
    print('Populate')

def add_item():
    print('Add')

def clear_text():
    print('Clear')


#window 
app = Tk()

#bagian nama
part_text = StringVar()
part_label = Label(app, text='Nama', font=('bold', 14), pady=20)
part_label.grid(row=0, column=0, sticky=W) 
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)

#no anggota 
anggota_text = StringVar()
anggota_label = Label(app, text='No.Anggota', font=('bold', 14))
anggota_label.grid(row=0, column=2, sticky=W) 
anggota_entry = Entry(app, textvariable=anggota_text)
anggota_entry.grid(row=0, column=3)

#jam datang 
datang_text = StringVar()
datang_label = Label(app, text='Jam Datang', font=('bold', 14))
datang_label.grid(row=1, column=0, sticky=W) 
datang_entry = Entry(app, textvariable=datang_text)
datang_entry.grid(row=1, column=1)

#jam pulang 
pulang_text = StringVar()
pulang_label = Label(app, text='Jam Pulang', font=('bold', 14))
pulang_label.grid(row=1, column=2, sticky=W) 
pulang_entry = Entry(app, textvariable=part_text)
pulang_entry.grid(row=1, column=3)

#tempat list
part_list = Listbox(app, height=10, width=55)
part_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

#scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)

#scrollbar to list box
part_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=part_list.yview)

#buttons
add_btn = Button(app, text='Ansen Masuk', width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

add_btn = Button(app, text='Absen Pulang', width=12, command=add_item)
add_btn.grid(row=2, column=1)

add_btn = Button(app, text='Hapus Input', width=12, command=clear_text)
add_btn.grid(row=2, column=2)



app.title("Absensi Pegawai")
app.geometry('700x350')

#muali program 
app.mainloop()
