import socket
from tkinter import *

tabs = {1: 'home'}
current = 1

window = Tk()
window.geometry('1000x600')
window.title('Night Browser')

if tabs[current] == 'home':
    url = Entry(window, text='Night', font='/System/Library/Fonts/Avenir.ttc', background='#292929', borderwidth='3px', foreground='white')
    search = Entry(window, text='Night', font='/System/Library/Fonts/Avenir.ttc', background='#292929', borderwidth='3px', foreground='white')

    url.place(x=100, y=50, width=800)
    search.place(x=300, y=300, width=400, height=50)

    window.configure(background='#191919')

window.mainloop()

