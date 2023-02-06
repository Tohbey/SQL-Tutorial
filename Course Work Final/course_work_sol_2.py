from course_work import Solution
import tkinter as tk
from tkinter import *

# GUI solution for updating store record info

res = Solution()

my_w = tk.Tk()
my_w.geometry("600x300")
my_w.title("Manager Info")

#res = Solution()

# add one Label
l0 = tk.Label(my_w,  text='Update Manager', font=('Helvetica', 16), width=30, anchor="c")
l0.grid(row=1, column=1, columnspan=4)

l1 = tk.Label(my_w,  text='Store Number: ', width=15, anchor="c")
l1.grid(row=3, column=1)

# add list box for selection of class
options = StringVar(my_w)
options.set(" ")  # default value

opt1 = OptionMenu(my_w, options, *res.returnStoreNumbers())
opt1.grid(row=3, column=2)

l2 = tk.Label(my_w,  text='Manager Name: ', width=15)
l2.grid(row=4, column=1)

# add one text box
t2 = tk.Text(my_w,  height=1, width=30, bg='white')
t2.grid(row=4, column=2)

l3 = tk.Label(my_w,  text='Years as Manager: ', width=15)
l3.grid(row=5, column=1)

# add one text box
t3 = tk.Text(my_w,  height=1, width=30, bg='white')
t3.grid(row=5, column=2)

l4 = tk.Label(my_w,  text='Manager Email: ', width=15)
l4.grid(row=6, column=1)

# add one text box
t4 = tk.Text(my_w,  height=1, width=30, bg='white')
t4.grid(row=6, column=2)

l5 = tk.Label(my_w,  text='Street Address: ', width=15)
l5.grid(row=7, column=1)

# add one text box
t5 = tk.Text(my_w,  height=1, width=30, bg='white')
t5.grid(row=7, column=2)

l7 = tk.Label(my_w,  text='City: ', width=15)
l7.grid(row=8, column=1)

# add one text box
t7 = tk.Text(my_w,  height=1, width=30, bg='white')
t7.grid(row=8, column=2)

l8 = tk.Label(my_w,  text='State: ', width=15)
l8.grid(row=9, column=1)

# add one text box
t8 = tk.Text(my_w,  height=1, width=30, bg='white')
t8.grid(row=9, column=2)

l9 = tk.Label(my_w,  text='Zipcode: ', width=15)
l9.grid(row=10, column=1)

# add one text box
t9 = tk.Text(my_w,  height=1, width=30, bg='white')
t9.grid(row=10, column=2)

b1 = tk.Button(my_w,  text='Update Record', width=10, command=lambda: update_data())
b1.grid(row=11, column=2)

my_str = tk.StringVar()
l5 = tk.Label(my_w,  textvariable=my_str, width=10)
l5.grid(row=6, column=3)
my_str.set("Email Check")

my_str = tk.StringVar()
l6 = tk.Label(my_w,  textvariable=my_str, width=50)
l6.grid(row=12, column=2)
my_str.set("Input Check")


def update_data():
   mail_validation = True  # set the flag
   flag_validation = True
   manager_name = t2.get("1.0", END)  # read name
   store_num = options.get()    # read store number
   year_manager = t3.get("1.0", END)  # read years as manager
   manager_email = t4.get("1.0", END)   # read manager email
   manager_address = t5.get("1.0", END)  # read manager address
   manager_city = t7.get("1.0", END) # read manager city
   manager_state = t8.get("1.0", END) # read manager state
   manager_zipcode = t9.get("1.0", END) # read manager zip code
   name_split = manager_name.split(" ", 2)
   

   if len(name_split) >= 2:
      name = name_split[0]+"."+name_split[1]
      mail_check = "".join([name.strip(),'@Walmart.org'])    
      print(mail_check)
      print(manager_email)
      if(manager_email.strip() != mail_check):
         mail_validation = False
   else:
      mail_validation = False
   
   # name_split => ['john', 'doe']
   
   try:
      val = int(year_manager)  # checking manager year as integer
   except:
      flag_validation = False
   
   print("mail validation ",mail_validation)
   print("flag validation ", flag_validation)
   if(mail_validation and flag_validation):
     
      try:
         res.updateStoreInfo(store_num.strip(), manager_name.strip(), year_manager.strip(), manager_email.strip(), manager_address.strip(),manager_city.strip(),manager_state.strip(), manager_zipcode.strip());
         my_str.set("Data Updated")
      except Exception as my_error:
         l5.grid()
         # return error
         l5.config(fg='red')   # foreground color
         l5.config(bg='yellow')  # background color
         print(my_error)
         my_str.set(my_error)
   
   else:
      l5.grid()
      l5.config(fg='red')   # foreground color
      l5.config(bg='yellow')  # background color
      if not mail_validation:
         my_str.set("Email Format should be xxx.yyy@Walmart.org")
      elif not flag_validation:
         my_str.set("Invalid input")
      else:
         my_str.set("Error")
      l5.after(3000, lambda: l5.grid_remove())

my_w.mainloop()