import random

DESCRIPTION = "What number is missing in the progression?"


def get_round_data():
	start = random.randint(1, 20)
	step = random.randint(2, 10)
	length = random.randint(5, 10)

	progression = [str(start + i * step) for i in range(length)]

	hidden_index = random.randint(0, length - 1)
	correct_answer = progression[hidden_index]

	progression[hidden_index] = '..'
	question = " ".join(progression)

	return question, correct_answer
