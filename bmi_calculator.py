#AAKANKSHA BHENDE
#SUMMER PROJECT
#19SE02CE083
#SEM-3

from tkinter import *
from tkinter import messagebox as mb
import pymysql as db
import smtplib
from mail import *

root=Tk()
root.title("BMI CALCULATOR")
root.minsize(300,300)

#-----------FUNCTIONS------------

def bmi():
	x=float(w.get())//(float(h.get())**2)
	ne=n.get()
	ee=e.get()
	print('''%s your BMI is: %d'''%(ne,x))
	if x in range(18,26):
		message='''
		Your BMI = %d
		Congrats you are healthy!
		EAT-SLEEP-REPEAT
		'''%x
		mb.showinfo("Hello %s"%ne,message)
		mail(message,ee)
		mb.showinfo("Success!","E-mail has been sent to you")

	elif x in range(25,30):
		message='''
		Your BMI = %d
		You fall in overweight category
		Start exercise..
		'''%x
		mb.showwarning("BMI Calculation",message)
		mail(message,ee)
		mb.showinfo("Success!","E-mail has been sent to you")

	elif x in range(2,18):
		message='''
		Your BMI = %d
		You fall in Underweight category
		Consume Calories
		'''%x
		mb.showwarning("BMI Calculation",message)
		mail(message,ee)
		mb.showinfo("Success!","E-mail has been sent to you")

	elif x in range(30,35):
		message='''
		Your BMI = %d
		Alert You fall in Obese Class I
		Start Exercising
		'''%x
		mb.showerror("BMI Calculation",message)
		mail(message,ee)
		mb.showinfo("Success!","E-mail has been sent to you")

	elif x in range(35,40):
		message='''
		Your BMI = %d
		Alert You fall in Obese Class II
		Start Exercising, Stop Fast fooding
		'''%x
		mb.showerror("BMI Calculation",message)
		mail(message,ee)
		mb.showinfo("Success!","E-mail has been sent to you")

	elif (x>40):
		message='''
		Your BMI = %d
		Alert You fall in Obese Class III
		Consult Doctor ASAP
		'''%x
		mb.showerror("BMI Calculation",message)
		mail(message,ee)
		mb.showinfo("Success!","E-mail has been sent to you")

	elif (x==0):
		mb.showwarning("ALert","Please enter Weight in KGS and Height in 'm'")
		
def con():	
		pide=int(pe.get())
		ne=n.get()
		ee=e.get()
		ae=int(a.get())
		ht=float(h.get())
		wt=float(w.get())
		x=int(float(w.get())/(float(h.get())**2))
		conn=db.connect(host="localhost", user="root", port=3306, passwd="", database="bmi")
		cur=conn.cursor()
		sql_insert_query="""INSERT INTO `bmi`(`id`,`name`, `age` , `weight`, `height`, `bmi`) VALUES (%d,"%s",%d,%d,%.4f,%d)"""%(pide,ne,ae,wt,ht,x)
		cur.execute(sql_insert_query)
		cur.close()
		conn.commit()
		conn.close()
		mb.showinfo("Database Connected","Your data has been saved on server")		


#-----------DECLARATIONS-------------
pid=Label(root,text="Patient's ID")
pid.grid(row=1,column=1,padx=5, pady=5)
pe=Entry()
pe.grid(row=1,column=2)

name=Label(root,text="Full name")
name.grid(row=2,column=1,padx=5, pady=5)
n=Entry()
n.grid(row=2,column=2)

email=Label(root,text="E-mail ID")
email.grid(row=3,column=1,padx=5, pady=5)
e=Entry()
e.grid(row=3,column=2)

age=Label(root,text="Age")
age.grid(row=4,column=1,padx=5, pady=5)
a=Entry()
a.grid(row=4,column=2)

ht=Label(root,text="Height (in m)")
ht.grid(row=5,column=1,padx=5, pady=5)
h=Entry()
h.grid(row=5,column=2)

wt=Label(root,text="Weight (in kgs)")
wt.grid(row=6,column=1,padx=5, pady=5)
w=Entry()
w.grid(row=6,column=2)

t=Label(root,text="BMI Calculator",bg="DeepSkyBlue4")
t.grid(row=0,column=2,columnspan=2,padx=20,pady=20)

btn=Button(root,text="BMI",bg="green3", command=bmi)
btn1=Button(root,text="SAVE",bg="lawn green", command=con)

btn.grid(row=7,column=2,padx=25,pady=30,ipadx=5,ipady=5)
btn1.grid(row=7,columnspan=3,padx=10, pady=10,ipadx=5,ipady=5)

root.mainloop()