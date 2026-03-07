import random

import prompt

# u_a = user_answer, c_a = correct_answer.
# Пришлось сократить, чтобы влезть в 80 символов.


def main():
	print("Welcome to the Brain Games!")
	name = prompt.string('May I have your name? ')
	print(f'Hello, {name}!')
	print('Answer "yes" if the number is even, otherwise answer "no".')

	rounds_count = 3
	for _ in range(rounds_count):
		number = random.randint(1, 100)
		print(f"Question: {number}")
		u_a = prompt.string("Your answer: ")

		c_a = 'yes' if number % 2 == 0 else 'no'

		if u_a == c_a:
			print("Correct!")
		else:
			print(f"'{u_a}' is wrong answer ;(. Correct answer was '{c_a}'.")
			print(f"Let's try again, {name}!")
			return

	print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
