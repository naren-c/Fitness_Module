""" BMI"""
height = float(input("Enter your height in meters "))
weight = int(input("Enter your weight in kilograms "))

bmi = weight/(height)**2
print("Your BMI is",bmi)

if bmi <15:
    print("You are very severely underweight")
elif bmi>=15 and bmi<16:
    print("You are severely underweight")
elif bmi>=16 and bmi<18.5:
    print("You are underweight")
elif bmi>=18.5 and bmi<25:
    print("You are HEALTHY :)")
elif bmi>=25 and bmi<30:
    print("You are overweight")
elif bmi>=30 and bmi<35:
    print("You are moderately obese")
elif bmi>=35 and bmi<40:
    print("You are severely obese")
else:
    print("Very severely obese")





""" FOR EVERY 500 STEPS, BURN IN CALORIES(TAKING AVERAGE AS 0.04 CALORIES PES STEP)"""
cal_500 = 500*0.04
n = int(input("Enter steps in multiples of 500 "))
cal={}
for i in range(n):
    cal[i*500] = (500*i*0.04)

for i,k in cal.items():
    print(str(i) + " steps:" + " " + str(k) + " calories burnt")




""" BLOOD PRESSURE CALCULATION"""

systolic = int(input("Enter your systolic BP (between 70 to 190) "))
diastolic = int(input("Enter your diastolic BP (between 40 to 100) "))

if systolic<90 and diastolic<60:
    print("You have low blood pressure")
elif (systolic>=90 and systolic<120) or (diastolic>=60 and diastolic<80):
    print("Your blood sugar levels are normal")
elif (systolic>=120 and systolic<140) or (diastolic>=80 and diastolic<90):
    print("You  are in prehypertension state")
elif (systolic>=140 and systolic<160) or (diastolic>=90 and diastolic<100):
    print("You are diagnosed with hypertension, stage 1")
elif systolic>=160 or diastolic>=100:
    print("You are diagnosed with hypertension, stage 2")




""" PULSE"""
pulse = systolic-diastolic

if pulse<40:
    print("You have low pulse pressure")
if pulse>=40 and pulse<60:
    print("Your pulse is normal")
else:
    print("Your pulse is high")




"""SUGAR"""
print("Read your blood sugar level using a glucometer ")
g = int(input("Enter 1 to check fasting(8hr/overnight) blood sugar or enter 2 to check blood sugar, 2 hours after eating "))
h = int(input("Enter your blood sugar reading in mg/dl "))
if g == 1:
    if h<60:
        print("Low sugar,  have a chocolate or sweet A.S.A.P")
    elif h>=60 and h<100:
        print("Your sugar levels are normal")
    elif h>=100 and h<126:
        print("Your sugar levels are in prediabetes state")
    else:
        print("You have diabetes")
elif g == 2:
    if h<70:
        print("Low sugar,  have a chocolate or sweet A.S.A.P")
    elif h>=70 and h<140:
        print("Your sugar levels are normal")
    elif h>=140 and h<199:
        print("Your sugar levels are in prediabetes state")
    else:
        print("You have diabetes")
else:
    print("Invalid input chosen. Choose either 1 or 2 ONLY")





        



"""HEART RATE"""
heart_rate = int(input("Enter your heart rate "))
                 
if heart_rate>50 and heart_rate<65:
    print("Your heart rate is Bradycardia")
elif heart_rate>100:
    print("Your eart rate is Tachycardia")
else:
    print("Heart rate is Normal")
