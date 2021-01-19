from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for item in question_data:
    q1 = item["question"]
    a1 = item["correct_answer"]
    question_bank += [Question(q1, a1)]

quiz = QuizBrain(question_bank)

while quiz:
    quiz.next_question()
    if quiz.question_number == len(question_bank):
        print(f"\nYou complete the Quiz\n"
              f"Your score is: {quiz.score}/{quiz.question_number}")
        break


