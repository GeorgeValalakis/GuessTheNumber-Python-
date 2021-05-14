from tkinter import*
import random
from tkinter import messagebox
import time
window = Tk()
window.geometry("830x740")
window.title("Guess The Number")
logo1 = PhotoImage(file="Downward.png")
logo1=logo1.subsample(2)
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0, weight=1)


logo2 = PhotoImage(file="Upward.png")
logo2=logo2.subsample(4)
logo3 = PhotoImage(file="TickArrow.png")
logo3=logo3.subsample(2)
x=0
y=0
turns=0
def win():
    global label1,label2,label3,label22,entry,btnre,btne
    label1= Label(window,text="Guess The Number",font=('Times', 40, 'bold'))
    label1.grid(column=0,row=0,columnspan=2, pady=3, padx=40)
    label2=Label(window,text="We pick a secret number.\nYour purpose is to guess what number it is!\nIf your guess is too high or too low,\nyou will be given a hint.\nPress Enter to start!",
                 font=('Times', 30, 'bold'))
    label2.grid(column=0,row=2,columnspan=2, pady=10, padx=40)
    label22=Label(window,text="",font=('Times', 15, 'bold'))
    label22.grid(column=0,row=3,columnspan=2, padx=40)
    entry=Entry(window,font=('Times', 40, 'bold'),width=10)
    entry.grid(column=0,row=4, pady=0, columnspan=2,padx=0)
    label3= Label(window,font=('Times', 30, 'bold'))
    label3.grid(column=1,row=4, pady=45,padx=222,columnspan=2)

    btnre = Button(window, text="Reset",width=9,bg="Light blue",font=('Times', 20, 'bold'),command=randomnumber)
    btnre.grid(column=0, row=5,columnspan=2,pady=4)
    btne = Button(window, text="Exit",width=9,bg="Green",font=('Times', 20, 'bold'),command=window.destroy)
    btne.grid(column=0, row=6,columnspan=2,pady=4)
def randomnumber():
    global yy, turns,x
    x=0
    if y==1:
        label1.destroy()
        label3.destroy()
        label22.destroy()
        label2.destroy()
        btnre.destroy()
        btne.destroy()
        entry.destroy()
        turns = 0
        entry.destroy()
        yy = random.randint(0,100)
        win()
    else:

        yy = random.randint(0, 100)
def end():
    global yy
    if turns>=10:
        label2.configure(text="Your score was:"+str(turns)+" turns   "+"\nBetter luck next time!    ")
        label22.configure(text="The secret number was: "+str(yy))
    elif turns<10 and turns>=7:
        label2.configure(text= "Your score was: "+str(turns)+ " turns "+ "\nGood, you are an amateur!       ")
        label22.configure(text="The secret number was: " + str(yy))
    elif turns<7 and turns>3:
        label2.configure(text=  "Your score was: " + str(turns) + " turns " + "\nPretty Good, you are an intermediate!     ")
        label22.configure(text="The secret number was: " + str(yy))
    elif turns <= 3 and turns > 1:
        label2.configure(text= "Your score was: " + str(turns) + " turns " + "\nAmazing, you are an expert!     ")
        label22.configure(text="The secret number was: " + str(yy))
    else:
        label2.configure(text= "Your score was: " + str(turns) + " turn " + "\nYou are the Boss!     ")
        label22.configure(text="The secret number was: " + str(yy))

def start(event):
    global turns,x,y
    if x==0:
        for i in range(25):
            label22.configure(text=random.randint(1, 100))
            label22.update()
            time.sleep(0.1)

        label22.after(100, label22.configure(text="The secret number has been picked successfully!"))
        label22.update()
        label22.after(2000, label22.configure(text=""))
        x=1
    else:

        turns=turns+1
        if int(entry.get())<yy:
            label3.configure(image=logo2)
        elif int(entry.get())>yy:
            label3.configure(image=logo1)
        else:
            label3.configure(image=logo3)
            end()
            y=1
        entry.delete(0, "end")




win()



window.bind("<Return>",start)

randomnumber()
window.mainloop()