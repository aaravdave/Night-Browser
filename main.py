import socket
from tkinter import *


def start_search():  # The Moon Search Engine
    the_search = search.get()


tabs = {1: 'home'}
current = 1

window = Tk()
window.geometry('1000x600')
window.title('Night Browser')

if tabs[current] == 'home':
    url = Entry(window, text='Night', font='/System/Library/Fonts/Avenir.ttc', background='#292929', borderwidth='3px', foreground='white')
    search = Entry(window, text='y', font='/System/Library/Fonts/Avenir.ttc', background='#292929', borderwidth='3px', foreground='white')

    url.place(x=100, y=50, width=800)
    search.place(x=275, y=300, width=400, height=50)

    search_button = Button(window, text='🔎', command=start_search)
    search_button.place(x=675, y=300, width=50, height=50)
else:
    pass

window.configure(background='#191919')
window.mainloop()
