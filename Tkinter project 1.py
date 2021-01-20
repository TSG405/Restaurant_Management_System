price={'Rice':150,
       'Daal':100,            # in this dict items stored as key and price of that item as value
       ' Kadai Paneer':130,
       'Butter paneer':150,
       'chicken Kasa':190,
       'Butter Chicken':200,
       'None':0}






def click():
# this func will be called when submit button will be pressed


    Customers_name=Name.get()
    Customers_phone=ph.get()


    A1=price[n1.get()]*q1.get()
    A2= price[n2.get() ]* q2.get()
    A3 = price[n3.get() ]* q3.get()
    A4 = price[n4.get() ]* q4.get()  #A sotres (price of item * quantity of that item) and calculates sub total
    A5 = price[n5.get() ]* q5.get()
    A6 = price[n6.get() ]* q6.get()
    A7 = price[n7.get() ]* q7.get()
    A8 = price[n8.get() ]* q8.get()
    A9 = price[n9.get() ]* q9.get()
    A10 = price[n10.get()] * q10.get()
    s1.set(A1)
    s2.set(A2)
    s3.set(A3)
    s4.set(A4)
    s5.set(A5)
    s6.set(A6) # setting the sub ammount entries
    s7.set(A7)
    s8.set(A8)
    s9.set(A9)
    s10.set(A10)
    total=A1+A2+A3+A4+A5+A6+A7+A8+A9+A10 # total amount to be payed
    AmmountToBePaid.set(total) #setting total ammount
    Payment_Mode=M.get()
    print(Payment_Mode)



        

from tkinter import *
root=Tk()
root.geometry('1200x600')
root.title('WELCOME TO Get Ready To Pay')
#Labels
Label(root,text="Contact Number").grid(row=1,column=3)
Label(root,text="Customer Name").grid(row=1)

Label(root,text=" Item Ordered").grid(row=2)
Label(root,text=" Item Ordered").grid(row=3)
Label(root,text=" Item Ordered").grid(row=4)
Label(root,text=" Item Ordered").grid(row=5)
Label(root,text=" Item Ordered").grid(row=6)
Label(root,text=" Item Ordered").grid(row=7)
Label(root,text=" Item Ordered").grid(row=8)
Label(root,text=" Item Ordered").grid(row=9)
Label(root,text=" Item Ordered").grid(row=10)
Label(root,text=" Item Ordered").grid(row=11)

Label(root,text="Ammount To Be Paid").grid(row=14)


Label(root,text="Quantity").grid(row=2,column=3)
Label(root,text="Quantity").grid(row=3,column=3)
Label(root,text="Quantity").grid(row=4,column=3)
Label(root,text="Quantity").grid(row=5,column=3)
Label(root,text="Quantity").grid(row=6,column=3)
Label(root,text="Quantity").grid(row=7,column=3)
Label(root,text="Quantity").grid(row=8,column=3)
Label(root,text="Quantity").grid(row=9,column=3)
Label(root,text="Quantity").grid(row=10,column=3)
Label(root,text="Quantity").grid(row=11,column=3)
Label(root,text="Amount").grid(row=2,column=6)
Label(root,text="Amount").grid(row=3,column=6)
Label(root,text="Amount").grid(row=4,column=6)
Label(root,text="Amount").grid(row=5,column=6)
Label(root,text="Amount").grid(row=6,column=6)
Label(root,text="Amount").grid(row=7,column=6)
Label(root,text="Amount").grid(row=8,column=6)
Label(root,text="Amount").grid(row=9,column=6)
Label(root,text="Amount").grid(row=10,column=6)
Label(root,text="Amount").grid(row=11,column=6)
# Payment mode
Label(root,text="Mode Of Payment").grid(row=15)





#Entry
#n stores name of item

n1 = StringVar()
n2 = StringVar()
n3= StringVar()
n4 = StringVar()
n5 = StringVar()
n6 = StringVar()
n7 = StringVar()
n8 = StringVar()
n9 = StringVar()
n10 = StringVar()
Name=StringVar()
ph=StringVar()
#q stores quantity
q1=IntVar()
q2=IntVar()
q3=IntVar()
q4=IntVar()
q5=IntVar()
q6=IntVar()
q7=IntVar()
q8=IntVar()
q9=IntVar()
q10=IntVar()
#S store Sub Ammount
s1=IntVar()
s2=IntVar()
s3=IntVar()
s4=IntVar()
s5=IntVar()
s6=IntVar()
s7=IntVar()
s8=IntVar()
s9=IntVar()
s10=IntVar()
# M stores payment mode
M=StringVar()


AmmountToBePaid=IntVar()

Entry(root,textvariable=Name).grid(row=1,column=2)
Entry(root,textvariable=ph).grid(row=1,column=4)
Entry(root,textvariable=AmmountToBePaid).grid(row=14,column=2)

# Entries for Quantity
Entry(root,textvariable=q1).grid(row=2,column=4)
Entry(root,textvariable=q2).grid(row=3,column=4)
Entry(root,textvariable=q3).grid(row=4,column=4)
Entry(root,textvariable=q4).grid(row=5,column=4)
Entry(root,textvariable=q5).grid(row=6,column=4)
Entry(root,textvariable=q6).grid(row=7,column=4)
Entry(root,textvariable=q7).grid(row=8,column=4)
Entry(root,textvariable=q8).grid(row=9,column=4)
Entry(root,textvariable=q9).grid(row=10,column=4)
Entry(root,textvariable=q10).grid(row=11,column=4)

# Entries for SubAmmount
Entry(root,textvariable=s1).grid(row=2,column=7)
Entry(root,textvariable=s2).grid(row=3,column=7)
Entry(root,textvariable=s3).grid(row=4,column=7)
Entry(root,textvariable=s4).grid(row=5,column=7)
Entry(root,textvariable=s5).grid(row=6,column=7)
Entry(root,textvariable=s6).grid(row=7,column=7)
Entry(root,textvariable=s7).grid(row=8,column=7)
Entry(root,textvariable=s8).grid(row=9,column=7)
Entry(root,textvariable=s9).grid(row=10,column=7)
Entry(root,textvariable=s10).grid(row=11,column=7)

#Drop Down Menu from this we can select items

items=['None','Rice',
       'Daal',
       ' Kadai Paneer',
       'Butter paneer',
       'chicken Kasa',
       'Butter Chicken']
OptionMenu(root, n1, *items).grid(row=2,column=2)
OptionMenu(root, n2, *items).grid(row=3,column=2)
OptionMenu(root, n3, *items).grid(row=4,column=2)
OptionMenu(root, n4, *items).grid(row=5,column=2)
OptionMenu(root, n5, *items).grid(row=6,column=2)
OptionMenu(root, n6, *items).grid(row=7,column=2)
OptionMenu(root, n7, *items).grid(row=8,column=2)
OptionMenu(root, n8, *items).grid(row=9,column=2)
OptionMenu(root, n9, *items).grid(row=10,column=2)
OptionMenu(root, n10, *items).grid(row=11,column=2)
#setting default value of the drop down as None
n1.set(items[0])
n2.set(items[0])
n3.set(items[0])
n4.set(items[0])
n5.set(items[0])
n6.set(items[0])
n7.set(items[0])
n8.set(items[0])
n9.set(items[0])
n10.set(items[0])

# Drop Down Menu For Selecting Payment Mode
mode=[
    'Cash',
    'Debit Card',
    'Credit Card',
    'UPI',
    'Google Pay',
    'Paytm']
OptionMenu(root, M, *mode).grid(row=15,column=2)



# Button
Button(root,text="SUBMIT",bg='Red',fg='Blue',command=click).grid(row=12,column=3)




root.mainloop()

