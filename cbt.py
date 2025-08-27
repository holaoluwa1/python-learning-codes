# Project Overview:Develop a simple Computer-Based Testing (CBT) program in Python that hardcodes a set of at least 5 objective questions and their answers. The program should ask these questions to the user one by one and display the user's score at the end.

# Requirements:

# Hardcode Questions and Answers:
# Create at least 5 objective questions (multiple choice or true/false).
# Hardcode these questions and their correct answers in your program.

# Question Prompting:
# Prompt the user with each question one by one.
# Allow the user to input their answer for each question.

# Scoring System:
# Compare the user's answers with the correct answers.
# Keep track of the user's score.
# Display Results:At the end of the quiz, display the user's total score.

test_scores = []

def selection_options():
    print("""
          welcome 
    Login to start Exam
    1. Login
    2. Exit

    Choose an option:
    """)

    option = int(input())

    if option not in [1, 2,]:
        print("Invalid option")
        exit()
    
    if option == 1:
        login = input('Enter your name: ')
        print(f'{login} your password is 12345')
        password = input('Enter your password: ')
        if password == "12345":
            print('login sucessful\n1. Start Exam\n2. exit')
        else:
            print('incorrect password')
            selection_options() 

        option_start_exam = input('Enter option: ')
        if option_start_exam == '1':
            print('''Instructions:
            Answer all questions.
            Each question carries 10 mark.
            Choose the most appropriate answer from the options given (A–D).
            Best of luck.

            Questions
            1. In Python, which symbol is used for single-line comments? A. //  B. #  C. /* */   D. --

            2. Which of the following is not a factor influencing language variation? A. Age B. Gender C. Education D. Gravity

            3. The square of 12 is: A. 124 B. 144 C. 122 D. 112

            4. In literature, the word “theme” refers to: 
            A. The physical setting of the story 
            B. The central message or idea in a work 
            C. The names of characters D. The introduction of the plot

            5. Which escape character is used in Python to insert a new line? A. \.n B. \.t) C. (\.b) D. (\.\)
            ''')
            question1 = input('Answer question one:').lower()
            question2 = input('Answer question two:').lower()
            question3 = input('Answer question three:').lower()
            question4 = input('Answer question four:').lower()
            question5 = input('Answer question five:').lower()
            exam_score(question1,question2,question3,question4,question5)
            print(f'{login} your exam score is {sum(test_scores)}')
            selection_options()

        
        
            
        # selection_options()    
                




            
            

                   
    elif option == 2:
        print("Exiting the program...")
        exit()



def exam_score(question1,question2,question3,question4,question5):
    if question1 == "b":
        test_scores.append(10)
    if question2 == "d":
        test_scores.append(10)
    if question3 == "b":
        test_scores.append(10)
    if question4 == "b": 
        test_scores.append(10)
    if question5 == "a":
        test_scores.append(10)
        return    
        test_scores
        sum(test_scores)
    



selection_options()
