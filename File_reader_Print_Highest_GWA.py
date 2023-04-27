# Paulean Marguerette F. Parrish
# Bscpe 1-4
# Problem no. 1
# Write a Python program that read a file containing the name of 20 students together with their GWA. 
# The program will outputs the name of the student who got the highest GWA (including the GWA).

# Header design
import pyfiglet

print(" \033[95mHello! I hope you're having a great day!!! ".center(70, "="))
print("")

# Ask for the name of the user
user_name = input("\033[92mMay I know your name? \033[0m")
print("\n\033[94mThank you", user_name,  "you may now proceed to the program!")
print("")

# Open the Name_and_GWA.txt and read the file
with open('Name_and_GWA.txt', 'r') as input_file:

    # Initialize the highest GWA and student name
    highest_gwa = 5.00

    # Iterate over each line 
    for line in input_file:

        # Split the line into the student name and GWA
        name, gwa = line.strip().split(',')

        # Convert the GWA to a float
        gwa = float(gwa)

        # Compare the GWA to the current highest GWA
        if gwa < highest_gwa:

            # Update the highest GWA and student name
            highest_gwa = gwa
            highest_student = name

# Print the name of the student who got the highest GWA
    print("\033[95mThe student with the highest GWA is", highest_student, "with a GWA of ", highest_gwa)  

# Column for the names and GWA
print("\n\033[93mAmong the list of students:")
with open("Name_and_GWA.txt") as column_file:
  print("{:<25}{:<25}".format("\nStudent Name:", "  GWA:\n"))
  for line in column_file:
    name, gwa = line.split(",")
    column_name = name
    column_gwa = gwa
    print("{:<25}{:<25}".format(column_name, column_gwa))

# Program is completed
from termcolor import colored
from pyfiglet import Figlet
f = Figlet(font = "banner3-d")
print(colored(f.renderText('Thank you!'), 'red'))

