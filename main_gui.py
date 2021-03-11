import tkinter as tk

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
        self.mag = 80
        self.rows = 4
        self.cols = 4

        self.c = tk.Canvas(self, width=self.mag*self.cols+2*self.mag, height = self.mag*self.rows+2*self.mag, bg='white')

        self.DrawGrid()

        grid = self.c
        grid.pack(side="top", fill="both", expand=True)

    def DrawGrid(self):
        for i in range(0,self.cols+1):
            self.c.create_line((i+1)*self.mag,self.mag, (i+1)*self.mag,(self.rows+1)*self.mag)
        for i in range(0,self.rows+1):
            self.c.create_line(self.mag,(i+1)*self.mag, self.mag*(1+self.cols),(i+1)*self.mag)


class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 2")
        label.pack(side="top", fill="both", expand=True)

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
    root.wm_geometry("800x480")
    root.title("Project ADMS")
    root.mainloop()

if __name__ == "__main__":
    main()