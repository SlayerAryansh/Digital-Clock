#!/usr/bin/env python
# coding: utf-8

# In[22]:


from tkinter import Tk
from tkinter import Label

import time

root = Tk()
root.title("Clock")
def present_time():
    display_time = time.strftime("%H:%M:%S    %d-%m-%y    %A")
    digi_clock.config(text = display_time)
    digi_clock.after(100,present_time)


digi_clock = Label(root,font = ("Arial",100), bg = "#99ccff", fg = "#ffcc00" )
digi_clock.pack()
present_time()

root.mainloop()


# In[ ]:




