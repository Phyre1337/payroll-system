import time
import os
import csv
import datetime
import calendar
from getpass import getpass
from sys import platform
#Importing all required libraries

global dated
#Globalizing dated for later use with the calendar/datetime library

class day_of_week:
    my_date = datetime.date.today()
    dated = calendar.day_name[(my_date.weekday())]
class actual_date:
    datetime.date.today()
#Creating classes to define datetime/calendar properties

#Making function to enter hours/view pay sheets
def enter_Hours():
    #Command to clear console at start of the function
    if platform == "linux" or platform == "linux2":
        # linux
        os.system('clear')
    elif platform == "darwin":
        # OS X
        os.system('clear')
    elif platform == "win32":
        # Windows...
        os.system('cls')
    #Making function to enter hours
    def actualHours():
        userid = input("What is your employee ID? ")
        #getting user/employee ID
        if platform == "linux" or platform == "linux2":
            # linux
            os.system('clear')
        elif platform == "darwin":
        # OS X
            os.system('clear')
        elif platform == "win32":
        # Windows...
            os.system('cls')
        print("Hello user #{}. Today is {}. Would you like to enter hours for today?".format(userid, day_of_week.dated))
        print("Y or N")
        answer = input("y for yes n for no ==> ")
        #Asking if they want to enter hours for today or another day
        
        #Making function to write to csv file
        def write_to_csv():
            hours_worked = input("How many hours have you worked? ")
            #Asking to input into the csv file
            title = "Time_Cards/{}.csv".format(userid)
            timesheet = open(title, mode = 'a+')
            #Writing into csv file with the name being the userid, if file not created already, make it
            time_entry = csv.writer(timesheet, delimiter = ',')
            #Delimiter is the seperator in between text
            time_entry.writerow([userid, date_used, hours_worked])
            timesheet.close()
            #Writing into csv file and closing it
            enter_Hours()
        
        #making if statements depending on whether user wants to enter hours for that day or not
        if answer == "y":
            date_used = day_of_week.dated
            write_to_csv()
        
        elif answer == "n":
            date_used = input("Enter day ==> ")
            #Asks which day you want to enter hours for
            write_to_csv()
        
        else:
            actualHours()
            #restart question if it couldn't detect what you said
    
    #Making time card function
    def timeCard():
        if platform == "linux" or platform == "linux2":
            # linux
            os.system('clear')
        elif platform == "darwin":
            # OS X
            os.system('clear')
        elif platform == "win32":
            # Windows...
            os.system('cls')
        userid = input("What is your employee ID? ")
        title = "Time_Cards/{}.csv".format(userid)
        
        total_hours = 0.0
        #Defining total hours to do math later
        
        time_Card = open(title)
        time_Card_Reader = csv.reader(time_Card)
        print("\n\n")
        #Reading from csv file of userid
        
        #Reading every line and printing them
        for item in time_Card_Reader:
            print("On {} you worked for {} hours".format(item[1], item[2]))
            total_hours = total_hours + float(item[2])
            print("\n\n     You worked for a total of {} hours.".format(total_hours))
        #If time is over 40 hours, show overtime also
        if total_hours > 40:
            over_Hours = total_hours - 40
            print("\n You have worked a total of {} hours of overtime.".format(over_Hours))
        input("Press any key to return")
        enter_Hours()
            
    #Asking whether you want to enter hours or view time cards
    print("Enter hours, view time cards")
    print("Press 1 to enter hours.")
    print("Press 2 to view time cards.")
    print("\n")
    print("Press x to exit to main menu.")
    hoursChoice = input("\nEnter your choice here... ")
    if hoursChoice == "1":
        if platform == "linux" or platform == "linux2":
            # linux
            os.system('clear')
        elif platform == "darwin":
            # OS X
            os.system('clear')
        elif platform == "win32":
            # Windows...
            os.system('cls')
        actualHours()
    elif hoursChoice == "2":
        if platform == "linux" or platform == "linux2":
            # linux
            os.system('clear')
        elif platform == "darwin":
            # OS X
            os.system('clear')
        elif platform == "win32":
            # Windows...
            os.system('cls')
        timeCard()
    elif hoursChoice == "x" or "X":
        mainMenu()
    else:
        enter_Hours()
    
#Defining function to edit employees
def editEmp():
    if platform == "linux" or platform == "linux2":
        # linux
        os.system('clear')
    elif platform == "darwin":
        # OS X
        os.system('clear')
    elif platform == "win32":
        # Windows...
        os.system('cls')
    
    def AdminPass(): #Creating function to type in admin password before being allowed to proceed
        pass_file = open("AdminPassword/Admin.txt", "r") #Opening .txt file with password in it
        print("\n")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("xx                      xx")
        print("xx     ENTER ADMIN      xx")
        print("xx      PASSWORD        xx")
        print("xx                      xx")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("\n")
        print("Type x to go back to main menu.")
        print("\n")
        user_Password = getpass("==> ") #Where user types in password, doesn't show in terminal
        for pword in pass_file: #Looks at line in .txt file for password
            if pword.rstrip() == user_Password: #Checks if entered password is the same
                if platform == "linux" or platform == "linux2":
                    # linux
                    os.system('clear')
                elif platform == "darwin":
                    # OS X
                    os.system('clear')
                elif platform == "win32":
                    # Windows...
                    os.system('cls')
                continue #Continues to the next function called if password is correct
            elif user_Password == ("x" or "X"):
                if platform == "linux" or platform == "linux2":
                    # linux
                    os.system('clear')
                elif platform == "darwin":
                    # OS X
                    os.system('clear')
                elif platform == "win32":
                    # Windows...
                    os.system('cls')
                mainMenu()
            else:
                AdminPass() #Restarts password function if wrong
    
    def new_Emp(): #Function to add new employee after admin password function
        print("New employee")
        #Empty lists to write inputted values to .csv later on
        emp_Personal = []
        emp_Financial = []
        #Asking for all info about employee and appending to the two lists above
        new_id = input("Employee ID ==> ")
        emp_Personal.append(new_id)
        emp_Financial.append(new_id)
        
        new_Last = input("Last name ==> ")
        emp_Personal.append(new_Last)
        
        new_First = input("First name ==> ")
        emp_Personal.append(new_First)
        
        new_DOB = input("Birth date ==> ")
        emp_Personal.append(new_DOB)
        
        new_Gender = input("Sex [M, F] ==> ")
        emp_Personal.append(new_Gender)
        
        new_Job = input("Current Job/Position ==> ")
        emp_Personal.append(new_Job)
        emp_Financial.append(new_Job)
        
        new_Pay = float(input("Payrate ==> "))
        emp_Financial.append(new_Pay)
        
        new_Depend = input("Does the employee have dependents? [y or n] ==> ")
        emp_Financial.append(new_Depend)
        
        new_Insur = input("Does the employee have insurance? [y or n] ==> ")
        emp_Financial.append(new_Insur)
        
    
        def confirm_New(): #Function to double-check info above with user if it is correct
            if platform == "linux" or platform == "linux2":
                # linux
                os.system('clear')
            elif platform == "darwin":
                # OS X
                os.system('clear')
            elif platform == "win32":
                # Windows...
                os.system('cls')
            print("Here is what you have entered.") #Prints all info to repeat to user 
            print("ID#:           {}\n".format(new_id))
            print("Last name:     {}\n".format(new_Last))
            print("First name:    {}\n".format(new_First))
            print("Date of birth: {}\n".format(new_DOB))
            print("Sex:           {}\n".format(new_Gender))
            print("Occupation:    {}\n".format(new_Job))
            print("Payrate:       {}\n".format(new_Pay))
            print("Dependents:    {}\n".format(new_Depend))
            print("Insurance:     {}\n".format(new_Insur))
            
            employee_Confirm = input("Is this information correct? [y = yes, n = no] ==> ")
            #If statement based on user input whether info needs to be re-typed or can be wrote to .csv already
            if employee_Confirm == "y":
                with open("employee_personal/employee_record.csv", mode = "a+")as add_Personal: #Opens personal .csv and assigns to variable
                    rec_adder = csv.writer(add_Personal, delimiter=",") #Writes info to .csv
                    rec_adder.writerow(emp_Personal)
                    add_Personal.close() #Closes .csv when done
                
                with open("employee_financial/financial_record.csv", mode= "a+") as add_Financial: #Opens financial .csv and assigns to variable
                    rec_adder = csv.writer(add_Financial, delimiter=",") #Writes info to .csv
                    rec_adder.writerow(emp_Financial)
                    add_Financial.close() #Closes .csv when done
                    
                editEmp() #Returns to adding employees if you want to add more
            
            elif employee_Confirm == "n":
                new_Emp() #Returns to edit employees function to start again
            
            else:
                confirm_New() #Repeats info again if you didn't understand what to type
        #Calling all the functions in order
        confirm_New()
    AdminPass()
    new_Emp()
#Defining option #3
def reports():
    print("You've chosen to view reports.")
    time.sleep(1)
    print("")
    mainMenu()
    #Defining option #4
def payrollFunc():
    total_file = open("payroll.csv")
    record = csv.reader(total_file)

    for item in record:
        if item[0] == ("Serial Number"):
            continue
        else:
            serial = item[0]
            name = item[2] + "" + item[1]
            payrate = item[3]
            time = item[4]
            insurance = item[5]
            if int(time) <= 40:
                gross = int(payrate) * int(time)
                fed = round((float(gross) * 0.0968), 2)
                state = round((float(gross) * 0.374), 2)
                ss = round((float(gross) * 0.0714), 2)
                try:
                    f = open(name + ".txt", "w+")
                    f.write("Serial Number -        " + serial)
                    f.write("\nPayrate -            $" + payrate)
                    f.write("\n\nHours worked -       " + time)
                    f.write("\n\nRegular Hrs. -       " + time)
                    f.write("\nOvertime Hrs.@ $0    0     $0")
                    f.write("\n\nTotal Pay - $" + str(gross))
                    f.write("\n\nFederal Income Tax:  $" + str(fed))
                    f.write("\nState Income Tax:    $" + str(state))
                    f.write("\nFICA:                $" + str(ss))
                    if insurance == "Y":
                        finalpay = round(float(gross - fed - state - ss - 39.40))
                        f.write("\n\nHealth Insurance:    $39.40")
                        f.write("\n\nTotal Pay to " + (item[2] + " " + item[1]) + ": $" + str(finalpay))
                    elif insurance == "N":
                        finalpay = round(float(gross - fed - state - ss), 2)
                        f.write("\n\nHealth Insurance:    $0")
                        f.write("\n\nTotal Pay to " + (item[2] + " " + item[1]) + ": $" + str(finalpay))
                finally:
                    f.close()
            elif int(time) > 40:
                ot = int(time) - 40
                otpay = int(payrate) * 1.5
                otgross = ot * otpay
                normpay = 40 * int(payrate)
                gross = otgross + normpay
                fed = round((float(gross) * 0.0968), 2)
                state = round((float(gross) * 0.374), 2)
                ss = round((float(gross) * 0.0714), 2)
                try:
                    f = open(name + ".txt", "w+")
                    f.write("Serial Number -        " + serial)
                    f.write("\nPayrate -            $" + payrate)
                    f.write("\n\nHours worked -       " + time)
                    f.write("\n\nRegular Hrs. -       " + time)
                    f.write("\nOvertime Hrs.@ $" + str(otpay) + "    " + str(ot) + "     $" + str(otgross))
                    f.write("\n\nTotal Pay - $" + str(gross))
                    f.write("\n\nFederal Income Tax:  $" + str(fed))
                    f.write("\nState Income Tax:    $" + str(state))
                    f.write("\nFICA:                $" + str(ss))
                    if insurance == "Y":
                        finalpay = round(float(gross - fed - state - ss - 39.40))
                        f.write("\n\nHealth Insurance:    $39.40")
                        f.write("\n\nTotal Pay to " + (item[2] + " " + item[1]) + ": $" + str(finalpay))
                    elif insurance == "N":
                        finalpay = round(float(gross - fed - state - ss), 2)
                        f.write("\n\nHealth Insurance:    $0")
                        f.write("\n\nTotal Pay to " + (item[2] + " " + item[1]) + ": $" + str(finalpay))
                finally:
                    f.close()
    #Making start function at the beginning of program
def mainMenu():
    if platform == "linux" or platform == "linux2":
        # linux
        os.system('clear')
    elif platform == "darwin":
        # OS X
        os.system('clear')
    elif platform == "win32":
        # Windows...
        os.system('cls')
    print("What task would you like to perform today?")
    print("1. Enter hours")
    print("2. Edit employees")
    print("3. Payroll") 
    print("x. Exit")
    print("Enter in your option below...")
    print("")
    choice = input(">>> ")
    #Choosing which option you want the program to run
    if choice == '1':
        enter_Hours()
    elif choice == '2':
        editEmp()
    elif choice == '3':
        payrollFunc()
    elif choice == 'x':
        os.system('clear')
    else:
        mainMenu()
#Starting the program.
mainMenu()