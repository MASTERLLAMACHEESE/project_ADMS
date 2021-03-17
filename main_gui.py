import tkinter as tk
import tkinter.font as tkfont
import tkinter.ttk
from tkinter import HORIZONTAL, VERTICAL

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
    #    label = tk.Label(self, text="This is page 1")
    #    label.pack(side="top", fill="both", expand=True)
        fontstyle = tkfont.Font(family="Lucida Grande", size=20)

        tk.Label(self, text="Kick 1", font=fontstyle).grid(row=1, column=1)
        tk.Label(self, text="Snare 1", font=fontstyle).grid(row=3, column=1)
        tk.Label(self, text="Closed Hat 1", font=fontstyle).grid(row=5, column=1)
        tk.Label(self, text="Closed Hat 5", font=fontstyle).grid(row=7, column=1)
        

        tk.Label(self, text="Kick 2", font=fontstyle).grid(row=1, column=3)
        tk.Label(self, text="Snare 2", font=fontstyle).grid(row=3, column=3)
        tk.Label(self, text="Closed Hat 2", font=fontstyle).grid(row=5, column=3)
        tk.Label(self, text="Crash 1", font=fontstyle).grid(row=7, column=3)


        tk.Label(self, text="Kick 3", font=fontstyle).grid(row=1, column=5)
        tk.Label(self, text="Snare 3", font=fontstyle).grid(row=3, column=5)
        tk.Label(self, text="Closed Hat 3", font=fontstyle).grid(row=5, column=5)
        tk.Label(self, text="Tom 1", font=fontstyle).grid(row=7, column=5)

        tk.Label(self, text="Kick 4", font=fontstyle).grid(row=1, column=7)
        tk.Label(self, text="Clap 1", font=fontstyle).grid(row=3, column=7)
        tk.Label(self, text="Closed Hat 4", font=fontstyle).grid(row=5, column=7)
        tk.Label(self, text="Floor Tom 1", font=fontstyle).grid(row=7, column=7)

        tkinter.ttk.Separator(self, orient=VERTICAL).grid(column=0, row=0, rowspan=8, sticky='ns')
        tkinter.ttk.Separator(self, orient=VERTICAL).grid(column=2, row=0, rowspan=8, sticky='ns')
        tkinter.ttk.Separator(self, orient=VERTICAL).grid(column=4, row=0, rowspan=8, sticky='ns')
        tkinter.ttk.Separator(self, orient=VERTICAL).grid(column=6, row=0, rowspan=8, sticky='ns')
        tkinter.ttk.Separator(self, orient=VERTICAL).grid(column=8, row=0, rowspan=8, sticky='ns')

        tkinter.ttk.Separator(self, orient=HORIZONTAL).grid(column=0, row=0, columnspan=8, sticky='ew')
        tkinter.ttk.Separator(self, orient=HORIZONTAL).grid(column=0, row=2, columnspan=8, sticky='ew')
        tkinter.ttk.Separator(self, orient=HORIZONTAL).grid(column=0, row=4, columnspan=8, sticky='ew')
        tkinter.ttk.Separator(self, orient=HORIZONTAL).grid(column=0, row=6, columnspan=8, sticky='ew')
        tkinter.ttk.Separator(self, orient=HORIZONTAL).grid(column=0, row=8, columnspan=8, sticky='ew')

class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        # label = tk.Label(self, text="This is page 2")
        # label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="   Pad   ", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Sequencer", command=p2.lift)

        b1.pack(side="left")
        b2.pack(side="left")

        p1.show()


def main():
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("800x800")
    root.title("Project ADMS")
    root.mainloop()

if __name__ == "__main__":
    main()