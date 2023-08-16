from tkinter import *
from tkinter.ttk import Progressbar
from Employee import employee


root = Tk()

image = PhotoImage(file='images\\loading33.png')
 
height = 653
width = 736
x = (root.winfo_screenwidth()//2)-(width//2)
y = (root.winfo_screenheight()//2)-(height//2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.overrideredirect(1)
 
root.wm_attributes('-topmost', True)

root.wm_attributes("-disabled", True)
root.wm_attributes("-transparentcolor", "black")
 
bg_label = Label(root, image=image, bg='black')
bg_label.place(x=0, y=0)
 
progress_label = Label(root, text="Please Wait...", font=('Arial', 10), fg='white', bg='#15193f')
progress_label.place(x=190, y=505)
progress = Progressbar(root, orient=HORIZONTAL, length=360, mode='determinate')
progress.place(x=190, y=480)
 

i = 0

def load_program():
    root.destroy()
    app = employee()
    app.mainloop()
    

 
def load():
    global i
    if i <= 100:
        txt = 'Loading Database...  ' + (str(i)+'%')
        progress_label.config(text=txt)
        progress_label.after(30, load)
        progress['value'] = i
        i += 1
    else:
      load_program()
        
load()
 
root.mainloop()
