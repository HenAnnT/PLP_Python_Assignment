""" def personalized_greeting():
   """"""
  Asks the user for their name and favorite color, then prints a personalized greeting.
   """"""

  # Get the user's name
  name = input("What is your name? ")

  # Get the user's favorite color
  color = input("What is your favorite color? ")

  # Print the personalized greeting
  print(f"Hello, {name}! Your favorite color, {color}, is awesome!")

# Call the function to execute the program
personalized_greeting() """

"""
def greeting():
     """
""" ask for the name:  """
"""
    name = input("Write your name ")
    color = input("What is your favorite color? ")

    print(f"Hello {name}!, your favorite color, {color}, is awesome!")

greeting() """

def math():
    # enter first num:
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform calculation based on the operation
    if operation == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation entered.")
math()


























