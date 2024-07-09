import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

class DCSApp:
    """
    simple demo appp for the data visualization

    """
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("DCS Data Visualization")
        self.root.minsize(1080, 800)
        self.frame_list = []

        self.xdata = [[] for _ in range(3)]
        self.ydata = []

    def set_ydata(self, ydata):
        self.ydata = ydata
        print(self.ydata)

    def create_plot(self, number:int) -> tuple:
        # Function to create a matplotlib plot
        # make the input outside the function
        fig = Figure(figsize=(10, 8), dpi=100)
        plot_list = []
        for i in range(1, number, 1):
            plot = fig.add_subplot(2, 2, i)
            plot.set_xlim(0, 40)
            plot.set_ylim(0, 10)
            plot_list.append(plot)
        return fig, plot_list

    def create_frame(self):
        frame = ttk.Frame(self.root, padding=10)
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        return frame

    def create_canvas(self, fig, frame):
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        return canvas

    def update_plot(self, fig, plots, canvas, frame):
        # make the input outside the function
        fig = Figure(figsize=(10, 8), dpi=100)
        for i in range(3):
            self.xdata[i].append(len(self.xdata[i]))
            # self.ydata[i].append(random.randint(0, 10))

            if len(self.xdata[i]) > 100:
                self.xdata[i] = self.xdata[i][1:]
                self.ydata[i] = self.ydata[i][1:]

            plots[i].clear()
            plots[i].plot(self.xdata[i], self.ydata[i])

        self.create_canvas(fig, frame)
        self.root.after(400, self.update_plot, fig, plots, canvas, frame)

    def button(self):
        raise NotImplementedError

    def run(self):
        frame = self.create_frame()

        # Create the matplotlib plot
        fig, plots = self.create_plot(5)
        canvas = self.create_canvas(fig, frame)

        # Embed the plot in the Tkinter frame

        # Start the update process
        self.root.after(400, self.update_plot, fig, plots, canvas, frame)
        # Run the Tkinter event loop
        self.root.mainloop()




