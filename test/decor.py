def simple_func():
	print('Я самостоятельная функция')




def decorator_func(func):

	def wrap():
		print('Действие до выполнения функции')
		func()
		print('Действие после выполнения функции')

	return wrap


decorator_func(simple_func)()



# ['apple', 'orange']

# Array('apple', 'orange')