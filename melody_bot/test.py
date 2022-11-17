# data = None
global data
data = None

def test():
	# print(data)
	# global data

	if 1 < 0:
		data = 'Artem'
	else:
		data = ['Artem', 'Kirill']

	print(data)

test()
print(data)