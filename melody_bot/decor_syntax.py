def decorator_func(func):
	print('Действие до выполнения функции')
	func()
	print('Действие после выполнения функции')


@decorator_func
def simple_func():
	print('Я самостоятельная функция')