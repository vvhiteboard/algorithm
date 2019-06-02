class ChatRoom:
    def __init__(self):
        self.user_info = {}
        self.messages = []

    def change_user_info(self, user_id, nickname):
        self.user_info[user_id] = nickname

    def join(self, cmd, user_id):
        if cmd == "Enter":
            self.messages.append("%s님이 들어왔습니다." % self.user_info[user_id])
        elif cmd == "Leave":
            self.messages.append("%s님이 나갔습니다." % self.user_info[user_id])


def solution(record):
    chat_room = ChatRoom()

    for command in record:
        cmd = command.split(" ")

        if cmd[0] == "Change" or cmd[0] == "Enter":
            chat_room.change_user_info(cmd[1], cmd[2])

    for command in record:
        cmd = command.split(" ")

        chat_room.join(cmd[0], cmd[1])

    return chat_room.messages


if __name__ == "__main__":
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

    answer = solution(record)
    print(answer)