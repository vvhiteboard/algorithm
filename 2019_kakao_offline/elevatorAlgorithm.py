from pprint import pprint

target_floor = {
    0: set(),
    1: set(),
    2: set(),
    3: set()
}

MAX_PASSENGERS = 8

def make_command(id, command, call_ids=()):
    commands = {
        "elevator_id": id,
        "command": command,
        "call_ids": call_ids
    }

    pprint(commands)
    return commands


# 내릴 사람이 있나?
def is_exit(elevator):
    floor = elevator["floor"]
    passengers = elevator["passengers"]

    for passenger in passengers:
        if floor == passenger["end"]:
            return True

    return False


# 탈 사람이 있나?
def is_enter(elevator, calls):
    floor = elevator["floor"]

    for call in calls:
        if floor == call["start"]:
            return True

    return False


# 현재 층이 내 목표층인가?
def is_target_floor(elevator):
    if elevator["floor"] in target_floor[elevator["id"]]:
        return True

    return False


# 현재층이 목표층 중에 없나?
def is_empty_target_floor(elevator):
    for id in target_floor.keys():
        if elevator["id"] == id:
            continue

        if elevator["floor"] in target_floor[id]:
            return False

    return True


def get_all_target():
    return target_floor[0] | target_floor[1] | target_floor[2] | target_floor[3]


def exist_upper_target(elevator):
    floor = elevator["floor"]
    target_floors = target_floor[elevator["id"]]

    for target in target_floors:
        if floor < target:
            return True

    return False


def more_upper_passenger(elevator, calls):
    floor = elevator["floor"]

    for call in calls:
        if floor < call["start"] < call["end"] and call["start"] not in get_all_target():
            return True

    return False


def exist_lower_target(elevator):
    floor = elevator["floor"]
    target_floors = target_floor[elevator["id"]]

    for target in target_floors:
        if floor > target:
            return True

    return False


def more_lower_passenger(elevator, calls):
    floor = elevator["floor"]

    for call in calls:
        if floor > call["start"] > call["end"] and call["start"] not in get_all_target():
            return True

    return False


def remove_target_floor(elevator):
    target_floor[elevator["id"]].remove(elevator["floor"])


def get_exit_passenger(elevator):
    floor = elevator["floor"]
    passengers = elevator["passengers"]

    return [p["id"] for p in passengers if p["end"] == floor]


def is_stopped(elevator):
    return len(target_floor[elevator["id"]]) == 0


def is_upward(elevator):
    id = elevator["id"]
    floor = elevator["floor"]

    if len(target_floor[id]) == 0:
        return False

    return tuple(target_floor[id])[0] > floor


def is_downward(elevator):
    id = elevator["id"]
    floor = elevator["floor"]

    if len(target_floor[id]) == 0:
        return False

    return tuple(target_floor[id])[0] < floor


def exist_upward_call(elevator, calls):
    floor = elevator["floor"]

    for call in calls:
        if floor == call["start"] and floor < call["end"]:
            return True

    return False


def exist_downward_call(elevator, calls):
    floor = elevator["floor"]

    for call in calls:
        if floor == call["start"] and floor > call["end"]:
            return True

    return False


def get_upward_passenger(elevator, calls):
    id = elevator["id"]
    floor = elevator["floor"]
    ps = []

    for call in calls:
        if len(elevator["passengers"]) + len(ps) >= MAX_PASSENGERS:
            break

        if floor == call["start"] and floor < call["end"]:
            target_floor[id].add(call["end"])
            ps.append(call)

    for p in ps:
        calls.remove(p)

    return [p["id"] for p in ps]


def get_downward_passenger(elevator, calls):
    id = elevator["id"]
    floor = elevator["floor"]
    ps = []

    for call in calls:
        if len(elevator["passengers"]) + len(ps) >= MAX_PASSENGERS:
            break

        if floor == call["start"] and floor > call["end"]:
            target_floor[id].add(call["end"])
            ps.append(call)

    for p in ps:
        calls.remove(p)

    return [p["id"] for p in ps]


def is_more_enter(elevator):
    id = elevator["id"]

    if MAX_PASSENGERS > len(elevator["passengers"]):
        return True

    return False


def find_next_target(elevator, calls):
    floor = elevator["floor"]
    id = elevator["id"]

    max = 0
    max_floor = 0

    if len(calls) == 0:
        return "STOP"

    for call in calls:
        start = call["start"]

        if start in get_all_target():
            continue

        if max < abs(floor - start):
            max = abs(floor - start)
            max_floor = start

    if max == 0:
        return "STOP"

    if max_floor > floor:
        target_floor[id].add(max_floor)
        return "UP"

    if max_floor < floor:
        target_floor[id].add(max_floor)
        return "DOWN"

    return "STOP"


def upward(elevator, call_info):
    id = elevator["id"]
    calls = call_info["calls"]
    elevators = call_info["elevators"]

    # 목표 층이었다면 멈춤
    if is_target_floor(elevator):
        remove_target_floor(elevator)
        return make_command(id, "STOP")

    # 현재층에 탈 사람이 있고 현재 층이 목표층 중에 없는 경우
    if is_enter(elevator, calls) and is_empty_target_floor(elevator):
        return make_command(id, "STOP")

    # 위로 더 올라가야되면 UP (목표층 혹은 탈 사람)
    if exist_upper_target(elevator) or more_upper_passenger(elevator, calls):
        return make_command(id, "UP")

    return make_command(id, "STOP")


def downward(elevator, call_info):
    id = elevator["id"]
    calls = call_info["calls"]
    elevators = call_info["elevators"]

    # 목표 층이었다면 멈춤
    if is_target_floor(elevator):
        remove_target_floor(elevator)
        return make_command(id, "STOP")

    # 현재층에 탈 사람이 있고 현재 층이 목표층 중에 없는 경우
    if is_enter(elevator, calls) and is_empty_target_floor(elevator):
        return make_command(id, "STOP")

    # 아래로 더 내려가야하면 (목표층 혹은 탈 사람)
    if exist_lower_target(elevator) or more_lower_passenger(elevator, calls):
        return make_command(id, "DOWN")

    return make_command(id, "STOP")


def stopped(elevator, call_info):
    id = elevator["id"]
    calls = call_info["calls"]
    elevators = call_info["elevators"]

    # 내릴 사람이 있으면
    if is_exit(elevator):
        return make_command(id, "OPEN")

    # 탈 사람이 있으면
    if is_enter(elevator, calls) and is_more_enter(elevator):
        if is_upward(elevator) and exist_upward_call(elevator, calls):
            return make_command(id, "OPEN")
        elif is_downward(elevator) and exist_downward_call(elevator, calls):
            return make_command(id, "OPEN")
        elif is_stopped(elevator):
            return make_command(id, "OPEN")

    if is_upward(elevator):
        return make_command(id, "UP")
    elif is_downward(elevator):
        return make_command(id, "DOWN")

    next_command = find_next_target(elevator, calls)

    return make_command(id, next_command)


def opened(elevator, call_info):
    id = elevator["id"]
    calls = call_info["calls"]
    elevators = call_info["elevators"]

    # 내릴 사람이 있으면
    if is_exit(elevator):
        ps = get_exit_passenger(elevator)
        return make_command(id, "EXIT", ps)

    # 탈 사람이 있으면
    if is_enter(elevator, calls) and is_more_enter(elevator):
        if is_upward(elevator):
            ps = get_upward_passenger(elevator, calls)
        elif is_downward(elevator):
            ps = get_downward_passenger(elevator, calls)
        else:
            ps = get_upward_passenger(elevator, calls) # 그냥 STOP 상태인 경우 올라가는것부터
            if len(ps) == 0:
                ps = get_downward_passenger(elevator, calls)

        if len(ps) > 0:
            return make_command(id, "ENTER", ps)

    return make_command(id, "CLOSE")


def pprint_target_floor():
    pprint(target_floor)
