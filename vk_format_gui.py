from tkinter import *
from tkinter import scrolledtext

def keypress(event):
        if event.keycode == 86:
            event.widget.event_generate('<<Paste>>')
        elif event.keycode == 67:
            event.widget.event_generate('<<Copy>>')
        elif event.keycode == 88:
            event.widget.event_generate('<<Cut>>')

def clear():
    txt_in.delete(1.0, END)
    txt_out.delete(1.0, END)

def format_txt():
    result = ''
    text = txt_in.get(1.0, END)
    underline = chk_state1.get()
    stroke = chk_state2.get()
    if underline == 1 and stroke == 1:
        for char in text:
            result += "&#817;" + "&#0822;" + char
    elif underline == 1 and stroke == 0:
        for char in text:
            result += "&#817;" + char
    elif underline == 0 and stroke == 1:
        for char in text:
            result += "&#0822;" + char
    txt_out.insert(INSERT, result)
    
def copy_clpbrd():
    window.clipboard_clear()
    txt = txt_out.get(1.0, END)
    window.clipboard_append(txt)

window = Tk()
window.title("Форматирование текста ВК")
window.geometry('400x250')
window.bind("<Control-KeyPress>", keypress)

f_check = Frame(window)
f_but = Frame(window)

chk_state1 = IntVar()
chk_state2 = IntVar()

lbl = Label(window, text="Введите текст, который хотите форматировать:")
lbl.pack()

txt_in = scrolledtext.ScrolledText(window, width=40, height=1)
txt_in.pack()

chk1 = Checkbutton(f_check, text='Подчёркнутый', variable = chk_state1, onvalue=1, offvalue=0, width=20)
chk2 = Checkbutton(f_check, text='Зачёркнутый', variable = chk_state2, onvalue=1, offvalue=0, width=20)
f_check.pack()
chk1.pack(side=LEFT)
chk2.pack(side=RIGHT)

submit = Button(f_but, text="Применить", command = format_txt)  
reset = Button(f_but, text="Очистить", command = clear)  
f_but.pack()
submit.pack(side=LEFT, padx=20)
reset.pack(side=RIGHT, padx=20)

lbl2 = Label(window, text="Отформатированный для ВК текст:")
lbl2.pack()

txt_out = scrolledtext.ScrolledText(window, width=40, height=1)
txt_out.pack()

copy = Button(window, text='Копировать в буфер обмена', command = copy_clpbrd)
copy.pack()

window.update()
window.mainloop()