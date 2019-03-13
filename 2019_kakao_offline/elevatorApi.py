import requests
from pprint import pprint

base_url = "http://localhost:8000"


def start(user_key, problem_id, number_of_elevators):
    start_api_url = "/start/{user_key}/{problem_id}/{number_of_elevators}"

    api_url = base_url + start_api_url.format(user_key=user_key, problem_id=problem_id, number_of_elevators=number_of_elevators)

    response = requests.post(api_url)
    return response.json()


def oncalls(token):
    on_calls_api_url = "/oncalls"

    headers = {
        "X-Auth-Token": token
    }

    api_url = base_url + on_calls_api_url
    response = requests.get(api_url, headers=headers)

    return response.json()


def action(token, commands):
    action_api_url = "/action"

    headers = {
        "X-Auth-Token": token,
        "Content-Type": "application/json"
    }

    json = {
        "commands": commands
    }

    api_url = base_url + action_api_url
    response = requests.post(api_url, headers=headers, json=json)

    return response.json()