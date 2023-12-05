class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = questions_list

    def still_has_questions(self):
        if self.question_number >= 12:
            print("Quiz ha ended")
            print(f'Your Final Score is: {self.score}/{self.question_number}')
            return False
        else:
            return len(self.questions_list) - self.question_number != 0

    def next_question(self):

        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}:  {current_question.text} (True/False)")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.score += 1
            print("You got it right")
            print(f"Your current score is: {self.score}/{self.question_number}")
        else:
            print("That's wrong")
        print(f"Correct answer was {correct_ans}")




