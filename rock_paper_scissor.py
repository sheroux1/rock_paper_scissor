

from random import randint

# player_input needs to be 1 for rock, 2 for scissor, 3 for paper
def printChoice(choice):
    if choice == 1:
        return(f'Rock')
    elif choice == 2:
        return(f'Paper')
    elif choice == 3:
        return(f'Scissor')

def whoWins(player_input):
    result = randint(1,3)
    print(f'You chose: {printChoice(player_input)}.')
    print(f'Computer chose: {printChoice(result)}.')
    if result == player_input:
        return f"It's a tie!"
    elif result == 1 and player_input == 3:
        return f'{printChoice(result)} beats {printChoice(player_input)}. Computer wins.'
    elif result == 2 and player_input == 1:
        return f'{printChoice(result)} beats {printChoice(player_input)}. Computer wins.'
    elif result == 3 and player_input == 2:
        return f'{printChoice(result)} beats {printChoice(player_input)}. Computer wins.'
    else:
        return f'{printChoice(player_input)} beats {printChoice(result)}. Player wins!'

print("\n\nLet's play! (type 'I quit' to quit)")
while True:
    choice = input("\nMake a choice. for Rock - [1], for Paper - [2], for Scissor - [3]. ")
    if choice.lower() == 'i quit':
        break
    # elif int(choice) > 3 or int(choice) < 1:
    #     print(f'{choice} is not a valid choice.')
    elif choice == '1' or choice == '2' or choice == '3':
        print(whoWins(int(choice)))
    else:
        print(f'{choice} is not a valid option.')

print("Thanks for playing!")