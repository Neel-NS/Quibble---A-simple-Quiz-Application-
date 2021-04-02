import mysql.connector
from tkinter import *
from tkinter import messagebox
import hashlib
import random


class Quiz:
    def __init__(self):
        self.root = Tk()
        self.load_gui_window(self.intro_gui)

    def load_gui_window(self, gui_type):
        self.root.geometry("1280x720+0+0")
        self.root.title("Quibble")
        self.root.config(bg="azure")
        self.root.resizable(0, 0)
        gui_type()
        self.root.mainloop()

    def intro_gui(self):
        self.banner = PhotoImage(
            file="C:\\Users\\Nabanil\\Desktop\\WT-Python\MyProject\Samples\Db-quibble\Resources\\logo_transparent480.png")
        self.lblbanner = Label(
            self.root,
            image=self.banner,
            bg="azure",
        )
        self.lblbanner.pack()
        self.lblbanner.place(x=400, y=10)

        self.register = Button(self.root, text="Register", width=20, height=2, fg="royalblue4", bg="lavender",
                               font=("Helvetica", 10, "bold italic"), command=self.load_reg_window)
        self.register.pack()
        self.register.place(x=450, y=500)
        self.login = Button(self.root, text="Log In", width=20, height=2, fg="royalblue4", bg="lavender",
                            font=("Helvetica", 10, "bold italic"), command=self.load_login_window)
        self.login.pack()
        self.login.place(x=650, y=500)

    def load_reg_window(self):
        self.lblbanner.destroy()
        self.register.destroy()
        self.login.destroy()
        self.register_gui()

    def load_login_window(self):
        self.lblbanner.destroy()
        self.register.destroy()
        self.login.destroy()
        self.login_gui()

    def register_gui(self):

        self.regImg = PhotoImage(
            file="C:\\Users\\Nabanil\\Desktop\\WT-Python\MyProject\Samples\Db-quiz\Resources\\RegisterNow_02.png")
        self.regNowImg = Label(self.root, image=self.regImg, bg="azure")
        self.regNowImg.pack()
        self.regNowImg.place(x=700, y=100)

        self.mainTitle = Label(self.root, text="Register Yourself", bg="#7fffd4",
                               font=("Consolas", 30, "bold italic"))
        self.mainTitle.place(x=50, y=10)
        self.name = Label(self.root, text="First Name : ", bg="azure", font=("Times New Roman", 10))
        self.lname = Label(self.root, text="Last name : ", bg="azure", font=("Times New Roman", 10))
        self.email = Label(self.root, text="Email id : ", bg="azure", font=("Times New Roman", 10))
        self.uname = Label(self.root, text="Username :", bg="azure", font=("Times New Roman", 10))
        self.pw = Label(self.root, text="Enter password : ", bg="azure", font=("Times New Roman", 10))

        self.var = IntVar()

        self.tname = Entry(self.root, width=30)
        self.tlname = Entry(self.root, width=30)
        self.temail = Entry(self.root, width=30)
        self.tuname = Entry(self.root, width=30)
        self.tpw = Entry(self.root, width=30, show="*")

        self.submit = Button(self.root, text="Submit", width=20, height=2, fg="royalblue4", bg="lavender",
                             font=("Helvetica", 10, "bold italic"), command=self.c_submit)
        self.cancel = Button(self.root, text="Cancel", width=20, height=2, fg="royalblue4", bg="lavender",
                             font=("Helvetica", 10, "bold italic"), command=self.c_cancel)

        self.checkB = Checkbutton(self.root, text='Show Password', bg="azure", fg="royalblue4",
                                  font=("Helvetica", 10, "bold italic"), variable=self.var, onvalue=1,
                                  offvalue=0, command=self.showpasswd)

        self.name.place(x=50, y=100)
        self.tname.place(x=200, y=100)
        self.lname.place(x=50, y=150)
        self.tlname.place(x=200, y=150)
        self.email.place(x=50, y=200)
        self.temail.place(x=200, y=200)
        self.uname.place(x=50, y=250)
        self.tuname.place(x=200, y=250)
        self.pw.place(x=50, y=300)
        self.tpw.place(x=200, y=300)
        self.submit.place(x=50, y=400)
        self.cancel.place(x=250, y=400)
        self.checkB.place(x=195, y=330)

    def showpasswd(self):
        if self.var.get():
            self.tpw.config(show="")
        else:
            self.tpw.config(show="*")

    def c_submit(self):
        conn = mysql.connector.connect(host='localhost', database='quibble', user='root', password='')
        cursor = conn.cursor()
        name = self.tname.get()
        lname = self.tlname.get()
        email = self.temail.get()
        uname = self.tuname.get()
        pw = self.tpw.get()
        p = hashlib.sha1((uname[:5] + pw).encode('utf-8')).hexdigest()
        str = "SELECT * FROM users WHERE uname='%s'"
        arg = (uname)
        cursor.execute(str % arg)
        row = cursor.fetchone()
        if row is not None:
            messagebox.showwarning("Error", "Username Already Taken, Try Again!")
        else:
            try:
                s = "INSERT INTO users(name,lname,email,uname,p,score) values('%s','%s','%s','%s','%s','%d')"
                arg = (name, lname, email, uname, p, 0)
                cursor.execute(s % arg)
                conn.commit()
                print("DEBUG: 1 ROW ADDED")
                self.tname.delete(0, 'end')
                self.tlname.delete(0, 'end')
                self.temail.delete(0, 'end')
                self.tuname.delete(0, 'end')
                self.tpw.delete(0, 'end')
                messagebox.showinfo("Success", "Registration Successful!")
            except:
                conn.rollback()
        cursor.close()
        conn.close()

    def c_cancel(self):
        self.regNowImg.destroy()
        self.mainTitle.destroy()
        self.name.destroy()
        self.tname.destroy()
        self.lname.destroy()
        self.tlname.destroy()
        self.email.destroy()
        self.temail.destroy()
        self.uname.destroy()
        self.tuname.destroy()
        self.pw.destroy()
        self.tpw.destroy()
        self.submit.destroy()
        self.cancel.destroy()
        self.checkB.destroy()
        self.intro_gui()

    def login_gui(self):
        self.l1 = Label(self.root, text="Enter Username: ", bg="azure", font=("Times New Roman", 20))
        self.e1 = Entry(self.root, width=30)
        self.l2 = Label(self.root, text="Enter Password: ", bg="azure", font=("Times New Roman", 20))
        self.e2 = Entry(self.root, width=30, show="*")
        self.b1 = Button(self.root, text="Login", width=20, height=2, fg="royalblue4", bg="lavender",
                         font=("Helvetica", 10, "bold italic"), command=self.clicked)
        self.b2 = Button(self.root, text="Cancel", width=20, height=2, fg="royalblue4", bg="lavender",
                         font=("Helvetica", 10, "bold italic"), command=self.back_to_main)

        self.var = IntVar()
        self.checkB = Checkbutton(self.root, text='Show Password', bg="azure", fg="royalblue4",
                                  font=("Helvetica", 10, "bold italic"), variable=self.var, onvalue=1,
                                  offvalue=0, command=self.showpassword)

        self.l1.place(x=420, y=100)
        self.e1.place(x=620, y=110)
        self.l2.place(x=420, y=150)
        self.e2.place(x=620, y=160)
        self.b1.place(x=420, y=250)
        self.b2.place(x=630, y=250)
        self.checkB.place(x=615, y=190)

    def showpassword(self):
        if self.var.get():
            self.e2.config(show="")
        else:
            self.e2.config(show="*")

    def back_to_main(self):
        self.l1.destroy()
        self.e1.destroy()
        self.l2.destroy()
        self.e2.destroy()
        self.b1.destroy()
        self.b2.destroy()
        self.checkB.destroy()
        self.intro_gui()

    def clicked(self):
        conn = mysql.connector.connect(host='localhost', database='quibble', user='root', password='')
        cursor = conn.cursor()
        u = self.e1.get()
        pw = self.e2.get()
        self.e1.delete(0, 200)
        self.e2.delete(0, 200)
        p = hashlib.sha1((u[:5] + pw).encode('utf-8')).hexdigest()
        s = "SELECT * FROM users WHERE uname='%s' and p='%s'"
        arg = (u, p)
        cursor.execute(s % arg)
        result = cursor.fetchall()
        if result:
            self.goinaccount(u)
        else:
            messagebox.showerror("Error", "Invalid Username or Password, Try Again!")
        cursor.close()
        conn.close()

    def goinaccount(self, u):
        self.l1.destroy()
        self.e1.destroy()
        self.l2.destroy()
        self.e2.destroy()
        self.b1.destroy()
        self.b2.destroy()
        self.checkB.destroy()
        self.u = u
        conn = mysql.connector.connect(host='localhost', database='quibble', user='root', password='')
        cursor = conn.cursor()
        q = "SELECT score FROM users WHERE uname='%s'"
        arg = (u)
        cursor.execute(q % arg)
        self.prevScore = cursor.fetchone()
        cursor.close()
        conn.close()
        self.greet = Label(self.root, text="Hey " + u + " !", bg="azure",
                           font=("Consolas", 30, "bold"))
        self.greet.place(x=400, y=200)
        self.lastScore = Label(self.root, text="Your Last Score is " + str(self.prevScore[0]), bg="azure",
                               font=("Consolas", 30, "bold"))
        self.lastScore.place(x=400, y=300)
        self.takeQuiz = Button(self.root, text="Start", width=20, height=2, fg="royalblue4", bg="lavender",
                               font=("Helvetica", 10, "bold italic"), command=self.goinside)
        self.takeQuiz.place(x=500, y=400)
        self.logout = Button(self.root, text="Logout", width=20, height=2, fg="royalblue4", bg="lavender",
                             font=("Helvetica", 10, "bold italic"), command=self.back_to_main_window)
        self.logout.place(x=750, y=400)

    def back_to_main_window(self):
        self.greet.destroy()
        self.lastScore.destroy()
        self.takeQuiz.destroy()
        self.logout.destroy()
        self.intro_gui()

    def goinside(self):
        self.playquiz(self.u)

    def playquiz(self, u):
        self.greet.destroy()
        self.lastScore.destroy()
        self.takeQuiz.destroy()
        self.user = u
        conn = mysql.connector.connect(host='localhost', database='quibble', user='root', password='')
        cursor = conn.cursor()

        global l1, answerstemp
        global questions
        questions = []
        global options
        options = []
        global answers
        answers = []
        answerstemp = []
        s1 = set()

        while len(s1) < 10:
            strQ = ""
            strA = ""
            id = random.randint(1, 30)
            s1.add(id)

        while len(s1) > 0:
            s = "SELECT qstn FROM questions WHERE QID=%d"
            id = s1.pop()
            arg = (id)
            cursor.execute(s % arg)
            strQ = strQ.join(list(cursor.fetchone()))
            questions.append(strQ)

            s = "SELECT opA,opB,opC,opD FROM questions WHERE QID=%d"
            arg = (id)
            cursor.execute(s % arg)
            options.append(list(cursor.fetchone()))

            s = "SELECT ans FROM questions WHERE QID=%d"
            arg = (id)
            cursor.execute(s % arg)
            l = list(cursor.fetchone())
            answerstemp.append(l)

        mydict = {}
        for i in range(10):
            mydict[questions[i]] = options[i]
        for i in range(len(answerstemp)):
            answers.append(answerstemp[i][0])

        print("DEBUG: Answers= ", answers)

        cursor.close()
        conn.close()
        l1 = {}
        for i in range(10):
            l1[i] = 0

        self.qno = 0
        self.score1 = 0
        self.ques = self.create_q(self.qno)
        self.opts = self.create_options()
        self.display_q(self.qno)
        self.Back = Button(self.root, text="<- Back", width=15, height=3, fg="royalblue4", bg="snow2",
                           font=("Helvetica", 10, "bold italic"), command=self.back).place(x=100, y=325)
        self.Next = Button(self.root, text="Next ->", width=15, height=3, fg="royalblue4", bg="snow2",
                           font=("Helvetica", 10, "bold italic"), command=self.next).place(x=250, y=325)
        self.submit = Button(self.root, text="Submit", width=34, height=2, fg="ghost white", bg="DeepSkyBlue2",
                             font=("Helvetica", 10, "bold italic"), command=self.Submit).place(x=100, y=400)

        imgID = random.randint(1, 4)
        filestr = "C:\\Users\\Nabanil\\Desktop\\WT-Python\MyProject\Samples\Db-quiz\Resources\\" + str(imgID) + ".png"
        self.quizImg = PhotoImage(file=filestr)
        img = Label(self.root, image=self.quizImg, bg="azure")
        img.place(x=700, y=200)

    def create_q(self, qno):
        qLabel = Label(self.root, text=questions[qno], bg='azure', font=("Times New Roman", 20))
        qLabel.place(x=30, y=70)
        return qLabel

    def create_options(self):
        b_val = 0
        b = []
        ht = 85
        self.opt_selected = IntVar()
        while b_val < 4:
            btn = Radiobutton(self.root, text="", variable=self.opt_selected, value=b_val + 1, bg='azure',
                              font=("Times New Roman", 20))
            b.append(btn)
            ht = ht + 40
            btn.place(x=30, y=ht)
            b_val = b_val + 1
        return b

    def display_q(self, qno):
        b_val = 0
        self.ques['text'] = str(qno + 1) + ". " + questions[qno]
        for op in options[qno]:
            self.opts[b_val]['text'] = op
            b_val = b_val + 1

    def next(self):
        self.qno += 1

        if self.qno >= len(questions):
            self.qno -= 1
            messagebox.showwarning("Warning", "You are at the end.Press Submit to proceed")
        else:
            l1[self.qno - 1] = self.opt_selected.get()
            self.opt_selected.set(l1[(self.qno)])
            self.display_q(self.qno)

    def back(self):
        l1[self.qno] = self.opt_selected.get()
        self.qno -= 1
        if self.qno < 0:
            self.qno += 1
            messagebox.showerror("Error", "You are already in the start!!!")
        else:
            self.display_q(self.qno)
            c = l1[self.qno]
            self.opt_selected.set(c)

    def Submit(self):
        global s
        l1[self.qno] = self.opt_selected.get()
        x = 0
        y = True
        for i in range(10):
            if (l1[i] == 0):
                x += 1
        if (x > 0 and x != 1):
            y = messagebox.askyesno("Warning", "You have not attempted " + str(
                x) + " questions, Are you sure you want to submit?, You won't be able to make changes again")
        elif (x == 1):
            y = messagebox.askyesno("Warning", "You have not attempted " + str(
                x) + " question, Are you sure you want to submit?, You won't be able to make changes again")
        if (y == True or x == 0):
            s = 0
            for i in range(10):
                if (l1[i] == answerstemp[i][0]):
                    s = s + 1
            print("DEBUG: Score: ", s)

        conn = mysql.connector.connect(host='localhost', database='quibble', user='root', password='')
        cursor = conn.cursor()
        q = "UPDATE users SET score='%d' WHERE uname= '%s'"
        arg = (s, self.user)
        cursor.execute(q % arg)
        conn.commit()
        cursor.close()
        conn.close()

        messagebox.showinfo("Score", "Your Score is: " + str(s) + "/10")


obj = Quiz()
