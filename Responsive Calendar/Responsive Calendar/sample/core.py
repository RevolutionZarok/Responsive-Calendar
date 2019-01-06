import time
import os
import calendarhelper
import calendar

# Set the current day, month and year
day_now = int(time.strftime("%d"))
month_now = int(time.strftime("%m"))
year_now = int(time.strftime("%Y"))

# Create the Calendarhelper object
Cal = calendarhelper.Calendarhelper(day_now, month_now, year_now)


# Interactive user menu
user_menu = {
    "advanceDay":"Advance one day on the calendar (1)",
    "showEvents":"Show all events for the next month (2)",
    "addEvent":"Add new event (3)",
    "removeEvent":"Remove existing event (4)",
    "exit":"Quit application (5)",
    "emptySpace":"\n"
    }

userInput = ""
while userInput != "y":
    print("\n> User menu:\n")
    for x in user_menu:
        print(user_menu[x])

    userInput = input()

    if userInput == "1":
        Cal.nextDay()
    elif userInput == "2":
        print("Placeholder")
    elif userInput == "3":
        print("Placeholder")
    elif userInput == "4":
        print("Placeholder")
    elif userInput == "5":
        print("Are you sure? (y/n)")
        userInput = input()
    else:
        print("\nInvalid input")

    print("\n")

# End of script
Cal.updateEvents()
print("Exit successful")
time.sleep(.5)
os._exit(0)

# Switch case for the user input
def user_input_switch(userInput):
    switcher = {
        1:"1",
        2:"2",
        3:"3",
        4:"4",
        5:"5"
        }

