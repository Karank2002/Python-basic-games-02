#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the tkinter library
import tkinter

# Define the Fibonacci series function
def fibonacii():
    print("Welcome to Fibonacci series")
    user_input = int(input("Enter your number: "))
    x, y, z = 0, 1, 0
    for i in range(user_input):
        print("x" * 10)
        print(z)
        print("x" * 10)
        x, y, z = y, z, x + y

# Define the Divisor Counter function
def divisor_counter():
    print("Welcome to Divisor Counter")
    user = int(input("Enter your number: "))
    count = 0
    divisors = []
    for i in range(1, 100):
        if i % user == 0:
            divisors.append(i)
            count += 1
    print("Number of divisors:", count)
    print("Divisors:", divisors)

# Define the Factorial function
def factorial():
    print("Welcome to Factorial")
    user = int(input("Enter your number: "))
    fact = 1
    for i in range(1, user + 1):
        fact *= i
    print("Factorial of", user, "is", fact)

# Create the main window using tkinter
window = tkinter.Tk()

# Set the window dimensions
window.geometry("500x500")

# Set the window title
window.title("Python Project - Karan")

# Create labels and buttons using tkinter
label = tkinter.Label(window, text='PYTHON PROJECT', font=("Arabic", 18))
label.place(x=135, y=35)

label1 = tkinter.Label(window, text='Made by Karan', font=("Arabic", 14))
label1.place(x=185, y=70)

button1 = tkinter.Button(window, text="Fibonacci", height=3, width=18, command=fibonacii)
button1.place(x=190, y=120)

button2 = tkinter.Button(window, text="Divisor Counter", height=3, width=18, command=divisor_counter)
button2.place(x=190, y=200)

button3 = tkinter.Button(window, text="Factorial", height=3, width=18, command=factorial)
button3.place(x=190, y=280)

# Run the main loop of the tkinter window
window.mainloop()


# In[ ]:




