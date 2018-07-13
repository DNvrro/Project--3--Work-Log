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
                "Sorry. That is not a valid date. Please enter a date "
                "in the MM/DD/YYYY format: \n>")

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
    results_list = []
    with open('work_log.csv') as file:
        for row in file:
            if search_criteria in row:
                results_list.append(row)
        results_sort(results_list)
        #return input('press Enter to return to the main menu')
       # clear()


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
                return input('Your search did not yield any results. Please '
                             'press Enter to return to the main menu')
                clear()


def results_sort(search_results):

    if len(search_results) >= 1:
        display_search_results(search_results[0])
        proceed(search_results)
    else:
        print('Sorry. Nothing matched your search.')

def proceed(results_sort):
    """Asks the user if they would like to proceed to the next search match"""
    result_index = 0
    good = True
    with open('work_log.csv', 'r') as file:
        while good:
            proceed_prompt = input('Would you like to see the next '
                               'match (Y/N)? \n>').upper()
            if proceed_prompt == 'Y':
                result_index += 1
                try:
                    display_search_results(results_sort[result_index])
                except IndexError:
                    print('There are no other entries that match your '
                          'search criteria.')
                    clear()
                    good = False
            elif proceed_prompt == 'N':
                good = False
                clear()



def display_search_results(results):
    """Displays the users desired criteria in a user friendly format"""

    new_list = results.split(',')

    print('Date : {}'.format(new_list[0]))
    print('Title : {}'.format(new_list[1]))
    print('Time Spent : {}'.format(new_list[2]))
    print('Notes : {}'.format(new_list[3]))
    #input("Press Enter to cycle through entries.")

    clear()
