#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from joblib import load
import numpy as np

def show_entry_fields():
    p1 = int(e1.get())   # CreditScore
    p2 = int(e2.get())   # Age
    p3 = int(e3.get())   # Tenure
    p4 = float(e4.get())  # Balance
    p5 = int(e5.get())   # NumOfProducts
    p6 = int(e6.get())   # HasCrCard
    p7 = int(e7.get())   # IsActiveMember
    p8 = float(e8.get())  # EstimatedSalary
    p9 = int(e9.get())   # Exited
    
    # Handling Geography values
    if p9 == 1:
        Geography_Germany = 1
        Geography_Spain = 0
        Geography_France = 0
    elif p9 == 2:
        Geography_Germany = 0
        Geography_Spain = 1
        Geography_France = 0
    elif p9 == 3:
        Geography_Germany = 0
        Geography_Spain = 0
        Geography_France = 1
    
    p10 = int(e10.get())  # Gender
    
    # Load the saved model
    model = load('churn_predict_model.joblib')  
    result = model.predict(np.array([[p1, p2, p3, p4, p5, p6, p7, p8, Geography_Germany, Geography_Spain, Geography_France, p10]]))
    
    if result == 0:
        print("Churn prediction: Not Churn")
    else:
        print("Churn prediction: Churn")

master = Tk()
master.title("Customer Churn Prediction")

Label(master, text='CreditScore').grid(row=1, column=0)
Label(master, text='Age').grid(row=2, column=0)
Label(master, text='Tenure').grid(row=3, column=0)
Label(master, text='Balance').grid(row=4, column=0)
Label(master, text='NumOfProducts').grid(row=5, column=0)
Label(master, text='HasCrCard').grid(row=6, column=0)
Label(master, text='IsActiveMember').grid(row=7, column=0)
Label(master, text='EstimatedSalary').grid(row=8, column=0)
Label(master, text='Geography').grid(row=9, column=0)
Label(master, text='Gender').grid(row=10, column=0)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)
e6 = Entry(master)
e7 = Entry(master)
e8 = Entry(master)
e9 = Entry(master)
e10 = Entry(master)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)
e5.grid(row=5, column=1)
e6.grid(row=6, column=1)
e7.grid(row=7, column=1)
e8.grid(row=8, column=1)
e9.grid(row=9, column=1)
e10.grid(row=10, column=1)

Button(master, text='Predict', command=show_entry_fields).grid(row=12, column=1)

mainloop()


# In[ ]:




