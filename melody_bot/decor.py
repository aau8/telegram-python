def simple_func():
	print('Я самостоятельная функция')

def decorator_func(func):
	print('Действие до выполнения функции')
	func()
	print('Действие после выполнения функции')


decorator_func(simple_func)
