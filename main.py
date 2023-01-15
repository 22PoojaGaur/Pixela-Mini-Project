from typing import List

import utils

if __name__ == '__main__':
    while True:
        command: str = input("Enter your command ->\n")
        cmd_list: List[str] = command.split(' ')

        if cmd_list[0] == "create":
            utils.create_user()
        elif cmd_list[0] == "add":
            utils.add_habit_for_user()
        elif cmd_list[0] == "record":
            utils.record_data_in_habit()
        elif cmd_list[0] == "get":
            utils.get_data()
        elif cmd_list[0] == "help":
            utils.help_msg()
        elif cmd_list[0] == "exit":
            print("Thanks for using, bye!")
            utils.exit_function()
        else:
            print("command not found")
