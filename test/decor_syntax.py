def decorator_func(self):

	def decorator(func):
		print('Действие до выполнения функции')

		return func

	return decorator


@decorator_func
def simple_func():
	print('Я самостоятельная функция')
