# ══════════════════════════════
#    🎮 MINI PROJECT – ROCK, PAPER, SCISSORS 🎮
# ══════════════════════════════
# import random
# def decide_winner(user, computer):
#     if user == computer:
#         return "Tie"
#     elif (user == "rock" and computer == "scissors") or \
#          (user == "paper" and computer == "rock") or \
#          (user == "scissors" and computer == "paper"):
#         return "Player"
#     else:
#         return "Computer"
# def play_game():
#     rounds = int(input("How many rounds do you want to play? "))
#     user_score = 0
#     comp_score = 0
#     choices = ["rock", "paper", "scissors"]
#     for r in range(1, rounds + 1):
#         print(f"\nRound {r}")
#         user_choice = input("Enter Rock, Paper, or Scissors: ").lower()

#         if user_choice not in choices:
#             print("❌ Invalid choice, try again!")
#             continue

#         comp_choice = random.choice(choices)
#         print(f"Computer chose: {comp_choice}")

#         winner = decide_winner(user_choice, comp_choice)

#         if winner == "Player":
#             print("✅ You win this round!")
#             user_score += 1
#         elif winner == "Computer":
#             print("💻 Computer wins this round!")
#             comp_score += 1
#         else:
#             print("🤝 It's a tie!")
#     print("\n--- Final Results ---")
#     print(f"Your Score: {user_score}")
#     print(f"Computer Score: {comp_score}")

#     if user_score > comp_score:
#         print("🎉 You are the FINAL WINNER!")
#     elif comp_score > user_score:
#         print("💻 Computer is the FINAL WINNER!")
#     else:
#         print("🤝 It's a TIE overall!")
# while True:
#     play_game()
#     replay = input("\nDo you want to play again? (yes/no): ").lower()
#     if replay != "yes":
#         print("👋 Thanks for playing! Goodbye.")
#         break
