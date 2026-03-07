import prompt

ROUNDS_COUNT = 3

# u_a = user_answer, c_a = correct_answer.
# Пришлось сократить, чтобы влезть в 80 символов.


def run_game(description, get_round_data):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(description)

    for _ in range(ROUNDS_COUNT):
        question, c_a = get_round_data()
        print(f"Question: {question}")
        u_a = prompt.string("Your answer: ")

        if u_a != c_a:
            print(f"'{u_a}' is wrong answer ;(. Correct answer was '{c_a}'.")
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")
