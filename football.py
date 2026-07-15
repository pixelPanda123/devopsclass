# football_quiz.py

def run_quiz():
    # A list of questions, possible choices, and the correct answer index
    questions = [
        {
            "question": "If a team scores 3 touchdowns (7 points each) and 2 field goals (3 points each), how many points do they have?",
            "choices": ["A) 21", "B) 27", "C) 30", "D) 24"],
            "answer": "B"
        },
        {
            "question": "A quarterback throws for 300 yards in the first half and 180 yards in the second half. What is his total?",
            "choices": ["A) 480 yards", "B) 400 yards", "C) 500 yards", "D) 460 yards"],
            "answer": "A"
        },
        {
            "question": "A running back averages 5 yards per carry. If he carries the ball 15 times, how many total yards does he get?",
            "choices": ["A) 60 yards", "B) 80 yards", "C) 75 yards", "D) 90 yards"],
            "answer": "C"
        },
        {
            "question": "If a team is penalized 5 yards on one play and 10 yards on the next, how many total yards did they lose?",
            "choices": ["A) 15 yards", "B) 50 yards", "C) 8 yards", "D) 12 yards"],
            "answer": "A"
        },
        {
            "question": "A wide receiver caught 8 passes for a total of 96 yards. What was his average yards per catch?",
            "choices": ["A) 10 yards", "B) 11 yards", "C) 12 yards", "D) 14 yards"],
            "answer": "C"
        }
    ]

    score = 0
    print("--- Welcome to the Football Math Quiz! ---\n")

    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['question']}")
        for choice in q['choices']:
            print(choice)
        
        # Get user input and convert to uppercase
        user_answer = input("Your answer (A, B, C, or D): ").strip().upper()
        
        if user_answer == q['answer']:
            print("Correct! 🏈\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {q['answer']}.\n")

    # Final results
    print("--- Quiz Finished! ---")
    print(f"Your final score: {score} out of {len(questions)}")
    
    if score == len(questions):
        print("Perfect score! You're the MVP! 🏆")
    elif score >= len(questions) // 2:
        print("Good job! Solid game plan.")
    else:
        print("Hit the film room and try again!")

if __name__ == "__main__":
    run_quiz()