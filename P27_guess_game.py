def main():
    def new_game():
        guesses = []
        correct_guesses = 0
        question_number = 1

        for key in questions:
            print("................................")
            print(key)
            for i in options [question_number-1]:
                print(i)
            guess =input("Enter (A, B, C, or D): ").upper()
            guesses.append(guess)

            correct_guesses += check_answer(questions.get(key), guess)
            question_number += 1
        display_score (correct_guesses, guesses)




