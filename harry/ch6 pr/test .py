def get_float_input(prompt, color):  
    print(colored(prompt, color)) 

from termcolor  import colored
print(colored("Welcome to my calculator", "yellow"))

number1 = float(input(colored("Enter a number here:", "blue")))
number2 = float(input(colored("Enter another number here:", "green")))

# number1 = get_float_input("Enter a number here:", "blue")
# number2 = get_float_input("Enter another number here:", "green")
print ("press 1 for addition \n press 2 for substraction \n press 3 for mulitplaction\npress 4 for division\n press 5 for average\npress 6 for Eixt")

choice = int (input("Enter your choice from 1 to 5 :"))

while choice<1 or choice>6:
        print("invalid input enter your choice from 1-5")
        choice = int(input())

if choice == 1 :
    print (number1 + number2)

elif choice == 2 :
    print ( number1 - number2)
elif choice == 3 :
    print ( number1 * number2 )

elif choice == 4:
       print (number1 / number2)
if number2 == 0:
    print("0 is an invalid number")
elif choice ==5:
    print (number1 + number2  /2)

elif choice == 6:
        print("Exiting the calculator. Goodbye!")

else:
    print(colored("Invalid input! Please enter a valid number.", "red"))
