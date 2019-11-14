# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 11:20:45 2019

@author: Jasleen Kaur
"""

from tkinter import *
import tkinter as tk
import tkinter.messagebox as tm
from SmartBlockChain import SmartBlockChain
from SmartBlock import SmartBlock

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
          w = Canvas(self, width=400, height=360, bg="Light Pink")
          w.pack(side=BOTTOM)
          label = tk.Label(self, text="Average Score Trends", bg="Light Pink")
          label.place(x=200, y=350, anchor=CENTER)
          analytics = PhotoImage(file="analytics.png")
          label1 = tk.Label(self, image=analytics)
          label1.image = analytics
          label1.place(x=200,y=150, anchor=CENTER)

          w.create_line(50, 350, 50, 50, tags="xaxis")
          w.create_line(50, 350, 350, 350, tags="yaxis")
          scores = [345, 300, 270, 220, 180, 100]
          accumulator = 50
          for x in range(1, len(scores)):
              w.create_line(accumulator, scores[x - 1], accumulator + 60, scores[x], tags="graph", activewidth=2)
              accumulator += 60

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
          w = Canvas(self, width=400, height=650)
          w.pack(side=BOTTOM, pady=10)
          user_name = "user1"
          file_name = "UserData.json"
          accumulator = 0
          chain = SmartBlockChain(user_name, file_name)
          temp_smartscore = 700
          for block_of_json in chain.decode_block_chain()[user_name]:
              temp_smartscore += block_of_json["score_delta"]
              Label(w, text="Change in score:", bg="Light Pink", borderwidth=1, relief="solid").grid(row=accumulator, column=0, sticky=W+E)
              Label(w, text=block_of_json["score_delta"], bg="Light Pink", borderwidth=1, relief="solid").grid(row=accumulator+1, column=0, sticky=W+E)
              Label(w, text="Factor:", bg="Light Pink", borderwidth=1, relief="solid").grid(row=accumulator+2, column=0, sticky=W+E)
              Label(w, text=block_of_json["factor_type"], bg="Light Pink", borderwidth=1, relief="solid").grid(row=accumulator+3, column=0, sticky=W+E, pady=(0,5))
              Label(w, text="Information:", bg="Light Pink", borderwidth=1, relief="solid").grid(row=accumulator, column=1, sticky=W+E)
              Label(w, text=block_of_json["data"], bg="Light Pink", borderwidth=1, relief="solid").grid(row=accumulator+1, column=1, rowspan=3, sticky=W+E+S+N, pady=(0,5))
              accumulator = accumulator+4
          house_loan_threshold = 702
          if (temp_smartscore >= house_loan_threshold):
              textbox = tk.Text(self, wrap=WORD)
              textbox.insert(INSERT, str("Congratulations! With a score of at least {} you qualify for a house loan.").format(house_loan_threshold))
              textbox.config(state=DISABLED)
              textbox.pack(side=TOP, expand=TRUE)

  class Page5(Page):
      def __init__(self, *args, **kwargs):
          Page.__init__(self, *args, **kwargs)
          w = Canvas(self, width=400, height=360)
          w.pack(side=BOTTOM)
          label = tk.Label(self, text="Transfer score")
          label.pack(side="bottom", fill="both")

  class Page6(Page):
      def __init__(self, *args, **kwargs):
          Page.__init__(self, *args, **kwargs)
          self.label_username = Label(self, text="Score Change")
          self.label_password = Label(self, text="Factor")

          self.entry_username = Entry(self)
          self.entry_password = Entry(self)

          self.label_username.grid(row=0, sticky=E)
          self.label_password.grid(row=1, sticky=E)
          self.entry_username.grid(row=0, column=1)
          self.entry_password.grid(row=1, column=1)

  class MainView(tk.Frame):
      def __init__(self, *args, **kwargs):
          tk.Frame.__init__(self, *args, **kwargs)
          p1 = Page1(self)
          p2 = Page2(self)
          p3 = Page3(self)
          p4 = Page4(self)
          p5 = Page5(self)
          p6 = Page6(self)
          
          buttonframe = tk.Frame(self)
          container = tk.Frame(self)
          buttonframe.pack(side="top", fill="x", expand=False)
          container.pack(side="top", fill="both", expand=True)

          p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
          p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
          p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
          p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
          p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
          p6.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

          b1 = tk.Button(buttonframe, text="Score", command=p1.lift)
          b2 = tk.Button(buttonframe, text="Analytics", command=p2.lift)
          b3 = tk.Button(buttonframe, text="Calculations", command=p3.lift)
          b4 = tk.Button(buttonframe, text="Blocks", command=p4.lift)
          b5 = tk.Button(buttonframe, text="Transfer", command=p5.lift)
          b6 = tk.Button(buttonframe, text="Add", command=p6.lift)

          b1.pack(side="left")
          b2.pack(side="left")
          b3.pack(side="left")
          b4.pack(side="left")
          b5.pack(side="left")
          b6.pack(side="left")

          p2.show()

  if __name__ == "__main__":
        root.title("SmartScore")
        main = MainView(root)
        main.pack(side="top", fill="both", expand=TRUE)
        root.wm_geometry("400x700")
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

            self.master.destroy()
            my_fun()


def logscreen():
    newwindow = Tk()
    newwindow.title("Log in Screen")
    LoginFrame(newwindow)

root = Tk()
root.title("SmartScore Web UI")
root.geometry('400x700')
Label(root, text="Smart", font="Roboto 30 bold").place(x=230, y=290, anchor=CENTER)
Label(root, text="Score", font="Roboto 30 bold").place(x=230, y=330, anchor=CENTER)
Label(root, text="Launched by", font="Roboto 15").place(x=200, y=600, anchor=CENTER)
Label(root, text="HSBC Canada", font="Roboto 15 bold").place(x=200, y=630, anchor=CENTER)
logo = PhotoImage(file="logo.png")
Label(root, image=logo, bg="white").place(x=120, y=280)
loginp = PhotoImage(file="login.png")
exitp = PhotoImage(file="exit.png")
login = Button(root, image=loginp, command=logscreen)
login.place(x=100, y=675, anchor=CENTER)
exit = Button(root, image=exitp, command=root.destroy)
exit.place(x=300, y=675, anchor=CENTER)
root.mainloop()