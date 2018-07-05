from util import *


class Worklog:

    def quit_program(self):
        """This quits the application"""
        print("Thank you for using WORK LOG. Goodbye.")
        exit()

    def main_menu(self):
        """This brings up the main menu of the program. Allowing
        users to pick which task they would like to do
        """

        menu_options = {'a': self.add_entry, 'b': self.search_entry,
                        'c': self.quit_program}

        while True:
            print("Welcome to WORK LOG")
            menu_choice = input("What would you like to do?"
                                "\na) Add new entry"
                                "\nb) Search in existing entries"
                                "\nc) Quit program"
                                "\n> ")

            try:
                choice = menu_options[menu_choice]
                clear()

            except KeyError:
                input("That is not a valid choice. Please try again ")
                self.main_menu()
            else:
                choice()
                clear()

    def add_entry(self):
        """Writes user input to a csv"""
        entry_date = date_format(input("Date of the task"
                                       "\nPlease use the "
                                       "DD/MM/YYYY:\n> ")).strip()
        clear()

        entry_title = input("Title of the task:\n> ").strip().upper()
        clear()

        entry_time_spent = time_format(input("Time spent "
                                             "(rounded in minutes):\n> "))
        clear()

        entry_notes = input("Notes (Optional):\n> ").strip().upper()
        clear()

        with open('work_log.csv', 'a') as file:
            file.write(entry_date + ',' + entry_title + ',' +
                       entry_time_spent + ',' + entry_notes + '\n')
        input("Your entry has been added. Press enter to return to the menu\n")
        clear()

    def search_entry(self):
        """This prompts the user with option of searching existing entries
        and gives the user four different options as to what to specifically
        search for
        """

        search_options = {'a': self.search_date, 'b': self.search_time_spent,
                          'c': self.exact_search, 'd': self.search_regex,
                          'e': self.main_menu}
        search_choice = input("What would you like to search by?"
                              "\na) Date"
                              "\nb) Time Spent"
                              "\nc) Exact Search"
                              "\nd) Regex pattern"
                              "\ne) Return to Main Menu"
                              "\n> ")
        try:
            choice = search_options[search_choice]
            clear()

        except KeyError:
            input("That is not a valid choice. Please try again \n>")
            self.search_entry()
            clear()
        else:
            choice()
            clear()


    def search_date(self):
        """This function takes the user's argument and passes it to the
        search_csv function which then displays it to the user
        """
        desired_date = date_format(input("What date would you like "
                                         "to search for? \n>"))
        search_csv(desired_date)

    def search_time_spent(self):
        """This function takes the user's argument and passes it to the
        search_csv function which then displays it to the user
        """
        spent_time = time_format(input('How much time did you spend on'
                                       ' this job task? \n>'))
        search_csv(spent_time)

    def exact_search(self):
        """This function takes the user's argument and passes it to the
        search_csv function which then displays it to the user
        """
        exactly = input('What is the exact task you are looking for? \n>')

        search_csv(exactly.upper())

    def search_regex(self):
        """This function takes the user's inputted regex pattern and passes
        it to the reg_csv_search funtion where it is then displayed to the
        user
        """
        pattern = input("Please enter the REGEX pattern you would like "
                        "to use to search for the log: \n>")
        reg_csv_search(pattern)


if __name__ == '__main__':
    Worklog().main_menu()
