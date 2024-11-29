balance = 100000
pin = 1234

print("**Insert your card**")
pin_num= int(input("Enter your pin\n"))

if pin_num==pin:
    while True:
        print('''1- Check Balance
2- Deposit
3- Withdraw
4- Exit''')
        option = int(input("Choose your option\n"))
        if option == 1:
            print(f"Your balance: RS{balance}\n") #f means format string 
        elif option == 2:
            deposit= int(input("Enter amount to deposit : RS"))
            balance= balance+ deposit
            print(f"Your update balance: RS{balance}\n")
        elif option ==3:
            withdraw= int(input("Enter amount: RS"))
            if withdraw>balance:
                print("Not enough balance")
            else : 
                deposit= deposit-withdraw
                print(f"Your update balance: RS{balance}\n")
        else:
            print("Thank you!!")
            break
        
else:
    print("Incorrect pin, Try again")