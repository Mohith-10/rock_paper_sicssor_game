import random

def get_user_choice():
    user_choice=input("Enter your Choice(rock,paper,sicssor ): ").lower()
    while user_choice not in ['rock','paper','sicssor']:
        user_choice=input("Invalid choice.Enter choice (rock,paper,sicssor : )").lower()
    return user_choice

def get_computer_choice():
    return random.choice(['rock','paper','sicssor'])

def determine_winner(user_choice,computer_choice):
    if user_choice==computer_choice:
        return "it's Tie!"
    elif (user_choice == 'rock' and computer_choice == 'sicssor') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'sicssor' and computer_choice =='paper'):
        return "you Win!"
    else:
      return "computer win!"
    

def play_game():
    print("Welcome to rock , paper & sicssor")
    user_choice=get_user_choice()
    computer_choice=get_computer_choice()
    print(f"\nyour choice is : {user_choice}")
    print(f"computer choice is : {computer_choice}")
    result=determine_winner(user_choice,computer_choice)
    print(result)

if __name__=="__main__":
    play_game()