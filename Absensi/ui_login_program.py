from tkinter import *
from functools import partial



def goPegawai():
    import ui_pegawai

def goAdmin():
    import ui_admin

#piplihan admin & pegawai
def goLogin(username, password):
    absen.destroy()
    login = Tk()
    login.geometry('200x150')
    login.title("Absensi Harian")
    
    lebel = Label(login, text="WELCOME!! Lets start a new day!!")
    lebel.grid(column=0, row=5)

    lebel2 = Label(login, text="What would you like to do!")
    lebel2.grid(column=0, row=6)
    
    tombol1 = Button(login, text="Absen Pegawai", bg="white", fg="black", command=goPegawai)
    tombol1.grid(column=0, row=8, pady=10)
    
    tombol2 = Button(login, text="Absen Admin", bg="white", fg="black", command= goAdmin)
    tombol2.grid(column=0,row=9)

    login.mainloop()


#login window absen 
absen = Tk()  
absen.geometry('250x200')
absen.title('Absensi Perusahaan UWU')

#username entry 
usernameLabel = Label(absen, text="User Name :", justify="left")
usernameLabel.place(x=1, y=80)
username = StringVar()
usernameEntry = Entry(absen, textvariable=username)
usernameEntry.place(x=90, y=80)

#password entry
passwordLabel = Label(absen,text="Password :", justify="left")
passwordLabel.place(x=1, y= 110)
password = StringVar()
passwordEntry = Entry(absen, textvariable=password, show='*')
passwordEntry.place(x=90, y= 110)

goLogin = partial(goLogin, username, password)

#tombol login
loginButton = Button(absen, text="Login", command=goLogin)
loginButton.place(x=105, y=140)

absen.mainloop()
