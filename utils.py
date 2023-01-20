import sys
from typing import List
import requests


def generate_graph_id(username: str, habit: str):
    return f"{username}-{habit}"[0:16]


def create_user(cmd_list: List):
    URL = "https://pixe.la/v1/users"

    request_body = {
        "username": cmd_list[1],
        "token": "issecret",
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
        }

    response = requests.post(url=URL, json=request_body)

    if response.status_code == 200:
        print(f'message -> {response.json()["message"]}')
        print("User created successfully")
    else:
        print(f'Status code -> {response.status_code}')
        print("Try again!")


def add_habit_for_user(cmd_list: List):
    URL = f'https://pixe.la/v1/users/{cmd_list[1]}/graphs'

    request_body = {
        "id": generate_graph_id(cmd_list[1], cmd_list[2]),
        "name": cmd_list[2],
        "unit": "commit",
        "type": "int",
        "color": "ajisai",
    }

    header = {
        "X-USER-TOKEN": "issecret"
    }

    response = requests.post(url=URL, headers=header, json=request_body)

    if response.status_code == 200:
        print(f'message -> {response.json()["message"]}')
        print("Graph created successfully")
    else:
        print(f'Status code -> {response.status_code}')
        print("Try again!")


def record_data_in_habit(cmd_list: List):

    graph_id = generate_graph_id(cmd_list[1], cmd_list[2])
    URL = f"https://pixe.la/v1/users/{cmd_list[1]}/graphs/{graph_id}"

    request_header = {
        "X-USER-TOKEN": "issecret"
    }

    request_body = {
        "date": cmd_list[3],
        "quantity": "1"
    }

    response = requests.post(url=URL, headers=request_header, json=request_body)

    if response.status_code == 200:
        print(f'message -> {response.json()["message"]}')
        print("Entry added in habit graph")
    else:
        print(f'Status code -> {response.status_code}')
        print("Try again!")


def get_data(cmd_list: List):
    graph_id = generate_graph_id(cmd_list[1], cmd_list[2])

    URL = f"https://pixe.la/v1/users/{cmd_list[1]}/graphs/{graph_id}.html"

    print(f"Hi, Please check your habit graph on this link ->{URL}")


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
