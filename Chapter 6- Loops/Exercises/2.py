while True: 
    #ask for the age input
    age=input("Enter you age: ")
    age=int(age)
    #if age is less than 3
    if age<3:
        print("Your ticket is free.")
    #if age is less than or equal to 12    
    elif age<=12:
        print("The cost of your movie ticket is $10.")
    #if none of the above    
    else:
        price=15
        print(f"The cost of your movie ticket is ${price}. ")

        