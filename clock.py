from tkinter import Tk #creating window
from tkinter import Label #label in that window
import time 

root=Tk()#storing the window
root.title("Digital clock")

def pre_time():
    display_time=time.strftime("%I:%M:%S:%p")#current time
    display_date=time.strftime("%D")
    digi_clock.config(text=f"{display_time}\n{display_date}")
    digi_clock.after(150,pre_time)#after 150ms time func wll run

digi_clock=Label(root,font=("times new roman",125))
digi_clock.pack()#fit into the window

def update_bg():
    current_hour = int(time.strftime("%H"))
    if 6 <= current_hour < 18:
        root.configure(bg="lightblue")
        digi_clock.configure(bg="lightblue")
       # date_label.configure(bg="lightblue")
    else:
        root.configure(bg="darkblue")
        digi_clock.configure(bg="darkblue", fg="white")
       # date_label.configure(bg="darkblue", fg="white")
    root.after(60000, update_bg)  # check every minute

update_bg()
pre_time()
root.mainloop()#displaying the output

