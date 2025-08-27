# Sample Question and Evaluation Criteria:

# Question: Explain the process of photosynthesis.

# Ideal Answer: Photosynthesis is a process used by plants and other organisms to convert light energy into chemical energy. It occurs in the chloroplasts of plant cells. The process involves the absorption of light by chlorophyll, the conversion of carbon dioxide and water into glucose and oxygen, and the storage of energy in the form of ATP.

# Keywords and Weights:
# Photosynthesis (2 points)
# Light energy (1 point)
# Chemical energy (1 point)
# Chloroplasts (2 points)
# Chlorophyll (1 point)
# Carbon dioxide (1 point)
# Water (1 point)
# Glucose (1 point)
# Oxygen (1 point)
# ATP (1 point)

scores = []
# check_answer = 'Photosynthesis, light energy, chemical energy, chloroplasts, chlorophyll, carbon dioxide, water,glucose,oxygen,atp'

def selection_options():
    print("""
    1. Start Exam
    2. Exit
    Choose an option:
    """)
    try:
        option = int(input())
    except:
        print("Error... Enter option 1 or 2") 
        exit()     

    if option not in [1, 2,]:
        print("Invalid option")
        exit()

    if option == 1:
        start_exam()
        print(scores)
    elif option == 2:
        print("Exiting the program...")
        exit()
    


def start_exam():

    for question in exam_question:

        print(question['question'])
        answer = input("Enter your answer: ").lower().split()
        for keyword, score in question["keyword"].items():
            if keyword in answer:
                scores.append(score)
    







                  
exam_question = [
    {
        "question": "What is photosynthesis?", 
        "keyword":{"plants": 2, "sunlight": 3,"energy": 2, "chlorophyll": 3},
    },
    {
       "question": "What is globalization?", 
       "keyword": {"economy": 2, "culture": 3, "interconnected": 2, "trade": 3}
    },
    {
        "question": "What causes rainfall?",  
        "keyword": {"evaporation": 2, "condensation": 3, "precipitation": 2, "water cycle": 3}
    },    
    {    "question": "What is democracy?", 
        "keyword": {"government": 2, "people": 3, "voting": 2, "freedom": 3,}
    },    
    {
        "question": "What is climate change?", 
        "keyword": {"temperature": 2, "greenhouse gases": 3, "global warming": 2, "environment": 3} 
    }
    ]







selection_options()
