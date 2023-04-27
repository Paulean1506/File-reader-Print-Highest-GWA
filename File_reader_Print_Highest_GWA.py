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
    highest_gwa = 1.00
    highest_student = ''

    # Iterate over each line 
    for line in input_file: