import random

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.total_questions = len(questions)

    def shuffle_options(self, options):
        random.shuffle(options)
        return options

    def ask_question(self, question, options, correct_answer):
        print(f"\n{question}")
        shuffled_options = self.shuffle_options(options)
        for i, option in enumerate(shuffled_options):
            print(f"{i + 1}. {option}")

        try:
            answer = int(input("Enter the option number: "))
            selected_option = shuffled_options[answer - 1]
        except (ValueError, IndexError):
            print("Invalid input! Moving to the next question.")
            return False

        return selected_option == correct_answer

    def run_quiz(self):
        for question_data in self.questions:
            question, options, correct_answer = question_data
            if self.ask_question(question, options, correct_answer):
                self.score += 1

    def display_result(self):
        percentage = (self.score / self.total_questions) * 100
        print(f"\nYou got {self.score} out of {self.total_questions} correct.")
        print(f"Your percentage: {percentage:.2f}%")

# Define the quiz questions
quiz_questions = [
    ("What is the capital of France?", ["Paris", "London", "Rome", "Berlin"], "Paris"),
    ("Which planet is known as the Red Planet?", ["Venus", "Mars", "Jupiter", "Saturn"], "Mars"),
    ("Who wrote 'To Kill a Mockingbird'?", ["Harper Lee", "J.K. Rowling", "Ernest Hemingway", "Mark Twain"], "Harper Lee"),
    ("What is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe", "Shark"], "Blue Whale"),
    ("What is the hardest natural substance on Earth?", ["Gold", "Iron", "Diamond", "Graphite"], "Diamond"),
]

# Create a quiz instance and run it
quiz = Quiz(quiz_questions)
quiz.run_quiz()
quiz.display_result()
