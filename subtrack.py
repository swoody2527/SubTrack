
from ast import main
from tkinter import *
from tokenize import Number
from prettytable import PrettyTable
import sqlite3
import re
from datetime import date, timedelta, datetime
from dateutil.relativedelta import relativedelta
import sys

CONN = sqlite3.connect('subs.db')
DB = CONN.cursor()

class Sub:
    def __init__(self, name, price, start_date, renewal):
        self.name = name
        self.price = price
        self.start_date = start_date
        self.renewal = renewal
    
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        try:
            price = float(price)
        except TypeError:
            raise TypeError("Invalid Price Format: e.g 6.99")
        self._price = price

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, date):
        if not re.search(r"^\d{4}(\-)(((0)[0-9])|((1)[0-2]))(\-)([0-2][0-9]|(3)[0-1])$", str(date)):
            raise ValueError(f"Invalid Date Format - {str(date)}")
        self._start_date = date

    @property
    def renewal(self):
        return self._renewal

    @renewal.setter
    def renewal(self, renewal):
        try:
            renewal = int(renewal)
        except ValueError:
            raise ValueError("Invalid renewal format. Input no. months")
        self._renewal = renewal
    

def main():
    action = input("What would you like to do?: ").lower()
    if action == "view":
        print(view())
        main()
    elif action == "add":
        sub = add()
        DB.execute("INSERT INTO subs (name, price, start_date, renewal, next_charge) VALUES (?,?,?,?,?)", 
        (sub.name, sub.price, sub.start_date, sub.renewal, calc_next(sub.start_date, sub.renewal)))
        CONN.commit()
        main()
    elif action == "delete":
        to_delete = delete()
        DB.execute("DELETE FROM subs WHERE name = (?)", (to_delete,))
        CONN.commit()
        main()
    elif action == "exit":
        sys.exit("### Thank you for using SubTrack ###")
    else:
        print("Invalid Command: use 'view', 'add' or 'delete'")

# Greets user upon startup
def greet():
    print("### Welcome to SubTrack. A program to help track your running subscriptions. ###")
    print("### Enter 'view' to see current subscriptions and 'delete' or 'add' to make changes ###")

# Prints a table of all current subscription info.
def view():
    DB.execute("SELECT name, price, start_date, renewal, next_charge FROM subs")
    subs = DB.fetchall()
    table = PrettyTable()
    table.field_names = ["Name", "Price", "Start Date", "Renewal(Months)", "Next Charge"]
    for row in subs:
        row = list(row)
        row[4] = format_view_dates(row[4])
        row[2] = format_view_dates(row[2])
        table.add_row(row)
    return table

def get_subs():
    DB.execute("SELECT name, price, start_date, renewal, next_charge FROM subs")
    subs = DB.fetchall()
    return subs


# Takes multiple inputs to create new subscriptions entry
def add(name=None, price=None, start_date=None, renewal=None):
    if name == None and price == None and start_date == None and renewal == None:
        name = input("Subscription Name: ")
        price = input("Price: ")
        start_date = input("Start Date(dd/mm/yyyy) or (d/m/yyyy): ")
        renewal = input("Renewal Period(months): ")
    start_date = datetime.strptime(start_date, '%d/%m/%Y').date()
    sub = Sub(name, price, start_date, renewal)
    print(f"{sub.name} subscription added at {sub.price} charged every {sub.renewal} month(s)")
    return sub

def insert(sub):
    DB.execute("INSERT INTO subs (name, price, start_date, renewal, next_charge) VALUES (?,?,?,?,?)", 
    (sub.name, sub.price, sub.start_date, sub.renewal, calc_next(sub.start_date, sub.renewal)))
    CONN.commit()
    check_over()

def dateobj(date):
    start_date = datetime.strptime(date, '%d/%m/%Y').date()
    return start_date


# Displays a table of subscriptions. Returns name to delete inputted by user.
def delete(name=None):
    DB.execute("SELECT name, price, start_date, renewal, next_charge FROM subs")
    subs = DB.fetchall()
    table = PrettyTable()
    print(subs)
    table.field_names = ["Name", "Price", "Start_Date", "Renewal", "Next_Charge"]
    for row in subs:
        row = list(row)
        row[4] = format_view_dates(row[4])
        row[2] = format_view_dates(row[2])
        table.add_row(row)
    table.add_autoindex("Index")
    print(table)
    if name == None:
        del_name = input("Subscription to delete(name): ")
    else:
        del_name = name
    if del_name in (item[0] for item in subs):
        check = input(f"Are you sure you want to delete {del_name}? y/n: ").lower()
        if check == "yes" or check == "y":
            print(f"{del_name} deleted from subscriptions.")
            return del_name
        else:
            print("No changes made")
            return main()
    else:
        print(f"No subscription named '{del_name}' found.")
        return main()

def delete2(name):
    DB.execute("DELETE FROM subs WHERE name = (?)", (name,))
    CONN.commit()
        

# Caculates the next charge date for a subscription 
def calc_next(date, renewal):
    renewal = int(renewal)
    new_date = date + relativedelta(months=renewal)
    print(new_date)
    return new_date

# Checks any subscriptions to see if they need charged today, caculates next if so.
def check_over():
    DB.execute("SELECT id, name, renewal, next_charge FROM subs")
    subs = DB.fetchall()
    for row in subs:
        row = list(row)
        db_date = datetime.strptime(row[3], '%Y-%m-%d').date()
        if db_date <= datetime.today().date():
            db_month = str(db_date).split("-")[1]
            today_month = str(datetime.today().date()).split("-")[1]
            month_change = int(today_month) - int(db_month)       
            if db_month == today_month:
                new_date = calc_next(db_date, row[2])
                DB.execute("UPDATE subs SET next_charge = (?) WHERE id = (?)", (new_date, row[0]))
            else:
                new_date = calc_next(db_date, month_change)
                DB.execute("UPDATE subs SET next_charge = (?) WHERE id = (?)", (new_date, row[0]))
    CONN.commit()

# Formats dates in yyyy/mm/dd format for better readability
def format_view_dates(date):
    year, month, day = str(date).split("-")
    try:
        int(year)
        int(month)
        int(day)
    except ValueError:
        raise ValueError("Invalid Date")
    return f"{day}/{month}/{year}"

if __name__=="__main__":
    greet()
    check_over()
    main()