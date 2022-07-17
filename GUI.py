import tkinter as tk
from tkinter import *
from tkinter.font import Font
from tkcalendar import DateEntry
from tkinter import ttk
from datetime import date
import sqlite3

#Connecting the Database to the GUI
connection = sqlite3.connect('CarRental.db')
c = connection.cursor()

#Getting the current date,formatting it.
CurrentDate = date.today()
FormatedDate = CurrentDate.strftime("%Y-%m-%d")

def window_close():
    window.destroy()


class Main_Window:
    def __init__(self, parent):
        self.parent = parent
        self.mainwindow = tk.Toplevel(self.parent)
        self.mainwindow.geometry("300x300")
        self.mainwindow.title("Car Rental System")
        MyWindow = self.mainwindow

        register_button = tk.Button(
            MyWindow, text="Register New Customer",font=("Arial", 15), width=25, command=self.open_register)
        register_button.grid(row=0, column=0)

        vehicle_button = tk.Button(MyWindow, text="Register New Vehicle",font= ("Arial", 15),width=25, command=self.open_vehicle)
        vehicle_button.grid(row=1, column=0)

        rental_button = tk.Button(MyWindow, text="Rent a car",font= ("Arial", 15),
                               width=25, command=self.open_rent)
        rental_button.grid(row=2, column=0)

        return_button = tk.Button(MyWindow, text="Return a car",font= ("Arial", 15),
                               width=25, command=self.open_return)
        return_button.grid(row=3, column=0)

        customersearch_button = tk.Button(MyWindow, text="Search customers",font= ("Arial", 15),
                                       width=25, command=self.open_customersearch)
        customersearch_button.grid(row=4, column=0)

        vehiclesearch_button = tk.Button(MyWindow, text="Search vehicles",font= ("Arial", 15),
                                      width=25, command=self.open_vehiclesearch)
        vehiclesearch_button.grid(row=5, column=0)

        MyWindow.protocol("WM_DELETE_WINDOW", window_close)
        MyWindow.mainloop()

    #This is for my first requirment. This function is called when the Register New Customer button is clicked.
    def open_register(self):
        #Closes the main window and starts the Reigster New Customer Window
        self.mainwindow.destroy()
        Register_Window(self.parent)

    #This is for my second requirment. This function is called when the Register New Vehicle button is clicked.
    def open_vehicle(self):
        #Closes the main window and starts the Reigster New Customer Window
        self.mainwindow.destroy()
        Vehicle_Window(self.parent)

    #This is for my third requirment. This function is called when the Rent a car button is clicked.
    def open_rent(self):
        self.mainwindow.destroy()
        Rent_Window(self.parent)

    #This is for my fourth requirment. This function is called when the Return a car button is clicked.
    def open_return(self):
        self.mainwindow.destroy()
        Return_Window(self.parent)

    #This is for my 5a requirment. This function is called when the Search customers button is clicked.
    def open_customersearch(self):
        self.mainwindow.destroy()
        CustomerSearch_Window(self.parent)

    #This is for my 5b requirment. This function is called when the Search Vehicles button is clicked.
    def open_vehiclesearch(self):
        self.mainwindow.destroy()
        VehicleSearch_Window(self.parent)
        pass


class Register_Window:
    #This is my window class to register a new customer.
    def __init__(self, parent):
        self.parent = parent
        self.registerwindow = tk.Toplevel(self.parent)
        self.registerwindow.geometry("300x300")
        self.registerwindow.title("Register a New Customer")
        regw = self.registerwindow

        self.user = tk.StringVar()
        self.phone = tk.StringVar()

        #Creating a name field for the Customer name and taking the input from the user.
        name_label = tk.Label(regw, text='Customer Name:',pady=18, padx=11)
        name_label.grid(column=0, row=0)
        name_entry = tk.Entry(regw, textvariable=self.user)
        name_entry.grid(row=0, column=1)
       
        #Creating a field for the phone number and taking the input from the user.
        phone_label = tk.Label(regw, text='Phone Number:', pady=18, padx=11)
        phone_label.grid(row=1, column=0)
        phone_entry = tk.Entry(regw, textvariable=self.phone)
        phone_entry.grid(row=1, column=1)

        #Creating a submit button to submit the input for the query.
        submit = tk.Button(regw, text='Submit', width=11,command=self.submit_handler)
        submit.grid(row=2, column=1)

        back_button = tk.Button(regw, text='Back', width=11, command=self.back)
        back_button.grid(row=2, column=0)
        regw.protocol("WM_DELETE_WINDOW", window_close)
        regw.mainloop()

    def back(self):
        self.registerwindow.destroy()
        Main_Window(self.parent)

    def submit_handler(self):
        newName = self.user.get()
        a = self.phone.get()
        newPhone = '('+a[0]+a[1]+a[2]+') '+a[3] + \
            a[4]+a[5]+'-'+a[6]+a[7]+a[8]+a[9]

        if not self.user.get().isnumeric():
            if self.phone.get().isnumeric() and len(self.phone.get()) == 10:
                #This is my query for Rquirement 1 of Task 2
                c.execute("INSERT INTO CUSTOMER(Name, Phone) VALUES(:newName, :newPhone)", {
                          'newName': newName, 'newPhone': newPhone})
                connection.commit()
                self.back()


class Vehicle_Window:
    #Creating a new vehicle registration.
    def __init__(self, parent):
        self.parent = parent
        self.vehiclewindow = tk.Toplevel(self.parent)
        self.vehiclewindow.geometry("300x350")
        self.vehiclewindow.title("Register New Vehicle")

        self.vehicleID = tk.StringVar()
        self.desc = tk.StringVar()
        self.year = tk.StringVar()
        self.ty = 0
        self.cat = 0

        self.type = tk.StringVar()
        type_opt = ["Compact", "Medium", "Large", "SUV", "Truck", "Van"]

        self.category = tk.StringVar()
        category_options = ["Basic", "Luxury"]

        vehiclew = self.vehiclewindow
        

        #Creating a label for the vehicle ID
        vehicle_label = tk.Label(vehiclew, text='Enter VehicleID', pady=22, padx=11)
        vehicle_label.grid(row=0, column=0)
        #Getting the input from the user.

        vehicle_entry = tk.Entry(vehiclew, textvariable=self.vehicleID)
        vehicle_entry.grid(row=0, column=1)
        
        #Creating a label for the vehicle ID
        desc_label = tk.Label(
            vehiclew, text='Enter Car Description', pady=22, padx=11)
        desc_label.grid(row=1, column=0)
        #Getting the input from the user
        desc_entry = tk.Entry(vehiclew, textvariable=self.desc)
        desc_entry.grid(row=1, column=1)
        
        #Creating a label for the Make of the car.
        year_label = tk.Label(
            vehiclew, text='Enter year of model', pady=22, padx=11)
        year_label.grid(row=3, column=0)
        year_entry = tk.Entry(vehiclew, textvariable=self.year)
        year_entry.grid(row=3, column=1)

        #Creating a label for the Type.
        type_label = tk.Label(
            vehiclew, text='Select Type', pady=22, padx=11)
        type_label.grid(row=4, column=0)
        #Getting the input from the user.
        type_menu = tk.OptionMenu(vehiclew, self.type, *type_opt)
        type_menu.grid(row=4, column=1)

        #Creating a label for the Category.

        category_label = tk.Label(
            vehiclew, text='Select Category', pady=22, padx=11)
        category_label.grid(row=2, column=0)
        category_menu = tk.OptionMenu(vehiclew, self.category, *category_options)
        category_menu.grid(row=2, column=1)

        #This is the Search button, that runs the register function on click.
        search_btn = tk.Button(
            vehiclew, text="Register", width=15, command=self.register)
        search_btn.grid(row=5, column=1)

        #This is the back button, that runs the back function on click.
        return_button = tk.Button(vehiclew, text="Back", width=15, command=self.back)
        return_button.grid(row=5, column=0)

        vehiclew.protocol("WM_DELETE_WINDOW", window_close)
        vehiclew.mainloop()

    def register(self):
        #This is my function to register a new car.
        type_opt = ["Compact", "Medium", "Large", "SUV", "Truck", "Van"]
        Category = 0
        Type = 0
        for i in range(len(type_opt)):
            if self.type.get() == type_opt[i]:
                Type = i + 1

        if self.category.get() == "Basic":
            Category = 0
        else:
            Category = 1
            #This is my second requirment query from Task 2
        c.execute("INSERT INTO VEHICLE VALUES(:VehicleID, :Description, :Year, :Type, :Category)", {'VehicleID': self.vehicleID.get(
        ), 'Description': self.desc.get(), 'Year': self.year.get(), 'Type': Type, 'Category': Category})
        connection.commit()
        self.vehiclewindow.destroy()
        Main_Window(self.parent)

    def back(self):
        self.vehiclewindow.destroy()
        Main_Window(self.parent)


class Rent_Window:
    #Creating a rent a car window
    def __init__(self, parent) -> None:
        self.parent = parent
        self.rent_window = tk.Toplevel(self.parent)
        self.rent_window.geometry("500x500")
        self.rent_window.title("Rent a car")
        rentw = self.rent_window

        self.user = tk.StringVar()
        self.dw = tk.StringVar()
        self.qty = tk.StringVar()
        self.ty = 0
        self.cat = 0
        self.startDate = ""
        self.returnDate = ""

        self.type = tk.StringVar()
        type_opt = ["Compact", "Medium", "Large", "SUV", "Truck", "Van"]

        self.category = tk.StringVar()
        category_options = ["Basic", "Luxury"]

        
        #This is for the creating of a type Table.

        type_label = tk.Label(
            rentw, text='Select Type', pady=22, padx=11)
        type_label.grid(row=0, column=0)

        #Getting input from the user.

        type_menu = tk.OptionMenu(rentw, self.type, *type_opt)
        type_menu.grid(row=0, column=1)

        #This is for creating a label for category.

        category_label = tk.Label(
            rentw, text='Select Category', pady=22, padx=11)
        category_label.grid(row=1, column=0)
        #Getting user input for the category.

        category_menu = tk.OptionMenu(rentw, self.category, *category_options)
        category_menu.grid(row=1, column=1)


        start_label = tk.Label(rentw, text='Rent start date:', pady=22, padx=11)
        start_label.grid(row=3, column=0)
        self.start_cal = DateEntry(rentw, width=13, year=2021, month=5, day=7,
                                   background='black', foreground='white', borderwidth=3)
        self.start_cal.grid(row=3, column=1)

        end_label = tk.Label(rentw, text='Return date:', pady=22, padx=11)
        end_label.grid(row=2, column=0)
        self.end_cal = DateEntry(rentw, width=13, year=2021, month=5, day=8,
                                 background='black', foreground='white', borderwidth=3)
        self.end_cal.grid(row=2, column=1)

        #This is the search button.

        search_btn = tk.Button(
            #runs the search command function.
            rentw, text="Find available cars", width=18, command=self.search)
        search_btn.grid(row=4, column=1)

        self.vehicle_selected = tk.StringVar()
        
        #This is the back button.

        back_btn = tk.Button(rentw, text="Back", width=18, command=self.back)
        back_btn.grid(row=4, column=0)

        rentw.protocol("WM_DELETE_WINDOW", window_close)
        rentw.mainloop()

    def search(self):
        self.rent_window.geometry("600x800")
        type_opt = ["Compact", "Medium", "Large", "SUV", "Truck", "Van"]

        for i in range(len(type_opt)):
            if self.type.get() == type_opt[i]:
                self.ty = i + 1

        if self.category.get() == "Basic":
            self.cat = 0
        else:
            self.cat = 1

        temp = self.start_cal.get().split('/')
        if int(temp[0]) < 10:
            temp[0] = '0' + temp[0]
        if int(temp[1]) < 10:
            temp[1] = '0' + temp[1]
        self.startDate = "20" + temp[2] + '-' + temp[0] + '-' + temp[1]

        temp2 = self.start_cal.get().split('/')
        if int(temp[0]) < 10:
            temp2[0] = '0' + temp2[0]
        if int(temp[1]) < 10:
            temp2[1] = '0' + temp2[1]
        self.returnDate = "20" + temp2[2] + '-' + temp2[0] + '-' + temp2[1]

        #This is my query for task 3. *Still working on its proper implementation it is not working yet.

        print("SELECT VEHICLE.VehicleID,VEHICLE.Description,VEHICLE.Year FROM Vehicle NATURAL JOIN RENTAL WHERE VEHICLE.Type= {Type} AND VEHICLE.Category = {Category} AND VEHICLE.VehicleID NOT IN (SELECT VehicleID FROM RENTAL WHERE (StartDate BETWEEN {startDate} AND {returnDate} OR  ReturnDate BETWEEN {startDate} AND {returnDate}))GROUP BY VehicleID").format(self.ty,self.cat,self.startDate,self.returnDate)
        #"SELECT VEHICLE.VehicleId,VEHICLE.Description,VEHICLE.Year FROM Vehicle NATURAL JOIN RENTAL WHERE VEHICLE.Type= :Type AND VEHICLE.Category=Category AND VEHICLE.VehicleId NOT IN (SELECT VehicleID FROM RENTAL WHERE (StartDate BETWEEN :StartTime AND :ReturnTime OR ReturnDate BETWEEN :StartTime AND :ReturnTime) )GROUP BY VehicleID",
        c.execute("SELECT VEHICLE.VehicleID,VEHICLE.Description,VEHICLE.Year FROM Vehicle NATURAL JOIN RENTAL WHERE VEHICLE.Type= :Type AND VEHICLE.Category = :Category AND VEHICLE.VehicleID NOT IN (SELECT VehicleID FROM RENTAL WHERE (StartDate BETWEEN :DATE(startDate) AND :DATE(returnDate) OR ReturnDate BETWEEN :DATE(startDate) AND :DATE(returnDate) )GROUP BY VehicleID", {
                  'Type': self.ty, 'Category': self.cat, 'startDate': self.startDate, 'returnDate': self.returnDate})
        vehicles = []
        for i in c.fetchall():
            vehicles.append(i[0] + " " + i[1] + " " + str(i[2]))
        
        #Create a label for rent.
        rent_label = tk.Label(
            self.rent_window, text='Select an available vehicle', pady=22, padx=11)
        rent_label.grid(row=5, column=0)
        #Getting ann input from the user for the car.
        rent_menu = tk.OptionMenu(
            self.rent_window, self.vehicle_selected, *vehicles)
        rent_menu.grid(row=5, column=1)

        #Label for the custommer ID
        ID_label = tk.Label(
            self.rent_window, text='Customer ID:', pady=22, padx=11)
        ID_label.grid(row=7, column=0)
        #Getting the input from the user for their id.
        name_entry = tk.Entry(self.rent_window, textvariable=self.user)
        name_entry.grid(row=7, column=1)
        
        #Label for the selection of rental type.
        dw_label = tk.Label(
            self.rent_window, text='Daily(1) or Weekly(7):', pady=22, padx=11)
        dw_label.grid(row=6, column=0)
        #Getting input from the user for their rental type.
        dw_entry = tk.Entry(self.rent_window, textvariable=self.dw)
        dw_entry.grid(row=6, column=1)

        #Label for the number of days and weeks.
        que_label = tk.Label(
            self.rent_window, text='How many days/weeks:', pady=22, padx=12)
        que_label.grid(row=8, column=0)
        #Getting input from the user for the days and the weeks.
        que_entry = tk.Entry(self.rent_window, textvariable=self.qty)
        que_entry.grid(row=8, column=1)

        #Creating a button to pay later.

        paylater_btn = tk.Button(
            self.rent_window, text="Pay Later", width=17, command=self.payLater)
        paylater_btn.grid(row=9, column=1)

        #Creating a pay now button.
        paynow_btn = tk.Button(
            self.rent_window, text="Pay Now", width=17, command=self.payNow)
        paynow_btn.grid(row=9, column=0)
        
    #These are my queries for Implementation 3 as well.
    def payNow(self):
        vID = self.vehicle_selected.get().split(' ')[0]
        c.execute("INSERT INTO RENTAL VALUES(:CustID, :VehicleID, :StartDate, :OrderDate, :RentalType, :Qty, :ReturnDate, :TotalAmount, :PaymentDate)", {'CustID': int(self.user.get(
        )), 'VehicleID': vID, 'StartDate': self.startDate, 'OrderDate': FormatedDate, 'RentalType': int(self.dw.get()), 'Qty': int(self.qty.get()), 'ReturnDate': self.returnDate, 'TotalAmount': 90, 'PaymentDate': FormatedDate})
        connection.commit()
        self.back()

    def payLater(self):
        vID = self.vehicle_selected.get().split(' ')[0]
        c.execute("INSERT INTO RENTAL VALUES(:CustID, :VehicleID, :StartDate, :OrderDate, :RentalType, :Qty, :ReturnDate, :TotalAmount, NULL)", {'CustID': int(
            self.user.get()), 'VehicleID': vID, 'StartDate': self.startDate, 'OrderDate': FormatedDate, 'RentalType': int(self.dw.get()), 'Qty': int(self.qty.get()), 'ReturnDate': self.returnDate, 'TotalAmount':90})
        connection.commit()
        self.back()

    def back(self):
        self.rent_window.destroy()
        Main_Window(self.parent)


class Return_Window:
    #Creating a return a car window.

    def __init__(self, parent):
        self.parent = parent
        self.return_window = tk.Toplevel(self.parent)
        self.return_window.geometry("400x400")
        self.return_window.title("Return a car")
        returnw = self.return_window


        self.user_name = tk.StringVar()
        self.vehicle_id = tk.StringVar()

        #Creating a label for the return date.
        return_label = tk.Label(returnw, text='Return date:', pady=22, padx=11)
        return_label.grid(row=0, column=0)
        
        #Getting user input for return  date.
        self.return_cal = DateEntry(returnw, width=12, year=2021, month=5, day=4,
                                    background='black', foreground='white', borderwidth=2)
        self.return_cal.grid(row=0, column=1)

        #Creating a label for the name
        name_label = tk.Label(returnw, text='Enter your name:', pady=22, padx=11)
        name_label.grid(row=1, column=0)
        #Taking user input for customer name.
        name_entry = tk.Entry(returnw, textvariable=self.user_name)
        name_entry.grid(row=1, column=1)


        #Creating a label for the vehicle ID
        vehicle_label = tk.Label(
            returnw, text='Enter Vehicle ID:', pady=22, padx=11)
        vehicle_label.grid(row=2, column=0)
        #Getting entry for the Vehicle ID
        vehicle_entry = tk.Entry(returnw, textvariable=self.vehicle_id)
        vehicle_entry.grid(row=2, column=1)

        search_btn = tk.Button(
            returnw, text="Search", width=18, command=self.search)
        search_btn.grid(row=3, column=1)

        back_btn = tk.Button(
            returnw, text="Back", width=18, command=self.back)
        back_btn.grid(row=3, column=0)

        returnw.protocol("WM_DELETE_WINDOW", window_close)
        returnw.mainloop()

    def back(self):
        self.return_window.destroy()
        Main_Window(self.parent)

    def search(self):

        temp = self.return_cal.get().split('/')
        if int(temp[0]) < 10:
            temp[0] = '0' + temp[0]
        if int(temp[1]) < 10:
            temp[1] = '0' + temp[1]
        returnDate = "20" + temp[2] + '-' + temp[0] + '-' + temp[1]
        #This is my Implentation 4 for task 2
        c.execute("SELECT RENTAL.TotalAmount FROM RENTAL, CUSTOMER WHERE CUSTOMER.Name = :Name AND CUSTOMER.CustID = RENTAL.CustID AND RENTAL.VehicleID = :VehicleID AND RENTAL.ReturnDate == DATE(:ReturnDate)", {'Name': self.user_name.get(), 'VehicleID': self.vehicle_id.get(), 'ReturnDate': returnDate})
        balance = c.fetchall()
        payment = '$'+str("{:.2f}".format(balance[0]))
        pay_label = tk.Label(self.return_window, text='Payment Due:', pady=22, padx=11)
        pay_label.grid(row=4, column=0)
        pay = tk.Label(self.return_window, text=payment, pady=22, padx=11)
        pay.grid(row=4, column=1)
        pay_btn = tk.Button(
            self.return_window, text="Pay", width=18, command=self.pay)
        pay_btn.grid(row=5, column=1)

#The function for the payment.
    def pay(self):
        temp = self.return_cal.get().split('/')
        if int(temp[0]) < 10:
            temp[0] = '0' + temp[0]
        if int(temp[1]) < 10:
            temp[1] = '0' + temp[1]
        returnDate = "20" + temp[2] + '-' + temp[0] + '-' + temp[1]
        #Another query  for Implentation 4 of task 2
        c.execute("UPDATE RENTAL SET PaymentDate = DATE(:payDate) WHERE VehicleID = :VehicleID AND ReturnDate == DATE(:ReturnDate)", {'VehicleID': self.vehicle_id.get(), 'ReturnDate': returnDate, 'payDate': FormatedDate})
        connection.commit()
        self.back()


class CustomerSearch_Window:
    # creating a customer Search Window.
    def __init__(self, parent):
        self.parent = parent
        self.customersearch_window = tk.Toplevel(self.parent)
        self.customersearch_window.geometry("800x800")
        self.customersearch_window.title("Search for a customer")
        csw = self.customersearch_window

        self.customerID = tk.StringVar()
        self.customer_name = tk.StringVar()

        customerID_label = tk.Label(
            csw, text='Enter customer ID', pady=20, padx=10)
        customerID_label.grid(row=0, column=0)
        customerID_entry = tk.Entry(csw, textvariable=self.customerID)
        customerID_entry.grid(row=0, column=1)

        customerName_label = tk.Label(
            csw, text='Enter customer name', pady=20, padx=10)
        customerName_label.grid(row=1, column=0)
        customerName_entry = tk.Entry(
            csw, textvariable=self.customer_name)
        customerName_entry.grid(row=1, column=1)

        back_btn = tk.Button(csw, text="Back", width=15, command=self.back)
        back_btn.grid(row=2, column=0)

        search_btn = tk.Button(csw, text="Search",
                               width=15, command=self.search)
        search_btn.grid(row=2, column=1)

        csw.protocol("WM_DELETE_WINDOW", window_close)
        csw.mainloop()

    def search(self):
       #These are my queries for Implementation 5 of task 2
        if len(self.customerID.get()) == 0:
            c.execute("SELECT rentalInfo.CustomerID, rentalInfo.CustomerName, SUM(rentalInfo.OrderAmount) FROM rentalInfo WHERE rentalInfo.CustomerName LIKE :Name GROUP BY rentalInfo.CustomerID", {
                    'Name': '%'+self.customer_name.get()+'%'})
        elif len(self.customer_name.get()) == 0:
            c.execute("SELECT rentalInfo.CustomerID,rentalInfo.CustomerName, SUM(rentalInfo.OrderAmount) FROM rentalInfo WHERE rentalInfo.CustomerID = :ID GROUP BY rentalInfo.CustomerID", {
                    'ID': self.customerID.get()})
        else:
            c.execute("SELECT rentalInfo.CustomerID, rentalInfo.CustomerName, SUM(rentalInfo.OrderAmount) FROM rentalInfo WHERE rentalInfo.CustomerName LIKE :Name AND rentalInfo.CustomerID = :ID GROUP BY rentalInfo.CustomerID", {
                    'Name': '%'+self.customer_name.get()+'%', 'ID': self.customerID.get()})
        info = c.fetchall()

        for i in range(len(info)):
            x = list(info[i])
            if x[2] is None:
                x[2] = '$0.00'
            else:
                x[2] = '$'+str("{:.2f}".format(x[2]))
            info[i] = tuple(x)

        customer_table = ttk.Treeview(self.customersearch_window, columns=(
            "Customer ID", "Name", "Remaining Balance"), show="headings")

        customer_table.insert("", "end", values=["Customer ID", "Name", "Remaining Balance"])
        for i in range(len(info)):
            customer_table.insert("", "end", values=info[i])
        customer_table.grid(row=3, column=0)
        pass

    def back(self):
        self.customersearch_window.destroy()
        Main_Window(self.parent)


class VehicleSearch_Window:
    # creating a Vehicle Search Window.
    def __init__(self, parent):
        self.parent = parent
        self.vehiclesearch_window = tk.Toplevel(self.parent)
        self.vehiclesearch_window.geometry("800x800")
        self.vehiclesearch_window.title("Search for a Vehicle")
        vsw = self.vehiclesearch_window

        
        #Creating a variable to store the vin of the car.
        self.VIN = tk.StringVar()
        #Creating a label for user input.
        VIN_label = tk.Label(vsw, text='Enter VIN',font= ("Arial", 15),pady=18, padx=11)
        VIN_label.grid(row=0, column=0)
        #Storing the data entry for VIN. This step is repeated for the vehicle description.
        VIN_entry = tk.Entry(vsw, textvariable=self.VIN)
        VIN_entry.grid(row=0, column=1)

        self.desc = tk.StringVar()
        desc_label = tk.Label(
            vsw, text='Enter vehicle description',font= ("Arial", 15), pady=18, padx=11)
        desc_label.grid(row=1, column=0)
        vehicleName_entry = tk.Entry(
            vsw, textvariable=self.desc)
        vehicleName_entry.grid(row=1, column=1)

        back_btn = tk.Button(vsw, text="Back", width=15, command=self.back)
        back_btn.grid(row=2, column=0)

        search_btn = tk.Button(vsw, text="Search",
                               width=15, command=self.search)
        search_btn.grid(row=2, column=2)

        vsw.protocol("WM_DELETE_WINDOW", window_close)
        vsw.mainloop()

    def search(self):
        #These are my queries for the 5th implentation of Task 2.
        if len(self.VIN.get()) == 0:
            c.execute("SELECT rentalInfo.VIN, rentalInfo.Vehicle, RATEVIEW.Daily FROM rentalInfo, RATEVIEW WHERE rentalInfo.Type = RATEVIEW.Type AND rentalInfo.Category = RATEVIEW.Category AND rentalInfo.vehicle LIKE :Description", {
                    'Description': '%'+self.desc.get()+'%'})
        elif len(self.desc.get()) == 0:
            c.execute("SELECT rentalInfo.VIN, rentalInfo.Vehicle, RATEVIEW.Daily FROM rentalInfo, RATEVIEW WHERE rentalInfo.Type = RATEVIEW.Type AND rentalInfo.Category = RATEVIEW.Category AND rentalInfo.VIN = :VIN", {
                    'VIN': self.VIN.get()})
        else:
            c.execute("SELECT rentalInfo.VIN, rentalInfo.Vehicle, RATEVIEW.Daily FROM rentalInfo, RATEVIEW WHERE rentalInfo.Type = RATEVIEW.Type AND rentalInfo.Category = RATEVIEW.Category AND rentalInfo.Vehicle LIKE :Description AND rentalInfo.VIN = :VIN", {
                    'Description': '%'+self.desc.get()+'%', 'VIN': self.VIN.get()})
        info = c.fetchall()
        vehicle_table = ttk.Treeview(self.vehiclesearch_window, columns=(
            "VIN", "Vehicle Description", "Average Daily Prices"), show="headings")

        for i in range(len(info)):
            x = list(info[i])
            x[2] = '$'+str("{:.2f}".format(x[2]))
            info[i] = tuple(x)

        vehicle_table.insert("", "end", values=["VIN", "Vehicle Description", "Average Daily Prices"])
        for i in range(len(info)):
            vehicle_table.insert("", "end", values=info[i])
        vehicle_table.grid(row=3, column=0)
        pass

    def back(self):
        self.vehiclesearch_window.destroy()
        Main_Window(self.parent)


window = tk.Tk()
window.withdraw()
Main_Window(window)
window.mainloop()
connection.close()
