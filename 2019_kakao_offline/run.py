from pprint import pprint
from elevatorApi import *
from elevatorAlgorithm import *


MAX_PASSENGERS = 8
building = [False for _ in range(100)]
action_map = {"UPWARD": upward, "DOWNWARD": downward, "STOPPED": stopped, "OPENED": opened}

def init():
    user_key = "loopin"
    problem_id = 2
    number_of_elevators = 4

    result = start(user_key, problem_id, number_of_elevators)

    return result["token"]


def decide_commands(call_info):
    commands = []

    calls = call_info["calls"]

    for elevator in call_info["elevators"]:
        command = action_map[elevator["status"]](elevator, call_info)
        commands.append(command)

    return commands


if __name__ == "__main__":
    token = init()

    while True:
        call_info = oncalls(token)
        pprint(call_info)
        pprint_target_floor()
        print("=========================================================================")

        if call_info["is_end"]:
            break

        commands = decide_commands(call_info)

        result = action(token, commands)

    pprint(call_info)
