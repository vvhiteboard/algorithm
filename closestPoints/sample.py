import random

if __name__ == "__main__":
	fp = open("test5.txt", "w")

	mm = {}

	# while len(mm) < 20000:
	# 	b = str(random.randint(-10000, 10000))
	# 	a = str(random.randint(-10000, 10000))
	# 	key = a + ":" + b
	# 	mm[key] = a + " " + b + "\n"

	# for key in mm:
	# 	fp.write(mm[key])

	for _ in range(100000):
		fp.write("0 0\n")

	fp.close()


# import random

# if __name__ == "__main__":
# 	fp = open("test2.txt", "w")

# 	mm = {}

# 	while len(mm) < 100000:
# 		a = str(random.randint(-10000, 10000))
# 		b = str(random.randint(-10000, 10000))
# 		key = a + ":" + b
# 		mm[key] = a + " " + b + "\n"

# 	for key in mm:
# 		fp.write(mm[key])

# 	fp.close()
