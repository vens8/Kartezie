import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
#products serac, cart, menu account, product page, order page and respective menupages.

login= Tk()
login.title("Login Page")
login.geometry("400x400")
grey="#C0C0C0"
lightgrey="#D3D3D3"
greengrey="#c8ffcb"


def cartwindow():
    def createListinListBox(shopping):
        for elem in shopping:
            theList.insert(END, elem[0] + "-" + str(elem[1]))

    def listIndex(shopping, item):
        index = -1
        for i in range(len(shopping)):
            if shopping[i][0] == item:
                index = i
        return index

    def addList(shopping, item, index):
        if index == -1:
            shopping.append([item, 1])
        else:
            shopping[index][1] += quantity.get()

    def removeList(sopping, index):
        del (shopping[index])

    def add():
        index = listIndex(shopping, item.get())
        addList(shopping, item.get(), index)
        if index >= 0:
            theList.delete(index)
            theList.insert(index, shopping[index][0] + "-" + str(shopping[index][1]))
        else:
            theList.insert(END, item.get() + "-" + str(quantity.get()))

    def remove():
        index = theList.index(ACTIVE)
        print(index)
        removeList(shopping, index)
        theList.delete(index)

    shopping = [["apple", 10], ["milk", 2], ["juice", 1], ["wine", 2], ["chicken", 1]]

    window = Tk()
    window.title("Cart")

    theList = Listbox(window, selectmode=SINGLE)
    theList.grid(row=0, column=0, columnspan=2, sticky=E)

    createListinListBox(shopping)

    item = StringVar()
    quantity = IntVar()

    quantity.set(1)

    Label(window, text="Item:").grid(row=1, column=0, sticky=E)
    Entry(window, textvariable=item).grid(row=1, column=1, sticky=W)

    Label(window, text="Quantity:").grid(row=2, column=0, sticky=E)
    Entry(window, textvariable=quantity).grid(row=2, column=1, sticky=W)

    Button(window, text="Add", command=add).grid(row=3, column=0, columnspan=3)
    Button(window, text="Remove", command=remove).grid(row=0, column=3)

    window.mainloop()

def accountwindow():
    Account=tk.Tk()
    Account.mainloop()


def make_Dashboard():
    dashboard = tk.Tk()
    dashboard.title("Dashboard")
    dashboard.geometry("1600x1000")

    def search(x):
        # TOBE FIXED AAA!!!!!!
        print(x)

        # if x==0 :
        #     item = SearchQuery.get(1.0, tk.END)
        #     print(item)
        #
        # elif x==1:
        #     item= "clothes"
        #     print(item)
        # elif x==2:
        #     item= "toys"
        #     print(item)
        # elif x==3:
        #     item= "furniture"
        #     print(item)
        # elif x==4:
        #     item= "grocery"
        #     print(item)
        # elif x==5:
        #     item= "decor"
        #     print(item)
        # elif x==6:
        #     item= "electronics"
        #     print(item)
        # elif x==7:
        #     item= "household"
        #     print(item)
        #
        # elif x==8:
        #     item= "gifts"
        #     print(item)
        #
        # else:
        #     print("unidentified")

        #search and pop a new window to display item


#search bar
    SearchQuery = tk.Text(dashboard, width=50, height=2.5, font=("montserrat", 20), bg="#f5e9dc")
    searchButton= tk.Button(dashboard,text=" Search ", font=("montserrat", 45),  command= lambda: search(0) ,fg="#5e3d1a", height=1)
    searchButton.place(x=1100, y=35)
    SearchQuery.place(x=400,y=25)

#cart
    cartButton = tk.Button(dashboard, text=" Cart ", font=("montserrat", 45), command=cartwindow ,fg="#5e3d1a")
    cartButton.place(x=1300, y=35)

#account
    accountButton = tk.Button(dashboard, text=" Account ", font=("montserrat", 45), command=accountwindow,fg="#5e3d1a")
    accountButton.place(x=175, y=35)



#categories
    clothesImg = ImageTk.PhotoImage(file="clothes.jpg")
    clothes = tk.Button(dashboard, image=clothesImg,  command=lambda:search(1), height=300, width=300)
    clothes.place(x=100, y=200)

    toysIMG = ImageTk.PhotoImage(file="toys.jpeg")
    toys = tk.Button(dashboard, image=toysIMG, command=lambda:search(2), height=300, width=300)
    toys.place(x=470, y=200)


    furnitureIMG= ImageTk.PhotoImage(file="furniture.jpeg")
    furniture = tk.Button(dashboard, image=furnitureIMG, command=lambda:search(3), height=300, width=300)
    furniture.place(x=830, y=200)


    groceryIMG = ImageTk.PhotoImage(file="grocery.jpeg")
    grocery = tk.Button(dashboard, image=groceryIMG, command=lambda:search(4), height=300, width=300)
    grocery.place(x=1200, y=200)

    # row 2


    decorIMG = ImageTk.PhotoImage(file="decor.jpeg")
    decor = tk.Button(dashboard, image=decorIMG, command=lambda:search(5), height=300, width=300)
    decor.place(x=100, y=600)

    electronicsImg = ImageTk.PhotoImage(file="electronics.jpeg")
    electronics = tk.Button(dashboard, image=electronicsImg, command=lambda:search(6), height=300, width=300)
    electronics.place(x=470, y=600)


    householdIMG= ImageTk.PhotoImage(file="household.jpeg")
    household = tk.Button(dashboard, image=householdIMG, command=lambda:search(7), height=300, width=300)
    household.place(x=830, y=600)


    giftIMG = ImageTk.PhotoImage(file="gift.jpeg")
    gift = tk.Button(dashboard, image=giftIMG, command=lambda:search(8), height=300, width=300)
    gift.place(x=1200, y=600)

    dashboard.mainloop()




def StartLogin():
    lblsecrow = tk.Label(login, text="             ID -")
    lblsecrow.place(x=50, y=50)
    idtxt = tk.Entry(login, font=("montserrat"), bg=lightgrey)

    lblsecrow = tk.Label(login, text="Password -")
    lblsecrow.place(x=50, y=125)
    passwordtxt = tk.Entry(login, show="*", bg=lightgrey)

    def Validate():
        enteredID = idtxt.get()
        enteredPass = passwordtxt.get()
        # insert check conditions else insert label, if true do these:
        login.destroy()
        make_Dashboard()

    loginButton = tk.Button(login, text="Login", bg=grey, activebackground=greengrey, command=Validate)

    idtxt.place(x=110, y=75)
    passwordtxt.place(x=110, y=150)
    loginButton.place(x=175, y=250)

    login.mainloop()


StartLogin()