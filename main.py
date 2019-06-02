import tkinter as tk
from tkinter import ttk
import frames
from Graphs import scatter,bargraph

strings = ''
# class SeaofBTCapp(tk.Tk):
class SentAna(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "SentAna App")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        # filemenu.add_command(label="Save settings", command=lambda:self.show_frame(frames.savesettings) )
        # filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        filemenu.add_command(label="collect data",command=lambda :self.show_frame(frames.CollectionData))
        menubar.add_cascade(label="File", menu=filemenu)

        algorithm = tk.Menu(menubar, tearoff=1)
        # algorithm.add_command(label="Naive-Bayes",
        #                            command=lambda: self.show_frame(frames.NaiveBayesGUI))
        # algorithm.add_command(label="MultinomialNaivebayes",
        #                            command=lambda: self.show_frame(frames.MultinomialNaivebayes))
        # algorithm.add_command(label="BernoulliNaivebayes",
        #                            command=lambda: self.show_frame(frames.BinomialNaivebayes))
        # algorithm.add_command(label="LogisticRegression",
        #                            command=lambda: self.show_frame(frames.LogisticRegeration))
        # algorithm.add_command(label="NuSVC",
        #                            command=lambda: self.show_frame(frames.NuSVC))
        #

        algorithm.add_command(label="Hybrid",
                                   command=lambda: self.show_frame(frames.Hybrid))
        menubar.add_cascade(label="SentAna", menu=algorithm)

        # dataTF = tk.Menu(menubar, tearoff=1)
        # dataTF.add_command(label="Tick",
        #                    command=lambda: frames.n.popupmessage('tick'))
        # dataTF.add_command(label="1 day",
        #                    command=lambda: frames.n.popupmessage('1d'))
        # dataTF.add_command(label="3 day",
        #                    command=lambda: frames.n.popupmessage('3d'))
        # dataTF.add_command(label="1 Week",
        #                    command=lambda: frames.n.popupmessage('7d'))
        # menubar.add_cascade(label="Data Time Frame", menu=dataTF)

        # TIME_INTR = tk.Menu(menubar, tearoff=1)
        #
        # TIME_INTR.add_command(label="Tick",
        #                   command=lambda: frames.n.popupmessage('tick'))
        # TIME_INTR.add_command(label="1 minute",
        #                   command=lambda: frames.n.popupmessage('1Min'))
        # TIME_INTR.add_command(label="5 minute",
        #                   command=lambda: frames.n.popupmessage('5Min'))
        # TIME_INTR.add_command(label="15 minute",
        #                   command=lambda: frames.n.popupmessage('15Min'))
        # TIME_INTR.add_command(label="30 minute",
        #                   command=lambda: frames.n.popupmessage('30Min'))
        # TIME_INTR.add_command(label="1 Hour",
        #                   command=lambda: frames.n.popupmessage('1H'))
        # TIME_INTR.add_command(label="3 Hour",
        #                   command=lambda: frames.n.popupmessage('3H'))
        # menubar.add_cascade(label="Time Interval", menu=TIME_INTR)

        # topIndi = tk.Menu(menubar, tearoff=1)
        # topIndi.add_command(label="None",
        #                     command=lambda: frames.n.popupmessage('none'))
        # topIndi.add_separator()
        # topIndi.add_command(label="MODI",
        #                     command=lambda: frames.n.popupmessage('MODI'))
        # topIndi.add_command(label="RAHUL",
        #                     command=lambda: frames.n.popupmessage('RAHUL'))
        # topIndi.add_command(label="Kejriwal",
        #                     command=lambda: frames.n.popupmessage('Kejriwal'))

        # menubar.add_cascade(label="Top Indicator", menu=topIndi)

        resultgraphs = tk.Menu(menubar, tearoff=1)
        # resultgraphs.add_command(label="None",
        #                   command=lambda: frames.n.popupmessage('none'))

        resultgraphs.add_command(label="BAR",
                          command=lambda: self.show_frame(frames.BarGraph))
#         resultgraphs.add_command(label="Scatter Plot",
#                           command=scatter.app.run_server(debug=True)
        resultgraphs.add_separator()
# )
        resultgraphs.add_command(label="Popularity Chart",
                          command=lambda: self.show_frame(frames.Wordcloud))
        resultgraphs.add_command(label="Popularity In Percentage",
                      command=lambda: self.show_frame(frames.Pychart))
        resultgraphs.add_separator()
        menubar.add_cascade(label="Graph Indicator", menu=resultgraphs)


        startStop = tk.Menu(menubar, tearoff=1)
        startStop.add_command(label="Party Comparison",
                              command=lambda: self.show_frame(frames.positivecomp))
        # startStop.add_command(label="Negative",
        #
        #                       command=lambda: self.show_frame(frames.Negativecomp))
        menubar.add_cascade(label="Comparison", menu=startStop)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Tutorial", command=lambda :self.show_frame(frames.helppage))
        menubar.add_cascade(label="Help", menu=helpmenu)

        tk.Tk.config(self,menu=menubar)

        self.frames = {}
        for F in (frames.helppage,frames.Negativecomp,frames.positivecomp,frames.StartPage,frames.CollectionData,frames.Hybrid,frames.Wordcloud,frames.BarGraph,frames.Pychart):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(frames.StartPage)

        tk.Tk.iconbitmap(self, default='photo/logo.ico')


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()



app = SentAna()
app.geometry("800x800")

# ani = animation.FuncAnimation(n.f, animate, interval=1000)
app.mainloop()
