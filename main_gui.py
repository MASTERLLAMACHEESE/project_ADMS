import tkinter as tk
import tkinter.font as tkfont
import tkinter.ttk
from tkinter import HORIZONTAL, VERTICAL
import module
import threading

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
    def __init__(self, *args, **kwargs):
        """
        layout for page 1, PAD, creates, grid to show what sound is where
        """
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
        self.active_list = [[] for y in range(16)]

        self.fontstyle = tkfont.Font(family="Lucida Grande", size=12)

        self.position = {
            1 : (1, 5, 9, 13),
            3 : (2, 6, 10, 14),
            5 : (3, 7, 11, 15),
            7 : (4, 8, 12, 16),
        }

        tk.Label(self, text="Bar 1", font=self.fontstyle).grid(row=0, column=0)
        tk.Label(self, text="Hit 1", font=self.fontstyle).grid(row=0, column=1)
        tk.Label(self, text="Hit 2", font=self.fontstyle).grid(row=0, column=3)
        tk.Label(self, text="Hit 3", font=self.fontstyle).grid(row=0, column=5)
        tk.Label(self, text="Hit 4", font=self.fontstyle).grid(row=0, column=7)

        tkinter.ttk.Separator(self, orient=VERTICAL).grid(column=0, row=1, rowspan=21, sticky='ns')
        tkinter.ttk.Separator(self, orient=VERTICAL).grid(column=2, row=0, rowspan=21, sticky='ns')
        tkinter.ttk.Separator(self, orient=VERTICAL).grid(column=4, row=0, rowspan=21, sticky='ns')
        tkinter.ttk.Separator(self, orient=VERTICAL).grid(column=6, row=0, rowspan=21, sticky='ns')
        tkinter.ttk.Separator(self, orient=VERTICAL).grid(column=8, row=0, rowspan=21, sticky='ns')

        tkinter.ttk.Separator(self, orient=HORIZONTAL).grid(column=0, row=1, columnspan=18, sticky='ew')
        tkinter.ttk.Separator(self, orient=HORIZONTAL).grid(column=0, row=6, columnspan=18, sticky='ew')
        tkinter.ttk.Separator(self, orient=HORIZONTAL).grid(column=0, row=11, columnspan=18, sticky='ew')
        tkinter.ttk.Separator(self, orient=HORIZONTAL).grid(column=0, row=16, columnspan=18, sticky='ew')
        tkinter.ttk.Separator(self, orient=HORIZONTAL).grid(column=0, row=21, columnspan=18, sticky='ew')

        tk.Label(self, text="Bar 2", font=self.fontstyle).grid(row=0, column=9)
        tk.Label(self, text="Hit 1", font=self.fontstyle).grid(row=0, column=10)
        tk.Label(self, text="Hit 2", font=self.fontstyle).grid(row=0, column=13)
        tk.Label(self, text="Hit 3", font=self.fontstyle).grid(row=0, column=15)
        tk.Label(self, text="Hit 4", font=self.fontstyle).grid(row=0, column=17)

        tkinter.ttk.Separator(self, orient=VERTICAL).grid(column=9, row=1, rowspan=21, sticky='ns')
        tkinter.ttk.Separator(self, orient=VERTICAL).grid(column=12, row=0, rowspan=21, sticky='ns')
        tkinter.ttk.Separator(self, orient=VERTICAL).grid(column=14, row=0, rowspan=21, sticky='ns')
        tkinter.ttk.Separator(self, orient=VERTICAL).grid(column=16, row=0, rowspan=21, sticky='ns')
        tkinter.ttk.Separator(self, orient=VERTICAL).grid(column=18, row=0, rowspan=21, sticky='ns')

        tk.Label(self, text="Bar 2", font=self.fontstyle).grid(row=22, column=0)
        tk.Label(self, text="Hit 1", font=self.fontstyle).grid(row=22, column=1)
        tk.Label(self, text="Hit 2", font=self.fontstyle).grid(row=22, column=3)
        tk.Label(self, text="Hit 3", font=self.fontstyle).grid(row=22, column=5)
        tk.Label(self, text="Hit 4", font=self.fontstyle).grid(row=22, column=7)

        tkinter.ttk.Separator(self, orient=VERTICAL).grid(column=0, row=23, rowspan=21, sticky='ns')
        tkinter.ttk.Separator(self, orient=VERTICAL).grid(column=2, row=22, rowspan=21, sticky='ns')
        tkinter.ttk.Separator(self, orient=VERTICAL).grid(column=4, row=22, rowspan=21, sticky='ns')
        tkinter.ttk.Separator(self, orient=VERTICAL).grid(column=6, row=22, rowspan=21, sticky='ns')
        tkinter.ttk.Separator(self, orient=VERTICAL).grid(column=8, row=22, rowspan=21, sticky='ns')

        tkinter.ttk.Separator(self, orient=HORIZONTAL).grid(column=0, row=23, columnspan=18, sticky='ew')
        tkinter.ttk.Separator(self, orient=HORIZONTAL).grid(column=0, row=28, columnspan=18, sticky='ew')
        tkinter.ttk.Separator(self, orient=HORIZONTAL).grid(column=0, row=33, columnspan=18, sticky='ew')
        tkinter.ttk.Separator(self, orient=HORIZONTAL).grid(column=0, row=38, columnspan=18, sticky='ew')
        tkinter.ttk.Separator(self, orient=HORIZONTAL).grid(column=0, row=43, columnspan=18, sticky='ew')

        tk.Label(self, text="Bar 2", font=self.fontstyle).grid(row=22, column=9)
        tk.Label(self, text="Hit 1", font=self.fontstyle).grid(row=22, column=10)
        tk.Label(self, text="Hit 2", font=self.fontstyle).grid(row=22, column=13)
        tk.Label(self, text="Hit 3", font=self.fontstyle).grid(row=22, column=15)
        tk.Label(self, text="Hit 4", font=self.fontstyle).grid(row=22, column=17)

        tkinter.ttk.Separator(self, orient=VERTICAL).grid(column=9, row=23, rowspan=21, sticky='ns')
        tkinter.ttk.Separator(self, orient=VERTICAL).grid(column=12, row=22, rowspan=21, sticky='ns')
        tkinter.ttk.Separator(self, orient=VERTICAL).grid(column=14, row=22, rowspan=21, sticky='ns')
        tkinter.ttk.Separator(self, orient=VERTICAL).grid(column=16, row=22, rowspan=21, sticky='ns')
        tkinter.ttk.Separator(self, orient=VERTICAL).grid(column=18, row=22, rowspan=21, sticky='ns')

    def gui_places(self):
        #get text created in adms.py from module.py and set it to the correct text field in grid
        for e in module.gui_list:
            if e not in self.active_list[module.beat_in_seq]:
                for x in range (16):
                    if module.beat_in_seq == x:
                        amount = len(self.active_list[module.beat_in_seq])
                        if amount < 4:
                            if amount >= 1 and (amount + 1) < 4:
                                amount =+ 1
                            for key, value in self.position:
                                if module.beat_in_seq in value:
                                    column_space = key
                            tk.Label(self, text=module.gui_list[module.beat_in_seq], font=self.fontstyle).grid(column=column_space, row=amount)

        #get text removed in adms.py from module.py and remove it from the correct text field in grid
        for y in self.active_list:
            if y not in module.gui_list[module.beat_in_seq]:
                 for x in range (16):
                    if module.beat_in_seq == x:
                        amount = len(self.active_list[module.beat_in_seq])
                        if amount < 4:
                            if amount >= 1 and (amount + 1) < 4:
                                amount =+ 1
                            for key, value in self.position:
                                if module.beat_in_seq in value:
                                    column_space = key
                            tk.Label(self, text="      ", font=self.fontstyle).grid(column=column_space, row=amount)


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

def start_gui():
    """
    Start gui thread
    ToDo These threads probably don't need to exist as threads, but there's no time to change that
    We could just make callback functions for them
    def change_seq_led(pos)
    def togglePitchLed() etc
    """
    threading.Thread(target=main).start()