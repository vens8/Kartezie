import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from datetime import *
from itertools import cycle
import sys
import pickle  # Store and load data locally in the form of bytestream
import os
import time
import webbrowser
import requests  # For updates (File reading)
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from win10toast import ToastNotifier
import winrt.windows.ui.notifications as notifications
import winrt.windows.data.xml.dom as dom
import smtplib, ssl  # For feedback: emails
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  # Send feedback
from sys import platform  # Check the operating system
import mysql.connector  # For SQL
import re  # For regex (string validation)

__authors__ = ['Sumit Soni', 'Subhanshu Bansal', 'Sunishka Sharma', 'Rahul Maddula']
__copyright__ = 'Copyright (C) 2022'
__credits__ = __authors__
__license__ = 'GNU General Public License v3.0'
__version__ = "1.0.0"
__maintainer__ = __authors__
__email__ = ['add later guys']
__AppName__ = 'Kartezie'

# update the code with states of updateclass button
now = datetime.now()  # Doesn't update with change of time. Uses same value from the time of execution.
today = date.today().weekday()  # 0 is Monday and 6 is Sunday
current_time = time.strftime("%H:%M:%S")
record_no = -1  # Default variable
notified = False  # To display the notification only once
notified_list = []


root = tk.Tk()
root.bind("<Control-w>", lambda x: close())  # Close main window on pressing Control + W
root.iconbitmap("images/kartezieLogo.ico")
root.grid_columnconfigure(0, weight=200)
root.grid_rowconfigure(0, weight=200)
root.title('Kartezie')  # Text to display on the title bar of the application
root.state('zoomed')  # Opens the maximised version of the window by default
root.resizable(0, 0)

mode = None  # Identify if customer or admin
mydb = mysql.connector.connect(host="localhost", user="root", passwd="Rahulmaddula@123", database="dbmsproject")
mycursor = mydb.cursor(buffered=True)


def close():  # to close a window
    destroy = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=root)
    if destroy:
        root.destroy()


root.protocol("WM_DELETE_WINDOW", close)

# Menu
menu1 = Menu(root)
root.config(menu=menu1)

# Canvas ---- Can remove as not used
canvas = tk.Canvas(root, height=root.winfo_screenheight(), width=root.winfo_screenwidth(), bg="#161616")
canvas.grid(sticky=N + E + W + S, column=0, pady=0, padx=0)
canvas.grid_rowconfigure(0, weight=1)
canvas.grid_columnconfigure(0, weight=1)

# LoginFrame
loginFrame = tk.Frame(root, bg="#161616")  # Frame placed inside the root. Same colour as canvas so invisible.
loginFrame.grid(sticky=N + E + W + S, row=0, column=0, pady=0, padx=0)
loginFrame.grid_rowconfigure(0, weight=1)
loginFrame.grid_columnconfigure(0, weight=1)
loginFrame.place(relwidth=1, relheight=1)

kartezieLogo = Label(loginFrame, background="#161616")
kartezieLogo.place(relx=0.34, rely=0.1)
img = ImageTk.PhotoImage(Image.open("images/kartezie.png").resize((438, 143), Image.ANTIALIAS))
kartezieLogo.configure(image=img)


class User:
    def __init__(self, username, name, DOB, phone, customerID, mode):
        self.username = username
        self.customerID = customerID
        self.mode = mode
        self.name = name
        self.DOB = DOB
        self.phone = phone
        self.address = []

    def getUsername(self):
        return self.username

    def getCustomerID(self):
        return self.customerID

    def getMode(self):
        return self.mode


currentUser = None  # Current user


class Category:
    def __init__(self, categoryID, categoryName, tax, image):
        self.categoryID = categoryID
        self.categoryName = categoryName
        self.tax = tax
        self.image = image

    def getCategoryID(self):
        return self.categoryID

    def getCategoryName(self):
        return self.categoryName

    def getTax(self):
        return self.tax

    def getImage(self):
        return self.image


categories = []


def getCategories():
    catgs = "SELECT * FROM `category`"
    mycursor.execute(catgs)
    records = mycursor.fetchall()
    for record in records:
        category = Category(record[0], record[1], record[2], record[3])
        categories.append(category)


class Company:
    def __init__(self, companyID, companyName, phone, category):
        self.companyID = companyID
        self.companyName = companyName
        self.phone = phone
        self.category = category


companies = []


def searchCategory(categoryID):
    for category in categories:
        if category.categoryID == categoryID:
            return category


def getCompanies():
    comps = "SELECT * FROM `company`"
    mycursor.execute(comps)
    records = mycursor.fetchall()
    for record in records:
        company = Company(record[0], record[2], record[1], searchCategory(record[3]))
        companies.append(company)


class Product:
    def __init__(self, productID, productName, category, company, currentPrice, discount, quantity, image):
        self.image = image
        self.quantity = quantity
        self.discount = discount
        self.currentPrice = currentPrice
        self.company = company
        self.category = category
        self.productName = productName
        self.productID = productID


products = []


def searchCompany(companyID):
    for company in companies:
        if company.companyID == companyID:
            return company


def getProducts():
    prods = "SELECT * FROM `product`"
    mycursor.execute(prods)
    records = mycursor.fetchall()
    for record in records:
        product = Product(record[0], record[7], searchCategory(record[1]), searchCompany(record[2]), record[3], record[4], record[6], record[8])
        products.append(product)


def activateBlock():
    textBlock.grid(sticky=N + E + W + S)
    textBlock.grid_rowconfigure(0, weight=100)
    textBlock.grid_columnconfigure(0, weight=100)
    textBlock.place(relx=0.35, rely=0.621, relheight=0.04, relwidth=0.3)
    registerNow.place_forget()  # No registrations allowed for admin (credentials provided by management internally)


def deactivateBlock():
    textBlock.place_forget()
    registerNow.place(relx=0.515, rely=0.621)


def showCustomers():
    deactivateBlock()
    usernameClear()
    passwordClear()
    back.place(relx=0.02, rely=0.03)
    for frame in frames:
        if frame != userLoginFrame:
            frame.place_forget()
    userLoginFrame.grid(sticky=N + E + W + S, row=0, column=0, pady=0, padx=0)
    userLoginFrame.grid_rowconfigure(0, weight=1)
    userLoginFrame.grid_columnconfigure(0, weight=1)
    userLoginFrame.place(relwidth=1, relheight=1)

    def validateUsername():  # Used to check if the username string is valid
        if usernameLogin.get():
            if not re.fullmatch(r'[A-Za-z0-9_]{4,16}', usernameLogin.get()):
                messagebox.showinfo("Invalid username", "Username length should be in the range 4-16 and special character  s are not allowed!")
            else:
                if not passwordLogin.get():
                    messagebox.showinfo("Invalid password", "Please enter the password")
                else:
                    validateLogin()
        else:
            messagebox.showinfo("Invalid username", "Please enter the username")

    userLoginFrame.bind("<Return>", validateUsername)
    login.configure(command=validateUsername)

    def validateLogin():
        count = None
        countUsernames = "SELECT COUNT(*) FROM `login` WHERE username=" + "'" + usernameLogin.get() + "'" + "and mode = 0"
        mycursor.execute(countUsernames)
        record1 = mycursor.fetchone()
        for row1 in record1:
            count = row1

        if count == 0:
            messagebox.showinfo("Invalid username", "Username does not exist")
            return "0"
        else:
            sqlform2 = "SELECT * FROM `login` WHERE username=" + "'" + usernameLogin.get() + "'" + "and mode = 0"
            mycursor.execute(sqlform2)
            record = mycursor.fetchone()
            sqlform2 = "SELECT * FROM `customers` WHERE customer_id=" + "'" + record[2] + "'"
            mycursor.execute(sqlform2)
            custDetails = mycursor.fetchone()
            currentUser = User(record[0], custDetails[1], custDetails[2], custDetails[3], record[2], record[3])

            if record[1] == passwordLogin.get():
                messagebox.showinfo("Login Successful", f"Welcome back {currentUser.name}")
                getCategories()  # Fetch and fill
                getCompanies()
                getProducts()
                fillCategories()
                back.place_forget()
                showCustomersMenu()
            else:
                messagebox.showinfo("Incorrect Password", f"Incorrect password for user {currentUser.username}")


def showAdmin():
    activateBlock()
    usernameClear()
    passwordClear()
    back.place(relx=0.02, rely=0.03)
    for frame in frames:
        if frame != userLoginFrame:
            frame.place_forget()
    userLoginFrame.grid(sticky=N + E + W + S, row=0, column=0, pady=0, padx=0)
    userLoginFrame.grid_rowconfigure(0, weight=1)
    userLoginFrame.grid_columnconfigure(0, weight=1)
    userLoginFrame.place(relwidth=1, relheight=1)

    def validateUsername():  # Used to check if the username string is valid
        if usernameLogin.get():
            if not re.fullmatch(r'[A-Za-z0-9_]{4,16}', usernameLogin.get()):
                messagebox.showinfo("Invalid username",
                                    "Username length should be in the range 4-16 and special characters are not allowed!")
            else:
                validateLogin()

        else:
            messagebox.showinfo("Invalid username", "Please enter the username")

    login.configure(command=validateUsername)

    def validateLogin():
        count = None
        print("Connection Successful")  # Log
        countUsernames = "SELECT COUNT(*) FROM `login` WHERE username=" + "'" + usernameLogin.get() + "'" + "and mode = 1"
        mycursor.execute(countUsernames)
        record1 = mycursor.fetchone()
        for row1 in record1:
            count = row1

        if count == 0:
            messagebox.showinfo("Invalid username", "Username does not exist")
            return "0"
        else:
            sqlform2 = "SELECT `password` FROM `login` WHERE username=" + "'" + usernameLogin.get() + "'" + "and mode = 1"
            mycursor.execute(sqlform2)
            record = mycursor.fetchone()
            currentUser = User(record[0], "Admin", None, None, None, 1)

            if record[0] == passwordLogin.get():
                messagebox.showinfo("Login Successful", f"Welcome back {currentUser.name}")
                back.place_forget()
                showAdminMenu()
                deactivateBlock()
            else:
                messagebox.showinfo("Incorrect Password", f"Incorrect password for user {currentUser.username}")


def goBack():
    back.place_forget()
    showLogin()


customerButton = Button(loginFrame)
customerButton.place(relx=0.316, rely=0.446)
customerButton.configure(relief="flat")
customerButton.configure(overrelief="flat")
customerButton.configure(activebackground="#161616")
customerButton.configure(cursor="hand2")
customerButton.configure(foreground="#161616")
customerButton.configure(background="#161616")
customerButton.configure(borderwidth="0")
img2 = ImageTk.PhotoImage(file="images/customers.png")
customerButton.configure(image=img2)
customerButton.configure(command=showCustomers)  # Open the customer mode

adminButton = Button(loginFrame)
adminButton.place(relx=0.566, rely=0.448)
adminButton.configure(relief="flat")
adminButton.configure(overrelief="flat")
adminButton.configure(activebackground="#161616")
adminButton.configure(cursor="hand2")
adminButton.configure(foreground="#161616")
adminButton.configure(background="#161616")
adminButton.configure(borderwidth="0")
img3 = ImageTk.PhotoImage(file="images/admins.png")
adminButton.configure(image=img3)
adminButton.configure(command=showAdmin)  # Open the admin mode

# userLoginFrame (Login)
userLoginFrame = tk.Frame(root, bg="#161616")  # Frame placed inside the root. Same colour as canvas so invisible.
customerLoginImageLabel = Label(userLoginFrame)
customerLoginImageLabel.place(relx=0.335, rely=0.05)
customerLoginImageLabel.configure(background="#161616")
customerLoginImage = PhotoImage(file="images/loginPage.png")
customerLoginImageLabel.configure(image=customerLoginImage)

textBlock = Label(userLoginFrame, text="HELLO", borderwidth=0, bg="#717171", fg="#717171")


# userLoginFrame (Login)
userRegisterFrame = tk.Frame(root, bg="#161616")  # Frame placed inside the root. Same colour as canvas so invisible.
userRegisterFrameLabel = Label(userRegisterFrame)
userRegisterFrameLabel.place(relx=0.15, rely=0.05)
userRegisterFrameLabel.configure(background="#161616")
userRegisterFrameImage = PhotoImage(file="images/registerUser.png")
userRegisterFrameLabel.configure(image=userRegisterFrameImage)

back = Button(root)
back.configure(relief="flat")
back.configure(overrelief="flat")
back.configure(activebackground="#161616")
back.configure(cursor="hand2")
back.configure(background="#161616")
back.configure(font="-family {Poppins SemiBold} -size 12")
back.configure(borderwidth="0")
backButtonImage = PhotoImage(file="images/backButton.png")
back.configure(command=goBack)
back.configure(image=backButtonImage)

usernameLogin = Entry(userLoginFrame)
usernameLogin.place(relx=0.38, rely=0.29, width=374, height=30)
usernameLogin.configure(font="-family {Poppins} -size 15")
usernameLogin.configure(relief="flat")
usernameLogin.configure(background="#717171")
usernameLogin.configure(foreground="#333333")


def usernameClear():
    usernameLogin.delete(0, "end")


# entry1.configure(textvariable=user)

passwordLogin = Entry(userLoginFrame)
passwordLogin.place(relx=0.38, rely=0.45, width=374, height=30)
passwordLogin.configure(font="-family {Poppins} -size 15")
passwordLogin.configure(background="#717171")
passwordLogin.configure(foreground="#333333")
passwordLogin.configure(relief="flat")
passwordLogin.configure(show="*")
# passwordLogin.configure(textvariable=passwd)


def passwordClear():
    passwordLogin.delete(0, "end")


registerNow = Button(userLoginFrame)
registerNow.place(relx=0.515, rely=0.621)
registerNow.configure(relief="flat")
registerNow.configure(overrelief="flat")
registerNow.configure(activebackground="#717171")
registerNow.configure(cursor="hand2")
registerNow.configure(foreground="#333333")
registerNow.configure(background="#717171")
registerNow.configure(font="-family {Poppins SemiBold} -size 12")
registerNow.configure(borderwidth="0")
registerNow.configure(text="Register Now")


def enter():
    pass


login = Button(userLoginFrame)
login.place(relx=0.43, rely=0.685)
login.configure(relief="flat")
login.configure(overrelief="flat")
login.configure(activebackground="#717171")
login.configure(cursor="hand2")
login.configure(foreground="#ffffff")
login.configure(background="#717171")
login.configure(borderwidth="0")
loginButton = PhotoImage(file="images/loginButton.png")
login.configure(image=loginButton)

# Register
usernameRegister = Entry(userRegisterFrame)
usernameRegister.place(relx=0.19, rely=0.32, width=300, height=30)
usernameRegister.configure(font="-family {Poppins} -size 15")
usernameRegister.configure(relief="flat")
usernameRegister.configure(background="#717171")
usernameRegister.configure(foreground="#333333")

nameRegister = Entry(userRegisterFrame)
nameRegister.place(relx=0.19, rely=0.51, width=300, height=30)
nameRegister.configure(font="-family {Poppins} -size 15")
nameRegister.configure(relief="flat")
nameRegister.configure(background="#717171")
nameRegister.configure(foreground="#333333")

passwordRegister = Entry(userRegisterFrame)
passwordRegister.place(relx=0.19, rely=0.68, width=300, height=30)
passwordRegister.configure(font="-family {Poppins} -size 15")
passwordRegister.configure(relief="flat")
passwordRegister.configure(background="#717171")
passwordRegister.configure(foreground="#333333")
passwordRegister.configure(show="*")

# Datepicker
cal = DateEntry(userRegisterFrame, width=16, background="#717171", foreground="#333333", bd=2)
cal.grid(pady=20)
cal.place(relx=0.6, rely=0.33)

phoneRegister = Entry(userRegisterFrame)
phoneRegister.place(relx=0.6, rely=0.52, width=300, height=30)
phoneRegister.configure(font="-family {Poppins} -size 15")
phoneRegister.configure(relief="flat")
phoneRegister.configure(background="#717171")
phoneRegister.configure(foreground="#333333")

userRegisterButton = Button(userRegisterFrame)
userRegisterButton.place(relx=0.43, rely=0.8)
userRegisterButton.configure(relief="flat")
userRegisterButton.configure(overrelief="flat")
userRegisterButton.configure(activebackground="#717171")
userRegisterButton.configure(cursor="hand2")
userRegisterButton.configure(foreground="#ffffff")
userRegisterButton.configure(background="#717171")
userRegisterButton.configure(borderwidth="0")
img4 = ImageTk.PhotoImage(file="images/registerButton.png")
userRegisterButton.configure(image=img4)


# creditsText = '''
# Group 50
# --------
# Subhanshu Bansal
# Sumit Soni
# Sunishka Sharma
# Rahul Maddula
# --------
# '''
# credits = Label(loginFrame, text=creditsText, borderwidth=0, bg="#161616", fg="#717171")
# credits.grid(sticky=N + E + W + S)
# credits.configure(font="-family {Poppins SemiBold} -size 20")
# credits.grid_rowconfigure(0, weight=100)
# credits.grid_columnconfigure(0, weight=100)
# credits.place(relx=0.25, rely=0.6, relheight=0.4, relwidth=0.5)


def showUserRegister():
    for frame in frames:
        if frame != userRegisterFrame:
            frame.place_forget()
    userRegisterFrame.grid(sticky=N + E + W + S, row=0, column=0, pady=0, padx=0)
    userRegisterFrame.grid_rowconfigure(0, weight=1)
    userRegisterFrame.grid_columnconfigure(0, weight=1)
    userRegisterFrame.place(relwidth=1, relheight=1)

    def calculateAge(DOB):
        today = date.today()
        return today.year - DOB.year - ((today.month, today.day) < (DOB.month, DOB.day))

    def validateFields():  # Used to check if the usernameLogin string is valid
        if usernameRegister.get():
            count = None
            countUsernames = "SELECT COUNT(*) FROM `login` WHERE username=" + "'" + usernameRegister.get() + "'" + "and mode = 0"
            mycursor.execute(countUsernames)
            record1 = mycursor.fetchone()
            for row1 in record1:
                count = row1

            if count == 0:
                if not re.fullmatch(r'[A-Za-z0-9_]{4,16}', usernameRegister.get()):
                    messagebox.showinfo("Invalid username",
                                        "Username length should be in the range 4-16 and special characters are not allowed!")
                else:
                    if nameRegister.get():
                        if not re.fullmatch(r"[A-Za-z' ]{1,64}", nameRegister.get()):
                            messagebox.showinfo("Invalid Name",
                                                "Name length should be in the range 1-64 and special characters are not allowed!")
                        else:
                            if passwordRegister.get():
                                if not re.fullmatch(r'[A-Za-z0-9@#$]{5,32}', passwordRegister.get()):
                                    messagebox.showinfo("Invalid password",
                                                        "Password length should be in the range 5-32")
                                else:
                                    if calculateAge(cal.get_date()) < 16:
                                        messagebox.showinfo("Invalid Age",
                                                            "You must be at least 16 years old to register!")
                                    else:
                                        if phoneRegister.get():
                                            if not re.fullmatch(r"[1-9][0-9]{9,9}", phoneRegister.get()):
                                                messagebox.showinfo("Invalid Phone Number",
                                                                    "Phone number should be of 10 digits and cannot start with 0!")
                                            else:
                                                register()
                                        else:
                                            messagebox.showinfo("Invalid Phone Number",
                                                                "Please enter the phone number")
                            else:
                                messagebox.showinfo("Invalid Password", "Please enter the password")
                    else:
                        messagebox.showinfo("Invalid Name", "Please enter the name")
            else:
                messagebox.showinfo("Invalid username", "Username already exists!")

        else:
            messagebox.showinfo("Invalid username", "Please enter the username")

    userRegisterButton.configure(command=validateFields)

    def register():
        getLastRow = "SELECT customer_id FROM customers ORDER BY customer_id desc"
        mycursor.execute(getLastRow)
        record = mycursor.fetchone()
        currentRow = int(record[0].split("cust_")[1]) + 1
        customerID = "'cust_" + f"{format(currentRow, '03d')}"
        registerUser = "INSERT INTO customers (customer_id, full_name, DOB, phone_no) values (" + customerID + "'," + "'" + nameRegister.get() + "'," + "'" + cal.get_date().strftime('%Y-%m-%d') + "'," + "'" + phoneRegister.get() + "'" + ")"
        print(registerUser)
        mycursor.execute(registerUser)
        mydb.commit()
        print(record)
        registerUserLogin = "INSERT INTO login (username, password, customer_id, mode) values (" + "'" + usernameRegister.get() + "'," + "'" + passwordRegister.get() + "'," + customerID + "', 0)"
        print(registerUserLogin)
        mycursor.execute(registerUserLogin)
        mydb.commit()
        print(record)
        messagebox.showinfo("Login added", f"Welcome to Kartezie, {nameRegister.get()}!")


registerNow.configure(command=showUserRegister)


def fillCategories():
    global categories  # list of category objects
    # sortRecords()
    # for i in categoriesTree.get_children():  # Clear table
    #     categoriesTree.delete(i)
    id_count = 0  # Parent
    c_count = 0  # Child
    for i in categories:
        print(i)
        print(i.image)
        if id_count % 2 == 0:
            categoriesTree.insert(parent='', index="end", iid=id_count, open=True, text=i.categoryName,
                         image=ImageTk.PhotoImage(file=i.image))
        else:
            categoriesTree.insert(parent='', index="end", iid=id_count, open=True, text=i.categoryName,
                         image=ImageTk.PhotoImage(file=i.image))
        id_count += 1
        # if id_count > 0:
        #     sep = ttk.Separator(categoriesTree, orient='horizontal')
        #     sep.grid(sticky="news")

    # for x in categories:
    #     print(x.image)
    #     print(os.path.exists(x.image))
    #     catgImage = Image.open(x.image)
    #     catgImage = catgImage.resize((30, 50), Image.ANTIALIAS)
    #     catgImage = ImageTk.PhotoImage(catgImage)
    #     categoriesTree.insert(parent='', index="end", open=True, text=x.categoryName,
    #                           image=catgImage, value=(x.categoryName, x.image))

    # for i in range(1, len(user_days)):
    #     if classes[days.index(user_days[i]) - 1][1]:
    #         for j in classes[days.index(user_days[i]) - 1][1]:
    #             if c_count < id_count:
    #                 tree1.insert(parent=f"{c_count}", index="end", iid=id_count, open=False, text="",
    #                              values=(j[0], j[1], j[2], j[3]), tags=('child',))
    #                 id_count += 1
    #             else:
    #                 break
    #         c_count += 1
    #         if c_count >= id_count:
    #             break
    #     else:
    #         c_count += 1
    # for i in classes:
    #     for j in i[1]:
    #         if c_count < id_count:
    #             tree1.insert(parent=f"{c_count}", index="end", iid=id_count, open=False, text="",
    #                          values=(j[0], j[1], j[2], j[3]), tags=('child',))
    #             id_count += 1
    #         else:
    #             break
    #     c_count += 1
    #     if c_count >= id_count:
    #         break


def showCustomersMenu():
    global currentUser
    # Menu items
    home = Menu(menu1,
                tearoff=0)  # Tear-off 0 removes the dashed lines in the menu which opens menu items in another window
    cartTab = Menu(menu1, tearoff=0)
    options = Menu(menu1, tearoff=0)
    helptab = Menu(menu1, tearoff=0)

    def homemenu():
        for frame in frames:
            if frame != homeFrame:
                frame.place_forget()
        homeFrame.grid(pady=0, padx=0)
        homeFrame.place(relwidth=1, relheight=1, relx=0, rely=0)

    def cartmenu():
        for frame in frames:
            if frame != cartFrame:
                frame.place_forget()
        cartFrame.grid(pady=0, padx=0)
        cartFrame.place(relwidth=1, relheight=1, relx=0, rely=0)

    def aboutmenu():
        for frame in frames:
            if frame != aboutFrame:
                frame.place_forget()
        aboutFrame.grid(pady=0, padx=0)
        aboutFrame.place(relwidth=1, relheight=1, relx=0, rely=0)

    def settingsmenu():
        for frame in frames:
            if frame != settingsFrame:
                frame.place_forget()
        settingsFrame.grid(pady=0, padx=0)
        settingsFrame.place(relwidth=1, relheight=1, relx=0, rely=0)

    def feedbackmenu():
        for frame in frames:
            if frame != feedbackFrame:
                frame.place_forget()
        feedbackFrame.grid(pady=0, padx=0)
        feedbackFrame.place(relwidth=1, relheight=1, relx=0, rely=0)

    def profilemenu():
        for frame in frames:
            if frame != profileFrame:
                frame.place_forget()
        profileFrame.grid(pady=0, padx=0)
        profileFrame.place(relwidth=1, relheight=1, relx=0, rely=0)

    def logout():
        global currentUser
        currentUser = None

    menu1.add_cascade(label="Home", menu=home)
    home.add_command(label="Kartezie Homepage", command=homemenu)
    homemenu()

    menu1.add_cascade(label="Cart", menu=cartTab)
    cartTab.add_command(label="View Cart", command=cartmenu)

    menu1.add_cascade(label="Options", menu=options)
    options.add_command(label="Settings", command=settingsmenu)
    options.add_command(label="View Profile", command=profilemenu)
    options.add_command(label="Logout", command=logout)

    menu1.add_cascade(label="Help", menu=helptab)
    helptab.add_command(label="Send Feedback", command=feedbackmenu)
    helptab.add_command(label="About Kartezie", command=aboutmenu)


def showAdminMenu():
    # Menu items
    home = Menu(menu1,
                tearoff=0)  # Tear-off 0 removes the dashed lines in the menu which opens menu items in another window
    cartTab = Menu(menu1, tearoff=0)
    options = Menu(menu1, tearoff=0)
    helptab = Menu(menu1, tearoff=0)

    def homemenu():
        for frame in frames:
            if frame != homeFrame:
                frame.place_forget()
        homeFrame.grid(pady=0, padx=0)
        homeFrame.place(relwidth=1, relheight=1, relx=0, rely=0)

    def cartmenu():
        for frame in frames:
            if frame != cartFrame:
                frame.place_forget()
        cartFrame.grid(pady=0, padx=0)
        cartFrame.place(relwidth=1, relheight=1, relx=0, rely=0)

    def aboutmenu():
        for frame in frames:
            if frame != aboutFrame:
                frame.place_forget()
        aboutFrame.grid(pady=0, padx=0)
        aboutFrame.place(relwidth=1, relheight=1, relx=0, rely=0)

    def settingsmenu():
        for frame in frames:
            if frame != settingsFrame:
                frame.place_forget()
        settingsFrame.grid(pady=0, padx=0)
        settingsFrame.place(relwidth=1, relheight=1, relx=0, rely=0)

    def feedbackmenu():
        for frame in frames:
            if frame != feedbackFrame:
                frame.place_forget()
        feedbackFrame.grid(pady=0, padx=0)
        feedbackFrame.place(relwidth=1, relheight=1, relx=0, rely=0)

    def profilemenu():
        for frame in frames:
            if frame != profileFrame:
                frame.place_forget()
        profileFrame.grid(pady=0, padx=0)
        profileFrame.place(relwidth=1, relheight=1, relx=0, rely=0)

    def logout():
        pass

    menu1.add_cascade(label="Home", menu=home)
    home.add_command(label="Kartezie Homepage", command=homemenu)
    homemenu()

    menu1.add_cascade(label="Cart", menu=cartTab)
    cartTab.add_command(label="View Cart", command=cartmenu)

    menu1.add_cascade(label="Options", menu=options)
    options.add_command(label="Settings", command=settingsmenu)
    options.add_command(label="View Profile", command=profilemenu)
    options.add_command(label="Logout", command=logout)

    menu1.add_cascade(label="Help", menu=helptab)
    helptab.add_command(label="Send Feedback", command=feedbackmenu)
    helptab.add_command(label="About Kartezie", command=aboutmenu)


def showLogin():
    usernameLogin.delete(0, 'end')
    passwordLogin.delete(0, 'end')
    for frame in frames:
        if frame != loginFrame:
            frame.place_forget()
    loginFrame.grid(pady=0, padx=0)
    loginFrame.place(relwidth=1, relheight=1, relx=0, rely=0)


# Other Frames
homeFrame = Frame(root, bg="#161616")  # Classes
cartFrame = Frame(root, bg="#161616")  # About
settingsFrame = Frame(root, bg="#161616")  # Help
profileFrame = Frame(root, bg="#161616")  # Help
feedbackFrame = Frame(root, bg="#161616")  # Help
aboutFrame = Frame(root, bg="#161616")  # Help
frames = [loginFrame, userLoginFrame, userRegisterFrame, homeFrame, cartFrame, settingsFrame, profileFrame, feedbackFrame, aboutFrame]

# Tree view frame
categoriesTreeFrame = tk.Frame(homeFrame, bg="#161616")
categoriesTreeFrame.grid(sticky=N + E + W + S, row=0, column=0, pady=0, padx=0)
categoriesTreeFrame.grid_rowconfigure(0, weight=1)
categoriesTreeFrame.grid_columnconfigure(0, weight=1)
categoriesTreeFrame.place(relx=0.05, rely=0.2, relwidth=0.96, relheight=0.7)

# Scrollbar
categoryScroll = ttk.Scrollbar(homeFrame, orient=VERTICAL)
categoryScroll.grid(sticky=N + S + E + W, row=0, column=1)
categoryScroll.grid_rowconfigure(0, weight=1)
categoryScroll.grid_columnconfigure(0, weight=1)

# Tree view table
categoriesTree = ttk.Treeview(categoriesTreeFrame, yscrollcommand=categoryScroll.set)
categoriesTree['columns'] = ("Image", "Category")
categoriesTree.column("#0", width=0, anchor=W)
categoriesTree.column("Image", anchor=W, width=150)
categoriesTree.column("Category", anchor=W, width=50)
categoriesTree.heading("#0", anchor="center")
categoriesTree.heading("Image", text="Image", anchor="center")
categoriesTree.heading("Category", text="Category", anchor="center")
categoryScroll.config(command=categoriesTree.yview)
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview.Heading",
                font=("Helvetica", 12, "bold"),
                background="#581845",
                foreground="white",
                relief="flat",
                )
style.configure("Treeview",
                font=("Helvetica", 11),
                background="#FFC30F",
                foreground="#FFFF00",
                rowheight=45,
                fieldbackground="black"
                )
style.configure("Vertical.TScrollbar", background="#581845", darkcolor="#FFC30F", lightcolor="#FFC30F",
                troughcolor="#B28500", bordercolor="black", arrowcolor="white"
                )
style.map("Treeview",
          background=[("selected", "#FFC30F")],
          foreground=[("selected", "black")]
          )

categoriesTree.tag_configure('even', background="#C70039", font=("Helvetica", 11, 'bold'))
categoriesTree.tag_configure('odd', background="#A50240", font=("Helvetica", 11, 'bold'))
categoriesTree.tag_configure('child', background="#FF5733")

categoriesTree.grid(pady=20, padx=20)
categoriesTree.place(relx=0, rely=0.3, relwidth=0.8, relheight=0.7)


def StartDashboard():
    pass

# Data
# system_in = open("data/settings.dat", "rb")
# settings = pickle.load(system_in)
# system_in.close()
# data = settings['data_location']


'''

# pickle_in = open(data, "rb")
# classes = pickle.load(pickle_in)
# pickle_in.close()


# Functions


# if settings['prompt']:
#     check_updates(0)


try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

images = ['images/ashish.png',
          'images/brain.png',
          'images/chat.png',
          'images/closenuke.png',
          'images/comform.png'
          ]
photos = cycle(ImageTk.PhotoImage(Image.open(image)) for image in images)
label1 = Label(frame8, bg="black", fg="yellow", text="Settings saved.", font=('Verdana', 11, 'italic'))

def slideShow():
    img = next(photos)
    label.config(image=img)
    root.after(50, slideShow)  # 0.05 seconds


root.after(10, lambda: slideShow())


def load_file():
    global data, classes, settings
    filetypes = (
        ('DAT files', '*.dat'),
        ('text files', '*.txt')
    )
    temp_data = fd.askopenfilename(filetypes=filetypes)  # Store in temporary variable to not disturb 'data' global.
    if len(temp_data) > 0:
        try:
            pickle_in = open(temp_data, "rb")
            temp_classes = pickle.load(pickle_in)
            pickle_in.close()
            if isinstance(temp_classes, list) and len(temp_classes) == 7:
                data = temp_data
                system_out = open("data/settings.dat", "wb")  # Change the value in the DAT file
                settings['data_location'] = data  # Update the location of data file
                pickle.dump(settings, system_out)
                system_out.close()
                pickle_in = open(data, "rb")
                classes = pickle.load(pickle_in)
                pickle_in.close()
                fill_table()
            else:
                messagebox.showinfo('Invalid file',
                                    "The file you're trying to load is not supported. Try loading another file.")
        except IndexError:
            print("No file selected.")  # Log
    else:
        print("No file selected.")  # Log


def sortRecords():
    global classes, data
    for record in classes:
        record[1].sort(key=lambda x: x[1])
    pickle_out = open(data, "wb")  # updates the dat file with sorted records
    pickle.dump(classes, pickle_out)
    pickle_out.close()


def clock():  # Used to update label text every n seconds.
    message1.config(text=live_status())
    message1.after(1000, clock)


# Tool tip to display additional information
class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() + 27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()


def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)

    def enter(event):
        toolTip.showtip(text)

    def leave(event):
        toolTip.hidetip()

    widget.bind('<Enter>', enter)  # To show the tool tip when the cursor enters the widget
    widget.bind('<Leave>', leave)  # To stop showing the tool tip when the cursor moves away from the widget


def addclass(event=None):
    global classes, url
    if combo1.get() == "--Select Day--":
        messagebox.showinfo("Invalid day", "Please select a valid day (Monday-Sunday)")
        if event == 1:
            return 0
    else:
        if entry1.get() == "":
            messagebox.showinfo("Empty subject", "Please type a subject in the input field")
            if event == 1:
                return 0
        else:
            if (entry2.get() == "hh:mm (24 hour format)" or entry2.get() == "" or len(entry2.get().split(":")) < 2
                or not entry2.get().split(":")[0].isdecimal() or not entry2.get().split(":")[1].isdecimal()
                or len(entry2.get().split(":")[1]) < 2 or int(entry2.get().split(":")[0]) < 0 or int(
                        entry2.get().split(":")[0]) > 23
                or int(entry2.get().split(":")[1]) < 0 or int(entry2.get().split(":")[1]) > 59) or (
                    entry3.get() == "hh:mm (24 hour format)"
                    or entry3.get() == "" or len(entry3.get().split(":")) < 2 or not entry3.get().split(":")[
                0].isdecimal()
                    or not entry3.get().split(":")[1].isdecimal() or len(entry3.get().split(":")[1]) < 2
                    or int(entry3.get().split(":")[0]) < 0 or int(entry3.get().split(":")[0]) > 24
                    or int(entry3.get().split(":")[1]) < 0 or int(entry3.get().split(":")[1]) > 60):
                messagebox.showinfo("Invalid time format", "Please type a 24 hour time format (hh:mm)")
                if event == 1:
                    return 0
            else:
                if int(entry2.get().split(":")[0]) < 10 and len(entry2.get().split(":")[0]) == 1:
                    entry2.insert(0, '0')
                if int(entry3.get().split(":")[0]) < 10 and len(entry3.get().split(":")[0]) == 1:
                    entry3.insert(0, '0')
                if int(entry2.get().split(":")[1]) < 10 and len(entry2.get().split(":")[1]) == 1:
                    entry2.insert(END, '0')
                if int(entry3.get().split(":")[1]) < 10 and len(entry3.get().split(":")[1]) == 1:
                    entry2.insert(END, '0')
                if entry2.get() > entry3.get():
                    messagebox.showinfo("Invalid value",
                                        "End time must be a time after start time. Imagine attending classes backwards.")
                    if event == 1:
                        return 0
                elif entry2.get() == entry3.get():
                    messagebox.showinfo("Invalid value",
                                        "Don't tell me your class lasts less than a minute.")
                    if event == 1:
                        return 0
                else:
                    if "." not in entry4.get() or entry4.get() == "--valid url--":
                        messagebox.showinfo("Invalid URL", "Please enter a valid url (.com, .net, .org, etc.)")
                        if event == 1:
                            return 0
                    else:
                        if not entry4.get().startswith('http'):
                            if entry4.get().startswith('www'):
                                url = "https://" + entry4.get()
                            else:
                                url = "https://www." + entry4.get()
                        else:
                            url = entry4.get()
                        for i in classes:
                            if i[0] == days.index(combo1.get()) - 1:
                                newdata = [entry1.get(), entry2.get(), entry3.get(), url]
                                if newdata not in i[1]:
                                    delete = open(data, "wb")  # clear existing data from the data file first
                                    pickle.dump([], delete)
                                    i[1].append(newdata)
                                    delete.close()
                                    pickle_out = open(data, "wb")
                                    pickle.dump(classes, pickle_out)
                                    pickle_out.close()
                                    fill_table()
                                    entry1.delete(0, END)
                                    entry2.delete(0, END)
                                    entry3.delete(0, END)
                                    entry4.delete(0, END)
                                    combo1.current(0)
                                    return 1


def removeClass():
    global classes, data
    if tree1.selection() != ():
        if not any(i in ('0', '1', '2', '3', '4', '5', '6') for i in tree1.selection()):
            result = messagebox.askquestion("Delete Record",
                                            f"Are you sure you want to delete {len(tree1.selection())} record(s)?",
                                            icon='warning', default='no')
            if result == 'yes':
                for record in tree1.selection():
                    values = tree1.item(record)['values']
                    for i in classes:
                        if i[0] == int(tree1.parent(record)):
                            for j in i[1]:
                                if j[0] == values[0] and j[1] == values[1] and j[2] == values[2] and j[3] == values[3]:
                                    j.clear()
                                    i[1] = [x for x in i[1] if
                                            x]  # replaces i[1] after removing all empty sub lists in i[1]
                                    tree1.delete(record)
                                    break
                            break
                delete = open(data, "wb")  # clear existing data from the data file first
                pickle.dump([], delete)
                delete.close()
                pickle_out = open(data, "wb")
                pickle.dump(classes, pickle_out)
                pickle_out.close()
                fill_table()
        else:
            messagebox.showinfo("Unable to delete", "Make sure you're only selecting classes and not the day headings.")
    else:
        messagebox.showinfo("No record selected",
                            "Please select a record that you want to delete. (Can't delete void)")


def removeAll():
    global classes, data
    result = messagebox.askquestion("Clear Table",
                                    "Are you sure you want to delete the entire table? (There's no undo though)",
                                    icon='warning', default='no')
    if result == 'yes':
        for record in tree1.get_children():
            for child in tree1.get_children(record):  # Get sub children
                values = tree1.item(child)['values']
                for i in classes:
                    if i[0] == int(record):
                        for j in i[1]:
                            if j[0] == values[0] and j[1] == values[1] and j[2] == values[2] and j[3] == values[3]:
                                j.clear()
                                i[1] = [x for x in i[1] if
                                        x]  # replaces i[1] after removing all empty sub lists in i[1]
                                tree1.delete(child)
                                break
                        break
            delete = open(data, "wb")  # clear existing data from the data file first
            pickle.dump([], delete)
            delete.close()
            pickle_out = open(data, "wb")
            pickle.dump(classes, pickle_out)
            pickle_out.close()
            fill_table()


def editClass():
    global record_no
    if len(tree1.selection()) != 0:
        if not any(i in ('0', '1', '2', '3', '4', '5', '6') for i in tree1.selection()):
            record_no = tree1.selection()[0]
            values = tree1.item(tree1.selection()[0])['values']
            combo1.current(int(tree1.parent(tree1.selection()[0])) + 1)
            entry1.delete(0, END)
            entry1.insert(0, values[0])
            entry2.delete(0, END)
            entry2.insert(0, values[1])
            entry3.delete(0, END)
            entry3.insert(0, values[2])
            entry4.delete(0, END)
            entry4.insert(0, values[3])
            button8["state"] = "active"
        else:
            messagebox.showinfo("Unable to delete", "Make sure you're only selecting classes and not the day headings.")
    else:
        messagebox.showinfo("No record selected", "Please select a class that you want to update.")


# # Button9
# img15 = PhotoImage(file="images/JoinNowButton.png")  # add "/" not "\"
# button9 = Button(frame6, image=img15, command=JoinNext, borderwidth=0, bg="#2B2B26", relief=FLAT)
# button9.grid(sticky=N + E + W + S)
# button9.grid_rowconfigure(0, weight=100)
# button9.grid_columnconfigure(0, weight=100)
# button9.place(relx=0.25, rely=0.7)


def updateClass():
    global classes, record_no, data
    error = True  # Assume always error at the beginning
    if tree1.selection() != ():
        if ('0' or '1' or '2' or '3' or '4' or '5' or '6') not in tree1.selection():
            values = tree1.item(record_no)['values']
            for i in classes:
                if i[0] == int(tree1.parent(record_no)):
                    for j in i[1]:
                        if j[0] == values[0] and j[1] == values[1] and j[2] == values[2] and j[3] == values[3]:
                            j.clear()
                            i[1] = [x for x in i[1] if
                                    x]  # replaces i[1] after removing all empty sub lists in i[1]
                            if addclass(1):  # Error doesn't exist if 1 is returned
                                tree1.delete(record_no)
                                error = False
                            else:
                                error = True
                            break
                    break
            if not error:  # update class only if no error is generated
                delete = open(data, "wb")  # clear existing data from the data file first
                pickle.dump([], delete)
                delete.close()
                pickle_out = open(data, "wb")
                pickle.dump(classes, pickle_out)
                pickle_out.close()
                fill_table()
                button8['state'] = 'disabled'
        else:
            messagebox.showinfo("Unable to update", "Make sure you're only selecting classes and not the day headings.")
    else:
        messagebox.showinfo("No record selected", "Please select a record that you want to update.")


def all_clear():
    combo1.current(0)
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry2.insert(0, "hh:mm (24 hour format)")
    entry3.delete(0, END)
    entry3.insert(0, "hh:mm (24 hour format)")
    entry4.delete(0, END)
    entry4.insert(0, "--valid url--")


# Save settings onto settings.dat
cb1 = tk.IntVar()
cb2 = tk.IntVar()
cb3 = tk.IntVar()
rb1 = tk.IntVar()


def savesettings():
    global settings
    system_out = open("data/settings.dat", "wb")  # Change the value in the DAT file
    settings['prompt'] = cb1.get()  # Update prompt setting
    settings['day'] = combo2.current()  # Update first day of the week setting
    settings['notifications'] = cb2.get()  # Update notifications setting
    if cb2.get():
        settings['noti_time'] = combo3.current()
        settings['launch'] = cb3.get()
    else:
        settings['launch'] = 0

    pickle.dump(settings, system_out)
    system_out.close()

    # Label15
    label15 = Label(frame8, bg="black", fg="yellow", text="Settings saved.", font=('Verdana', 11, 'italic'))
    label15.grid(sticky=N + E + W + S, pady=0, padx=0)
    label15.grid_columnconfigure(0, weight=100)
    label15.grid_rowconfigure(0, weight=100)
    label15.place(relx=0.875, rely=0.9)
    frame8.update_idletasks()
    frame8.after(2000, label15.place_forget())


# # Label17
# label17 = Label(frame8, bg="black", fg="yellow", text="Note: Changes will take effect the next time you open OCH", font=('Verdana', 11, 'bold'))
# label17.grid(sticky=N + E + W + S, pady=0, padx=0)
# label17.grid_columnconfigure(0, weight=100)
# label17.grid_rowconfigure(0, weight=100)
# label17.place(relx=0.35, rely=0.1)


def sendFeedback():
    feedback = scr1.get('1.0', 'end-1c')
    if rb1.get() == 1:  # Suggestion
        type = 0
    elif rb1.get() == 2:  # Feedback
        type = 1
    else:
        messagebox.showinfo('Error', 'Please choose Suggestion/Feedback')
        return
    if not feedback:
        messagebox.showinfo('Error', "Message can't be empty")
        return
    port = 465  # 465 for SSL and 587 for TSL
    smtp_server = "smtp.gmail.com"
    sender_email = "xxx@gmail.com"
    receiver_email = "xxx@gmail.com"
    password = ""  # Email password

    message = MIMEMultipart("alternative")
    if type:  # whether feedback/suggestion radio button is selected before sending.
        message["Subject"] = "Feedback for OCH"
    else:
        message["Subject"] = "Suggestion for OCH"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = f"""{feedback}"""

    # Turn these into plain MIMEText objects
    toAttach = MIMEText(text, "plain")
    message.attach(toAttach)

    # Create secure connection with server and send email
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
            server.quit()
        scr1.delete(1.0, END)
        # Label19
        label19 = Label(frame9, bg="black", fg="yellow", text="Message sent", font=('Verdana', 11, 'italic'))
        label19.grid(sticky=N + E + W + S, pady=0, padx=0)
        label19.grid_columnconfigure(0, weight=100)
        label19.grid_rowconfigure(0, weight=100)
        label19.place(relx=0.9, rely=0.9)
        frame9.update_idletasks()
        frame9.after(2000, label19.place_forget())
    except Exception as e:
        messagebox.showinfo('Error Sending', 'Unable to send message, please check your internet connection!')


def time_diff(time1, time2):  # Returns the time difference in seconds between time1 and time2 where time1 > time2
    ftr = [3600, 60, 1]
    return sum([a * b for a, b in zip(ftr, map(int, time1.split(':')))]) - sum(
        [a * b for a, b in zip(ftr, map(int, time2.split(':')))])


# # Message1
# message1 = Message(loginFrame, text="", font=('Verdana', 15), borderwidth=2, bg="black", fg="yellow", justify="left",
#                    aspect=int(root.winfo_screenwidth() / 2))
# message1.grid(sticky=N + E + W + S)
# message1.grid_rowconfigure(0, weight=100)
# message1.grid_columnconfigure(0, weight=100)
# message1.place(relx=0.4, rely=0.55)
#
# # Message2
# message2 = Message(frame6, bg="#2B2B26", fg="yellow", text="", relief=FLAT, justify="left", font=('Verdana', 11),
#                    aspect=int(frame6.winfo_screenwidth() - 20))
# message2.grid(sticky=N + E + W + S)
# message2.grid_rowconfigure(0, weight=100)
# message2.grid_columnconfigure(0, weight=100)
# message2.place(relx=0.08, rely=0.2)
# clock()  # Call the function clock which recursively calls itself every second.
#
# # Button1
# img = PhotoImage(file="images/JoinButton.png")  # add "/" not "\"
# button1 = Button(loginFrame, image=img, command=Join, borderwidth=0, bg="black", relief=FLAT)
# button1.grid(sticky=N + E + W + S)
# button1.grid_rowconfigure(0, weight=100)
# button1.grid_columnconfigure(0, weight=100)
# button1.place(relx=0.455, rely=0.68)
#
# # Button2
# img2 = PhotoImage(file="images/NewClassButton.png")  # add "/" not "\"
# button2 = Button(frame2, image=img2, command=addclass, borderwidth=0, bg="black", relief=FLAT)
# button2.grid(sticky=N + E + W + S)
# button2.grid_rowconfigure(0, weight=100)
# button2.grid_columnconfigure(0, weight=100)
# button2.place(relx=0.84, rely=0.335)
#
# # Button3
# img9 = PhotoImage(file="images/ClearButton.png")
# button3 = Button(frame2, image=img9, command=all_clear, borderwidth=0, bg="black", relief=FLAT)
# button3.grid(sticky=N + E + W + S)
# button3.grid_rowconfigure(0, weight=100)
# button3.grid_columnconfigure(0, weight=100)
# button3.place(relx=0.8, rely=0.12)
#
# # Button4
# img10 = PhotoImage(file="images/RemoveSelectedClassesButton.png")  # add "/" not "\"
# button4 = Button(frame2, image=img10, command=removeClass, borderwidth=0, bg="black", relief=FLAT)
# button4.grid(sticky=N + E + W + S)
# button4.grid_rowconfigure(0, weight=100)
# button4.grid_columnconfigure(0, weight=100)
# button4.place(relx=0.05, rely=0.92)
# CreateToolTip(button4, "Hold the control button and select the records you want to delete")
#
# # Button5
# img11 = PhotoImage(file="images/RemoveAllClassesButton.png")  # add "/" not "\"
# button5 = Button(frame2, image=img11, command=removeAll, borderwidth=0, bg="black", relief=FLAT)
# button5.grid(sticky=N + E + W + S)
# button5.grid_rowconfigure(0, weight=100)
# button5.grid_columnconfigure(0, weight=100)
# button5.place(relx=0.835, rely=0.92)
# CreateToolTip(button5, "Clear the table")
#
# # Button6
# img12 = PhotoImage(file="images/EditButton.png")  # add "/" not "\"
# button6 = Button(frame2, image=img12, command=editClass, borderwidth=0, bg="black", relief=FLAT)
# button6.grid(sticky=N + E + W + S)
# button6.grid_rowconfigure(0, weight=100)
# button6.grid_columnconfigure(0, weight=100)
# button6.place(relx=0.05, rely=0.85)
# CreateToolTip(button6, "Select a class and make changes")
#
# # Button8
# img13 = PhotoImage(file="images/UpdateClassButton.png")  # add "/" not "\"
# button8 = Button(frame2, image=img13, command=updateClass, borderwidth=0, bg="black", relief=FLAT)
# button8.grid(sticky=N + E + W + S)
# button8.grid_rowconfigure(0, weight=100)
# button8.grid_columnconfigure(0, weight=100)
# button8.place(relx=0.845, rely=0.25)
# button8['state'] = 'disabled'
#
# # Button10
# img19 = PhotoImage(file="images/CheckForUpdatesButton.png")  # add "/" not "\"
# button10 = Button(frame7, image=img19, command=lambda: check_updates(1), bg="black", relief=FLAT)
# button10.grid(sticky=N + E + W + S)
# button10.grid_rowconfigure(0, weight=100)
# button10.grid_columnconfigure(0, weight=100)
# button10.place(relx=0.42, rely=0.6)
#
# # Button11
# img24 = PhotoImage(file="images/savebutton.png")  # add "/" not "\"
# button11 = Button(frame8, image=img24, command=savesettings, bg="black", relief=FLAT)
# button11.grid(sticky=N + E + W + S)
# button11.grid_rowconfigure(0, weight=100)
# button11.grid_columnconfigure(0, weight=100)
# button11.place(relx=0.45, rely=0.9)
#
# # Button12
# img27 = PhotoImage(file="images/SendButton.png")  # add "/" not "\"
# button12 = Button(frame9, image=img27, command=sendFeedback, bg="black", relief=FLAT)
# button12.grid(sticky=N + E + W + S)
# button12.grid_rowconfigure(0, weight=100)
# button12.grid_columnconfigure(0, weight=100)
# button12.place(relx=0.46, rely=0.81)
#
# # RadioButton1
# img28 = PhotoImage(file="images/SuggestionLabel.png")  # add "/" not "\"
# radio1 = Radiobutton(frame9, image=img28, variable=rb1, bg="black", value=1, relief=FLAT)
# radio1.grid(sticky=N + E + W + S)
# radio1.grid_rowconfigure(0, weight=100)
# radio1.grid_columnconfigure(0, weight=100)
# radio1.place(relx=0.32, rely=0.38)
#
# # RadioButton2
# img29 = PhotoImage(file="images/FeedbackLabel.png")  # add "/" not "\"
# radio2 = Radiobutton(frame9, image=img29, variable=rb1, bg="black", value=2, relief=FLAT)
# radio2.grid(sticky=N + E + W + S)
# radio2.grid_rowconfigure(0, weight=100)
# radio2.grid_columnconfigure(0, weight=100)
# radio2.place(relx=0.56, rely=0.38)
#
# # Label18
# label18 = Label(frame9, bg="black", fg="yellow", text=feedbacktext, font=('Verdana', 11, 'bold'), relief=FLAT)
# label18.grid(sticky=N + E + W + S)
# label18.grid_rowconfigure(0, weight=100)
# label18.grid_columnconfigure(0, weight=100)
# label18.place(relx=0.28, rely=0.3)
#
# # ScrolledText1
# scr1 = scrolledtext.ScrolledText(frame9, wrap=tk.WORD, width=50, height=10, font=("Helvetica", 15), bg="black",
#                                  fg="yellow")
# scr1.configure(insertbackground="yellow")
# scr1.grid(sticky=N+E+W+S, column=0, pady=5, padx=5)  # area widget
# scr1.grid_columnconfigure(0, weight=100)
# scr1.grid_rowconfigure(0, weight=100)
# scr1.place(relx=0.31, rely=0.47)
#
# style.map('TCombobox', fieldbackground=[('readonly', 'green')])
# style.map('TCombobox', selectbackground=[('readonly', 'blue')])
# style.map('TCombobox', selectforeground=[('readonly', 'red')])
#
# logo = Image.open("images/OCH_Logo.png")
# logo = logo.resize((180, 200), Image.ANTIALIAS)
# img16 = ImageTk.PhotoImage(logo)
# label9 = Label(loginFrame, image=img16, borderwidth=0, bg="black")
# label9.grid(sticky=N + E + W + S, pady=0, padx=0)
# label9.grid_columnconfigure(0, weight=100)
# label9.grid_rowconfigure(0, weight=100)
# label9.place(relx=0.438, rely=0.03)
#
# logo2 = Image.open("images/OCH_Logo2.png")
# logo2 = logo2.resize((100, 98), Image.ANTIALIAS)
# img17 = ImageTk.PhotoImage(logo2)
# label10 = Label(frame2, image=img17, borderwidth=0, bg="black")
# label10.grid(sticky=N + E + W + S, pady=0, padx=0)
# label10.grid_columnconfigure(0, weight=100)
# label10.grid_rowconfigure(0, weight=100)
# label10.place(relx=0.87, rely=0.07)
#
# logo4 = Image.open("images/OCH_Logo.png")
# logo4 = logo4.resize((200, 220), Image.ANTIALIAS)
# img20 = ImageTk.PhotoImage(logo4)
# label11 = Label(frame7, image=img20, borderwidth=0, bg="black")
# label11.grid(sticky=N + E + W + S, pady=0, padx=0)
# label11.grid_columnconfigure(0, weight=100)
# label11.grid_rowconfigure(0, weight=100)
# label11.place(relx=0.438, rely=0.15)
#
# label12 = Label(frame7, text=f"Version {__version__}", font=('Times New Roman', 18), borderwidth=0, bg="black",
#                 fg="yellow")
# label12.grid(sticky=N + E + W + S)
# label12.grid_rowconfigure(0, weight=100)
# label12.grid_columnconfigure(0, weight=100)
# label12.place(relheight=0.05, relwidth=0.1, relx=0.448, rely=0.5)
#
# # Label Frame (Add Class)
# labelframe1 = LabelFrame(frame2, bg="black", font=("Helvetica", 12), foreground="yellow", text="Add Class")
# labelframe1.grid(sticky=N + E + W + S)
# labelframe1.place(relwidth=0.75, relheight=0.25, relx=0.05, rely=0.13)
#
# # Label Frame (Settings)
# labelframe2 = LabelFrame(frame8, bg="black", font=("Helvetica", 12), foreground="yellow", text="Settings")
# labelframe2.grid(sticky=N + E + W + S)
# labelframe2.place(relwidth=0.9, relheight=0.75, relx=0.05, rely=0.13)
#
# # Label1
# img4 = PhotoImage(file="images/ChooseDayLabel.png")
# label1 = Label(labelframe1, bg="black", image=img4, command=None, relief=FLAT)
# label1.grid(sticky=N + E + W + S)
# label1.grid_rowconfigure(0, weight=100)
# label1.grid_columnconfigure(0, weight=100)
# label1.place(relx=0.02, rely=0.18)
#
# # Label2
# img5 = PhotoImage(file="images/EnterSubjectLabel.png")
# label2 = Label(labelframe1, bg="black", image=img5, command=None, relief=FLAT)
# label2.grid(sticky=N + E + W + S)
# label2.grid_rowconfigure(0, weight=100)
# label2.grid_columnconfigure(0, weight=100)
# label2.place(relx=0.02, rely=0.61)
#
# # Label3
# img6 = PhotoImage(file="images/StartTimeLabel.png")
# label3 = Label(labelframe1, bg="black", image=img6, command=None, relief=FLAT)
# label3.grid(sticky=N + E + W + S)
# label3.grid_rowconfigure(0, weight=100)
# label3.grid_columnconfigure(0, weight=100)
# label3.place(relx=0.36, rely=0.18)
#
# # CheckButton1
# img21 = PhotoImage(file="images/promptbutton.png")  # add "/" not "\"
# checkbutton1 = Checkbutton(labelframe2, bg="black", image=img21, relief=FLAT, variable=cb1)
# if settings['prompt']:
#     checkbutton1.select()
# else:
#     checkbutton1.deselect()
# checkbutton1.grid(sticky=N + E + W + S)
# checkbutton1.grid_rowconfigure(0, weight=100)
# checkbutton1.grid_columnconfigure(0, weight=100)
# checkbutton1.place(relx=0.02, rely=0.1)
#
# # Label14
# img22 = PhotoImage(file="images/daylabel.png")  # add "/" not "\"
# label14 = Label(labelframe2, bg="black", image=img22, relief=FLAT, highlightcolor='yellow')
# label14.grid(sticky=N + E + W + S)
# label14.grid_rowconfigure(0, weight=100)
# label14.grid_columnconfigure(0, weight=100)
# label14.place(relx=0.35, rely=0.1)
#
# # Combo2 - Drop down menu
# combo2 = ttk.Combobox(labelframe2, value=days, state="readonly", style="TCombobox")
# combo2.current(settings['day'])
# combo2.bind("<<ComboboxSelected>>", None)
# combo2.grid(sticky=N + E + W + S)
# combo2.grid_rowconfigure(0, weight=100)
# combo2.grid_columnconfigure(0, weight=100)
# combo2.place(relx=0.56, rely=0.12, relwidth=0.165)
#
# # CheckButton2
# img23 = PhotoImage(file="images/notifybutton.png")  # add "/" not "\"
# checkbutton2 = Checkbutton(labelframe2, bg="black", command=checkNotification, image=img23, relief=FLAT, variable=cb2)
# if settings['notifications']:
#     checkbutton2.select()
# else:
#     checkbutton2.deselect()
# checkbutton2.grid(sticky=N + E + W + S)
# checkbutton2.grid_rowconfigure(0, weight=100)
# checkbutton2.grid_columnconfigure(0, weight=100)
# checkbutton2.place(relx=0.02, rely=0.3)
#
# # Combo3 - Drop down menu
# combo3 = ttk.Combobox(labelframe2, value=minutes, state="readonly", style="TCombobox")
# combo3.current(settings['noti_time'])
# if settings['notifications']:
#     combo3['state'] = 'readonly'
# else:
#     combo3['state'] = 'disabled'
# combo3.bind("<<ComboboxSelected>>", None)
# combo3.grid(sticky=N + E + W + S)
# combo3.grid_rowconfigure(0, weight=100)
# combo3.grid_columnconfigure(0, weight=100)
# combo3.place(relx=0.147, rely=0.325, relwidth=0.05)
#
# # Label16
# img25 = PhotoImage(file="images/beforebutton.png")
# label16 = Label(labelframe2, bg="black", image=img25, command=None, relief=FLAT)
# label16.grid(sticky=N + E + W + S)
# label16.grid_rowconfigure(0, weight=100)
# label16.grid_columnconfigure(0, weight=100)
# label16.place(relx=0.2, rely=0.3)
#
# # CheckButton3
# img26 = PhotoImage(file="images/launchbutton.png")  # add "/" not "\"
# checkbutton3 = Checkbutton(labelframe2, bg="black", image=img26, relief=FLAT, variable=cb3)
# if settings['notifications']:
#     checkbutton3['state'] = NORMAL
#     if settings['launch']:
#         checkbutton3.select()
#     else:
#         checkbutton3.deselect()
# else:
#     checkbutton3['state'] = DISABLED
#     checkbutton3.deselect()
#
# checkbutton3.grid(sticky=N + E + W + S)
# checkbutton3.grid_rowconfigure(0, weight=100)
# checkbutton3.grid_columnconfigure(0, weight=100)
# checkbutton3.place(relx=0.05, rely=0.4)
#
# # Label4
# img7 = PhotoImage(file="images/EndTimeLabel.png")
# label4 = Label(labelframe1, bg="black", image=img7, command=None, relief=FLAT)
# label4.grid(sticky=N + E + W + S)
# label4.grid_rowconfigure(0, weight=100)
# label4.grid_columnconfigure(0, weight=100)
# label4.place(relx=0.36, rely=0.61)
#
# # Label5
# img8 = PhotoImage(file="images/ClassLinkLabel.png")
# label5 = Label(labelframe1, bg="black", image=img8, command=None, relief=FLAT)
# label5.grid(sticky=N + E + W + S)
# label5.grid_rowconfigure(0, weight=100)
# label5.grid_columnconfigure(0, weight=100)
# label5.place(relx=0.67, rely=0.18)
#
# # Label6
#
# label6 = Label(frame3, text=abouttext, font=('Times New Roman', 18), borderwidth=0, bg="black", fg="yellow")
# label6.grid(sticky=N + E + W + S)
# label6.grid_rowconfigure(0, weight=100)
# label6.grid_columnconfigure(0, weight=100)
# label6.place(relheight=1.3, relwidth=1)
#
# logo3 = Image.open("images/OCH_Logo2.png")
# logo3 = logo3.resize((200, 196), Image.ANTIALIAS)
# img18 = ImageTk.PhotoImage(logo3)
# label8 = Label(frame3, image=img18, borderwidth=0, bg="black")
# label8.grid(sticky=N + E + W + S, pady=0, padx=0)
# label8.grid_columnconfigure(0, weight=100)
# label8.grid_rowconfigure(0, weight=100)
# label8.place(relx=0.438, rely=0.075)
#
# # Label7
# helptext = For any kind of bugs/issues/help/details please contact the owner through the following:
# Personal Email: vensr.maddula@gmail.com
# Business Email: ravensenterprises8@gmail.com
# Personal Instagram handle: @vens8
# Personal Twitter handle: @vens_8
# '''
#
# label7 = Label(frame4, text=helptext, font=('Times New Roman', 18), borderwidth=0, bg="black", fg="yellow")
# label7.grid(sticky=N + E + W + S)
# label7.grid_rowconfigure(0, weight=100)
# label7.grid_columnconfigure(0, weight=100)
# label7.place(relheight=1, relwidth=1)
#
# # Combo1 - Drop down menu
# combo1 = ttk.Combobox(labelframe1, value=user_days, state="readonly", style="TCombobox")
# combo1.current(0)
# combo1.bind("<<ComboboxSelected>>", None)
# combo1.grid(sticky=N + E + W + S)
# combo1.grid_rowconfigure(0, weight=100)
# combo1.grid_columnconfigure(0, weight=100)
# combo1.place(relx=0.165, rely=0.2, relwidth=0.165)
#
#
# def e2_clear(event):
#     if entry2.get() == "hh:mm (24 hour format)":
#         entry2.delete(0, "end")
#
#
# def e3_clear(event):
#     if entry3.get() == "hh:mm (24 hour format)":
#         entry3.delete(0, "end")
#
#
# def e4_clear(event):
#     if entry4.get() == "--valid url--":
#         entry4.delete(0, "end")
#
#
# # Entry1
# entry1 = Entry(labelframe1, fg="yellow", bg="black", highlightcolor="green", highlightthickness=0.5, justify="left",
#                font=("Helvetica", 10), insertbackground='yellow')
# entry1.grid(sticky=N + E + W + S)
# entry1.grid_rowconfigure(0, weight=100)
# entry1.grid_columnconfigure(0, weight=100)
# entry1.place(relx=0.165, rely=0.64, relwidth=0.165)
#
# # Entry2
# entry2 = Entry(labelframe1, fg="yellow", bg="black", highlightcolor="green", highlightthickness=0.5, justify="left",
#                font=("Helvetica", 10), insertbackground='yellow')
# entry2.insert(0, "hh:mm (24 hour format)")
# entry2.grid(sticky=N + E + W + S)
# entry2.grid_rowconfigure(0, weight=100)
# entry2.grid_columnconfigure(0, weight=100)
# entry2.bind("<FocusIn>", e2_clear)
# entry2.place(relx=0.48, rely=0.21, relwidth=0.165)
#
# # Entry3
# entry3 = Entry(labelframe1, fg="yellow", bg="black", highlightcolor="green", highlightthickness=0.5, justify="left",
#                font=("Helvetica", 10), insertbackground='yellow')
# entry3.insert(0, "hh:mm (24 hour format)")
# entry3.grid(sticky=N + E + W + S)
# entry3.grid_rowconfigure(0, weight=100)
# entry3.grid_columnconfigure(0, weight=100)
# entry3.bind("<FocusIn>", e3_clear)
# entry3.place(relx=0.48, rely=0.64, relwidth=0.165)
#
# # Entry4
# entry4 = Entry(labelframe1, fg="yellow", bg="black", highlightcolor="green", highlightthickness=0.5, justify="left",
#                font=("Helvetica", 10), width=40, insertbackground='yellow')
# entry4.insert(0, "--valid url--")
# entry4.grid(sticky=N + E + W + S)
# entry4.grid_rowconfigure(0, weight=100)
# entry4.grid_columnconfigure(0, weight=100)
# entry4.bind("<FocusIn>", e4_clear)
# entry4.place(relx=0.79, rely=0.21, relwidth=0.2)
#
#
# # Tree view frame
# frame5 = tk.Frame(frame2, bg="black")
# frame5.grid(sticky=N + E + W + S, row=0, column=0, pady=0, padx=0)
# frame5.grid_rowconfigure(0, weight=1)
# frame5.grid_columnconfigure(0, weight=1)
# frame5.place(relx=0.05, rely=0.42, relwidth=0.96, relheight=0.4)

#
# # Scrollbar
# scrollbar1 = ttk.Scrollbar(frame5, orient=VERTICAL)
# scrollbar1.grid(sticky=N + S + E + W, row=0, column=1)
# scrollbar1.grid_rowconfigure(0, weight=1)
# scrollbar1.grid_columnconfigure(0, weight=1)
#
# # Tree view table
# tree1 = ttk.Treeview(frame5, yscrollcommand=scrollbar1.set)
# tree1['columns'] = ("Day", "Start time", "End time", "Class link")
# tree1.column("#0", width=0, anchor=W)
# tree1.column("Day", anchor=W, width=100)
# tree1.column("Start time", anchor=W, width=50)
# tree1.column("End time", anchor=W, width=50)
# tree1.column("Class link", anchor=W, width=700)
# tree1.heading("#0", text="", anchor=W)
# tree1.heading("Day", text="Day : Subject", anchor=W)
# tree1.heading("Start time", text="Start time", anchor=W)
# tree1.heading("End time", text="End time", anchor=W)
# tree1.heading("Class link", text="Class link", anchor=W)
# scrollbar1.config(command=tree1.yview)
# style.theme_use("clam")
# style.configure("Treeview.Heading",
#                 font=("Helvetica", 12, "bold"),
#                 background="#581845",
#                 foreground="white",
#                 relief="flat",
#                 )
# style.configure("Treeview",
#                 font=("Helvetica", 11),
#                 background="#FFC30F",
#                 foreground="#FFFF00",
#                 rowheight=45,
#                 fieldbackground="black"
#                 )
# style.configure("Vertical.TScrollbar", background="#581845", darkcolor="#FFC30F", lightcolor="#FFC30F",
#                 troughcolor="#B28500", bordercolor="black", arrowcolor="white"
#                 )
# style.map("Treeview",
#           background=[("selected", "#FFC30F")],
#           foreground=[("selected", "black")]
#           )
# tree1.tag_configure('even', background="#C70039", font=("Helvetica", 11, 'bold'))
# tree1.tag_configure('odd', background="#A50240", font=("Helvetica", 11, 'bold'))
# tree1.tag_configure('child', background="#FF5733")


# Table data
# def fill_table():
#     global classes, user_days  # user_days is the list of days in the order of user's choice
#     sortRecords()
#     for i in tree1.get_children():  # Clear table
#         tree1.delete(i)
#     id_count = 0
#     c_count = 0
#     for i in classes:
#         if id_count % 2 == 0:
#             tree1.insert(parent='', index="end", iid=id_count, open=True, text="",
#                          values=(user_days[i[0] + 1], "", "", ""),
#                          tags=('even',))
#         else:
#             tree1.insert(parent='', index="end", iid=id_count, open=True, text="",
#                          values=(user_days[i[0] + 1], "", "", ""),
#                          tags=('odd',))
#         id_count += 1
#         if id_count > 0:
#             sep = ttk.Separator(tree1, orient='horizontal')
#             sep.grid(sticky="news")
#
#     for i in range(1, len(user_days)):
#         if classes[days.index(user_days[i]) - 1][1]:
#             for j in classes[days.index(user_days[i]) - 1][1]:
#                 if c_count < id_count:
#                     tree1.insert(parent=f"{c_count}", index="end", iid=id_count, open=False, text="",
#                                  values=(j[0], j[1], j[2], j[3]), tags=('child',))
#                     id_count += 1
#                 else:
#                     break
#             c_count += 1
#             if c_count >= id_count:
#                 break
#         else:
#             c_count += 1
'''
    for i in classes:
        for j in i[1]:
            if c_count < id_count:
                tree1.insert(parent=f"{c_count}", index="end", iid=id_count, open=False, text="",
                             values=(j[0], j[1], j[2], j[3]), tags=('child',))
                id_count += 1
            else:
                break
        c_count += 1
        if c_count >= id_count:
            break
    '''


# fill_table()
# tree1.grid(pady=20, padx=20)
# tree1.place(relx=0, rely=0, relwidth=0.937, relheight=1)

# # Button 7
# img3 = PhotoImage(file="images/LoadDataButton.png")
# button7 = Button(frame2, image=img3, command=load_file, borderwidth=0, bg="black", relief=RIDGE)
# button7.grid(sticky=N + E + W + S)
# button7.grid_rowconfigure(0, weight=100)
# button7.grid_columnconfigure(0, weight=100)
# button7.place(relx=0.875, rely=0.85)

root.mainloop()
