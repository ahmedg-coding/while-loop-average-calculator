# Initialization of variables 
sum = 0  
counter = 0

# Continually ask the user to enter a number by making a while loop.
while True:
    # Obtain input from user
    user_input = input("Please enter a number, if you want the program to stop then enter '-1': ")

    # Make an if statement so that when user enters '-1', the program stops requesting user input.
    if user_input == "-1":
        break  

    # Take the user input and convert it into a float i.e a number, if user_input isn't valid i.e cant convert to a float then prompt user.
    try:
        value = float(user_input)  
        sum += value  
        counter += 1   
    except ValueError:
        print("Input entered is not valid, please input a numerical value.")

# Calculate the average of the numbers entered, excluding the -1
if counter > 0:
    average = sum / counter
    print(f"The average of the numbers entered, excluding the -1 is: {average}")
else:
    print("Numbers inputted are not valid.")

