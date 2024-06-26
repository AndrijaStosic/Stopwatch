from tkinter import *


prozor = Tk()
prozor.config(bg="peachpuff")
prozor.geometry("950x500")
prozor.title("Stoperica")

sati_int = 0
minuti_int = 0
sekunde_int = 0
running = False
after_id = None

def azuriraj_vreme():
    global sati_int, minuti_int, sekunde_int, running, after_id
    if not running:  
        return
    
    sekunde_int += 1
    if sekunde_int == 60:
        sekunde_int = 0
        minuti_int += 1
        if minuti_int == 60:
            minuti_int = 0
            sati_int += 1
    
    sati_str = '{:02d}'.format(sati_int)
    minuti_str = '{:02d}'.format(minuti_int)
    sekunde_str = '{:02d}'.format(sekunde_int)

    sati.config(text=sati_str)
    minuti.config(text=minuti_str)
    sekunde.config(text=sekunde_str)
    
    after_id = prozor.after(1000, azuriraj_vreme)

pocetni_text = Label(text="Stoperica", font=("Comfortaa, 40"), bg="peachpuff")
pocetni_text.place(x=335, y=25)

sati = Label(text="00", font="Arial, 35", bg="snow")
sati.place(x=350, y=150)

minuti = Label(text="00", font="Arial, 35", bg="snow")
minuti.place(x=441, y=150)

sekunde = Label(text="00", font="Arial, 35", bg="snow")
sekunde.place(x=525, y=150)

def startuj_stopericu():
    global running, after_id
    if not running:
        running = True
        azuriraj_vreme()

def zaustavi_stopericu():
    global running, after_id
    running = False
    if after_id:
        prozor.after_cancel(after_id)
        after_id = None

def resetuj_stopericu():
    global sati_int, minuti_int, sekunde_int, running, after_id
    running = False
    if after_id:
        prozor.after_cancel(after_id)
        after_id = None
    sati_int = 0
    minuti_int = 0
    sekunde_int = 0
    sati.config(text="00")
    minuti.config(text="00")
    sekunde.config(text="00")

start_dugme = Button(text="Kreni", font=("Arial, 14"), bg="ORANGE", command=startuj_stopericu)
start_dugme.place(x=200, y=325)

zaustavi_dugme = Button(text="Zaustavi", font=("Arial, 14"), bg="darkorange", command=zaustavi_stopericu)
zaustavi_dugme.place(x=400, y=325)

resetuj_dugme = Button(text="Resetuj", bg="gold", font=("Arial, 14"), command=resetuj_stopericu)
resetuj_dugme.place(x=600, y=325)

mainloop()
