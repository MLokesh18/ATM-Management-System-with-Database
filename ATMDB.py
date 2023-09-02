import mysql.connector
from tabulate import tabulate

#from main import select

con = mysql.connector.connect(host="localhost", user="root", password="", database="atmdb")
def Create_Account(C_id, Name, Pin, Balance, Mobile_no, Account_type):
    res = con.cursor()
    sql = "insert into account (C_id, Name, Pin, Balance,Mobile_no,Account_type) values (%s,%s,%s,%s,%s,%s)"
    res.execute(sql, (C_id, Name, Pin, Balance, Mobile_no, Account_type))
    con.commit()
    print("\n")
    print("Record Inserted Successfully")
def select():
    res = con.cursor()
    sql = "SELECT * from account order by c_id asc"
    res.execute(sql)
    result = res.fetchall()
    print("\n")
    print(tabulate(result, headers=["C_id", "Name", "Pin", "Balance", "Mobile_no", "Account_type"]))

def update():
        print("1.C_id")
        print("2.Name")
        print("3.Pin")

        print("4.Mobile_no")
        print("5.Account_type")

        option = int(input("\nWhich field you want to update?:"))
        if option == 1:
            C_id = input("Enter Your C_id:")
            Name = input("Enter Your Name:")
            cur = con.cursor()
            sql = "UPDATE account set C_id=%s where Name=%s"
            cur.execute(sql, (Name, C_id))
            con.commit()
            select()
            print("\n")
            print("Update Successfully")
        elif option == 2:
            C_id = input("Enter Your C_id:")
            Name = input("Enter Your Name:")
            cur = con.cursor()
            sql = "UPDATE account set Name=%s where C_id=%s"
            cur.execute(sql, (Name, C_id))
            con.commit()
            select()
            print("\n")
            print("Update Successfully")
        elif option == 3:
            C_id = input("Enter Your C_id:")
            Pin = input("Enter Your pin:")
            cur = con.cursor()
            sql = "UPDATE account set Pin=%s where C_id=%s"
            cur.execute(sql, (Pin, C_id))
            con.commit()
            select()
            print("\n")
            print("Update Successfully")
        elif option == 4:
            C_id = input("Enter Your C_id")
            Mobile_no = input("Enter Your Mobile Number:")
            cur = con.cursor()
            sql = "UPDATE account set Mobile_no=%s where C_id=%s"
            cur.execute(sql, (Mobile_no, C_id))
            con.commit()
            select()
            print("\n")
            print("Update Successfully")
        elif option == 5:
            C_id = input("Enter Your C_id:")
            Account_type = input("Enter Your Account_type:")
            cur = con.cursor()
            sql = "UPDATE account set Account_type=%s where C_id=%s"
            cur.execute(sql, (Account_type, C_id))
            con.commit()
            select()
            print("\n")
            print("Update Successfully")

        else:
            print("Invalid")

def delete():
    C_id = input("Enter Your ID:")
    res = con.cursor()
    sql = "delete from account where C_id=%s"
    res.execute(sql, (C_id,))
    con.commit()
    print("\n")
    print("Record Deleted Successfully...!!!")

def check_balance():
    Pin =input("Enter Your Pin ")

    res = con.cursor()

    sql = "SELECT balance from account where Pin=%s"

    res.execute(sql, (Pin,))
    result = res.fetchone()

    print("\n")
    print("Your Balance is", result[0])
    # print(tabulate(result, headers=["C_id",  "Balance"]))



def withdraw():
    Pin = input("Enter Your Pin ")

    res = con.cursor()
    sql = "SELECT balance from account where Pin=%s"
    res.execute(sql,(Pin,))
    result = res.fetchone()
    Amount = int(input("Enter the withdrawn amount "))

    A=(result[0])
    if A<Amount:
        print("Enter the amount within ",A)
        withdraw()
    else:

        B=A-Amount

        sql="update account set balance=%s where Pin=%s"
        res.execute(sql,(B,Pin))
        con.commit()

        print(B)
        print("WithDrawn Successful")




def deposit():
    C_id = input("Enter Your Id ")
    Amount = int(input("Enter the Deposit amount "))
    res = con.cursor()
    sql = "SELECT balance from account where C_id=%s"
    res.execute(sql, (C_id,))

    result = res.fetchone()

    A = (result[0])
    B = A + Amount
    sql = "update account set balance = %s where C_id=%s"
    res.execute(sql, (B,C_id))
    #res.fetchone()

    print("your balance",Amount ,"is successfully deposited","Your current Balance is ",B)
    con.commit()
    print(6)
    #print(Balance)
    print("Deposit Successful")


while True:
        print("1.Create Account")
        print("2.Select")
        print("3.Update Details")
        print("4.Delete")
        print("5.Check Balance")
        print("6.Withdraw")
        print("7.Deposit")
        print("8.Exit")
        choice=input("Chooce Your choice : ")
        if choice=="1":
            C_id = input("Customer_id: Its Generated Automatically Press Enter")
            Name = input("Name : ")
            Pin = input("Pin : ")
            Balance = int(input("Balance : "))
            Mobile_no = input("Mobile number : ")
            Account_type = input("Account Type : ")
            Create_Account(C_id, Name, Pin, Balance, Mobile_no, Account_type)
        elif choice == "2":
            select()
        elif choice=="3":
            update()
        elif choice=="4":
            delete()
        elif choice=="5":
            check_balance()
        elif choice=="6":
            withdraw()
        elif choice=="7":
            deposit()
        elif choice=="8":
            print("Thankyou for using our ATM")
            break
        else:
            print("Invalid option Please try again...")


