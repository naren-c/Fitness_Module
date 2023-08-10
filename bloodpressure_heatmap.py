
def blood_pressure_heatmap(systolic,diastolic):
    
    blpr = np.arange(200*200).reshape(200, 200)#blood pressure array
    fig, ax = plt.subplots()
    im = ax.imshow(blpr,cmap='inferno_r')
    

    if systolic<90 and diastolic<60:
        text=plt.text(systolic,diastolic,("0<-- you are here,\nlow blood pressure"))

    elif (systolic>=90 and systolic<120) or (diastolic>=60 and diastolic<80):
        plt.text(systolic,diastolic,("0<-- you are here,\nblood sugar levels are normal"))

    elif (systolic>=120 and systolic<140) or (diastolic>=80 and diastolic<90):
        plt.text(systolic,diastolic,("0<-- you are here,\nin prehypertension state"))

    elif (systolic>=140 and systolic<160) or (diastolic>=90 and diastolic<100):
        plt.text(systolic,diastolic,("0<-- you are here,\ndiagnosed with hypertension, stage 1"))

    elif systolic>=160 or diastolic>=100:
        plt.text(systolic,diastolic,("0<-- you are here,\ndiagnosed with hypertension, stage 2"))

    ax.set_title("blood pressure graph")
    ax.set_xlabel('systolic')
    ax.set_ylabel('diastolic')
    plt.show()

"""
systolic=80#just taking values now to show as an example
diastolic=50
#you will have to take value of systolic and diastolic from gui and pass it through this haeatmap


#blood_pressure_heatmap(systolic,diastolic)#calling the heatma
"""
