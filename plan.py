import tkinter as tk
from tkinter import ttk
import sys, os

os.chdir(sys._MEIPASS)

window = tk.Tk()
window.geometry('1130x652')
window.resizable(False, False)
window.title('Plan')

base = tk.PhotoImage(file='includes/base.png')

file = open('includes/dni.txt','r')
dni = []
for line in file:
    x=line.split(';')
    x.pop(5)
    dni.append(x)
file.close()

weeks=[]
for week in dni:
    weeks.append(week[0]+'-'+week[4])

file = open('includes/wolne.txt','r')
wolne = []
for line in file:
    wolne.append(line.strip())
file.close()

class przedmiot:
    def __init__(self, name, typ, dzien, start, end, tygodnie, sala, krotki):
        self.name = name
        self.typ = typ
        self.dzien = dzien
        self.start = start
        self.end = end
        self.tygodnie = tygodnie
        self.sala = sala
        self.krotki = krotki

def lista(s):
    return sum(((list(range(*[int(j) + k for k,j in enumerate(i.split('-'))]))
        if '-' in i else [int(i)]) for i in s.split(',')),[])

file = open("includes/przedmioty.txt", "r",encoding="utf-8")
przedmioty=[]
for line in file:
    x=line.split(';')
    przedmioty.append(przedmiot(x[0],x[1],int(x[2]),x[3],x[4],lista(x[5]),x[6],int(x[7])))
file.close()

kolory={
    'Wykład':'#CAFF0E',
    'Ćwiczenia':'#0EFF46',
    'Labolatoria':'#FFC20E',
    'Fakultet':'#FF420E',
    'Lektorat':'#FF57FC',
    'Projekt':'#57C9FF'
}

week=tk.StringVar()
combobox=ttk.Combobox(window,textvariable=week)
combobox['state'] = 'readonly'
combobox['values'] = weeks
combobox.pack(padx=5, pady=5)

canvas = tk.Canvas(window, width=1130, height=650)

def generuj_plan(event):
    canvas.delete('all')
    canvas.create_image((565,309),image=base)
    current_week=weeks.index(week.get())+(weeks.index(week.get())<6)
    akt_dni=dni[current_week+(weeks.index(week.get())>=6)-1]
    for i in range(5):
        canvas.create_text(
            (280+206*i,15),
            text=akt_dni[i],
            fill='black',
            font='Verdana 8'
        )
    for item in przedmioty:
        if current_week in item.tygodnie and akt_dni[item.dzien] not in wolne:
            start=item.start.split(':')
            start=int(start[0])*4-32+int(start[1])/15
            end=item.end.split(':')
            end=int(end[0])*4-32+int(end[1])/15
            canvas.create_rectangle((94+206*item.dzien,28+11.24*start),(298+206*item.dzien,38+11.24*(end-1)),fill=kolory[item.typ],outline='')
            if item.krotki:
                skrot=item.name.split(' ')
                skrot=''.join([i[0] for i in skrot])
                tekst=skrot+'; '+item.sala+'\n'+item.start+'-'+item.end
            else:
                tekst=item.name+'\n'+item.typ+'\n'+item.sala+'\n'+item.start+'-'+item.end
                
            canvas.create_text(
                (196+206*item.dzien,30+11.24*start),
                anchor=tk.N,
                text=tekst,
                justify=tk.CENTER,
                fill='black',
                font='Verdana 8',
                width=200
            )
    
    canvas.pack(anchor=tk.CENTER)

combobox.bind('<<ComboboxSelected>>',generuj_plan)

window.mainloop()