import enum


class Elevator:
    def __init__(self):
        self.is_idle = True
        self.target_floor = 1
        self.passenger_num = 0

        self.target_floors = []
        self.call_ids = []
        self.command = "STOP"

    def enter(self, call_id):
        self.command = "ENTER"
        self.call_ids.append(call_id)

    def exit(self, call_id):
        self.command = "EXIT"
        self.call_ids.append(call_id)

    def open(self):
        self.command = "OPEN"

    def close(self):
        self.command = "CLOSE"

    def up(self, target_floor):
        self.target_floor = target_floor
        self.command = "UP"

    def down(self, target_floor):
        self.target_floor = target_floor
        self.command = "DOWN"

    def stop(self):
        self.command = "STOP"


class STATUS(enum.Enum):
    STOPPED = "STOPPED"
    OPENED = "OPENED"
    UPWARD = "UPWARD"
    DOWNWARD = "DOWNWARD"