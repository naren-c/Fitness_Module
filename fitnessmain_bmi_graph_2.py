from tkinter import *
#import fitness
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt


def display_all():
    
    #bmi
    bmi_count,bmi_message=bmi()
    bmi_label=Label(root,text='your bmi is '+str(bmi_count)+" "+bmi_message).grid(row=3,column = 0)
    bmi_plotgraph(bmi_count)

def bmi_plotgraph(bmi):
    y=[2400,5000,9000,12500,14000,12900,11000,8700,7400,6500,5200,4800,3750,3200,2800,2350,2000,1700,1450,1250,1150,1000,850]
    x=np.arange(len(y))
    x_bmi = x+18

    fig, ax = plt.subplots(figsize =(10, 6))


    ax.bar(x,y,width=0.8,color='y')
    ax.set_ylabel("number of patients")
    ax.set_title("number of patients and bmi")
    ax.set_xlabel("bmi")
    ax.set_xticks(x)
    ax.set_xticklabels(x_bmi)
    ax.set_yticks(np.arange(0,15000,1000))

    for index,value in enumerate(y):
        if (index+18)<=bmi and (index+18)>bmi-1:
            plt.text(index-0.5,value,str(value)+"<--you are here")
        else:
            plt.text(index-0.5,value,str(value))


    plt.show()




def bmi():
    
    height = float(bmi_entry1.get())
    weight = int(bmi_entry2.get())
    
    bmi = weight/(height)**2
    print("Your BMI is",bmi)

    if bmi <15:
        message =("You are very severely underweight")
    elif bmi>=15 and bmi<16:
        message = ("You are severely underweight")
    elif bmi>=16 and bmi<18.5:
        print("You are underweight")
    elif bmi>=18.5 and bmi<25:
        message=("You are HEALTHY :)")
    elif bmi>=25 and bmi<30:
        message=("You are overweight")
    elif bmi>=30 and bmi<35:
        message=("You are moderately obese")
    elif bmi>=35 and bmi<40:
        message=("You are severely obese")
    else:
        message=("Very severely obese")

    return bmi,message

        
root = Tk()
root.title("fitness module")


bmi_label1 = Label(root,text="Enter your height in meters").grid(row=1,column = 0) 
bmi_entry1= Entry(root,width=50)
bmi_entry1.grid(row=1,column=1)
        

bmi_label2 = Label(root,text="Enter your weight in kilograms ").grid(row=2,column = 0)
bmi_entry2= Entry(root,width=50)
bmi_entry2.grid(row=2,column=1)

    


display_button = Button(root,text='get results',command = display_all)
display_button.grid(row=3,column=2)

root.mainloop()
