import random

DESCRIPTION = 'What is the result of the expression?'


def get_round_data():
	num1 = random.randint(1, 20)
	num2 = random.randint(1, 20)
	operator = random.choice(['+', '-', '*'])

	question = f"{num1} {operator} {num2}"

	match operator:
		case '+':
			answer = num1 + num2
		case '-':
			answer = num1 - num2
		case '*':
			answer = num1 * num2
		case _:
			raise ValueError(f"Unknown operator: {operator}")

	return question, str(answer)


