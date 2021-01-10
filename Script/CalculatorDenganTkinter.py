from tkinter import *

root = Tk()
root.title('calculator')

# variabel
angka = ''
nilai = StringVar()
angka1 = 0

# input from button
def addentry(dapat):
    global angka
    angka = angka + str(dapat)
    nilai.set(angka)

# get aritmatik
def aritmatik(dapat):
    global angka,angka1
    global operasi
    operasi = dapat
    angka1 = angka
    angka = ''
    nilai.set(angka)

# key input
def key_pressed(event):
    global angka
    angka = angka + str(event.char,)
    nilai.set(angka)

# result
def hasil(dapat):
    global angka,angka1,operasi
    ambil = angka
    if operasi == '+':
        hasil = int(angka1) + int(ambil)
    if operasi == '-':
        hasil = int(angka1) - int(ambil)
    if operasi == 'x':
        hasil = int(angka1) * int(ambil)
    if operasi == '/':
        hasil = int(angka1) / int(ambil)
    angka1 = hasil
    angka = hasil
    nilai.set(hasil)

def clear():
    global angka,angka1
    angka = ''
    angka1 = 0 
    nilai.set(angka)

# def gui
lihatangka = Entry(root,width=42,text=nilai)
nilai.set('Silahkan masukan nilainya mas eko')

button1 = Button(root,text='1',width=8,command=lambda:addentry(1))
button2 = Button(root,text='2',width=8,command=lambda:addentry(2))
button3 = Button(root,text='3',width=8,command=lambda:addentry(3))

button4 = Button(root,text='4',width=8,command=lambda:addentry(4))
button5 = Button(root,text='5',width=8,command=lambda:addentry(5))
button6 = Button(root,text='6',width=8,command=lambda:addentry(6))

button7 = Button(root,text='7',width=8,command=lambda:addentry(7))
button8 = Button(root,text='8',width=8,command=lambda:addentry(8))
button9 = Button(root,text='9',width=8,command=lambda:addentry(9))

button0 = Button(root,text='0',width=8,command=lambda:addentry(0))
btnspace = Button(root,text='clear',width=8,command=lambda:clear())

buttonadd = Button(root,text='+',width=8,command=lambda:aritmatik('+'))
buttonkurang = Button(root,text='-',width=8,command=lambda:aritmatik('-'))
buttonkali = Button(root,text='x',width=8,command=lambda:aritmatik('x'))
buttonbagi = Button(root,text='/',width=8,command=lambda:aritmatik('/'))
buttonequal = Button(root,text='=',width=8,command=lambda:hasil('='))

# def position
lihatangka.grid(columnspan=4,pady=10,padx=2,ipady=10)

button1.grid(column=0,row=1,ipady=10)
button2.grid(column=1,row=1,ipady=10)
button3.grid(column=2,row=1,ipady=10)
buttonadd.grid(column=3,row=1,ipady=10)

button4.grid(column=0,row=2,ipady=10)
button5.grid(column=1,row=2,ipady=10)
button6.grid(column=2,row=2,ipady=10)
buttonkurang.grid(column=3,row=2,ipady=10)

button7.grid(column=0,row=3,ipady=10)
button8.grid(column=1,row=3,ipady=10)
button9.grid(column=2,row=3,ipady=10)
buttonkali.grid(column=3,row=3,ipady=10)

btnspace.grid(column=0,row=4,ipady=10)
button0.grid(column=1,row=4,ipady=10)
buttonbagi.grid(column=2,row=4,ipady=10)
buttonequal.grid(column=3,row=4,ipady=10)


root.bind("<Key>",key_pressed)
root.mainloop()