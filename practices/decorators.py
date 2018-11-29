PASSWORD = '12345'

def password_required(func):
	def wrapper():
		password = input('Cual es tu contrasena?')

		if password == PASSWORD:
			return func()
		else:
			print('Contrasena incorrecta')

	return	wrapper

@password_required
def needs_password():
	print('Contrasena correcta')


def upper(func):
	def wrapper(*args, **kwargs):
		result = func(*args, **kwargs).upper()

		return result

	return wrapper


@upper
def say_my_name(name):
	return f'Hola, {name}'

if __name__ == '__main__':
	print(say_my_name('Gabriel'))
	# needs_password()
