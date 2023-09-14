import tkinter as tk
import pandas as pd
import numpy as np
 
app=tk.Tk()
app.geometry("950x500")
app.title("breast_cancer_detection.pkl")
m=pd.read_pickle("breast_cancer_detection.pkl")

input1=tk.Variable(app)
input2=tk.Variable(app)
input3=tk.Variable(app)
input4=tk.Variable(app)
input5=tk.Variable(app)
input6=tk.Variable(app)
input7=tk.Variable(app)
input8=tk.Variable(app)
input9=tk.Variable(app)
input10=tk.Variable(app)
input11=tk.Variable(app)
input12=tk.Variable(app)
input13=tk.Variable(app)
input14=tk.Variable(app)
input15=tk.Variable(app)
input16=tk.Variable(app)
input17=tk.Variable(app)
input18=tk.Variable(app)
input19=tk.Variable(app)
input20=tk.Variable(app)
input21=tk.Variable(app)
input22=tk.Variable(app)
input23=tk.Variable(app)
input24=tk.Variable(app)
input25=tk.Variable(app)
input26=tk.Variable(app)
input27=tk.Variable(app)
input28=tk.Variable(app)
input29=tk.Variable(app)
input30=tk.Variable(app)



tk.Entry(textvariable=input1).place(x=30,y=40)
tk.Label(fg="blue",font=("arial",10),text="mean radius",).place(x=26,y=20)

tk.Entry(textvariable=input2).place(x=180,y=40)
tk.Label(fg="blue",font=("arial",10),text='mean texture',).place(x=176,y=20)

tk.Entry(textvariable=input3).place(x=330,y=40)
tk.Label(fg="blue",font=("arial",10),text="mean perimeter",).place(x=326,y=20)

tk.Entry(textvariable=input4).place(x=480,y=40)
tk.Label(fg="blue",font=("arial",10),text="mean area",).place(x=476,y=20)

tk.Entry(textvariable=input5).place(x=630,y=40)
tk.Label(fg="blue",font=("arial",10),text="mean smoothness",).place(x=626,y=20)

tk.Entry(textvariable=input6).place(x=780,y=40)
tk.Label(fg="blue",font=("arial",10),text="mean compactness",).place(x=776,y=20)



tk.Entry(textvariable=input7).place(x=30,y=100)
tk.Label(fg="blue",font=("arial",10),text="mean concavity",).place(x=26,y=80)

tk.Entry(textvariable=input8).place(x=180,y=100)
tk.Label(fg="blue",font=("arial",10),text="mean concave points",).place(x=176,y=80)

tk.Entry(textvariable=input9).place(x=330,y=100)
tk.Label(fg="blue",font=("arial",10),text="mean symmetry",).place(x=326,y=80)

tk.Entry(textvariable=input10).place(x=480,y=100)
tk.Label(fg="blue",font=("arial",10),text="mean fractal dimension",).place(x=476,y=80)

tk.Entry(textvariable=input11).place(x=630,y=100)
tk.Label(fg="blue",font=("arial",10),text="radius error",).place(x=626,y=80)

tk.Entry(textvariable=input12).place(x=780,y=100)
tk.Label(fg="blue",font=("arial",10),text="texture error",).place(x=776,y=80)




tk.Entry(textvariable=input13).place(x=30,y=160)
tk.Label(fg="blue",font=("arial",10),text="perimeter error",).place(x=26,y=140)

tk.Entry(textvariable=input14).place(x=180,y=160)
tk.Label(fg="blue",font=("arial",10),text="area error",).place(x=176,y=140)

tk.Entry(textvariable=input15).place(x=330,y=160)
tk.Label(fg="blue",font=("arial",10),text="smoothness error",).place(x=326,y=140)

tk.Entry(textvariable=input16).place(x=480,y=160)
tk.Label(fg="blue",font=("arial",10),text="compactness error",).place(x=476,y=140)

tk.Entry(textvariable=input17).place(x=630,y=160)
tk.Label(fg="blue",font=("arial",10),text="concavity error",).place(x=626,y=140)

tk.Entry(textvariable=input18).place(x=780,y=160)
tk.Label(fg="blue",font=("arial",10),text="concave points error",).place(x=776,y=140)



tk.Entry(textvariable=input19).place(x=30,y=220)
tk.Label(fg="blue",font=("arial",10),text="symmetry error",).place(x=26,y=200)

tk.Entry(textvariable=input20).place(x=180,y=220)
tk.Label(fg="blue",font=("arial",10),text="fractal dimension error",).place(x=176,y=200)

tk.Entry(textvariable=input21).place(x=330,y=220)
tk.Label(fg="blue",font=("arial",10),text="worst radius",).place(x=326,y=200)

tk.Entry(textvariable=input22).place(x=480,y=220)
tk.Label(fg="blue",font=("arial",10),text="worst texture",).place(x=476,y=200)

tk.Entry(textvariable=input23).place(x=630,y=220)
tk.Label(fg="blue",font=("arial",10),text="worst perimeter",).place(x=626,y=200)

tk.Entry(textvariable=input24).place(x=780,y=220)
tk.Label(fg="blue",font=("arial",10),text="worst area",).place(x=776,y=200)




tk.Entry(textvariable=input25).place(x=30,y=280)
tk.Label(fg="blue",font=("arial",10),text="worst smoothness",).place(x=26,y=260)

tk.Entry(textvariable=input26).place(x=180,y=280)
tk.Label(fg="blue",font=("arial",10),text="worst compactness",).place(x=176,y=260)

tk.Entry(textvariable=input27).place(x=330,y=280)
tk.Label(fg="blue",font=("arial",10),text="worst concavity",).place(x=326,y=260)

tk.Entry(textvariable=input28).place(x=480,y=280)
tk.Label(fg="blue",font=("arial",10),text="worst concave points",).place(x=476,y=260)

tk.Entry(textvariable=input29).place(x=630,y=280)
tk.Label(fg="blue",font=("arial",10),text="worst fractal dimension",).place(x=626,y=260)

tk.Entry(textvariable=input30).place(x=780,y=280)
tk.Label(fg="blue",font=("arial",10),text="worst symmetry",).place(x=776,y=260)
















def function():
    i1= eval(input1.get())
    i2= eval(input2.get())
    i3= eval(input3.get())
    i4= eval(input4.get())
    i5= eval(input5.get())
    i6= eval(input6.get())
    i7= eval(input7.get())
    i8= eval(input8.get())
    i9= eval(input9.get())
    i10= eval(input10.get())
    i11= eval(input11.get())
    i12= eval(input12.get())
    i13= eval(input13.get())
    i14= eval(input14.get())
    i15= eval(input15.get())
    i16= eval(input16.get())
    i17= eval(input17.get())
    i18= eval(input18.get())
    i19= eval(input19.get())
    i20= eval(input20.get())
    i21= eval(input21.get())
    i22= eval(input22.get())
    i23= eval(input23.get())
    i24= eval(input24.get())
    i25= eval(input25.get())
    i26= eval(input26.get())
    i27= eval(input27.get())
    i28= eval(input28.get())
    i29= eval(input29.get())
    i30= eval(input30.get())
    

    query = pd.DataFrame({'1':[i1],'2':[i2], '3':[i3],'4':[i4],"5":[i5],"6":[i6] 
                         ,'7':[i7],'8':[i8], '9':[i9],'10':[i10],"11":[i11],"12":[i12] 
                          ,'13':[i13],'14':[i14], '15':[i15],'16':[i16],"17":[i17],"18":[i18] 
                         , '19':[i19],'20':[i20], '21':[i21],'22':[i22],"23":[i23],"24":[i24] 
                         , '25':[i25],'26':[i26], '27':[i27],'28':[i28],"29":[i29],"30":[i30] })
    a=m.predict(query)[0]
    op=a.reshape(-1)[0]
    if op==0:
      result.set("MALIGNANT")
    elif op==1:
      result.set("BENIGN")
    
    
        
        

result=tk.Variable(app)
result.set("ENTER THE ABOVE DETAILS TO \nFIND OUT THE TYPE OF BREAST CANCER")
tk.Label(textvariable=result,font=("arial",15),height=7,width=50,borderwidth=2,).place(x=200,y=380)

tk.Button(app,text='FIND OUT',font=("arial",13),bg="green",fg="white",command=function).place(x=430,y=340)


app.mainloop()
