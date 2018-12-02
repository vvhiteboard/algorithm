import sys


def calc_area(_picture, _x, _y, _size_x, _size_y):
	_area = 0

	if _picture[_x][_y] != "1":
		return _area

	_picture[_x][_y] = "-1"
	_area += 1

	if _x + 1 < _size_x:
		_area += calc_area(_picture, _x + 1, _y, _size_x, _size_y)

	if _x - 1 >= 0:
		_area += calc_area(_picture, _x - 1, _y, _size_x, _size_y)

	if _y + 1 < _size_y:
		_area += calc_area(_picture, _x, _y + 1, _size_x, _size_y)

	if _y - 1 >= 0:
		_area += calc_area(_picture, _x, _y - 1, _size_x, _size_y)

	return _area


if __name__ == "__main__":
	sys.setrecursionlimit(1000000)
	temp = input().split(" ")
	x, y = int(temp[0]), int(temp[1])

	picture = []

	for _ in range(x):
		picture.append(input().split(" "))

	max_area = 0
	picture_count = 0

	for i in range(x):
		for j in range(y):
			area = 0

			if picture[i][j] == "1":
				area = calc_area(picture, i, j, x, y)
				picture_count += 1

			if max_area < area:
				max_area = area

	print(picture_count)
	print(max_area)

