import time
import sys

# Set the current day, month, year and time
day_now = time.strftime("%A")
day_now_int = int(time.strftime("%d"))
month_now = time.strftime("%B")
month_now_int = int(time.strftime("%m"))
year_now = time.strftime("%Y")
time_now = time.strftime("%H:%M:%S")

''' Override the formatyear and depending functions in the calendar class
in order to show current day and event days'''
class PersonalizedCalendar(calendar.TextCalendar):
    def formatyear(self, theyear, w=2, l=1, c=6, m=3):
        w = max(2, w)
        l = max(1, l)
        c = max(2, c)
        colwidth = (w + 1) * 7 - 1
        v = []
        a = v.append
        a(repr(theyear).center(colwidth*m+c*(m-1)).rstrip())
        a('\n'*l)
        header = self.formatweekheader(w)
        for (i, row) in enumerate(self.yeardays2calendar(theyear, m)):
            # months in this row
            months = range(m*i+1, min(m*(i+1)+1, 13))
            a('\n'*l)
            names = (self.formatmonthname(theyear, k, colwidth, False)
                     for k in months)
            a(calendar.formatstring(names, colwidth, c).rstrip())
            a('\n'*l)
            headers = (header for k in months)
            a(calendar.formatstring(headers, colwidth, c).rstrip())
            a('\n'*l)
            # max number of weeks for this row
            height = max(len(cal) for cal in row)
            print("Height = " + str(height))
            for j in range(height):
                weeks = []
                for cal in row:
                    if j >= len(cal):
                        weeks.append('')
                    else:
                        weeks.append(self.formatweek(cal[j], w))
                a(calendar.formatstring(weeks, colwidth, c).rstrip())
                a('\n' * l)
        return ''.join(v)

# Instantiate the basic eventless calendar that shows the first day
print(PersonalizedCalendar().formatyear(int(year_now)))

# Interactive user menu
user_menu = {
    "advanceDay":"Advance one day on the calendar (1)",
    "showEvents":"Show all events for the next month (2)",
    "addEvent":"Add new event (3)",
    "removeEvent":"Remove existing event (4)",
    "exit":"Quit application (5)"
    }

userInput = ""
while userInput != "y":
    print("Chose interaction")
    for x in user_menu:
        print(user_menu[x])

    userInput = input()

    if userInput == "1":
        print("Placeholder")
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
        print("\nPlease input 1, 2, 3, 4 or 5 depending on what you want to do")

    print("\n")

# End of script
print("Exit successful")
time.sleep(.5)
sys.exit()



