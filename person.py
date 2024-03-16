"""
Write a program that uses a dictionary to store information about a person,
such as their name, age, and favorite color. 
Ask the user for input and store the information in the dictionary. 
Then, print the dictionary to the console.
"""

person_info = {}

person_info = {"name": input("Enter your name:" ),"age": input("Enter your age:" ), "color": input("Enter your favorite color:")}
print("Person info;")
for key, value in person_info.items():
    print(f"{key}: {value}")
