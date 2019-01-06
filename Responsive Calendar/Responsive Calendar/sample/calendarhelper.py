import json
from pprint import pprint

# Calendar constants
daysInMonthNormal = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
daysInMonthLeap = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
monthNames = {
        1:"January", 
        2:"February", 
        3:"March", 
        4:"April", 
        5:"May", 
        6:"June", 
        7:"July", 
        8:"August", 
        9:"September", 
        10:"October", 
        11:"November", 
        12:"December"
        }

class Calendarhelper:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

        # Load the events from the Json file into the events list

        with open("./docs/events.json") as event_data:
            self.events = json.load(event_data)

        print("It's the %02i.%02i.%4i" % (day, month, year))

    def nextDay(self):
        if not isleap(self.year):
            setNextDay(self, daysInMonthNormal)
        else:
            setNextDay(self, daysInMonthLeap)

    # Adds an event on the given date
    def addEvent(day, month, year):
        return null

    # Adds an event on the given date
    def removeEvent(day, month, year):
        return null

    # Update the Json file with the new event list
    def updateEvents(self):
        with open("./docs/events.json", "w") as event_data:
            json.dump(self.events, event_data, indent = 4)

# Check if current year is a leap year. Returns true/false.
def isleap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Algorithm to get the next day
def setNextDay(self, monthDays):
    if self.day+1 <= monthDays[self.month]:
        self.day += 1
    elif self.day+1 > monthDays[self.month] and self.month != 12:
        self.day = 1
        self.month += 1
    elif self.day == 31 and self.month == 12:
        self.day = 1
        self.month = 1
        self.year += 1
    else:
        print("Error in nextDay Algorithm")
    print("It's the %02i.%02i.%4i" % (self.day, self.month, self.year))
