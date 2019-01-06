import time
import os
import calendarhelper

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
        Cal.previewEvents()
    elif userInput == "3":
        Cal.addEvent()
    elif userInput == "4":
        Cal.removeEvent(userInput)
    elif userInput == "5":              # End of script and update Json file
        print("Are you sure? (y/n)")
        if input() == "y":
            Cal.updateEvents()
            print("Exit successful")
            time.sleep(.5)
            os._exit(0)
    else:
        print("\nInvalid input")

