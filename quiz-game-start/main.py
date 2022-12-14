from data import question_data
from question_model import Question
from quiz_brain import Quiz

question_bank = []
for i in question_data:
    question = i["text"]
    answer = i["answer"]
    new_qa = Question(question, answer)
    question_bank.append(new_qa)
quiz_start = Quiz(question_bank)
quiz_start.ask_questions()

