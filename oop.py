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
