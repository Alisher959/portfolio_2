from datetime import datetime
from tkinter import *

oyna = Tk()
oyna.title("Dasturcha")
oyna.geometry("300x300")

natija=Label(text='Natija', bg='white')
natija.place(x=90, y=135, width=120, height=40)

yil = Entry()
yil.place(x=75, y=50, width=150, height=30)

def farq():
    bugun = datetime.today()
    natija.config(text=bugun.year - int(yil.get())) 


tugma=Button(text='hisoblash', command=farq)
tugma.place(x=90, y=90, width=120, height=30 )


oyna.mainloop()

# def farq(yil):
#     bugun = datetime.today()
#     natija = bugun.year - yil
#     return natija


# tugilgan_yil = int(input("Tug`ilgan yilingizni yozing "))


# natija_f = farq(tugilgan_yil)

# print("Natija: ", natija_f)

# maktab_yil = int(input("Yilni kiriting: "))
# natija_f = farq(maktab_yil)
# print("Natija: ", natija_f)
