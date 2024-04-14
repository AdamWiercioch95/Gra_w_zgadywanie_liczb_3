from flask import Flask


app = Flask(__name__)


def user_input():
    possible_inputs = ["too big", "too small", "you win"]
    while True:
        print("[too big", "too small", "you win]")
        user_answer = input().lower()
        if user_answer in possible_inputs:
            break
        print("Please enter a valid input.")
    return user_answer


@app.route("/")
def guess_number():
    print("Think of a number between 1 and 1000 and I will guess it in max. 10 tries.")
    minimum = 0
    maximum = 1000
    user_answer = ''
    while user_answer != 'you win':
        guess = int((maximum - minimum) / 2) + minimum
        print(f"I'm guessing: {guess}")
        user_answer = user_input()
        if user_answer == 'too big':
            maximum = guess
        elif user_answer == 'too small':
            minimum = guess

    print("I knew it!!")


if __name__ == "__main__":
    app.run()
