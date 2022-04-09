


sum = 0
print("Enter q for quit!")
while(True): 
    try:
        UserInput = input("Enter the price: \n")
        if (UserInput!= 'q'):
            sum = sum + int(UserInput)
            print(f"Your order total so far {sum}")

        else:
             print(f"Your total bill is {sum} Rupess. Thanks for shopping with us. Have a graet day! ")
             break
    except Exception as e:
        print("Please enter a valid price:")