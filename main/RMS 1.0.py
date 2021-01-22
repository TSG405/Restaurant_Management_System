from tkinter import *
import random
import time
import datetime
from tkinter import messagebox, ttk



#================ INITIALIZATION =================
root=Tk()
root.geometry("1680x860")
root.title("Restaurant--Management--System KIOSK")
root.configure(background='pink')


#==================== FRAMING ====================
Tops = Frame(root, width=1550, height=80, bd=12, relief="raise")
Tops.pack(side = TOP)
lblTitle = Label(Tops, font=("aria", 28, 'bold'), text="      RESTAURANT  MANAGEMENT  SYSTEM      ",fg="steel blue",bd=10,anchor='w').grid(row=0, column=0)


#================ DISPLAY - TIME =================
localtime=time.asctime(time.localtime(time.time()))
lblInfo=Label(Tops,font=('aria',20,'bold'),text=localtime,fg="steel blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)

lblTitle = Label(Tops, font=("aria", 15, 'bold'), text="     __ TSG __    ",fg="steel blue",bd=10,anchor='w').grid(row=2, column=0)
BottomMainFrame = Frame(root, width=1550, height=770, bd=12, relief="raise")
BottomMainFrame.pack(side=BOTTOM)

f1 = Frame(BottomMainFrame, width=500, height=770, bd=12, relief=SUNKEN)
f1.pack(side=LEFT)
f1top = Frame(f1, width=500, height=570, bd=12, relief="raise")
f1top.pack(side=TOP)
f1bottom = Frame(f1, width=500, height=200, bd=12, relief="raise")
f1bottom.pack(side=BOTTOM)

f2 = Frame(BottomMainFrame, width=400, height=770, bd=12, relief=SUNKEN)
f2.pack(side=LEFT)
f2Top = Frame(f2, width=400, height=350, bd=4, relief="raise")
f2Top.pack(side=TOP)
f2Bottom = Frame(f2, width=400, height=450,bd=4, relief="raise")
f2Bottom.pack(side=BOTTOM)

f3 = Frame(BottomMainFrame, width=400, height=770, bd=12, relief=SUNKEN)
f3.pack(side=RIGHT)
f3top = Frame(f3, width=400, height=770, bd=12, relief="raise")
f3top.pack(side=TOP)
f3bottom = Frame(f3, width=400, height=100, bd=12, relief="raise")
f3bottom.pack(side=BOTTOM)


#==================== VARIABLES ===================
Receipt_Ref = StringVar()
DateofOrder = StringVar()
DateofOrder.set(time.strftime("%d/%m/%y"))

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var100 = IntVar()

var1.set(0)
var2.set(0)
var3.set(0)
var4.set(0)
var5.set(0)
var6.set(0)
var7.set(0)
var8.set(0)
var9.set(0)
var10.set(0)
var11.set(0)
var12.set(0)
var13.set(0)
var14.set(0)
var15.set(0)
var16.set(0)
var17.set(0)
var18.set(0)
var19.set(0)
var20.set(0)
var21.set(0)
var100.set(0)


#=========================== FRAME 1 VARIABLES =============================
varFries = StringVar()
varSalad = StringVar()
varHamburger = StringVar()
varDahiKabab = StringVar()
varKhandvi = StringVar()
varCheeseSandwich = StringVar()
varChickenSandwich = StringVar()
varFishSandwich = StringVar()

varFries.set(0)
varSalad.set(0)
varHamburger.set(0)
varDahiKabab.set(0)
varKhandvi.set(0)
varCheeseSandwich.set(0)
varChickenSandwich.set(0)
varFishSandwich.set(0)


#========================== FRAME 2 VARIABLES =============================
varChocoBrownie = StringVar()
varIcecream = StringVar()
varPaan = StringVar()
varBakedRasgulla = StringVar()
varJalebi = StringVar()

varChocoBrownie.set(0)
varIcecream.set(0)
varPaan.set(0)
varBakedRasgulla.set(0)
varJalebi.set(0)

varTotal = StringVar()
varCGST = StringVar()
varSGST = StringVar()
varServiceCharge = StringVar()
varPay = StringVar()
varPM = StringVar()
varTotal.set(0)
varCGST.set(0)
varSGST.set(0)
varServiceCharge.set(0)
varPay.set(0)


#========================== FRAME 3 VARIABLES =============================
varTea = StringVar()
varCola = StringVar()
varCoffee = StringVar()
varJuice = StringVar()
varWater= StringVar()
varChocolateShake = StringVar()
varFruitCocktail = StringVar()
varVanillaShake = StringVar()
varOreoKrusher = StringVar()

varTea.set(0)
varCoffee.set(0)
varCola.set(0)
varJuice.set(0)
varWater.set(0)
varChocolateShake.set(0)
varVanillaShake.set(0)
varOreoKrusher.set(0)



#============================= UTILITIES ==================================

def iExit():
    qExit = messagebox.askyesno("Restaurant Management KIOSK","Do you want to Quit ?")
    if qExit > 0:
        root.destroy()
        return 
    

def Reset():
    varFries.set(0)
    varSalad.set(0)
    varHamburger.set(0)
    varDahiKabab.set(0)
    varKhandvi.set(0)
    varCheeseSandwich.set(0)
    varChickenSandwich.set(0)
    varFishSandwich.set(0)
    varChocoBrownie.set(0)
    varIcecream.set(0)
    varPaan.set(0)
    varBakedRasgulla.set(0)
    varJalebi.set(0)
    varTotal.set(0)
    varCGST.set(0)
    varSGST.set(0)
    varServiceCharge.set(0)
    varPay.set(0)
    varTea.set(0)
    varCoffee.set(0)
    varCola.set(0)
    varJuice.set(0)
    varWater.set(0)
    varChocolateShake.set(0)
    varVanillaShake.set(0)
    varOreoKrusher.set(0)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)

    txtFries.configure(state=DISABLED)
    txtSalad.configure(state=DISABLED)
    txtHamburger.configure(state=DISABLED)
    txtDahiKabab.configure(state=DISABLED)
    txtKhandvi.configure(state=DISABLED)
    txtCheeseSandwich.configure(state=DISABLED)
    txtChickenSandwich.configure(state=DISABLED)
    txtFishSandwich.configure(state=DISABLED)
    txtChocoBrownie.configure(state=DISABLED)
    txtIcecream.configure(state=DISABLED)
    txtPaan.configure(state=DISABLED)
    txtBakedRasgulla.configure(state=DISABLED)
    txtJalebi.configure(state=DISABLED)
    txtTotal.configure(state=DISABLED)
    txtCGST.configure(state=DISABLED)
    txtSGST.configure(state=DISABLED)
    txtServiceCharge.configure(state=DISABLED)
    txtpay.configure(state=DISABLED)
    txtTea.configure(state=DISABLED)
    txtCoffee.configure(state=DISABLED)
    txtCola.configure(state=DISABLED)
    txtJuice.configure(state=DISABLED)
    txtWater.configure(state=DISABLED)
    txtChocolateShake.configure(state=DISABLED)
    txtOreoKrusher.configure(state=DISABLED)
    txtVanillaShake.configure(state=DISABLED)
    txtOreoKrusher.configure(state=DISABLED)



def Receipt():
    roor = Tk()
    roor.geometry("660x800")

    f1 = Frame(roor, width = 1600, height = 700, bd = 12, relief = "raise")
    f1.pack()
    lblReceipt = Label(f1, font=('arial', 12, 'bold'), text="Receipt", bd=2, anchor='w')
    lblReceipt.grid(row=0, column=0, sticky=W)
    txtReceipt = Text(f1, width=64, height=35, bg="white", bd=8, font=('arial', 11, 'bold'))
    txtReceipt.grid(row=1, column=0)
    txtReceipt.delete("1.0", END)
    
    x = random.randint(1000, 500890)
    randomRef = str(x)
    Receipt_Ref.set("BILL" + randomRef)

    txtReceipt.insert(END, 'Receipt Ref:\t\t\t'+ Receipt_Ref.get() + '\t\t\t' + DateofOrder.get()+"\n")
    txtReceipt.insert(END, '\n\nITEMS\t\t\t\t' + "No. of ITEMS \n\n")
    txtReceipt.insert(END, 'Fries:\t\t\t\t\t' + varFries.get() + "\n")
    txtReceipt.insert(END, 'Salad: \t\t\t\t\t' + varSalad.get() + "\n")
    txtReceipt.insert(END, 'HamBurger: \t\t\t\t\t' + varHamburger.get() + "\n")
    txtReceipt.insert(END, 'Dahi Kabab: \t\t\t\t\t' + varDahiKabab.get() + "\n")
    txtReceipt.insert(END, 'Khandvi: \t\t\t\t\t' + varKhandvi.get() + "\n")
    txtReceipt.insert(END, 'Veg Sandwich: \t\t\t\t\t' + varCheeseSandwich.get() + "\n")
    txtReceipt.insert(END, 'Chicken Sandwich: \t\t\t\t\t' + varChickenSandwich.get() + "\n")
    txtReceipt.insert(END, 'Fish Sandwich: \t\t\t\t\t' + varFishSandwich.get() + "\n")
    txtReceipt.insert(END, 'Chocolate Brownie: \t\t\t\t\t' + varChocoBrownie.get() + "\n")
    txtReceipt.insert(END, 'Icecream: \t\t\t\t\t' + varIcecream.get() + "\n")
    txtReceipt.insert(END, 'Paan: \t\t\t\t\t' + varPaan.get() + "\n")
    txtReceipt.insert(END, 'Baked Rasgulla: \t\t\t\t\t' + varBakedRasgulla.get() + "\n")
    txtReceipt.insert(END, 'Jalebi: \t\t\t\t\t' + varJalebi.get() + "\n")
    txtReceipt.insert(END, 'Tea: \t\t\t\t\t' + varTea.get() + "\n")
    txtReceipt.insert(END, 'Coffee: \t\t\t\t\t' + varCoffee.get() + "\n")
    txtReceipt.insert(END, 'Cola: \t\t\t\t\t' + varCola.get() + "\n")
    txtReceipt.insert(END, 'Juice: \t\t\t\t\t' + varJuice.get() + "\n")
    txtReceipt.insert(END, 'Water: \t\t\t\t\t' + varWater.get() + "\n")
    txtReceipt.insert(END, 'Chocolate K: \t\t\t\t\t' + varChocolateShake.get() + "\n")
    txtReceipt.insert(END, 'Vanilla K: \t\t\t\t\t' + varVanillaShake.get() + "\n")
    txtReceipt.insert(END, 'Oreo K: \t\t\t\t\t' + varOreoKrusher.get() + "\n")
    txtReceipt.insert(END, '\nTotal Cost of Food: \t\t' + varTotal.get() + "\nCGST:\t\t" + varCGST.get() + "\nSGST:\t\t" +
                      varSGST.get() + "\nService Charge:\t\t" + varServiceCharge.get() + "\nTotal Payble amount:\t\t" + varPay.get())
    
    roor.mainloop()


def price_list():
    roo = Tk()
    roo.geometry("600x700")
    roo.title("Price List")

    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="_____________", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Fries", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="59", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Salad", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="49", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Hamburger", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="99", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Dahi Kabab", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="99", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Khandvi", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="59", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Veg Sandwich", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="79", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Chicken Sandwich", fg="steel blue", anchor=W)
    lblinfo.grid(row=7, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="99", fg="steel blue", anchor=W)
    lblinfo.grid(row=7, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Fish Sandwich", fg="steel blue", anchor=W)
    lblinfo.grid(row=8, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="119", fg="steel blue", anchor=W)
    lblinfo.grid(row=8, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Chocolate Brownie", fg="steel blue", anchor=W)
    lblinfo.grid(row=9, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="139", fg="steel blue", anchor=W)
    lblinfo.grid(row=9, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Icecream", fg="steel blue", anchor=W)
    lblinfo.grid(row=10, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="59", fg="steel blue", anchor=W)
    lblinfo.grid(row=10, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Paan", fg="steel blue", anchor=W)
    lblinfo.grid(row=11, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="39", fg="steel blue", anchor=W)
    lblinfo.grid(row=11, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Baked Rasgulla", fg="steel blue", anchor=W)
    lblinfo.grid(row=12, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="20", fg="steel blue", anchor=W)
    lblinfo.grid(row=12, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Jalebi", fg="steel blue", anchor=W)
    lblinfo.grid(row=13, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="39", fg="steel blue", anchor=W)
    lblinfo.grid(row=13, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Tea", fg="steel blue", anchor=W)
    lblinfo.grid(row=14, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="49", fg="steel blue", anchor=W)
    lblinfo.grid(row=14, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Coffee", fg="steel blue", anchor=W)
    lblinfo.grid(row=15, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="79", fg="steel blue", anchor=W)
    lblinfo.grid(row=15, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cola", fg="steel blue", anchor=W)
    lblinfo.grid(row=16, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="20", fg="steel blue", anchor=W)
    lblinfo.grid(row=16, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Juice", fg="steel blue", anchor=W)
    lblinfo.grid(row=17, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
    lblinfo.grid(row=17, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Mineral Water", fg="steel blue", anchor=W)
    lblinfo.grid(row=18, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="25", fg="steel blue", anchor=W)
    lblinfo.grid(row=18, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Chocolate K.", fg="steel blue", anchor=W)
    lblinfo.grid(row=19, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
    lblinfo.grid(row=19, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Oreo K.", fg="steel blue", anchor=W)
    lblinfo.grid(row=20, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="105", fg="steel blue", anchor=W)
    lblinfo.grid(row=20, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Vanilla K.", fg="steel blue", anchor=W)
    lblinfo.grid(row=21, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
    lblinfo.grid(row=21, column=3)
    
    roo.mainloop()


def TotalCost():
    m1 = float(varFries.get())
    m2 = float(varSalad.get())
    m3 = float(varHamburger.get())
    m4 = float(varDahiKabab.get())
    m5 = float(varKhandvi.get())
    m6 = float(varCheeseSandwich.get())
    m7 = float(varChickenSandwich.get())
    m8 = float(varFishSandwich.get())
    m9 = float(varChocoBrownie.get())
    m10 = float(varIcecream.get())
    m11 = float(varPaan.get())
    m12 = float(varBakedRasgulla.get())
    m13 = float(varJalebi.get())
    m14 = float(varTea.get())
    m15 = float(varCola.get())
    m16 = float(varCoffee.get())
    m17 = float(varJuice.get())
    m18 = float(varWater.get())
    m19 = float(varChocolateShake.get())
    m20 = float(varVanillaShake.get())
    m21 = float(varOreoKrusher.get())

    iTotal = (m1*59 + m2*49 + m3*99 + m4*99 + m5*59 + m6*79 + m7*99 + m8*119 + m9*139 + m10*59 + m11*39 + m12*20 + m13*39 + m14*49 + m15*20 + m16*79 +
                 m17*50 + m18*25 + m19*50 + m20*50 + m21*105)

    striTotal = 'Rs',str(iTotal)
    varTotal.set(striTotal)

    cgst = (9/100)*iTotal
    strcgst = 'Rs',str(cgst)
    varCGST.set(strcgst)

    sgst = (9/100)*iTotal
    strsgst = 'Rs',str(sgst)
    varSGST.set(strsgst)

    service_charge = 0.1*iTotal
    strService_charge = "Rs",str(service_charge)
    varServiceCharge.set(strService_charge)

    strPay = 'Rs', str('%.2f'%(iTotal+cgst+sgst+service_charge))
    varPay.set(strPay)


#============================== CHECK-BOXES =================================

def a():
    if var1.get() == 1:
        txtFries.configure(state=NORMAL)
        varFries.set("")
    elif var1.get() == 0:
        txtFries.configure(state=DISABLED)
        varFries.set("0")

def b():
    if var2.get() == 1:
        txtSalad.configure(state=NORMAL)
        varSalad.set("")
    elif var2.get() == 0:
        txtSalad.configure(state=DISABLED)
        varSalad.set("0")

def c():
    if var3.get() == 1:
        txtHamburger.configure(state=NORMAL)
        varHamburger.set("")
    elif var3.get() == 0:
        txtHamburger.configure(state=DISABLED)
        varHamburger.set("0")

def d():
    if var4.get() == 1:
        txtDahiKabab.configure(state=NORMAL)
        varDahiKabab.set("")
    elif var4.get() == 0:
        txtDahiKabab.configure(state=DISABLED)
        varDahiKabab.set("0")

def e():
    if var5.get() == 1:
        txtKhandvi.configure(state=NORMAL)
        varKhandvi.set("")
    elif var5.get() == 0:
        txtKhandvi.configure(state=DISABLED)
        varKhandvi.set("0")


def f():
    if var6.get() == 1:
        txtCheeseSandwich.configure(state=NORMAL)
        varCheeseSandwich.set("")
    elif var6.get() == 0:
        txtCheeseSandwich.configure(state=DISABLED)
        varCheeseSandwich.set("0")

def g():
    if var7.get() == 1:
        txtChickenSandwich.configure(state=NORMAL)
        varChickenSandwich.set("")
    elif var7.get() == 0:
        txtChickenSandwich.configure(state=DISABLED)
        varChickenSandwich.set("0")

def h():
    if var8.get() == 1:
        txtFishSandwich.configure(state=NORMAL)
        varFishSandwich.set("")
    elif var8.get() == 0:
        txtFishSandwich.configure(state=DISABLED)
        varFishSandwich.set("0")

def i():
    if var9.get() == 1:
        txtChocoBrownie.configure(state=NORMAL)
        varChocoBrownie.set("")
    elif var9.get() == 0:
        txtChocoBrownie.configure(state=DISABLED)
        varChocoBrownie.set("0")

def j():
    if var10.get() == 1:
        txtIcecream.configure(state=NORMAL)
        varIcecream.set("")
    elif var10.get() == 0:
        txtIcecream.configure(state=DISABLED)
        varIcecream.set("0")

def k():
    if var11.get() == 1:
        txtPaan.configure(state=NORMAL)
        varPaan.set("")
    elif var11.get() == 0:
        txtPaan.configure(state=DISABLED)
        varPaan.set("0")
        
def l():
    if var12.get() == 1:
        txtBakedRasgulla.configure(state=NORMAL)
        varBakedRasgulla.set("")
    elif var12.get() == 0:
        txtBakedRasgulla.configure(state=DISABLED)
        varBakedRasgulla.set("0")
        
def m():
    if var13.get() == 1:
        txtJalebi.configure(state=NORMAL)
        varJalebi.set("")
    elif var13.get() == 0:
        txtJalebi.configure(state=DISABLED)
        varJalebi.set("0")
        
def n():
    if var14.get() == 1:
        txtTea.configure(state=NORMAL)
        varTea.set("")
    elif var14.get() == 0:
        txtTea.configure(state=DISABLED)
        varTea.set("0")
        
def o():
    if var15.get() == 1:
        txtCola.configure(state=NORMAL)
        varCola.set("")
    elif var15.get() == 0:
        txtCola.configure(state=DISABLED)
        varCola.set("0")
        
def p():
    if var16.get() == 1:
        txtCoffee.configure(state=NORMAL)
        varCoffee.set("")
    elif var16.get() == 0:
        txtCoffee.configure(state=DISABLED)
        varCoffee.set("0")
        
def q():
    if var17.get() == 1:
        txtJuice.configure(state=NORMAL)
        varJuice.set("")
    elif var17.get() == 0:
        txtJuice.configure(state=DISABLED)
        varJuice.set("0")
        
def r():
    if var18.get() == 1:
        txtWater.configure(state=NORMAL)
        varWater.set("")
    elif var18.get() == 0:
        txtWater.configure(state=DISABLED)
        varWater.set("0")
        
def s():
    if var19.get() == 1:
        txtChocolateShake.configure(state=NORMAL)
        varChocolateShake.set("")
    elif var19.get() == 0:
        txtChocolateShake.configure(state=DISABLED)
        varChocolateShake.set("0")
        
def t():
    if var20.get() == 1:
        txtVanillaShake.configure(state=NORMAL)
        varVanillaShake.set("")
    elif var20.get() == 0:
        txtVanillaShake.configure(state=DISABLED)
        varVanillaShake.set("0")
        
def u():
    if var21.get() == 1:
        txtOreoKrusher.configure(state=NORMAL)
        varOreoKrusher.set("")
    elif var21.get() == 0:
        txtOreoKrusher.configure(state=DISABLED)
        varOreoKrusher.set("0")





#================================================================================
#                               FRAMING 1
#================================================================================

lblMeal = Label(f1top,font=("arial",25,'bold'), text="FAST MEAL")
lblMeal.grid(row=0, column=0)

Fries = Checkbutton(f1top, text="Fries", variable=var1, onvalue=1, offvalue=0, font=("arial", 18, 'bold'),fg="steel blue", command=a)
Fries.grid(row=1, column=0, sticky = W)
txtFries = Entry(f1top, font=("arial", 18, 'bold'), bd=8, textvariable = varFries, width=4, justify="right",state=DISABLED)
txtFries.grid(row=1, column=1)

Salad = Checkbutton(f1top, text="Salad", variable=var2, onvalue=1, offvalue=0, font=("arial", 18, 'bold'),fg="steel blue", command=b)
Salad.grid(row=2, column=0, sticky = W)
txtSalad = Entry(f1top, font=("arial", 18, 'bold'), bd=8, textvariable = varSalad, width=4, justify="right",state=DISABLED)
txtSalad.grid(row=2, column=1)

Hamburger = Checkbutton(f1top, text="Hamburger", variable=var3, onvalue=1, offvalue=0, font=("arial", 18, 'bold'),fg="steel blue", command=c)
Hamburger.grid(row=3, column=0, sticky = W)
txtHamburger = Entry(f1top, font=("arial", 18, 'bold'), bd=8, textvariable = varHamburger, width=4, justify="right",state=DISABLED)
txtHamburger.grid(row=3, column=1)

DahiKabab = Checkbutton(f1top, text="Dahi Kabab", variable=var4, onvalue=1, offvalue=0, font=("arial", 18, 'bold'),fg="steel blue", command=d)
DahiKabab.grid(row=4, column=0, sticky = W)
txtDahiKabab = Entry(f1top, font=("arial", 18, 'bold'), bd=8, textvariable = varDahiKabab, width=4, justify="right",state=DISABLED)
txtDahiKabab.grid(row=4, column=1)

Khandvi = Checkbutton(f1top, text="Khandvi", variable=var5, onvalue=1, offvalue=0, font=("arial", 18, 'bold'),fg="steel blue", command=e)
Khandvi.grid(row=5, column=0, sticky = W)
txtKhandvi = Entry(f1top, font=("arial", 18, 'bold'), bd=8, textvariable = varKhandvi, width=4, justify="right",state=DISABLED)
txtKhandvi.grid(row=5, column=1)

lblSpace = Label(f1top,text="\n")
lblSpace.grid(row=6, column=0)
lblSandwich = Label(f1top,font=("arial",25,'bold'), text="SANDWICHES")
lblSandwich.grid(row=7, column=0)

VegSandwich = Checkbutton(f1top, text="Veg Sandwich", variable=var6, onvalue=1, offvalue=0, font=("arial", 18, 'bold'),fg="steel blue", command=f)
VegSandwich.grid(row=8, column=0, sticky = W)
txtVegSandwich = Entry(f1top, font=("arial", 18, 'bold'), bd=8, textvariable = varCheeseSandwich, width=4, justify="right",state=DISABLED)
txtVegSandwich.grid(row=8, column=1)

ChickenSandwich = Checkbutton(f1top, text="Chicken Sandwich", variable=var7, onvalue=1, offvalue=0, font=("arial", 18, 'bold'),fg="steel blue", command=g)
ChickenSandwich.grid(row=9, column=0, sticky = W)
txtChickenSandwich = Entry(f1top, font=("arial", 18, 'bold'), bd=8, textvariable = varChickenSandwich, width=4, justify="right",state=DISABLED)
txtChickenSandwich.grid(row=9, column=1)

FishSandwich = Checkbutton(f1top, text="Fish Sandwich", variable=var8, onvalue=1, offvalue=0, font=("arial", 18, 'bold'),fg="steel blue", command=h)
FishSandwich.grid(row=10, column=0, sticky = W)
txtFishSandwich = Entry(f1top, font=("arial", 18, 'bold'), bd=8, textvariable = varFishSandwich, width=4, justify="right",state=DISABLED)
txtFishSandwich.grid(row=10, column=1)

btnReceipt=Button(f1bottom,padx=20,pady=2,bd=14,font=('arial',16,'bold'),width=16,text="GENERATE RECEIPT",fg="steel blue", command = Receipt)
btnReceipt.grid(row=0,column=0)



#================================================================================
#                               FRAMING 2 (TOP)
#================================================================================

lblMeal = Label(f2Top,font=("arial",25,'bold'), text="DESSERTS")
lblMeal.grid(row=0, column=0)

ChocoBrownie = Checkbutton(f2Top, text="Chocolate Brownie", variable=var9, onvalue=1, offvalue=0, font=("arial", 18, 'bold'),fg="steel blue", command=i)
ChocoBrownie.grid(row=1, column=0, sticky = W)
txtChocoBrownie = Entry(f2Top, font=("arial", 18, 'bold'), bd=8, textvariable = varChocoBrownie, width=4, justify="right",state=DISABLED)
txtChocoBrownie.grid(row=1, column=1)

Icecream  = Checkbutton(f2Top, text="Icecream (Chocolate/Mango/Vanilla/Juice)", variable=var10, onvalue=1, offvalue=0, font=("arial", 18, 'bold'),fg="steel blue", command=j)
Icecream.grid(row=2, column=0, sticky = W)
txtIcecream = Entry(f2Top, font=("arial", 18, 'bold'), bd=8, textvariable = varIcecream, width=4, justify="right",state=DISABLED)
txtIcecream.grid(row=2, column=1)

Paan = Checkbutton(f2Top, text="Paan", variable=var11, onvalue=1, offvalue=0, font=("arial", 18, 'bold'),fg="steel blue", command=k)
Paan.grid(row=3, column=0, sticky = W)
txtPaan = Entry(f2Top, font=("arial", 18, 'bold'), bd=8, textvariable = varPaan, width=4, justify="right",state=DISABLED)
txtPaan.grid(row=3, column=1)

BakedRasgulla = Checkbutton(f2Top, text="Baked Rasgulla", variable=var12, onvalue=1, offvalue=0, font=("arial", 18, 'bold'),fg="steel blue", command=l)
BakedRasgulla.grid(row=4, column=0, sticky = W)
txtBakedRasgulla = Entry(f2Top, font=("arial", 18, 'bold'), bd=8, textvariable = varBakedRasgulla, width=4, justify="right",state=DISABLED)
txtBakedRasgulla.grid(row=4, column=1)

Jalebi = Checkbutton(f2Top, text="Jalebi", variable=var13, onvalue=1, offvalue=0, font=("arial", 18, 'bold'),fg="steel blue", command=m)
Jalebi.grid(row=5, column=0, sticky = W)
txtJalebi = Entry(f2Top, font=("arial", 18, 'bold'), bd=8, textvariable = varJalebi, width=4, justify="right",state=DISABLED)
txtJalebi.grid(row=5, column=1)



#================================================================================
#                               FRAMING 2 (BOTTOM)
#================================================================================

lblPaymentMethod = Label(f2Bottom, font=("aria", 19, 'bold'), text = "PAYMENT MODE",fg="black", bd=10, width=16, anchor='w')
lblPaymentMethod.grid(row=0,column=0)

cmbPaymentMethod = ttk.Combobox(f2Bottom, textvariable=varPM, state="readonly", font=("arial", 10, 'bold'), width=20)
cmbPaymentMethod['value']=('Cash','Paytm','Google-Pay','Phone-pe','Amazon-Pay','Credit Card','Debit Card')
cmbPaymentMethod.current(0)
cmbPaymentMethod.grid(row=0, column=1)

lblTotal = Label(f2Bottom, font=("arial", 18, 'bold'), text = "Total",fg="steel blue", bd=10, width=16, anchor='e')
lblTotal.grid(row=2,column=1)
txtTotal = Entry(f2Bottom, font=("arial", 18, 'bold'), bd=8, textvariable = varTotal, width=10, justify="right",state=DISABLED)
txtTotal.grid(row=2, column=2)

lblSGST = Label(f2Bottom, font=("arial", 18, 'bold'), text = "SGST @9%",fg="steel blue", bd=10, width=16, anchor='e')
lblSGST.grid(row=3,column=1)
txtSGST = Entry(f2Bottom, font=("arial", 18, 'bold'), bd=8, textvariable = varSGST, width=10, justify="right",state=DISABLED)
txtSGST.grid(row=3, column=2)

lblCGST = Label(f2Bottom, font=("arial", 18, 'bold'), text = "CGST @9%",fg="steel blue", bd=10, width=16, anchor='e')
lblCGST.grid(row=4,column=1)
txtCGST = Entry(f2Bottom, font=("arial", 18, 'bold'), bd=8, textvariable = varCGST, width=10, justify="right",state=DISABLED)
txtCGST.grid(row=4, column=2)

lblServiceCharge = Label(f2Bottom, font=("arial", 18, 'bold'), text = "Service Charge @10%",fg="steel blue", bd=10, width=16, anchor='e')
lblServiceCharge.grid(row=5,column=1)
txtServiceCharge = Entry(f2Bottom, font=("arial", 18, 'bold'), bd=8, textvariable = varServiceCharge, width=10, justify="right",state=DISABLED)
txtServiceCharge.grid(row=5, column=2)



#================================================================================
#                               BUTTONS
#================================================================================

btnprice=Button(f2Bottom,padx=20,pady=1, bd=14 ,fg="steel blue",font=('arial' ,16,'bold'),width=5, text="PRICE LIST", command = price_list)
btnprice.grid(row=2, column=0)

btnTotal = Button(f2Bottom, padx=20, pady=1, bd=14, fg="steel blue", font=("arial", 16, 'bold'), width=5,text="TOTAL", command = TotalCost).grid(row=3, column=0)

btnReset=Button(f2Bottom,padx=20,pady=1,bd=14,fg="steel blue",font=('arial',16,'bold'),width=5,text="RESET", command=Reset)
btnReset.grid(row=4,column=0)

btnExit=Button(f2Bottom,padx=20,pady=1,bd=14,fg="steel blue",font=('arial',16,'bold'),width=5,text="EXIT", command = iExit)
btnExit.grid(row=5,column=0)



#================================================================================
#                               FRAMING 3
#================================================================================

lblDrinks = Label(f3top,font=("aria",25,'bold'), text="DRINKS")
lblDrinks.grid(row=0, column=0)

Tea = Checkbutton(f3top, text="Tea",fg="steel blue", variable=var14, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=n)
Tea.grid(row=1, column=0, sticky = W)
txtTea = Entry(f3top, font=("arial", 18, 'bold'), bd=8, textvariable = varTea, width=4, justify="right",state=DISABLED)
txtTea.grid(row=1, column=1)

Coffee = Checkbutton(f3top, text="Coffee",fg="steel blue", variable=var16, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=p)
Coffee.grid(row=2, column=0, sticky = W)
txtCoffee = Entry(f3top, font=("arial", 18, 'bold'), bd=8, textvariable = varCoffee, width=4, justify="right",state=DISABLED)
txtCoffee.grid(row=2, column=1)

Cola = Checkbutton(f3top, text="Cola",fg="steel blue", variable=var15, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=o)
Cola.grid(row=3, column=0, sticky = W)
txtCola = Entry(f3top, font=("arial", 18, 'bold'), bd=8, textvariable = varCola, width=4, justify="right",state=DISABLED)
txtCola.grid(row=3, column=1)

Juice = Checkbutton(f3top, text="Juice (Juice/Apple/Mango)",fg="steel blue", variable=var17, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=q)
Juice.grid(row=4, column=0, sticky = W)
txtJuice = Entry(f3top, font=("arial", 18, 'bold'), bd=8, textvariable = varJuice, width=4, justify="right",state=DISABLED)
txtJuice.grid(row=4, column=1)

Water = Checkbutton(f3top, text="Mineral Water",fg="steel blue", variable=var18, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=r)
Water.grid(row=5, column=0, sticky = W)
txtWater = Entry(f3top, font=("arial", 18, 'bold'), bd=8, textvariable = varWater, width=4, justify="right",state=DISABLED)
txtWater.grid(row=5, column=1)

lblSpace = Label(f3top,text="\n\n")
lblSpace.grid(row=6, column=0)

lblShakes = Label(f3top,font=("arial",25,'bold'), text="KRUSHERS")
lblShakes.grid(row=7, column=0)

ChocolateShake = Checkbutton(f3top, text="Chocolate K.",fg="steel blue", variable=var19, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=s)
ChocolateShake.grid(row=8, column=0, sticky = W)
txtChocolateShake = Entry(f3top, font=("arial", 18, 'bold'), bd=8, textvariable = varChocolateShake, width=4, justify="right",state=DISABLED)
txtChocolateShake.grid(row=8, column=1)

VanillaShake = Checkbutton(f3top, text="Vanilla K.",fg="steel blue", variable=var20, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=t)
VanillaShake.grid(row=9, column=0, sticky = W)
txtVanillaShake = Entry(f3top, font=("arial", 18, 'bold'), bd=8, textvariable = varVanillaShake, width=4, justify="right",state=DISABLED)
txtVanillaShake.grid(row=9, column=1)

OreoKrusher = Checkbutton(f3top, text="Oreo K.",fg="steel blue", variable=var21, onvalue=1, offvalue=0, font=("arial", 18, 'bold'), command=u)
OreoKrusher.grid(row=10, column=0, sticky = W)
txtOreoKrusher = Entry(f3top, font=("arial", 18, 'bold'), bd=8, textvariable = varOreoKrusher, width=4, justify="right",state=DISABLED)
txtOreoKrusher.grid(row=10, column=1)

lblpay = Label(f3bottom, font=("arial", 18, 'bold'), text = "Total Payable Amount", fg="red", bd=10, width=16, anchor='e')
lblpay.grid(row=0, column=0)
txtpay = Entry(f3bottom, font=("arial", 18, 'bold'), bd=8, textvariable = varPay, width=10, justify="right",state=DISABLED)
txtpay.grid(row=0, column=1)

root.mainloop()



@ CODED BY TSG405, 2021
