from tkinter import *

#window
app = Tk()

def masuk_admin():
    print('Add')

#bagian nama
part_text = StringVar()
part_label = Label(app, text='Nama', font=('bold', 14), pady=20)
part_label.grid(row=0, column=0, sticky=W) 
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)

#no anggota 
anggota_text = StringVar()
anggota_label = Label(app, text='ID Admin', font=('bold', 14))
anggota_label.grid(row=1, column=0, sticky=W) 
anggota_entry = Entry(app, textvariable=anggota_text)
anggota_entry.grid(row=1, column=1)

#button
add_btn = Button(app, text='Masuk', width=12, command=masuk_admin)
add_btn.grid(row=2, column=0, pady=20, padx=20)


app.title("Admin")
app.geometry('550x250')

#muali program 
app.mainloop()
