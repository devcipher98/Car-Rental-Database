import sqlite3
import csv

conn = sqlite3.connect('CarRental.db')
c = conn.cursor()

c.execute("DROP TABLE CUSTOMER")
c.execute("DROP TABLE VEHICLE")
c.execute("DROP TABLE RENTAL")
c.execute("DROP TABLE RATE")

c.execute("""
CREATE TABLE CUSTOMER(
    [CustID]    INTEGER PRIMARY KEY,
    [Name] VARCHAR(30)  NOT NULL,
    [Phone] VARCHAR(15)
);
""")
c.execute("""
CREATE TABLE VEHICLE(
    [VehicleID] VARCHAR(18) PRIMARY KEY,
    [Description]   VARCHAR(30) NOT NULL,
    [Year]  INT NOT NULL,
    [Type]  INT NOT NULL,
    [Category]  INT NOT NULL
);
""")
c.execute("""
CREATE TABLE RENTAL(
    [CustID]    INT NOT NULL,
    [VehicleID] VARCHAR(18) NOT NULL,
    [StartDate] DATE    NOT NULL,
    [OrderDate] DATE NOT NULL,
    [RentalType]    INT     NOT NULL,
    [Qty]   INT NOT NULL,
    [ReturnDate]    DATE    NOT NULL,
    [TotalAmount]   DOUBLE NOT NULL,
    [PaymentDate]   DATE,
    FOREIGN KEY(CustID) REFERENCES CUSTOMER(CustID),
    FOREIGN KEY(VehicleID) REFERENCES VEHICLE(VehicleID)
);
""")
c.execute("""
CREATE TABLE RATE(
    [Type]  INT NOT NULL,
    [Category]  INT NOT NULL,
    [Weekly]    DOUBLE NOT NULL,
    [Daily] DOUBLE NOT NULL
);
""")

with open('./entryfiles/CUSTOMER.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for x in csv_reader:
        c.execute("INSERT INTO CUSTOMER VALUES(:CustID, :Name, :Phone)",{'CustID': x[0], 'Name': x[1], 'Phone': x[2]})
with open('./entryfiles/VEHICLE.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for x in csv_reader:
        c.execute("INSERT INTO VEHICLE VALUES(:VehicleID, :Description, :Year, :Type, :Category)",{'VehicleID': x[0], 'Description': x[1], 'Year': x[2], 'Type': x[3], 'Category': x[4]})
with open('./entryfiles/RENTAL.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for x in csv_reader:
        if x[8] == 'NULL':
            c.execute("INSERT INTO RENTAL VALUES(:CustID, :VehicleID, :StartDate, :OrderDate, :RentalType, :Qty, :ReturnDate, :TotalAmount, NULL)",{'CustID': x[0], 'VehicleID': x[1], 'StartDate': x[2], 'OrderDate': x[3], 'RentalType': x[4], 'Qty': x[5], 'ReturnDate': x[6], 'TotalAmount': x[7]})
        else:
            c.execute("INSERT INTO RENTAL VALUES(:CustID, :VehicleID, :StartDate, :OrderDate, :RentalType, :Qty, :ReturnDate, :TotalAmount, :PaymentDate)",{'CustID': x[0], 'VehicleID': x[1], 'StartDate': x[2], 'OrderDate': x[3], 'RentalType': x[4], 'Qty': x[5], 'ReturnDate': x[6], 'TotalAmount': x[7], 'PaymentDate': x[8]})
with open('./entryfiles/RATE.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for x in csv_reader:
        c.execute("INSERT INTO RATE VALUES(:Type, :Category, :Weekly, :Daily)",{'Type': x[0], 'Category': x[1], 'Weekly': x[2], 'Daily': x[3]})

conn.commit()
conn.close()