from course_work import Solution
import tkinter  as tk 
from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# GUI solution for ploting graph of sales vs date

my_w = tk.Tk()
my_w.geometry("400x400") 
my_w.title("Store Visualization Analysis")
# add one Label 
l0 = tk.Label(my_w, text='Store Info', font=('Helvetica', 16), width=30,anchor="c" )  
l0.grid(row=1,column=1,columnspan=4)

l2 = tk.Label(my_w,  text='Store Number: ', width=15)  
l2.grid(row=4,column=1)

# add one text box
t2 = tk.Text(my_w,  height=1, width=15,bg='white') 
t2.grid(row=4,column=2)

l3 = tk.Label(my_w,  text='Department Number: ', width=18 )  
l3.grid(row=5,column=1)

# add one text box
t3 = tk.Text(my_w,  height=1, width=15,bg='white') 
t3.grid(row=5,column=2)

b1 = tk.Button(my_w,  text='Store Viz Analysis', width=15, command=lambda: storeChart())  
b1.grid(row=8,column=2) 
my_str = tk.StringVar()

my_str = tk.StringVar()
l5 = tk.Label(my_w,  textvariable=my_str, width=10)
l5.grid(row=6, column=3)


def storeChart():
    flag_validation = True
    store = t2.get("1.0", END) 
    dept = t3.get("1.0", END) 
    
    # to check if the values inputted are integers
    try:
      int(store)
      int(dept)
    except:
      flag_validation = False
      
    header = ['Store','Dept','Date', 'Weekly_Sales']

    if flag_validation:
        sales_data = pd.read_csv('sales_data-set.csv', usecols=header)
        
        # to select only records that have the same store and department number inputed
        sales_new = sales_data[(sales_data.Store == int(store)) &(sales_data.Dept == int(dept))]
        print(sales_new)
        
        plt.plot(sales_new.Date, sales_new.Weekly_Sales)
        plt.xticks(rotation = 50)
        # to select only 50 records to show
        plt.xlim([0, 50])
        plt.show()
    else:
        my_str.set("Invalid input")
    

    
    
my_w.mainloop()