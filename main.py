# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 11:20:45 2019

@author: Jasleen Kaur
"""

from tkinter import *
import tkinter as tk
import tkinter.messagebox as tm


def my_fun():

  class Page(tk.Frame):
      def __init__(self, *args, **kwargs):
          tk.Frame.__init__(self, *args, **kwargs)

      def show(self):
          self.lift()

  class Page1(Page):
      def __init__(self, *args, **kwargs):
          Page.__init__(self, *args, **kwargs)

          tk.Label(self, text="With your current score, you qualify for these HSBC products:", font=("Arial Bold", 20)).grid(row=0, sticky=W)
          tk.Label(self, text="House loans", font=("Arial", 15)).grid(row=1, column=0, sticky=W)
          tk.Label(self, text="Car loans", font=("Arial", 15)).grid(row=1, column=1, sticky=W)
          tk.Label(self, text="Mortgages", font=("Arial", 15)).grid(row=2, column=0, sticky=W)
          tk.Label(self, text="Credit Cards", font=("Arial", 15)).grid(row=2, column=1, sticky=W)
          tk.Label(self, text="Savings Accounts", font=("Arial", 15)).grid(row=3, column=0, sticky=W)
          tk.Label(self, text="More...", font=("Arial", 15)).grid(row=3, column=1, sticky=W)

  class Page2(Page):
      def __init__(self, *args, **kwargs):
          Page.__init__(self, *args, **kwargs)
          w = Canvas(self, width=700, height=360)
          w.pack(side=BOTTOM)
          label = tk.Label(self, text="Smart Score History")
          label.pack(side="bottom", fill="both")
          
          label1 = tk.Label(self, text="Analytics:")
          label1.place(x=0,y=0)

          label2 = tk.Label(self, text="Your current score is: 330 ")
          label2.place(x=0, y=20)

          label3 = tk.Label(self, text="The factor that has improved your score most is: timely rent payments")
          label3.place(x=0, y=40)

          w.create_line(50, 350, 50, 50, tags="xaxis")
          w.create_line(50, 350, 550, 350, tags="yaxis")
          scores = [345, 300, 270, 220, 180, 100]
          accumulator = 50
          for x in range(1, 6):
              w.create_line(accumulator, scores[x - 1], accumulator + 100, scores[x], tags="graph", activewidth=2)
              accumulator += 100

  class Page3(Page):
      def __init__(self, *args, **kwargs):
          Page.__init__(self, *args, **kwargs)
          label = tk.Label(self, text="Transparency, to you.")
          label.pack(side="top", anchor=NW)

          textbox = tk.Text(self, wrap=WORD)
          textbox.insert(INSERT, "Here at SmartScore, we believe that we can make credit scores easy and transparent. ")
          textbox.insert(INSERT, "Here at SmartScore, we believe that we can make credit scores easy and transparent. ")
          textbox.insert(INSERT, "Here at SmartScore, we believe that we can make credit scores easy and transparent. ")
          textbox.insert(INSERT, "Here at SmartScore, we believe that we can make credit scores easy and transparent. ")
          textbox.insert(INSERT, "Here at SmartScore, we believe that we can make credit scores easy and transparent. ")
          textbox.insert(INSERT, "Here at SmartScore, we believe that we can make credit scores easy and transparent. ")
          textbox.insert(INSERT, "Here at SmartScore, we believe that we can make credit scores easy and transparent. ")
          textbox.insert(INSERT, "Here at SmartScore, we believe that we can make credit scores easy and transparent. ")
          textbox.insert(INSERT, "Here at SmartScore, we believe that we can make credit scores easy and transparent. ")
          textbox.insert(INSERT, "Here at SmartScore, we believe that we can make credit scores easy and transparent. ")
          textbox.insert(INSERT, "Here at SmartScore, we believe that we can make credit scores easy and transparent. ")
          textbox.insert(INSERT, "Here at SmartScore, we believe that we can make credit scores easy and transparent. ")
          textbox.insert(INSERT, "Here at SmartScore, we believe that we can make credit scores easy and transparent. ")
          textbox.insert(INSERT, "Here at SmartScore, we believe that we can make credit scores easy and transparent. ")
          textbox.insert(INSERT, "Here at SmartScore, we believe that we can make credit scores easy and transparent. ")
          textbox.insert(INSERT, "Here at SmartScore, we believe that we can make credit scores easy and transparent. ")
          textbox.insert(INSERT, "Here at SmartScore, we believe that we can make credit scores easy and transparent. ")
          textbox.insert(INSERT, "Here at SmartScore, we believe that we can make credit scores easy and transparent. ")
          textbox.insert(INSERT, "Here at SmartScore, we believe that we can make credit scores easy and transparent. ")
          textbox.insert(INSERT, "Here at SmartScore, we believe that we can make credit scores easy and transparent. ")
          textbox.config(state=DISABLED)
          textbox.pack(side=TOP, expand=TRUE)

  class Page4(Page):
      def __init__(self, *args, **kwargs):
          Page.__init__(self, *args, **kwargs)
          w = Canvas(self, width=700, height=360)
          w.pack(side=BOTTOM)
          label = tk.Label(self, text="Block chain visualization")
          label.pack(side="bottom", fill="both")

  class Page5(Page):
      def __init__(self, *args, **kwargs):
          Page.__init__(self, *args, **kwargs)
          w = Canvas(self, width=700, height=360)
          w.pack(side=BOTTOM)
          label = tk.Label(self, text="Transfer score")
          label.pack(side="bottom", fill="both")

  class MainView(tk.Frame):
      def __init__(self, *args, **kwargs):
          tk.Frame.__init__(self, *args, **kwargs)
          p1 = Page1(self)
          p2 = Page2(self)
          p3 = Page3(self)
          p4 = Page4(self)
          p5 = Page5(self)
          
          buttonframe = tk.Frame(self)
          container = tk.Frame(self)
          buttonframe.pack(side="top", fill="x", expand=False)
          container.pack(side="top", fill="both", expand=True)

          p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
          p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
          p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
          p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
          p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            
          b1 = tk.Button(buttonframe, text="HSBC Products", command=p1.lift)
          b2 = tk.Button(buttonframe, text="Analytics", command=p2.lift)
          b3 = tk.Button(buttonframe, text="Score Calculation", command=p3.lift)
          b4 = tk.Button(buttonframe, text="Blockchain", command=p4.lift)
          b5 = tk.Button(buttonframe, text="Transfer Score", command=p5.lift)

          b1.pack(side="left")
          b2.pack(side="left")
          b3.pack(side="left")
          b4.pack(side="left")
          b5.pack(side="left")

          p1.show()

  if __name__ == "__main__":
        root = tk.Tk()
        root.title("SmartScore")
        main = MainView(root)
        main.pack(side="top", fill="both", expand=TRUE)
        root.wm_geometry("700x700")
        root.mainloop()



class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_username = Label(self, text="Username:")
        self.label_password = Label(self, text="Password:")

        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")

        self.label_username.grid(row=0, sticky=E)
        self.label_password.grid(row=1, sticky=E)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        self.checkbox = Checkbutton(self, text="Keep me logged in")
        self.checkbox.grid(columnspan=2)

        self.logbtn = Button(self, text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2)

        self.pack()
        
    def _login_btn_clicked(self):
        # print("Clicked")
        username = self.entry_username.get()
        password = self.entry_password.get()

        # print(username, password)

        if username == "j" and password == "a":
            # tm.showinfo("SmartScore", "Welcome John")
            #
            # window = Tk()
            # window.geometry('700x700')
            # window.title("Welcome to SmartScore")
            self.master.destroy()
            my_fun()
            #
            #
            # #title
            # theLabel = Label(window, text="Your Score", font=("Arial Bold", 40))
            # #theLabel.pack()
            # theLabel.place(x=35,y=20)
            #
            #
            # theLabe2 = Label(window, text="Would you like to transfer your score internationally?")
            # #theLabel.pack()
            # theLabe2.place(x=40,y=80)
            #
            #
            # #make a button
            # btn1 = Button(window, text="Transfer Score Now", bg="grey", fg="blue")
            # btn1.place(x=120, y= 100)
            #
            #
            # btn2 = Button(window, text="Later", command = my_fun)
            # btn2.place(x= 150, y=130)

            #keep loop running
            #window.mainloop()

def logscreen():
    newwindow = Tk()
    newwindow.title("Log in Screen")
    LoginFrame(newwindow)

root = Tk()
root.title("SmartScore Web UI")
root.geometry('400x700')
Label(root, text="Smart Score", font="none 30 bold").place(x=200, y=300, anchor=CENTER)
Label(root, text="Launched by HSBC Canada", font="none 15 bold").place(x=200, y=600, anchor=CENTER)
login = Button(root, text="Log In", command=logscreen)
login.pack(side=LEFT, anchor=S, fill=X)
exit = Button(root, text="Exit", command=root.destroy)
exit.pack(side=RIGHT, anchor=S, fill=X)
root.mainloop()