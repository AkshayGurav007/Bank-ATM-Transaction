pin=1234
accbal = 10000.00

input_pin = int(input("Enter the PIN\n"))

if pin==input_pin:
    print("Valid PIN")
    amt = float(input("enter the amount to be withdrawn\n"))
    print("Withdrawing Rs ",amt)

    if amt < accbal:
        accbal = accbal - amt
        print("Withdraw success")
    else:
        print("Withdraw Failed")
        print("Insufficient Balance in account")

    print("Account Balance is Rs ",accbal)
else:
    print("Invalid PIN")

