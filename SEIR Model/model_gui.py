from model_core import *
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
matplotlib.use('TkAgg')

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('SEIR Model')
        self.root.geometry('1200x500')
        self.mainframe = tk.Frame(self.root)
        self.mainframe.grid()
        self.label_text = ['Total population', 'Number of person infected at time = 0',
                    'Number of person infected by another person per day', 'Duration of the infection in days',
                      'Incubation period in days','Duration of the simulation']
        self.nb_var=6
        label_list=[0]*self.nb_var
        entry_list=[0]*self.nb_var
        # setting entry and labels
        for k in range(self.nb_var):
            label_list[k] = tk.Label(self.mainframe, text=self.label_text[k], pady='5')
            label_list[k].grid(row=2*k, column=0)
            entry_list[k] = tk.Entry(self.mainframe,)
            entry_list[k].grid(row=2*k+1, column=0)
        button=tk.Button(self.mainframe, text='Compute', pady='10', command=lambda : self.compute(entry_list))
        button.grid(row=12,column=0)

        self.root.mainloop()

    def compute(self,entry_list):
        vector = [0]*len(entry_list)
        for k in range(len(entry_list)):
            vector[k] = entry_list[k].get()
        model = Model(float(vector[0]), float(vector[1]), float(vector[2]), float(vector[3]), float(vector[4]), int(vector[5]))
        fig = model.plot(model.run_model())
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.get_tk_widget().grid(row=0, rowspan=12, column=1)
        canvas.draw()


if __name__ == '__main__':
    U = GUI()