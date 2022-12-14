class Quiz:
    def __init__(self, q_list):
        self.q_no = 0
        self.q_list = q_list

    def ask_questions(self):
        your_score = 0
        option = "(True/False)? : "
        question_no = self.q_no
        for i in range(12):
            question_ans = self.q_list[question_no]
            question_no += 1
            ans = input(f"Q.{question_no} {question_ans.text + option}").lower()
            if ans == question_ans.ans.lower():
                your_score += 1
                print("You got it right!")
                print(f"The correct answer was: {question_ans.ans}")
                print(f"Your score is {your_score}/{question_no}")
            else:
                print("You got it right!")
                print(f"The correct answer was: {question_ans.ans}")
                print(f"Your score is {your_score} / {question_no}")

        print()
        print("Thanks for playing")
        print("We're working on it, You will see new question soon")


