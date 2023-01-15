import sys

def create_user():
    pass

def add_habit_for_user():
    pass

def record_data_in_habit():
    pass

def get_data():
    pass


def help_msg():
    print('''
    Here's the list of available commands -
        h : Show help msg
        e : Exit the code
        create <username> : Create new user on pixela api
        add <username> <habit_name>  : Add tracker for a new habit
        record <username> <habit_name> <value> : Add entry for the habit
        get <username> <habit_name> : Get link to see the habit graph
    ''')


def exit_function():
    sys.exit()
