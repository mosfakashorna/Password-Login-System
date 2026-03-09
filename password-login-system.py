# Password Login System
# This program allows the user to enter a password.
# The user has 3 attempts.
# If all attemptes fail, the program waits 5 seconds
# and then allows the user to try again.

import time

correct_password = "python123"
attempt_limit = 3


while True:
    attempt_count = 0

    while attempt_count < attempt_limit:
        user_entry = input("Enter the password: ")
        attempt_count += 1

        if user_entry == correct_password:
            print("Access allowed.")
            break
        else:
            print("Incorrect password!")
    else:
        print("Too many incorrect attempts! Try again in 5 seconds.")
        time.sleep(5)
        print("You can try again now.\n")
        continue
    break


