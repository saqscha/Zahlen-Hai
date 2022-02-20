
from tkinter import *
from PIL import Image, ImageTk
import os.path

class App():
    def level1(self):
        lvl1 = Toplevel(root)
        lvl1.title('Zahlen-Hai Lvl 1')
        lvl1.geometry('400x200')

    def level2(self):
        lvl2 = Toplevel(root)
        lvl2.title('Zahlen-Hai Lvl 2')
        lvl2.geometry('400x200')

    def level3(self):
        lvl3 = Toplevel(root)
        lvl3.title('Zahlen-Hai Lvl 3')
        lvl3.geometry('400x200')


    def __init__(self, master):
        root.geometry('320x550')
        root.title('Zahlenhai')
        root.config(background='black')

        #head_image
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.head_img = Image.open(os.path.join(self.script_dir, 'Assets/head_img.png')).convert('RGB')
        self.head_img = ImageTk.PhotoImage(self.head_img)
        

        #frames
        self.top_frame = Frame(master, width=300, bg='black')
        self.bottom_frame = Frame(master, width=300, height=100, bg='black')

        self.top_frame.grid(row=0, column=0)
        self.bottom_frame.grid(row=1, column=0, pady=100)

        #widgets
        self.head_label = Label(self.top_frame, bg='black', image=self.head_img,)
        self.button1 = Button(self.bottom_frame, text='Level 1', width=30, highlightbackground='black', \
            font=('Arial',16,'bold'), command=self.level1)
        self.button2 = Button(self.bottom_frame, text='Level 2', width=30, highlightbackground='black', \
            font=('Arial',16,'bold'), command=self.level2)
        self.button3 = Button(self.bottom_frame, text='Level 3', width=30, highlightbackground='black', \
            font=('Arial',16,'bold'), command=self.level3)

        self.head_label.grid(row=0, column=0, padx=10, pady=40)
        self.button1.grid(row=0, pady=10)
        self.button2.grid(row=1, pady=10)
        self.button3.grid(row=2, pady=10)

        #config widgets
        
        
root = Tk()
app = App(root)
root.mainloop()