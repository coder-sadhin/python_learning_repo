def ask_question(question, options, correct_answer):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    user_choice = int(input("Enter your choice (1, 2, 3, ...): "))
    if user_choice == correct_answer:
        print("Correct!\n")
    else:
        print(f"Oops! The correct answer was {correct_answer}.\n")


questions = [
    {
        "question": "What does the acronym 'CPU' stand for?",
        "options": ["Central Processing Unit", "Computer Peripheral Unit", "Control Processing Unit"],
        "correct_answer": 1,
    },
    {
        "question": "Which data structure follows the 'Last In, First Out' (LIFO) principle?",
        "options": ["Queue", "Stack", "Linked List"],
        "correct_answer": 2,
    },
    {
        "question": "What does the acronym 'CPU' stand for?",
        "options": ["Central Processing Unit", "Computer Peripheral Unit", "Control Processing Unit"],
        "correct_answer": 1,
    },
    # Add more questions here...
]

for q in questions:
    ask_question(q["question"], q["options"], q["correct_answer"])