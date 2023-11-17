import os
import time

# Get the current date and time.
now = time.time()

# Number of days to look back.
days_to_look_back = 30

# Get a list of all files in multiple directories.
files = os.listdir(os.path.join("/home/user/Documents", "Projects"))

# Iterate over the files and check if they are older than the specified number of days.
for file in files:
    # Get the file's creation date.
    creation_date = os.path.getctime(file)

    # calculating difference between the file's creation date and the latest date.
    difference = now - creation_date

    # If the file is older than the specified number of days, print a message.
    if difference > days_to_look_back:
    # Comment this line if you dont want to print the files in the std out
        print("The file {} is older than {} days.".format(file, days_to_look_back))

        # Save the extracted files details in a file.
        with open("old_files.txt", "a") as f:
            f.write("{} : {}\n".format(file, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(creation_date))))

        # Prompt the user to delete the file.
        #Comment this line 32 and 35 if you dont want the prompt
answer = input("Do you want to delete the file? (y/n)")

        # wait for user input and proceed.
if answer == "y":
    with open("old_files.txt", "r") as f:
        for line in f:
            os.remove(file)

        # Print the file's details.
        print("The file {} has been deleted.".format(file))
