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

        if selected_option == correct_answer:
            print("Correct!")
            return True
        else:
            print(f"Wrong! The correct answer is: {correct_answer}")
            return False

    def run_quiz(self):
        cnt=0
        for question_data in self.questions:
            if cnt==10:
                break
            cnt+=1
            question, options, correct_answer = question_data
            if self.ask_question(question, options, correct_answer):
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
    ("What is the largest desert in the world?", ["Sahara", "Gobi", "Kalahari", "Arctic"], "Sahara"),
    ("What is the fastest land animal?", ["Cheetah", "Lion", "Tiger", "Horse"], "Cheetah"),
    ("What is the chemical symbol for water?", ["H2O", "O2", "CO2", "N2"], "H2O"),
    ("Who wrote 'Pride and Prejudice'?", ["Jane Austen", "Emily Brontë", "Charles Dickens", "Mark Twain"], "Jane Austen"),
    ("What is the largest planet in our solar system?", ["Jupiter", "Saturn", "Neptune", "Uranus"], "Jupiter"),
    ("Which country is known as the Land of the Rising Sun?", ["Japan", "China", "South Korea", "Thailand"], "Japan"),
    ("What is the hardest substance in the human body?", ["Enamel", "Bone", "Hair", "Nails"], "Enamel"),
    ("Who was the first President of the United States?", ["George Washington", "Abraham Lincoln", "Thomas Jefferson", "John Adams"], "George Washington"),
    ("What is the capital of Italy?", ["Rome", "Paris", "Berlin", "Madrid"], "Rome"),
    ("Which is the largest organ in the human body?", ["Skin", "Liver", "Heart", "Lungs"], "Skin"),
    ("What is the speed of light?", ["300,000 km/s", "150,000 km/s", "500,000 km/s", "100,000 km/s"], "300,000 km/s"),
    ("Which planet is known as the Earth's twin?", ["Venus", "Mars", "Jupiter", "Saturn"], "Venus"),
    ("Who wrote '1984'?", ["George Orwell", "Aldous Huxley", "Ray Bradbury", "J.D. Salinger"], "George Orwell"),
    ("What is the chemical symbol for gold?", ["Au", "Ag", "Pb", "Fe"], "Au"),
    ("Which animal is known for its black and white stripes?", ["Zebra", "Tiger", "Panda", "Skunk"], "Zebra"),
    ("Who invented the telephone?", ["Alexander Graham Bell", "Thomas Edison", "Nikola Tesla", "Guglielmo Marconi"], "Alexander Graham Bell"),
    ("What is the capital of Egypt?", ["Cairo", "Alexandria", "Giza", "Luxor"], "Cairo"),
    ("Which country is known for the Great Wall?", ["China", "Japan", "South Korea", "Vietnam"], "China"),
    ("What is the national flower of Japan?", ["Cherry Blossom", "Rose", "Lotus", "Sunflower"], "Cherry Blossom"),
    ("Who is known as the Father of Computers?", ["Charles Babbage", "Alan Turing", "Bill Gates", "Steve Jobs"], "Charles Babbage"),
    ("Which planet has the most moons?", ["Jupiter", "Saturn", "Uranus", "Neptune"], "Jupiter"),
    ("Which country is known for the pyramids?", ["Egypt", "Mexico", "Greece", "India"], "Egypt"),
    ("Who wrote 'The Catcher in the Rye'?", ["J.D. Salinger", "F. Scott Fitzgerald", "Ernest Hemingway", "Mark Twain"], "J.D. Salinger"),
    ("Which is the smallest continent?", ["Australia", "Europe", "Antarctica", "South America"], "Australia"),
    ("What is the largest island in the world?", ["Greenland", "Australia", "Madagascar", "Iceland"], "Greenland"),
    ("Which gas do plants absorb from the atmosphere?", ["Carbon Dioxide", "Oxygen", "Nitrogen", "Helium"], "Carbon Dioxide"),
    ("Who was the first man to walk on the moon?", ["Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "Michael Collins"], "Neil Armstrong"),
    ("Which is the most spoken language in the world?", ["Mandarin Chinese", "English", "Spanish", "Hindi"], "Mandarin Chinese"),
    ("What is the tallest waterfall in the world?", ["Angel Falls", "Niagara Falls", "Victoria Falls", "Iguazu Falls"], "Angel Falls"),
    ("Which planet is closest to the sun?", ["Mercury", "Venus", "Earth", "Mars"], "Mercury"),
    ("What is the national animal of India?", ["Tiger", "Elephant", "Lion", "Peacock"], "Tiger"),
    ("Who wrote 'Moby Dick'?", ["Herman Melville", "Charles Dickens", "Jules Verne", "Mark Twain"], "Herman Melville"),
    ("What is the main gas found in the air we breathe?", ["Nitrogen", "Oxygen", "Carbon Dioxide", "Hydrogen"], "Nitrogen"),
    ("Which country is home to the kangaroo?", ["Australia", "New Zealand", "South Africa", "India"], "Australia"),
    ("What is the largest ocean on Earth?", ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Southern Ocean"], "Pacific Ocean"),
    ("What is the chemical symbol for iron?", ["Fe", "Ir", "In", "I"], "Fe"),
    ("Who painted the ceiling of the Sistine Chapel?", ["Michelangelo", "Leonardo da Vinci", "Raphael", "Donatello"], "Michelangelo"),
    ("Which organ is responsible for pumping blood in the human body?", ["Heart", "Lungs", "Liver", "Kidneys"], "Heart"),
    ("What is the capital of Canada?", ["Ottawa", "Toronto", "Vancouver", "Montreal"], "Ottawa"),
    ("Which planet is known for its rings?", ["Saturn", "Jupiter", "Uranus", "Neptune"], "Saturn"),
    ("What is the smallest bone in the human body?", ["Stapes", "Femur", "Tibia", "Ulna"], "Stapes"),
    ("Which country is known for the Eiffel Tower?", ["France", "Italy", "Germany", "Spain"], "France"),
    ("What is the capital of Russia?", ["Moscow", "Saint Petersburg", "Sochi", "Kazan"], "Moscow"),
    ("Which scientist is known for the theory of relativity?", ["Albert Einstein", "Isaac Newton", "Galileo Galilei", "Stephen Hawking"], "Albert Einstein"),
    ("What is the chemical symbol for sodium?", ["Na", "S", "Sn", "N"], "Na"),
    ("Which country is famous for tulips?", ["Netherlands", "France", "Germany", "Belgium"], "Netherlands"),
    ("Who was the first woman to win a Nobel Prize?", ["Marie Curie", "Rosalind Franklin", "Ada Lovelace", "Jane Goodall"], "Marie Curie"),
    ("Which planet is known as the Blue Planet?", ["Earth", "Neptune", "Uranus", "Mars"], "Earth"),
    ("What is the most abundant gas in the Earth's atmosphere?", ["Nitrogen", "Oxygen", "Carbon Dioxide", "Argon"], "Nitrogen"),
    ("Which country is known for the Colosseum?", ["Italy", "Greece", "Turkey", "Spain"], "Italy"),
    ("What is the capital of Australia?", ["Canberra", "Sydney", "Melbourne", "Brisbane"], "Canberra"),
    ("Who discovered gravity?", ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Johannes Kepler"], "Isaac Newton"),
    ("Which animal is the largest living species?", ["Blue Whale", "Elephant", "Great White Shark", "Giraffe"], "Blue Whale"),
    ("What is the capital of Spain?", ["Madrid", "Barcelona", "Valencia", "Seville"], "Madrid"),
    ("Which country is famous for sushi?", ["Japan", "China", "Thailand", "Vietnam"], "Japan"),
    ("Who wrote 'Hamlet'?", ["William Shakespeare", "George Bernard Shaw", "Oscar Wilde", "Charles Dickens"], "William Shakespeare"),
    ("What is the chemical symbol for silver?", ["Ag", "Au", "Si", "Pb"], "Ag"),
    ("Which continent is the Sahara Desert located on?", ["Africa", "Asia", "Australia", "North America"], "Africa"),
    ("Who was the first person to fly solo across the Atlantic Ocean?", ["Charles Lindbergh", "Amelia Earhart", "Howard Hughes", "Orville Wright"], "Charles Lindbergh"),
    ("What is the largest land animal?", ["Elephant", "Rhino", "Hippopotamus", "Giraffe"], "Elephant"),
    ("What is the capital of Brazil?", ["Brasilia", "Rio de Janeiro", "Sao Paulo", "Salvador"], "Brasilia"),
    ("Who was the first woman to fly solo across the Atlantic Ocean?", ["Amelia Earhart", "Bessie Coleman", "Harriet Quimby", "Jacqueline Cochran"], "Amelia Earhart"),
    ("Which is the smallest country in the world?", ["Vatican City", "Monaco", "San Marino", "Liechtenstein"], "Vatican City"),
    ("What is the capital of Germany?", ["Berlin", "Munich", "Frankfurt", "Hamburg"], "Berlin"),
    ("Which country is known for Mount Fuji?", ["Japan", "China", "South Korea", "Thailand"], "Japan"),
    ("What is the chemical symbol for potassium?", ["K", "P", "Pb", "Pt"], "K"),
    ("Which planet is farthest from the sun?", ["Neptune", "Uranus", "Saturn", "Pluto"], "Neptune"),
    ("Who invented the light bulb?", ["Thomas Edison", "Nikola Tesla", "Alexander Graham Bell", "Benjamin Franklin"], "Thomas Edison"),
    ("What is the capital of Mexico?", ["Mexico City", "Guadalajara", "Monterrey", "Cancun"], "Mexico City"),
    ("What is the largest species of shark?", ["Great White Shark", "Hammerhead Shark", "Whale Shark", "Tiger Shark"], "Whale Shark"),
    ("What is the chemical symbol for chlorine?", ["Cl", "Cr", "Co", "Ca"], "Cl"),
    ("Who wrote 'The Odyssey'?", ["Homer", "Virgil", "Sophocles", "Aristophanes"], "Homer"),
    ("What is the capital of India?", ["New Delhi", "Mumbai", "Kolkata", "Chennai"], "New Delhi"),
    ("What is the smallest mammal?", ["Bumblebee Bat", "Pygmy Shrew", "Etruscan Shrew", "Mouse Lemur"], "Bumblebee Bat"),
    ("Which country is known for pizza?", ["Italy", "France", "Spain", "Greece"], "Italy"),
    ("Who wrote 'The Great Gatsby'?", ["F. Scott Fitzgerald", "Ernest Hemingway", "John Steinbeck", "William Faulkner"], "F. Scott Fitzgerald"),
    ("What is the chemical symbol for carbon?", ["C", "Ca", "Cu", "Co"], "C"),
    ("Which is the largest planet in the solar system?", ["Jupiter", "Saturn", "Neptune", "Uranus"], "Jupiter")
]


# Create a quiz instance and run it
quiz = Quiz(quiz_questions)
quiz.run_quiz()
quiz.display_result()
