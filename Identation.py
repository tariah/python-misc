print("Welcome!")
fuel = int(input("Enter Fuel Level: "))
if fuel > 3:
    print("It's OK")
    print("You can drive downtown.")
else:
    money = int(input("How much do you have?: "))
    if money > 10:
        print("You should buy some gas.")
    else:
        print("You'd better stay at home.")
print("What's next?")
