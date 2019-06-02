def solution(N, stages):
    sorted_stages = sorted(stages)
    result = []

    stage_map = {}
    stage_arr = []
    for stage in sorted_stages:
        if stage > N:
            break
        if stage_map.get(stage) is None:
            stage_arr.append(stage)
            stage_map[stage] = 1
        else:
            stage_map[stage] += 1

    stage_count = len(stages)
    for stage in stage_arr:
        count = stage_map[stage]
        result.append((stage, count / stage_count))
        stage_count -= count

    empty_stage = [n for n in range(1, N + 1) if stage_map.get(n) is None]
    result = sorted(result, key=lambda value: (-value[1], value[0]))
    answer = [val[0] for val in result]
    answer.extend(empty_stage)
    return answer


if __name__ == "__main__":
    N = 4
    stages = [4,4,4,4,4]

    answer = solution(N, stages)
    print(answer)
