from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

Question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    Question_bank.append(new_question)

quiz = QuizBrain(Question_bank)

while quiz.still_has_questions() :
    quiz.next_question()

print("You've completed this quiz.")
print(f"Your final score is {quiz.score}/{len(Question_bank)}")