import random

DESCRIPTION = 'What is the result of the expression?'


def get_round_data():
	num1 = random.randint(1, 20)
	num2 = random.randint(1, 20)
	operator = random.choice(['+', '-', '*'])

	question = f"{num1} {operator} {num2}"

	if operator == '+':
		answer = num1 + num2
	elif operator == '-':
		answer = num1 - num2
	else:
		answer = num1 * num2

	return question, str(answer)
