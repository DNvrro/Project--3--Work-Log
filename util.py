import re
import datetime
import os
import csv


def clear():
    """
    Clears the screen for a clean user experience

    """
    os.system('cls' if os.name == 'nt' else 'clear')


def date_format(date):
    """Checks that the user has entered
        a date in the specified format
    """

    formatted = True
    task_date = date
    while formatted:
        try:
            datetime.datetime.strptime(task_date, "%m/%d/%Y")
            formatted = False
            clear()
        except ValueError:
            clear()
            task_date = input(
                "Sorry. That is not a valid date. Please enter a date"
                "in the specified format: \n>")

    return task_date



def time_format(time):
    """Verifies that the user has entered the time spent in a rounded
    minutes format
    """
    task_time = time
    formatted = True
    while formatted:
        try:
            int(task_time)
            formatted = False
            clear()
        except ValueError:
            clear()
            task_time = input("Please submit the time in rounded minutes: \n>")
    return task_time


def search_csv(search_criteria):
    """Searches the CSV for the user provided criteria, then calls the
    display_search_results function once it is found
    """
    with open('work_log.csv', 'r') as file:
        csvreader = csv.reader(file, delimiter=',')
        rows = list(csvreader)
        for row in rows:
            if search_criteria in row:
                display_search_results(row)
            else:
                input("Your search did not yield any results. "
                      "Please press Enter to return to the main menu")
                clear()


def reg_csv_search(arg):
    """Uses a regex pattern to search the CSV for the users specified
    criteria
    """
    with open('work_log.csv', 'r') as file:
        csvreader = csv.reader(file, delimiter=',')
        rows = list(csvreader)
        for row in rows:
            if re.search(arg, str(row)):
                display_search_results(row)
            else:
                input('Your search did not yield any results. Please press '
                      'Enter to return to the main menu')
                clear()


def display_search_results(results):
    """Displays the users desired criteria in a user friendly format"""

    print('Date : {}'.format(results[0]))
    print('Title : {}'.format(results[1]))
    print('Time Spent : {}'.format(results[2]))
    print('Notes : {}'.format(results[3]))
    input("Press Enter to cycle through entries or "
          "return to the main menu\n")
    clear()
