import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_gcd(a, b):
	while b:
		a, b = b, a % b
	return a


def get_round_data():
	num1 = random.randint(1, 100)
	num2 = random.randint(1, 100)
	question = f"{num1} {num2}"
	answer = str(get_gcd(num1, num2))
	return question, answer
