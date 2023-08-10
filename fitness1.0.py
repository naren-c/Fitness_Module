from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt


root = Tk()
root.minsize(1000, 1000) 
title = Label(root , text = "FITNESS MODULE",font =('Verdana', 20))
title.configure(anchor = 'center')
title.grid(row = 0, column = 3, sticky = "W")




wtLabel = Label(root, text = "Enter your weight in kilograms").grid(row = 1, column = 0, sticky = "W", pady = 20)
wt = Entry(root, width = 20)
wt.grid(row = 1, column = 1, sticky = "W", pady = 20)

htLabel = Label(root, text = "Enter your height in meters").grid(row = 2, column = 0, sticky = "W", pady = 20)
ht = Entry(root, width = 20)
ht.grid(row = 2, column = 1, sticky = "W", pady = 20)

def calculate_bmi():
    bmi = float(wt.get())/float(ht.get())**2
    
    if bmi <15:
        bmi_msg = "You are very severely underweight"
    elif bmi>=15 and bmi<16:
        bmi_msg = "You are severely underweight"
    elif bmi>=16 and bmi<18.5:
        bmi_msg = "You are underweight"
    elif bmi>=18.5 and bmi<25:
        bmi_msg = "You are HEALTHY :)"
    elif bmi>=25 and bmi<30:
        bmi_msg = "You are overweight"
    elif bmi>=30 and bmi<35:
        bmi_msg = "You are moderately obese"
    elif bmi>=35 and bmi<40:
        bmi_msg = "You are severely obese"
    else:
        bmi_msg = "Very severely obese"
    bmi_output = Label(root, text = "Your BMI is "+str(round(bmi,2))+". "+bmi_msg).grid(row = 2 , column = 3, sticky = "W", padx = 10, pady = 10)
    bmi_plotgraph(bmi)

def bmi_plotgraph(bmi):
    y=[2400,5000,9000,12500,14000,12900,11000,8700,7400,6500,5200,4800,3750,3200,2800,2350,2000,1700,1450,1250,1150,1000,850]
    x=np.arange(len(y))
    x_bmi = x+18

    fig, ax = plt.subplots(figsize =(10, 6))


    ax.bar(x,y,width=0.8,color='y')
    ax.set_ylabel("Number of patients")
    ax.set_title("Number of patients and bmi")
    ax.set_xlabel("BMI")
    ax.set_xticks(x)
    ax.set_xticklabels(x_bmi)
    ax.set_yticks(np.arange(0,15000,1000))

    for index,value in enumerate(y):
        if (index+18)<=bmi and (index+18)>bmi-1:
            plt.text(index-0.5,value,str(value)+"<--You are here")
        else:
            plt.text(index-0.5,value,str(value))

    plt.show()

    
bt1 = Button(root,text="Calculate your BMI",bg="light blue", command=calculate_bmi)
bt1.grid(row=1,column=3, sticky = "W", padx = 10, pady = 10)




sysLabel = Label(root, text = "Enter your systolic BP (between 70 to 190)").grid(row = 3, column = 0, sticky = "W", pady = 20)
sys = Entry(root, width = 20)
sys.grid(row = 3, column = 1, sticky = "W", pady = 20)

diaLabel = Label(root, text = "Enter your diastolic BP (between 40 to 100)").grid(row = 4, column = 0, sticky = "W", pady = 20)
dia = Entry(root, width = 20)
dia.grid(row = 4, column = 1, sticky = "W", pady = 20)

def bloodpressure():
    systolic = int(sys.get())
    diastolic = int(dia.get())
               
    if systolic<90 and diastolic<60:
        bp_msg = "You have low blood pressure"
    elif (systolic>=90 and systolic<120) or (diastolic>=60 and diastolic<80):
        bp_msg = "Your blood pressure levels are normal"
    elif (systolic>=120 and systolic<140) or (diastolic>=80 and diastolic<90):
        bp_msg = "You  are in prehypertension state"
    elif (systolic>=140 and systolic<160) or (diastolic>=90 and diastolic<100):
        bp_msg = "You are diagnosed with hypertension, stage 1"
    elif systolic>=160 or diastolic>=100:
        bp_msg = "You are diagnosed with hypertension, stage 2"
    bloodpressure_output = Label(root, text = bp_msg).grid(row = 3 , column = 4, sticky = "W", padx = 10, pady = 10)
    blood_pressure_heatmap(systolic,diastolic)

def blood_pressure_heatmap(systolic,diastolic):
    
    blpr = np.arange(200*200).reshape(200, 200)#blood pressure array
    fig, ax = plt.subplots()
    im = ax.imshow(blpr,cmap='inferno_r')
    

    if systolic<90 and diastolic<60:
        text=plt.text(systolic,diastolic,("<-- you are here,\nlow blood pressure"))

    elif (systolic>=90 and systolic<120) or (diastolic>=60 and diastolic<80):
        plt.text(systolic,diastolic,("<-- you are here,\nblood pressure levels are normal"))

    elif (systolic>=120 and systolic<140) or (diastolic>=80 and diastolic<90):
        plt.text(systolic,diastolic,("<-- you are here,\nin prehypertension state"))

    elif (systolic>=140 and systolic<160) or (diastolic>=90 and diastolic<100):
        plt.text(systolic,diastolic,("<-- you are here,\ndiagnosed with hypertension, stage 1"))

    elif systolic>=160 or diastolic>=100:
        plt.text(systolic,diastolic,("<-- you are here,\ndiagnosed with hypertension, stage 2"))

    ax.set_title("blood pressure graph")
    ax.set_xlabel('systolic')
    ax.set_ylabel('diastolic')
    plt.show()


bt2 = Button(root,text="Evaluate your Blood Pressure",bg = "light blue",command=bloodpressure)
bt2.grid(row=3,column=3, sticky = "W", padx = 10, pady = 10)


def cal_pulse():
    systolic = int(sys.get())
    diastolic = int(dia.get())
    pulse = systolic-diastolic
    
    if pulse<40:
        pul_msg = "You have low pulse pressure"
    if pulse>=40 and pulse<60:
        pul_msg = "Your pulse is normal"
    else:
        pul_msg = "Your pulse is high"
    pulse_output = Label(root, text = pul_msg).grid(row = 4 , column = 4, sticky = "W",padx = 10, pady = 10)

bt3 = Button(root,text="Calculate pulse",bg = "light blue",command=cal_pulse)
bt3.grid(row=4,column=3, sticky = "W", padx = 10, pady = 10)






hrLabel = Label(root, text = "Enter your heart rate ").grid(row = 5, column = 0, sticky = "W", pady = 20)
hr = Entry(root, width = 20)
hr.grid(row = 5 , column = 1, sticky = "W", pady = 20)

def heart_rate():
    heart_rate = int(hr.get())
                 
    if heart_rate>50 and heart_rate<65:
        heart_msg = "Your heart rate is Bradycardia"
    elif heart_rate>100:
        heart_msg = "Your eart rate is Tachycardia"
    else:
        heart_msg = "Heart rate is Normal"
    heartrate_output = Label(root, text = heart_msg).grid(row = 5 , column = 4, sticky = "W", padx = 10, pady = 10)

bt4 = Button(root,text="Evaluate heart rate",bg= "light blue",command=heart_rate)
bt4.grid(row=5,column=3, sticky = "W", padx = 10, pady = 10)





gluLabel = Label(root, text = "Read your blood sugar level using a glucometer ").grid(row = 6, column = 0, sticky = "W", pady = 20)

fastingLabel = Label(root, text = "Enter your blood sugar reading in mg/dl after fasting(8hr/overnight) ").grid(row = 7, column = 0, sticky = "W", pady = 20)
fasting = Entry(root, width = 20)
fasting.grid(row = 7, column = 1, sticky = "W", pady = 20)

afterfoodLabel = Label(root, text = "Enter your blood sugar reading in mg/dl 2 hours after eating ").grid(row = 8, column = 0, sticky = "W", pady = 20)
afterfood = Entry(root, width = 20)
afterfood.grid(row = 8, column = 1, sticky = "W", pady = 20)

def bloodsugar1():
    
    fasting_sugar = int(fasting.get())
    sugar1_msg = ""
    if fasting_sugar<60:
        sugar1_msg = "Low sugar,  have a chocolate or sweet A.S.A.P"
    elif fasting_sugar>=60 and fasting_sugar<100:
        sugar1_msg = "Your sugar levels are normal"
    elif fasting_sugar>=100 and fasting_sugar<126:
        sugar1_msg = "Your sugar levels are in prediabetes state"
    else:
        sugar1_msg = "You have diabetes"
    fastingdisplayLabel = Label(root, text = sugar1_msg).grid(row = 7, column = 4, sticky = "W", padx = 10, pady = 10)
        
def bloodsugar2():
    
    afterfood_sugar = int(afterfood.get())
    sugar2_msg = ""
    if afterfood_sugar<70:
        sugar2_msg = "Low sugar,  have a chocolate or sweet A.S.A.P"
    elif afterfood_sugar>=70 and afterfood_sugar<140:
        sugar2_msg = "Your sugar levels are normal"
    elif afterfood_sugar>=140 and afterfood_sugar<199:
        sugar2_msg = "Your sugar levels are in prediabetes state"
    else:
        sugar2_msg = "You have diabetes"
    afterfooddisplayLabel = Label(root, text = sugar2_msg).grid(row = 8, column = 4, sticky = "W",padx = 10, pady = 10)

bt5 = Button(root,text="Evaluate fasting sugar level",bg = "light blue",command=bloodsugar1)
bt5.grid(row=7,column=3, sticky = "W",padx = 10, pady = 10)

bt6 = Button(root,text="Evaluate after food sugar level",bg = "light blue",command=bloodsugar2)
bt6.grid(row=8,column=3, sticky = "W", padx = 10, pady = 10)




calLabel = Label(root, text = "Enter steps in multiples of 500 ").grid(row = 9, column = 0, sticky = "W", pady = 20)
cal = Entry(root, width = 20)
cal.grid(row = 9, column = 1, sticky = "W", pady = 20)

def calories():

    n = int(cal.get())
    cal_500 = 500*0.04
    cal1={}
    for i in range(n):
        cal1[(i+1)*500] = (500*(i+1)*0.04)

    for i,k in cal1.items():
        cal1_msg = str(i) + " steps:" + " " + str(k) + " calories burnt"
    caldisplayLabel = Label(root, text = cal1_msg).grid(row = 9, column = 4, sticky = "W", padx = 10, pady = 10)

bt7 = Button(root,text="Check calories burned ",bg = "light blue",command=calories)
bt7.grid(row=9,column=3, sticky = "W", padx = 10, pady = 10)




root.mainloop()






