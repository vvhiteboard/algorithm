dac_call_count = 0
dp_call_count = 0


def get_user_input() :
    coin_types_input = input()
    splited_coin_types = coin_types_input.split(",")
    coin_types = []

    for type in splited_coin_types:
        coin_types.append(int(type.strip()))

    changes = input()

    return (coin_types, int(changes))


def divide_and_conquer(coin_types, changes):
    min = get_min_coin_count_dac(coin_types, changes)

    print("divide and conquer coin count : " + str(min))


def get_min_coin_count_dac(coin_types, changes):
    global dac_call_count
    dac_call_count = dac_call_count + 1

    if changes == 0:
        return 0
    elif changes < coin_types[0]:
        return None

    min = -1

    for coin in coin_types:
        temp = get_min_coin_count_dac(coin_types, changes - coin)

        if temp is None:
            continue

        if min == -1 or min > temp:
            min = temp

    if min == -1:
        return None

    return min + 1



def dynamic_programming(coin_types, changes):
    coin_map = {}
    get_min_coin_count_dp(coin_types, changes, coin_map)
    print("dynamic programming coin count : " + str(coin_map[changes]))
    print(coin_map)


def get_min_coin_count_dp(coin_types, changes, coin_map):
    global dp_call_count
    dp_call_count = dp_call_count + 1

    if changes == 0:
        return 0
    elif changes < coin_types[0]:
        return None

    min = -1

    for coin in coin_types:
        temp = coin_map.get(changes - coin)

        if temp is None:
            temp = get_min_coin_count_dp(coin_types, changes - coin, coin_map)

        if temp is None:
            continue

        if min == -1 or min > temp:
            min = temp

    if min == -1:
        return None

    coin_map[changes] = min + 1

    return min + 1


if __name__ == "__main__":
    (coin_types, changes) = get_user_input()

    divide_and_conquer(coin_types, changes)

    dynamic_programming(coin_types, changes)

    print("dac method call count : " + str(dac_call_count))
    print("dp method call count : " + str(dp_call_count))


