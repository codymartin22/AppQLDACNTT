from tkinter import *
from tkinter import ttk
from functools import partial
from tkinter import messagebox
from LoginF import LoginF
import random
import time
import datetime
from backend import Database
#from tkinter.ttk import Notebook
databaseUser = LoginF("userInfo.db")
database = Database("books.db")
class Window(object):
        def __init__(self,master):
                self.master = master
                self.master.title("Book Store Login")
                self.frame = Frame(self.master)
                self.frame.pack()
                
                self.Username = StringVar()
                self.Password = StringVar()
                #===============================Title======================================
                self.lblTitle = Label(self.frame,text ="Book Store Login System",font =('arial',20,'bold'),bg='green',fg='red')
                self.lblTitle.grid(row=0,column=0,columnspan = 2,pady = 40)
                #===============================Frame======================================
                self.LoginFrame1 = LabelFrame(self.frame,width=1350,height=100,font=('arial',20,'bold'),relief='ridge',bg='violet',bd=20)
                self.LoginFrame1.grid(row=1,column=0)
                self.LoginFrame2 = LabelFrame(self.frame,width=1000,height=100,font=('arial',20,'bold'),relief='ridge',bg='violet',bd=20)
                self.LoginFrame2.grid(row=2,column=0)
                #===============================Label and Entry======================================
                self.lblUsername = Label(self.LoginFrame1,text ="Username",font=('arial',20,'bold'))
                self.lblUsername.grid(row=0,column=0)
                self.txtUsername = Entry(self.LoginFrame1,textvariable=self.Username,font=('arial',20,'bold'))
                self.txtUsername.grid(row=0,column=1)

                self.lblPassword= Label(self.LoginFrame1,text ="Password",font=('arial',20,'bold'))
                self.lblPassword.grid(row=1,column=0)
                self.txtPassword = Entry(self.LoginFrame1,textvariable=self.Password,show="*",font=('arial',20,'bold'))
                self.txtPassword.grid(row=1,column=1)
                #===============================ButtonFunction======================================
                self.btnLogin = Button(self.LoginFrame2,width = 17,text ='Login',command = self.Login_System)
                self.btnLogin.grid(row = 3,column =0)
                
                self.btnRegister = Button(self.LoginFrame2,width = 17,command=self.Go_Register,text ='Register')
                self.btnRegister.grid(row = 3,column =1)

                self.btnExit = Button(self.LoginFrame2,command=self.IExit,width = 17,text ='Exit')
                self.btnExit.grid(row = 3,column =2)
        def Login_System(self):
                u = (self.Username.get())
                p = (self.Password.get())
                if (databaseUser.Login(u,p) > 0):               
                        self.newWindow = Toplevel(self.master)
                        self.app = windowBookStoreMain(self.newWindow)
                else:
                        messagebox.askyesno("Login Systems","Invalid Login Detail")
                        self.Username.set("")
                        self.Password.set("")
                        self.txtUsername.focus()
        def Go_Register(self):
                self.newWindow = Toplevel(self.master)
                self.app = windowRegister(self.newWindow)
        def IExit(self):
                self.IExit = messagebox.askyesno("Login Systens","Comfirm if you want to exit")
                if self.IExit > 0:
                        self.master.destroy()
                else:
                        command = self.new_window
                        return

class windowRegister:
        def __init__(self,master):
                self.master = master
                self.master.title("Book Register Store")
                self.master.config(bg ="blue")
                self.frame = Frame(self.master,bg="blue")
                self.frame.pack()

                self.Username = StringVar()
                self.Password = StringVar()
                self.rePassword = StringVar()
                #===============================Title======================================
                self.lblTitle = Label(self.frame,text ="Book Store Register System",font =('arial',20,'bold'),bg='green',fg='red')
                self.lblTitle.grid(row=0,column=0,columnspan = 2,pady = 40)
                #===============================Frame======================================
                self.LoginFrame1 = LabelFrame(self.frame,width=1350,height=100,font=('arial',20,'bold'),relief='ridge',bg='violet',bd=20)
                self.LoginFrame1.grid(row=1,column=0)
                self.LoginFrame2 = LabelFrame(self.frame,width=1000,height=100,font=('arial',20,'bold'),relief='ridge',bg='violet',bd=20)
                self.LoginFrame2.grid(row=2,column=0)
                #===============================Label and Entry======================================
                self.lblUsername = Label(self.LoginFrame1,text ="Username",font=('arial',20,'bold'),bg='violet')
                self.lblUsername.grid(row=0,column=0)
                self.txtUsername = Entry(self.LoginFrame1,textvariable=self.Username,font=('arial',20,'bold'))
                self.txtUsername.grid(row=0,column=1)

                self.lblPassword= Label(self.LoginFrame1,text ="Password",font=('arial',20,'bold'),bg='violet')
                self.lblPassword.grid(row=1,column=0)
                self.txtPassword = Entry(self.LoginFrame1,textvariable=self.Password,show="*",font=('arial',20,'bold'))
                self.txtPassword.grid(row=1,column=1)

                self.lblrePassword= Label(self.LoginFrame1,text ="Re-Password",font=('arial',20,'bold'),bg='violet')
                self.lblrePassword.grid(row=2,column=0)
                self.txtrePassword = Entry(self.LoginFrame1,textvariable=self.rePassword,show="*",font=('arial',20,'bold'))
                self.txtrePassword.grid(row=2,column=1)
                #===============================ButtonFunction======================================
                self.btnLogin = Button(self.LoginFrame2,command=self.Register_System,width = 17,text ='Register')
                self.btnLogin.grid(row = 3,column =0)

                self.btnExit = Button(self.LoginFrame2,command=self.IExit,width = 17,text ='Exit')
                self.btnExit.grid(row = 3,column =2)
        def Register_System(self):
                u = (self.Username.get())
                p = (self.Password.get())
                rp = (self.rePassword.get())
                if (databaseUser.Register(u,p,rp) == 2):                                       
                        messagebox.askyesno("Register Systems","Register done! Login to continue")   
                elif (databaseUser.Register(u,p,rp) == 1):
                        messagebox.askyesno("Register Systems","Member had been exist")
                        self.Username.set("")
                        self.Password.set("")
                        self.rePassword.set("")
                        self.txtUsername.focus()
                else:
                        messagebox.askyesno("Register Systems","Invalid Register Detial")
                        self.Username.set("")
                        self.Password.set("")
                        self.rePassword.set("")
                        self.txtUsername.focus()
        def IExit(self):
                        self.master.destroy()
class windowBookStoreMain:
        def __init__(self,master):
                self.master = master
                self.master.title("Book Store")
                self.master.geometry('1350x750+0+0')
                self.master.config(bg ="red")
                self.frame = Frame(self.master,bg="red")
                self.frame.pack()

                self.Title = StringVar()
                self.Author = StringVar()
                self.Year = int
                self.ISBN = int
                self.Amount = int
                self.Cost = int
                #===============================Title======================================
                self.lblTitle = Label(self.frame,text ="Book Store Manager System",font =('arial',20,'bold'),bg='green',fg='red')
                self.lblTitle.grid(row=0,column=0,columnspan = 2,pady = 40)
                #===============================Frame======================================
                self.Frame1 = LabelFrame(self.frame,width=1350,height=100,font=('arial',20,'bold'),relief='ridge',bg='violet',bd=20)
                self.Frame1.grid(row=1,column=0)
                self.Frame2 = LabelFrame(self.frame,width=1000,height=100,font=('arial',20,'bold'),relief='ridge',bg='violet',bd=20)
                self.Frame2.grid(row=2,column=0)
                self.Frame3 = LabelFrame(self.frame,width=1000,height=100,font=('arial',20,'bold'),relief='ridge',bg='violet',bd=20)
                self.Frame3.grid(row=3,column=0)
                #===============================Label and Entry======================================
                self.lblTitle = Label(self.Frame1,text ="Title",font=('arial',20,'bold'),bg='violet')
                self.lblTitle.grid(row=0,column=0)
                self.txtTitle = Entry(self.Frame1,textvariable=self.Title,font=('arial',20,'bold'))
                self.txtTitle.grid(row=0,column=1)

                self.lblAuthor = Label(self.Frame1,text ="Author",font=('arial',20,'bold'),bg='violet')
                self.lblAuthor.grid(row=0,column=2)
                self.txtAuthor = Entry(self.Frame1,textvariable=self.Author,font=('arial',20,'bold'))
                self.txtAuthor.grid(row=0,column=3)

                self.lblYear = Label(self.Frame1,text ="Year",font=('arial',20,'bold'),bg='violet')
                self.lblYear.grid(row=1,column=0)
                self.txtYear = Entry(self.Frame1,textvariable=self.Year,font=('arial',20,'bold'))
                self.txtYear.grid(row=1,column=1)

                self.lblISBN = Label(self.Frame1,text ="ISBN",font=('arial',20,'bold'),bg='violet')
                self.lblISBN.grid(row=1,column=2)
                self.txtISBN = Entry(self.Frame1,textvariable=self.ISBN,font=('arial',20,'bold'))
                self.txtISBN.grid(row=1,column=3)
                
                self.lblAmount = Label(self.Frame1,text ="Amount",font=('arial',20,'bold'),bg='violet')
                self.lblAmount.grid(row=2,column=0)
                self.txtAmount = Entry(self.Frame1,textvariable=self.Amount,font=('arial',20,'bold'))
                self.txtAmount.grid(row=2,column=1)

                self.lblCost = Label(self.Frame1,text ="Cost",font=('arial',20,'bold'),bg='violet')
                self.lblCost.grid(row=2,column=2)
                self.txtCost = Entry(self.Frame1,textvariable=self.Cost,font=('arial',20,'bold'))
                self.txtCost.grid(row=2,column=3)
                #===============================Table======================================
                #self.TabLayout=Notebook(self.Frame2)
                #self.Tab1 = Frame(self.TabLayout)
                #self.Tab1.pack(fill="both")
                #Info column
                #for row in range(3):
                #        for column in range(6):
                #                if row==0:
                #                        if column == 0: self.label = Label(self.Tab1,text = "Title",bg="black",fg="white",padx=3,pady=3)
                #                        elif column == 1: self.label = Label(self.Tab1,text = "Author",bg="red",fg="white",padx=3,pady=3)
                #                        elif column == 2: self.label = Label(self.Tab1,text = "Year",bg="green",fg="white",padx=3,pady=3)
                #                        elif column == 3: self.label = Label(self.Tab1,text = "ISBN",bg="blue",fg="white",padx=3,pady=3)
                #                        elif column == 4: self.label = Label(self.Tab1,text = "Amount",bg="violet",fg="white",padx=3,pady=3)
                #                        elif column == 5: self.label = Label(self.Tab1,text = "Cost",bg="pink",fg="white",padx=3,pady=3)


                #                        self.label.config(font=('Arial',14))
                #                        self.label.grid(row=row,column=column,sticky = "nsew",padx=1,pady=1)
                #                        self.Tab1.grid_columnconfigure(column,weight=1)
                #                else:
                #                        self.label = Label(self.Tab1,text = "("+str(row)+","+str(column)+")",bg="Orange",fg="white",padx=3,pady=3)
                #                        self.label.config(font=('Arial',14))
                #                        self.label.grid(row=row,column=column,sticky = "nsew",padx=1,pady=1)
                #                        self.Tab1.grid_columnconfigure(column,weight=1)   
                
                #Tab name
                #self.TabLayout.add(self.Tab1,text="Book List")
                
                #end add Info
                #self.TabLayout.pack(fill="both")
                #===============================ListBox=============================================
                self.list1 = Listbox(self.Frame2, height=5, width=45)
                self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)
                self.list1.config(font=('arial',20,'bold'))

                self.list1.bind('<<ListboxSelect>>',self.get_selected_row)
                #scrollbar
                self.sb1 = Scrollbar(self.Frame2,orient="vertical")
                self.sb1.grid(row=2, column=2, rowspan=6)
                self.list1.config(yscrollcommand=self.sb1.set)
                self.sb1.config(command=self.list1.yview)
                #===============================ButtonFunction======================================
                self.btnView = Button(self.Frame3,width = 17,text ='View All',command=self.view_command)
                self.btnView.grid(row = 3,column =0)

                self.btnSearch = Button(self.Frame3,width = 17,text ='Search',command=self.search_command)
                self.btnSearch.grid(row = 3,column =1)

                self.btnAdd = Button(self.Frame3,width = 17,text ='Add',command=self.add_command)
                self.btnAdd.grid(row = 3,column =2)
                
                self.btnUpdate = Button(self.Frame3,width = 17,text ='Update',command=self.update_command)
                self.btnUpdate.grid(row = 3,column =3)
                
                self.btnDelete = Button(self.Frame3,width = 17,text ='Delete',command=self.delete_command)
                self.btnDelete.grid(row = 3,column =4)
                
                self.btnExit = Button(self.Frame3,width = 17,text ='Clear Entries',command=self.clear_command)
                self.btnExit.grid(row = 3,column =5)

                self.btnExit = Button(self.Frame3,width = 17,text ='Exit',command=self.IExit)
                self.btnExit.grid(row = 3,column =6)
                #=============================Function==============================================
        def get_selected_row(self,event):   #the "event" parameter is needed b/c we've binded this function to the listbox
                        try:
                            index = self.list1.curselection()[0]
                            self.selected_tuple = self.list1.get(index)
                            self.txtTitle.delete(0,END)
                            self.txtTitle.insert(END,self.selected_tuple[1])
                            self.txtAuthor.delete(0, END)
                            self.txtAuthor.insert(END,self.selected_tuple[2])
                            self.txtYear.delete(0, END)
                            self.txtYear.insert(END,self.selected_tuple[3])
                            self.txtISBN.delete(0, END)
                            self.txtISBN.insert(END,self.selected_tuple[4])
                            self.txtAmount.delete(0, END)
                            self.txtAmount.insert(END,self.selected_tuple[5])
                            self.txtCost.delete(0, END)
                            self.txtCost.insert(END,self.selected_tuple[6])
                        except IndexError:
                            pass                #in the case where the listbox is empty, the code will not execute

        def view_command(self):
                        self.list1.delete(0, END)  # make sure we've cleared all entries in the listbox every time we press the View all button
                        for row in database.view():
                                self.list1.insert(END, row)

        def search_command(self):
                        self.list1.delete(0, END)
                        for row in database.search(self.txtTitle.get(), self.txtAuthor.get(), self.txtYear.get(), self.txtISBN.get(),self.txtAmount.get(),self.txtCost.get()):
                                 self.list1.insert(END, row)

        def add_command(self):
                        database.insert(self.txtTitle.get(), self.txtAuthor.get(), self.txtYear.get(), self.txtISBN.get(),self.txtAmount.get(),self.txtCost.get())
                        self.list1.delete(0, END)
                        self.list1.insert(END, (self.txtTitle.get(), self.txtAuthor.get(), self.txtYear.get(), self.txtISBN.get(),self.txtAmount.get(),self.txtCost.get()))

        def delete_command(self):
                        database.delete(self.selected_tuple[0])
                        self.view_command()

        def update_command(self):
                        #be careful for the next line ---> we are updating using the texts in the entries, not the selected tuple
                        database.update(self.selected_tuple[0],self.txtTitle.get(), self.txtAuthor.get(), self.txtYear.get(), self.txtISBN.get(),self.txtAmount.get(),self.txtCost.get())
                        self.view_command()
        def clear_command(self):
                        self.txtTitle.delete(0,END)
                        self.txtAuthor.delete(0,END)
                        self.txtYear.delete(0,END)
                        self.txtISBN.delete(0,END)
                        self.txtAmount.delete(0,END)
                        self.txtCost.delete(0,END)
        def IExit(self):
                self.IExit = messagebox.askyesno("Login Systens","Comfirm if you want to exit")
                if self.IExit > 0:
                        self.master.destroy()
                else:
                        command = self.new_window
                        return
#code GUI
window = Tk()
Window(window)

window.mainloop()
