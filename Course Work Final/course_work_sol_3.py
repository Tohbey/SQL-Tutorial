from course_work import Solution
import tkinter  as tk 
from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# GUI solution for calculating mean date

res = Solution()

my_w = tk.Tk()
my_w.geometry("400x250") 
my_w.title("Store Analysis")
# add one Label 
l0 = tk.Label(my_w, text='Store Info', font=('Helvetica', 16), width=30,anchor="c" )  
l0.grid(row=1,column=1,columnspan=4)

l1 = tk.Label(my_w,  text='Store Type: ', width=10,anchor="c")  
l1.grid(row=3,column=1)


# add list box for selection of class
options = StringVar(my_w)
options.set("A") # default value

opt1 = OptionMenu(my_w, options, *res.returnStoreTypes())
opt1.grid(row=3,column=2)


b1 = tk.Button(my_w,  text='Store Mean Size', width=15, command=lambda: meanStoreSize())  
b1.grid(row=8,column=2) 
my_str = tk.StringVar()
l5 = tk.Label(my_w,  textvariable=my_str, width=10 )  
l5.grid(row=3,column=3) 
my_str.set("Mean Size")

# Visualization
l6 = tk.Label(my_w, text='Store Visualization', font=('Helvetica', 16), width=30,anchor="c" )  
l6.grid(row=9,column=1,columnspan=4)

l7 = tk.Label(my_w,  text='Store Number: ', width=15)  
l7.grid(row=10,column=1)

# add one text box
t7 = tk.Text(my_w,  height=1, width=15,bg='white') 
t7.grid(row=10,column=2)

l8 = tk.Label(my_w,  text='Department Number: ', width=18 )  
l8.grid(row=11,column=1)

# add one text box
t8 = tk.Text(my_w,  height=1, width=15,bg='white') 
t8.grid(row=11,column=2)

b2 = tk.Button(my_w,  text='Store Viz Analysis', width=15, command=lambda: storeChart())  
b2.grid(row=12,column=2) 
my_str1 = tk.StringVar()

my_str1 = tk.StringVar()
l9 = tk.Label(my_w,  textvariable=my_str1, width=10)
l9.grid(row=13, column=3)


def meanStoreSize():
  store_type = options.get()
  my_str.set(res.meanStoreSizeFn(store_type.strip()))

def storeChart():
  flag_validation = True
  store = t7.get("1.0", END)     
  dept = t8.get("1.0", END) 
    
  # to check if the values inputted are integers
  try:
    int(store)
    int(dept)
  except:
    flag_validation = False
        
    
  if flag_validation:
    select_statement = '''SELECT date, weekly_sales FROM sales WHERE store=? and dept=?'''
    print(select_statement)
    res.cursor.execute(select_statement,(int(store), int(dept)))
    data = res.cursor.fetchall()
    weeklySales = []
    dates = []
    print(data)
    for row in data:
      dates.append(row[0])
      weeklySales.append(row[1])
      
    print(len(dates))
    print(len(weeklySales))
    
    plt.plot(dates,weeklySales)
    plt.xticks(rotation = 50)
    plt.xlim([0, 20])
    
    plt.show()
  else:
    my_str1.set("Invalid input")  
    
my_w.mainloop()