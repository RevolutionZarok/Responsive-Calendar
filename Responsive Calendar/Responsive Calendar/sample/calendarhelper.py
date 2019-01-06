import re
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
eventTypes = ["Birthday", "Meeting", "Appointment"]

class Calendarhelper:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

        # Load the events from the Json file into the events list

        with open("./docs/events.json") as event_data:
            self.events = json.load(event_data)

        print(">>> It's the %02i.%02i.%4i   <<<" % (day, month, year))

    def nextDay(self):
        if not isleap(self.year):
            setNextDay(self, daysInMonthNormal)
            checkAlerts(self)
        else:
            setNextDay(self, daysInMonthLeap)
            checkAlerts(self)

    # Adds an event at the given date
    def addEvent(self):
               
        # Set the event type
        print("\n>Pick your event type")
        for (i, eventType) in zip(range(1,4), eventTypes):
            print("%i. %s" % (i, eventType))
        userInput = int(input())
        while (userInput != 1) and (userInput != 2) and (userInput != 3):
            print("Wrong input. Enter 1, 2 or 3")
            userInput = int(input())
        eventType = eventTypes[userInput-1]

        # Set the event date
        if eventType == "Birthday":
            print("\n>Enter date (xx.xx)")
            userInput = dateInputCheck(self, input(), eventType)
            eventDay = int(re.search("(\d\d).", userInput).group(1))
            eventMonth = int(re.search("\d\d.(\d\d)", userInput).group(1))
            eventYear = None
        else:
            print("\n>Enter date (xx.xx.xxxx)")
            userInput = dateInputCheck(self, input(), eventType)
            eventDay = int(re.search("(\d\d).", userInput).group(1))
            eventMonth = int(re.search("\d\d.(\d\d).", userInput).group(1))
            eventYear = int(re.search("\d\d.\d\d.(\d\d\d\d)", userInput).group(1))

        # Set the event subject
        print("\nWho is concerned by <%s>?" % eventType)
        eventSubject = input()

        tmpEvent = {
            "type": eventType,
            "subject": eventSubject,
            "day": eventDay,
            "month": eventMonth,
            "year": eventYear
            }

        self.events["events"].append(tmpEvent)
        if eventYear is None:
            print("\n>Successfully added new event on %02i.%02i" % (eventDay, eventMonth))
        else:
            print("\n>Successfully added new event on %02i.%02i.%4i" % (eventDay, eventMonth, eventYear))

    # Remove an event on the given date
    def removeEvent(self):
        print("Enter event date (xx.xx.xxxx)")
        date = dateInputCheck(self, input())
        eventDay = int(re.search("(\d\d).", date).group(1))
        eventMonth = int(re.search("\d\d.(\d\d).", date).group(1))
        eventYear = int(re.search("\d\d.\d\d.(\d\d\d\d)", date).group(1))

        removeEvents = []
        for event in self.events["events"]:
           if event["day"] == eventDay and event["month"] == eventMonth and event["year"] is None:
               removeEvents.append(event)
           elif event["day"] == eventDay and event["month"] == eventMonth and event["year"] == eventYear:
               removeEvents.append(event)
    
        # Confirm all the events to remove which are on the given date
        if len(removeEvents) == 1:
            print("Confirm remove <%s %s>(y/n)?" % (removeEvents[0]["subject"], removeEvents[0]["type"]))
            if input() == "y":
                self.events["events"].remove(removeEvents[0])
                print(">Removed event")
            else:
                print(">Aborted delete event")
        elif len(removeEvents) == 0:
            print("No events found on %02i.%02i.%4i" % (eventDay, eventMoney, eventYear))
        else:
            print("Multiple events found. Which one to remove?")
            for (i, event) in (range(1, len(removeEvents)), removeEvents):
                print("Remove <%s,%s>" %(event["type"], event["subject"]))          # TODO Add remove multiple events


    # Method that returns a list of all the events ocurring in the next 31 days
    def previewEvents(self):
       for event in self.events["events"]:
           for x in event.values():
                if x is not None:
                    print(x, end=" ")        # TODO Make it for the next 31 days and improve visualisation

    # Update the Json file with the new event list
    def updateEvents(self):
        with open("./docs/events.json", "w") as event_data:
            json.dump(self.events, event_data, indent = 4)

# Check if current year is a leap year. Returns true/false.
def isleap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Algorithm to set the next date
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
    print(">>> It's the %02i.%02i.%4i <<<" % (self.day, self.month, self.year))  # TODO Improve visualisation

def checkAlerts(self):                                                   # TODO Add alert function
    print("Alerts not implemented yet")

# check if the input has the correct date foramt
def dateInputCheck(self, date):
    while re.search("\d\d.\d\d.\d\d\d\d", date) is None:   
        print("Invalid input. Enter date (xx.xx.xxxx)")
        date = input()
    return date

def dateInputCheck(self, date, type):
    if type == "Birthday":
        while re.search("\d\d.\d\d", date) is None:   
            print("Invalid input. Enter date (xx.xx)")
            date = input()
    else:
        date = dateInputCheck(self, date)
    return date
