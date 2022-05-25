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


class Item:
    def __init__(self, customerID, productID, price, quantity, image, productName):
        self.customerID = customerID
        self.productID = productID
        self.price = price
        self.quantity = quantity
        self.image = image
        self.productName = productName


cart = []


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
        self.currentPrice = round(currentPrice * (1 - (discount/100)), 2)
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
        global currentUser
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
        global currentUser
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
    for i in categoriesTree.get_children():  # Clear table
        categoriesTree.delete(i)
    id_count = 0  # Parent
    for i in categories:
        if id_count % 2 == 0:
            categoriesTree.insert(parent='', index="end", iid=id_count, open=True, text=i.categoryID,
                         image=ImageTk.PhotoImage(file=i.image), value=(i.image, i.categoryName), tags=('even',))
        else:
            categoriesTree.insert(parent='', index="end", iid=id_count, open=True, text=i.categoryID,
                         image=ImageTk.PhotoImage(file=i.image), value=(i.image, i.categoryName), tags=('odd',))
        id_count += 1

        if id_count > 0:
            sep = ttk.Separator(categoriesTree, orient='horizontal')
            sep.grid(sticky="news")


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


kartezieLogo2 = Label(homeFrame, background="#161616")
kartezieLogo2.place(relx=0.34, rely=0.05)
kartezieLogo2.configure(image=img)


# Tree view frame
categoriesTreeFrame = tk.Frame(homeFrame, bg="#161616")
categoriesTreeFrame.grid(sticky=N + E + W + S, row=0, column=0, pady=0, padx=0)
categoriesTreeFrame.grid_rowconfigure(0, weight=1)
categoriesTreeFrame.grid_columnconfigure(0, weight=1)
categoriesTreeFrame.place(relx=0.1, rely=0.25, relwidth=0.96, relheight=0.45)

# Scrollbar
categoryScroll = ttk.Scrollbar(categoriesTreeFrame, orient=VERTICAL)
categoryScroll.grid(sticky=N + S + E + W, row=0, column=1)
categoryScroll.grid_rowconfigure(0, weight=1)
categoryScroll.grid_columnconfigure(0, weight=1)

# Tree view frame
productsTreeFrame = tk.Frame(homeFrame, bg="#161616")
productsTreeFrame.grid(sticky=N + E + W + S, row=0, column=0, pady=0, padx=0)
productsTreeFrame.grid_rowconfigure(0, weight=1)
productsTreeFrame.grid_columnconfigure(0, weight=1)
productsTreeFrame.place(relx=0.1, rely=0.61, relwidth=0.96, relheight=0.45)

# Scrollbar
productScroll = ttk.Scrollbar(productsTreeFrame, orient=VERTICAL)
productScroll.grid(sticky=N + S + E + W, row=0, column=1)
productScroll.grid_rowconfigure(0, weight=1)
productScroll.grid_columnconfigure(0, weight=1)

# Tree view table
categoriesTree = ttk.Treeview(categoriesTreeFrame, yscrollcommand=categoryScroll.set, selectmode="browse")
categoriesTree['columns'] = ("Image", "Category")
categoriesTree.column("#0", width=0, anchor=W)
categoriesTree.column("Image", anchor=W, width=100)
categoriesTree.column("Category", anchor=W, width=50)
categoriesTree.heading("#0", text="Category ID", anchor=W)
categoriesTree.heading("Image", text="Image", anchor=W)
categoriesTree.heading("Category", text="Category", anchor=W)
categoryScroll.config(command=categoriesTree.yview)
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview.Heading",
                font="-family {Poppins} -size 15",
                background="#581845",
                foreground="white",
                rowheight=45,
                relief="flat",
                )
style.configure("Treeview",
                font="-family {Poppins} -size 15",
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

categoriesTree.tag_configure('even', background="#C70039", font="-family {Poppins} -size 15")
categoriesTree.tag_configure('odd', background="#A50240", font="-family {Poppins} -size 15")
categoriesTree.tag_configure('child', background="#FF5733")

categoriesTree.grid(pady=20, padx=20)
categoriesTree.place(relx=0, rely=0, relwidth=0.8, relheight=0.6)


selectCategoryButton = Button(homeFrame)
selectCategoryButton.place(relx=0.41, rely=0.53)
selectCategoryButton.configure(relief="flat")
selectCategoryButton.configure(overrelief="flat")
selectCategoryButton.configure(activebackground="#161616")
selectCategoryButton.configure(cursor="hand2")
selectCategoryButton.configure(background="#161616")
selectCategoryButton.configure(borderwidth="0")
img5 = ImageTk.PhotoImage(file="images/selectCategory.png")
selectCategoryButton.configure(image=img5)

# Tree view table
productsTree = ttk.Treeview(productsTreeFrame, yscrollcommand=productScroll.set)
productsTree['columns'] = ("Image", "Product", "Price")
productsTree.column("#0", width=0, anchor=W)
productsTree.column("Image", anchor=W, width=100)
productsTree.column("Product", anchor=W, width=50)
productsTree.column("Price", anchor=W, width=50)
productsTree.heading("#0", text="Product ID", anchor=W)
productsTree.heading("Image", text="Image", anchor=W)
productsTree.heading("Product", text="Product", anchor=W)
productsTree.heading("Price", text="Price", anchor=W)

productScroll.config(command=productsTree.yview)
# style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview.Heading",
                font="-family {Poppins} -size 15",
                background="#581845",
                foreground="white",
                rowheight=45,
                relief="flat",
                )
style.configure("Treeview",
                font="-family {Poppins} -size 15",
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

productsTree.tag_configure('even', background="#C70039", font="-family {Poppins} -size 15")
productsTree.tag_configure('odd', background="#A50240", font="-family {Poppins} -size 15")
productsTree.tag_configure('child', background="#FF5733")

productsTree.grid(pady=20, padx=20)
productsTree.place(relx=0, rely=0, relwidth=0.8, relheight=0.6)

addToCartButton = Button(homeFrame)
addToCartButton.place(relx=0.41, rely=0.9)
addToCartButton.configure(relief="flat")
addToCartButton.configure(overrelief="flat")
addToCartButton.configure(activebackground="#161616")
addToCartButton.configure(cursor="hand2")
addToCartButton.configure(background="#161616")
addToCartButton.configure(borderwidth="0")
img6 = ImageTk.PhotoImage(file="images/addToCart.png")
addToCartButton.configure(image=img6)


kartezieLogo2 = Label(cartFrame, background="#161616")
kartezieLogo2.place(relx=0.34, rely=0.05)
kartezieLogo2.configure(image=img)


# Tree view frame
cartTreeFrame = tk.Frame(cartFrame, bg="#161616")
cartTreeFrame.grid(sticky=N + E + W + S, row=0, column=0, pady=0, padx=0)
cartTreeFrame.grid_rowconfigure(0, weight=1)
cartTreeFrame.grid_columnconfigure(0, weight=1)
cartTreeFrame.place(relx=0.1, rely=0.25, relwidth=0.96, relheight=0.6)

# Scrollbar
cartScroll = ttk.Scrollbar(cartTreeFrame, orient=VERTICAL)
cartScroll.grid(sticky=N + S + E + W, row=0, column=1)
cartScroll.grid_rowconfigure(0, weight=1)
cartScroll.grid_columnconfigure(0, weight=1)

# Tree view table
cartTree = ttk.Treeview(cartTreeFrame, yscrollcommand=cartScroll.set)
cartTree['columns'] = ("Image", "Product", "Quantity", "Price")
cartTree.column("#0", width=0, anchor=W)
cartTree.column("Image", anchor=W, width=100)
cartTree.column("Product", anchor=W, width=50)
cartTree.column("Quantity", anchor=W, width=50)
cartTree.column("Price", anchor=W, width=50)
cartTree.heading("#0", text="Product ID", anchor=W)
cartTree.heading("Image", text="Image", anchor=W)
cartTree.heading("Product", text="Product", anchor=W)
cartTree.heading("Quantity", text="Quantity", anchor=W)
cartTree.heading("Price", text="Price", anchor=W)
productScroll.config(command=cartTree.yview)
# style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview.Heading",
                font="-family {Poppins} -size 15",
                background="#581845",
                foreground="white",
                rowheight=45,
                relief="flat",
                )
style.configure("Treeview",
                font="-family {Poppins} -size 15",
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

cartTree.tag_configure('even', background="#C70039", font="-family {Poppins} -size 15")
cartTree.tag_configure('odd', background="#A50240", font="-family {Poppins} -size 15")
cartTree.tag_configure('child', background="#FF5733")

cartTree.grid(pady=20, padx=20)
cartTree.place(relx=0, rely=0, relwidth=0.8, relheight=0.6)


def fillProducts(productRecords):
    for i in productsTree.get_children():  # Clear table
        productsTree.delete(i)
    global products  # list of category objects
    auxProduct = []
    for i in productRecords:
        for j in products:
            if i[0] == j.productID:
                auxProduct.append(j)

    id_count = 0  # Parent

    for i in auxProduct:
        if id_count % 2 == 0:
            pImage = Image.open(i.image)
            productImage = ImageTk.PhotoImage(pImage)
            productsTree.insert(parent='', index="end", iid=id_count, open=True, text=i.productID,
                                  image=productImage, value=(i.image, i.productName.capitalize(), i.currentPrice),
                                  tags=('even',))
        else:
            pImage = Image.open(i.image)
            productImage = ImageTk.PhotoImage(pImage)
            productsTree.insert(parent='', index="end", iid=id_count, open=True, text=i.productID,
                                  image=productImage, value=(i.image, i.productName.capitalize(), i.currentPrice),
                                  tags=('odd',))
        id_count += 1
        if id_count > 0:
            sep = ttk.Separator(productsTree, orient='horizontal')
            sep.grid(sticky="news")


def fillCart():
    global cart  # list of category objects
    # sortRecords()
    for i in cartTree.get_children():  # Clear table
        cartTree.delete(i)
    id_count = 0  # Parent
    for i in cart:
        if id_count % 2 == 0:
            cartTree.insert(parent='', index="end", iid=id_count, open=True, text=i.productID,
                                  image=ImageTk.PhotoImage(file=i.image), value=(i.image, i.productName, i.quantity, f"{i.price} * {i.quantity} = {i.quantity * i.price}"),
                                  tags=('even',))
        else:
            cartTree.insert(parent='', index="end", iid=id_count, open=True, text=i.productID,
                                  image=ImageTk.PhotoImage(file=i.image), value=(i.image, i.productName, i.quantity, f"{i.price} * {i.quantity} = {i.quantity * i.price}"),
                                  tags=('odd',))
        id_count += 1
        if id_count > 0:
            sep = ttk.Separator(categoriesTree, orient='horizontal')
            sep.grid(sticky="news")


def selectCategory():
    if categoriesTree.selection() != ():
        selectedCategory = categories[int(categoriesTree.selection()[0])]
        countUsernames = "SELECT * FROM `product` WHERE category_id=" + "'" + selectedCategory.categoryID + "'"
        mycursor.execute(countUsernames)
        records = mycursor.fetchall()
        fillProducts(records)
    else:
        messagebox.showinfo("Invalid Selection", "Select a category first!")


def addToCart():
    global cart

    def checkDuplicate(productID):
        for x in cart:
            if x.productID == productID:
                x.quantity += 1
                return True

    if productsTree.selection() != ():
        selectedProducts = productsTree.selection()
        for row in selectedProducts:
            for product in products:
                if product.productID == productsTree.item(row)["text"]:
                    if not checkDuplicate(product.productID):
                        item = Item(currentUser.customerID, product.productID, product.currentPrice, 1, product.image, product.productName)
                        cart.append(item)
                    break

        messagebox.showinfo("Added to Cart", "Your items have successfully been added to your cart!")
        for i in productsTree.get_children():  # Clear products table
            productsTree.delete(i)
        fillCart()

    else:
        messagebox.showinfo("Invalid Selection", "Select at least one product!")


selectCategoryButton.configure(command=selectCategory)
addToCartButton.configure(command=addToCart)

root.mainloop()
