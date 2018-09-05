#Pico y Placa Program Interview test
#by Austin Reed
#Version 1.0



from tkinter import *
from datetime import datetime

#build GUI
root = Tk()
root.title("Pico y Placa Program")
root.geometry('470x470+0+0')
theLabel = Label(root, text="Enter Your Liscence Plate Number:").place(x=10, y=50)
theLabel1 = Label(root, text="Time: (0:00)").place(x=10, y=100)
theLabel2 = Label(root, text="Date:(M/D/Y)").place(x=10, y=150)


#plate Number
lnum = StringVar()
#time
hnum = StringVar()
#date
dnum = StringVar()
#am/pm
time1 = StringVar()
time1.set("AM")

lentry = Entry(root, textvariable=lnum, width=15).place(x=200, y=50)
hentry = Entry(root, textvariable=hnum, width=15).place(x=200, y=100)
dentry = Entry(root, textvariable=dnum, width=10).place(x=200, y=150)
w = OptionMenu(root,time1, "AM", "PM").place(x=300, y=96)

#display statuses
def status(b):
	label = Label(root,text=b).place(x=10,y=300)
def status1(b):
	label = Label(root,text=b).place(x=10,y=200)
def status2(b):
	label = Label(root,text=b).place(x=10,y=250)

#Licence Check Function
def sbmt():
	#timecheck variables
	def timecheck(t):

		#split time
		f = t.split(':')
		g = f[0]
		h = int(f[1])
		#check for morning
		if str(time1.get()) == "AM":
			#check hours
			if g == "7" or g == "8":
				
				status("You are restricted to drive at this hour! Please wait until 9:30pm to drive.")
			elif g == "9":
				if h >30:
					status("You are safe to drive but watch out tonight at 4pm to 7:30pm")
				else:
					status("Your vehicle is restricted right now! Do not drive until 9:30am.")

			else:
				status("You are safe to drive at the moment. Please advise the restricted times for your  vehicle today from 7am to 9am and 4pm to 7:30pm")
				pass
		#Check afternoon
		elif str(time1.get()) == "PM":
			#Check Hours
			if g == "4" or g == "5" or g == "6":
				status("You are restricted to drive at this hour! Please wait until 9:30pm to drive.")
			elif g == "7":
				if h >30:
					status("You are safe to drive! Watch out next week.")
				else:
					status("Your vehicle is restricted right now! Do not drive until 7:30pm.")

			else:
				status("You are safe to drive at the moment. Please advise the restricted times for your  vehicle today from 7am to 9am and 4pm to 7:30pm")
				pass
	
	if lnum.get() and hnum.get() and dnum.get():
		converted = str(hnum.get())+str(time1.get())
		datetime_object = datetime.strptime(str(dnum.get()), '%m/%d/%Y')
		day = datetime_object.weekday()
		t = str(hnum.get())
		if day == 0:
			status1("Today is Monday")
		elif day ==1:
			status1("Today is Tuesday")
		elif day ==2:
			status1("Today is Wednesday")
		elif day ==3:
			status1("Today is Thursday")
		elif day ==4:
			status1("Today is Friday")
		elif day ==5:
			status1("Today is Saterday")
		elif day ==6:
			status1("Today is Sunday")
		#apple = the last numer of the plate
		apple = int(lnum.get()[-1:])
		#monday
		if  apple == 1 or apple ==2:
			if day == 0:
				status2("Your Vehicle has restrictions today between 7:00am to 9:30am & 4:00pm to 7:30pm")
				timecheck(t)					
			else:
				status2("Your vehicle is safe to drive today! Your Vehicles Restricted day is Monday." )			
		#Tuesday
		elif apple == 3 or apple ==4:
			if day == 1:
				status2("Your Vehicle has restrictions today between 7:00am to 9:30am & 4:00pm to 7:30pm")
				timecheck(t)					
			else:
				status("Your vehicle is safe to drive today! Your Vehicles Restricted day is Tuesday." )			
		#wednesday
		elif apple == 5 or apple ==6:
			if day == 2:
				status2("Your Vehicle has restrictions today between 7:00am to 9:30am & 4:00pm to 7:30pm")
				timecheck(t)					
			else:
				status2("Your vehicle is safe to drive today! Your Vehicles Restricted day is Wednesday." )			
		#thursday
		elif apple == 7 or apple ==8:
			if day == 3:
				status2("Your Vehicle has restrictions today between 7:00am to 9:30am & 4:00pm to 7:30pm")
				timecheck(t)					
			else:
				status2("Your vehicle is safe to drive today! Your Vehicles Restricted day is Thursday." )			
		#friday	
		elif apple == 9 or apple ==0: 
			if day == 4:
				status2("Your Vehicle has restrictions today between 7:00am to 9:30am & 4:00pm to 7:30pm")
				timecheck(t)					
			else:
				status2("Your vehicle is safe to drive today! Your Vehicles Restricted day is Friday." )			
	else:
		status2("Please fill out all required feilds!")	

submit = Button(root, text="Submit", bg="green", fg="white", command=sbmt)
submit.pack(side=BOTTOM)



root.mainloop()
