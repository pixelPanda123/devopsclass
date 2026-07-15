# soccer_math_quiz.py

def run_quiz():
    # A list of soccer math questions, choices, and correct answers
    questions = [
        {
            "question": "In the Premier League, a team wins 5 matches, draws 3, and loses 2. How many total points do they have?",
            "choices": ["A) 15 points", "B) 18 points", "C) 20 points", "D) 17 points"],
            "answer": "B"  # (5 wins * 3pts) + (3 draws * 1pt) = 15 + 3 = 18
        },
        {
            "question": "A striker scored 24 goals in 32 matches. What is their exact goals-per-match average?",
            "choices": ["A) 0.50", "B) 0.65", "C) 0.75", "D) 0.80"],
            "answer": "C"  # 24 / 32 = 0.75
        },
        {
            "question": "A team finished the season scoring 65 goals but conceded 42. What is their final Goal Difference (GD)?",
            "choices": ["A) +23", "B) -23", "C) +107", "D) +27"],
            "answer": "A"  # 65 - 42 = 23
        },
        {
            "question": "If a winger records an assist every 180 minutes, how many assists do they project to get in a 900-minute tournament?",
            "choices": ["A) 3 assists", "B) 4 assists", "C) 5 assists", "D) 6 assists"],
            "answer": "C"  # 900 / 180 = 5
        },
        {
            "question": "A goalkeeper keeps 12 clean sheets in a 38-game season. Rounding to the nearest whole percentage, what percentage of games did they keep a clean sheet?",
            "choices": ["A) 28%", "B) 32%", "C) 35%", "D) 40%"],
            "answer": "B"  # (12 / 38) * 100 = 31.57% -> 32%
        }
    ]

    score = 0
    print("--- Welcome to the Real Football (Soccer) Math Quiz! ---\n")

    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['question']}")
        for choice in q['choices']:
            print(choice)
        
        user_answer = input("Your answer (A, B, C, or D): ").strip().upper()
        
        if user_answer == q['answer']:
            print("Goal!!! Correct! ⚽\n")
            score += 1
        else:
            print(f"Missed the target. The correct answer was {q['answer']}.\n")

    # Final results
    print("--- Full-Time Whistle! ---")
    print(f"Your final score: {score} out of {len(questions)}")
    
    if score == len(questions):
        print("Flawless victory! You've won the Ballon d'Or! 🏆")
    elif score >= len(questions) // 2:
        print("Solid performance. Safely mid-table.")
    else:
        print("Relegation zone form. Back to the training pitch!")

if __name__ == "__main__":
    run_quiz()
