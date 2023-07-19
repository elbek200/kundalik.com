from tkinter import *

def terminal(code):
   oyna = Tk()
   oyna.title("Activity")
   oyna.geometry('400x400')
   
   yuz = Label(text = "KOD EMAILINGIZGA YUBORILDI \n KODNI TASDIQLANG!!!" , bg = "white")
   yuz.place(x = 50 , y = 30 , width = 180 , height = 60)
   natija = Label(text = " Natija " , bg = "white")
   natija.place(x = 180, y = 100 , width = 120 , height = 40)
   son = Entry()
   son.place(x = 50 , y = 100 ,width = 70 ,height = 40)
   
   
   def farq ():
      text1 = ""
      if int(son.get()) == code:
          text1 = "KODINGGIZ TOG'RI"
      else:
          text1 = "KODINGGIZ NOTOG'RI"
      natija.config(text = text1)
      return natija
   
   tugma = Button(text = " ok " , command = farq)
   tugma.place(x = 50 , y = 155 ,width = 30,height = 30)
   oyna.mainloop()
   
    