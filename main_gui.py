import tkinter
import tkinter.font as tkFont

#myFont = tkFont.Font(family = 'Helvetica', size = 36, weight = 'bold')

class App:

    def __init__(self, master) -> None:

        self.master = master
        self.pad_view_btn=tkinter.Button(self.master, text="PAD", command = self.pad_view, background="white")
        self.pad_view_btn.grid(row=1,column=0)

        self.seq_view_btn=tkinter.Button(self.master, text="Sequencer", command = self.seq_view, background="white")
        self.seq_view_btn.grid(row=2,column=0)

    def pad_view(self):
        print ("Pad view pressed")
        self.pad_view_btn.configure(background='green')
        self.seq_view_btn.configure(background='white')


    def	seq_view(self):
        print ("Seq view pressed")
        self.seq_view_btn.configure(background='green')
        self.pad_view_btn.configure(background='white')








if __name__ == "__main__":

    master=tkinter.Tk()
    master.title("Project ADMS")
    master.geometry('800x480')

    app = App(master)

    master.mainloop()