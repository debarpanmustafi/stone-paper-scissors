print('''
|A SIMPLE STONE PAPER SCISSOR GAME|
\nGame Rules:
- Stone beats Scissors (Stone crushes Scissors)
- Scissors beats Paper (Scissors cut Paper)
- Paper beats Stone (Paper covers Stone)
- If both choices are the same, it's a tie.
''')

import random
import time

win_messages = [
    "Victory! The computer bows down to your greatness.",
    "You win! Somewhere, a robot is crying.",
    "Well played! Even the AI is impressed.",
    "Nice move! The machine didn't see that coming.",
    "Congratulations! You're officially smarter than an AI… for now.",
    "The computer tried its best, but you were better."]

lose_messages = [
    "Oops! The computer outsmarted you this time.",
    "Tough luck! Maybe try again with a different strategy?",
    "Well, that didn't go as planned. Want to try again?",
    "The AI overlord has spoken. You have been defeated.",
    "It’s okay, even champions have bad days.",
    "You lost. The computer is now celebrating… silently."]

goodbye_messages = [
    "Thanks for playing! The computer will miss you… kind of.",
    "Game over! Go out and conquer the real world now.",
    "Goodbye! The AI will sit here, waiting for your return.",
    "Come back soon! The computer needs another chance to win.",
    "You quit while you’re ahead… or behind. Either way, respect!",
    "Shutting down… but don’t worry, the AI will remember this."]

tie_messages = [
    "It’s a tie! Great minds think alike… or maybe just lucky guessing.",
    "A perfect balance. The universe approves.",
    "Nobody wins, nobody loses. Just pure equality!",
    "You and the computer are evenly matched. Try again?",
    "Well, that was anticlimactic… rematch?",
    "This round is a tie. But who will break the cycle?"
]

def game():
    choices = ["stone","paper","scissors"]

    while True:
        user = input("\nEnter your choice (Stone/Paper/Scissors): ").strip().lower()
        
        if user in choices:
            break
        else:
            print("\nSomething went wrong. Please try again.")

    print("\nUmm... The computer is thinking...")
    time.sleep(random.uniform(2, 3))

    computer = random.choice(choices)
    
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")

    if (user == computer):
        print("\n"+random.choice(tie_messages))
    elif (user, computer) in {("stone", "scissors"), ("scissors", "paper"), ("paper", "stone")}:
        print("\n"+random.choice(win_messages))
    else:
        print("\n"+random.choice(lose_messages))

playing = True

while playing:
    game()
    while True:
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again in ("yes", "y", "no", "n"):
            break
        else:
            print("Oops! Invalid input!")
    playing = play_again in ("yes", "y")

print("\n"+random.choice(goodbye_messages)+"\n")
