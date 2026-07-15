# soccer_trivia_quiz.py

def run_quiz():
    # A list of genuine soccer trivia questions, choices, and answers
    questions = [
        {
            "question": "Which country has won the most FIFA World Cup titles in history?",
            "choices": ["A) Germany", "B) Italy", "C) Brazil", "D) Argentina"],
            "answer": "C"  # Brazil (5 titles)
        },
        {
            "question": "Who is the all-time top goalscorer in UEFA Champions League history?",
            "choices": ["A) Lionel Messi", "B) Cristiano Ronaldo", "C) Robert Lewandowski", "D) Karim Benzema"],
            "answer": "B"  # Cristiano Ronaldo
        },
        {
            "question": "Which club has won the most European Cup / UEFA Champions League titles?",
            "choices": ["A) Real Madrid", "B) AC Milan", "C) Liverpool", "D) Barcelona"],
            "answer": "A"  # Real Madrid
        },
        {
            "question": "Which player holds the record for the most goals scored in a single calendar year (91 goals in 2012)?",
            "choices": ["A) Pelé", "B) Gerd Müller", "C) Cristiano Ronaldo", "D) Lionel Messi"],
            "answer": "D"  # Lionel Messi
        },
        {
            "question": "In what year did the Premier League officially rebrand and begin its inaugural season?",
            "choices": ["A) 1988", "B) 1990", "C) 1992", "D) 1994"],
            "answer": "C"  # 1992
        }
    ]

    score = 0
    print("--- Welcome to the Ultimate Football Trivia Quiz! ---\n")

    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['question']}")
        for choice in q['choices']:
            print(choice)
        
        user_answer = input("Your answer (A, B, C, or D): ").strip().upper()
        
        if user_answer == q['answer']:
            print("Back of the net! Correct! \n")
            score += 1
        else:
            print(f"Ref says no. The correct answer was {q['answer']}.\n")

    # Final results
    print("--- Full-Time Whistle! ---")
    print(f"Your final score: {score} out of {len(questions)}")
    
    if score == len(questions):
        print("Tactical masterclass! You've won the Ballon d'Or!")
    elif score >= len(questions) // 2:
        print("Solid performance. You qualify for European football.")
    else:
        print("Relegation form. Back to the training pitch to watch the tape!")

if __name__ == "__main__":
    run_quiz()
