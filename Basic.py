import tkinter as tk
from tkinter import ttk
from tkinter import Tk
from tkinter import *
from tkinter import messagebox
from dbhelper import *


class UserLogin():
	def __init__(self):
		#self.window = tk.Tk()
		self.root= Tk() 
		self.root.title("ALCARMEN, BRANDON V.")
		self.root.geometry("500x500")
		self.root.resizable(False,False)

		self.frame = Frame(self.root,bd=20)
		self.frame.grid()		
		
		#>>>>IDNO<<<<<
		self.lbl_idno=Label(self.frame,text="IDNO",font="Verdana,20",bd=20)
		self.lbl_idno.grid(row=0,column=0)
		#>>>>LastName<<<<
		self.lbl_Lastname=Label(self.frame,text="LASTNAME",font="Verdana,20",bd=20)
		self.lbl_Lastname.grid(row=1,column=0)
		#>>>FirstName<<<<
		self.lbl_Firstname=Label(self.frame,text="FIRSTNAME",font="Verdana,20",bd=20)
		self.lbl_Firstname.grid(row=2,column=0)
		#>>>>Course<<<<
		self.lbl_Course=Label(self.frame, text = "COURSE :",font="Verdana,20",bd=20)
		self.lbl_Course.grid(row=3,column=0)
		n= tk.StringVar()
		Course = ttk.Combobox(self.frame, width= 27, textvariable = n)
		Course['values'] = ('BSIT',
							'CCS',
							'COMP-E')
		Course.grid(column=1, row=3)
		Course.current()
		#>>>>>Level<<<<<
		self.lbl_Level=Label(self.frame, text = "LEVEL :",font="Verdana,20",bd=20)
		self.lbl_Level.grid(row=4,column=0)
		L= tk.StringVar()
		Level = ttk.Combobox(self.frame, width= 27, textvariable = L)
		Level['values'] = ('1',
							'2',
							'3',
							'4')
		Level.grid(column=1, row=4)
		Level.current()
		#---------------------------------------------------------
		self.txt_idno=Entry(self.frame,text="idno",font="Verdana,20")
		self.txt_idno.grid(row=0,column=1)		
		self.txt_Lastname=Entry(self.frame,text="Lastname",font="Verdana,20")
		self.txt_Lastname.grid(row=1,column=1)		
		self.txt_Firstname=Entry(self.frame,text="Firstname",font="Verdana,20")
		self.txt_Firstname.grid(row=2,column=1)
		
		self.btn_Find = Button(self.frame,text="Find", font="Verdana,20")
		self.btn_Find.grid(row=0,column=2,columnspan=1)
		
		
		self.Butt = Frame(self.frame,bd=20)
		self.Butt.grid(row=10,column=0, columnspan=2)
		
		self.btn_New = Button(self.Butt,text="New", font="Verdana,20")
		self.btn_New.grid(row=0,column=0, padx=10, sticky="w")
		self.btn_Save = Button(self.Butt,text="Save", font="Verdana,20")
		self.btn_Save.grid(row=0,column=2, padx=10, sticky="w")
		self.btn_Delete = Button(self.Butt,text="Delete", font="Verdana,20")
		self.btn_Delete.grid(row=0,column=4, padx=10, sticky="w")
		self.btn_Update = Button(self.Butt,text="Update", font="Verdana,20")
		self.btn_Update.grid(row=0,column=6, padx=10, sticky="w")		
		
		
		self.root.eval("tk::PlaceWindow . center")
		self.root.mainloop()
	def savestudent(self):
		idno:str = self.txt_idno.get()
		lastname:str=self.txt_Lastname.get()
		firstname:str=self.txt_Firstname.get()
		course:str = Course.get()
		level:str = Level.get()
		
		okey:bool = addrecord('student', idno=idno, lastname=lastname,firstname=firstname,course=course,level=level)
		if okey:
			messagebox.showinfo("login status","LOGIN ACCEPTED")
		else:
			messagebox.showerror("login status", "Login Fail!")
		
def main()->None:
	UserLogin()
if __name__=="__main__":
	main()

