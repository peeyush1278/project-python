import random

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.total_questions = len(questions)

    def shuffle_options(self, options):
        random.shuffle(options)
        return options

    def ask_question(self, question_data):
        question, options, correct_answer = question_data
        shuffled_options = self.shuffle_options(options.copy())  # Shuffle options for this question
        print(f"\n{question}")
        for i, option in enumerate(shuffled_options):
            print(f"{i + 1}. {option}")

        try:
            answer = int(input("Enter the option number: "))
            selected_option = shuffled_options[answer - 1]
        except (ValueError, IndexError):
            print("Invalid input! Moving to the next question.")
            return False

        if selected_option == correct_answer:
            print("Correct!")
            return True
        else:
            print(f"Wrong! The correct answer is: {correct_answer}")
            return False

    def run_quiz(self):
        random.shuffle(self.questions)  # Shuffle the questions before starting the quiz
        for cnt, question_data in enumerate(self.questions):
            if cnt == 10:  # Limit to 10 questions
                break
            if self.ask_question(question_data):
                self.score += 1

    def display_result(self):
        percentage = (self.score / 10) * 100
        print(f"\nYou got {self.score} out of {10} correct.")
        print(f"Your percentage: {percentage:.2f}%")

# Define the quiz questions
quiz_questions = [
    ("What is the smallest planet in our solar system?", ["Mercury", "Venus", "Earth", "Mars"], "Mercury"),
    ("Which element has the chemical symbol 'O'?", ["Oxygen", "Gold", "Iron", "Osmium"], "Oxygen"),
    ("Who painted the Mona Lisa?", ["Leonardo da Vinci", "Michelangelo", "Vincent van Gogh", "Pablo Picasso"], "Leonardo da Vinci"),
    ("What is the longest river in the world?", ["Amazon River", "Nile River", "Yangtze River", "Mississippi River"], "Nile River"),
    ("Which country hosted the 2016 Summer Olympics?", ["Brazil", "Japan", "China", "USA"], "Brazil"),
    ("What is the main ingredient in guacamole?", ["Avocado", "Tomato", "Onion", "Corn"], "Avocado"),
    ("Which is the tallest mountain in the world?", ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"], "Mount Everest"),
    ("Which ocean is the largest?", ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Southern Ocean"], "Pacific Ocean"),
    ("Who discovered penicillin?", ["Alexander Fleming", "Marie Curie", "Isaac Newton", "Albert Einstein"], "Alexander Fleming"),
    ("Which country is famous for the Eiffel Tower?", ["France", "Italy", "Germany", "Spain"], "France"),
    ("What is the hardest substance in the human body?", ["Enamel", "Bone", "Hair", "Nails"], "Enamel"), 
    ("Who was the first President of the United States?", ["George Washington", "Abraham Lincoln", "Thomas Jefferson", "John Adams"], "George Washington"),
    ("What is the capital of Italy?", ["Rome", "Paris", "Berlin", "Madrid"], "Rome"), 
    ("Which is the largest organ in the human body?", ["Skin", "Liver", "Heart", "Lungs"], "Skin"), 
    ("What is the speed of light?", ["300,000 km/s", "150,000 km/s", "500,000 km/s", "100,000 km/s"], "300,000 km/s"), 
    ("Which is the longest river in the world?", ["Amazon River", "Nile River", "Yangtze River", "Mississippi River"], "Nile River"),
]

# Create a quiz instance and run it
quiz = Quiz(quiz_questions)
quiz.run_quiz()
quiz.display_result()