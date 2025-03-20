def get_winner(p1, p2):
    if p1 == p2:
        return "It's a tie"
    elif p1 == 'rock':
        if p2 == 'paper':
            return '2nd player wins.'
        elif p2 == 'scissor':
            return '1st player wins'
    elif p1 == 'scissors':
        if p2 == 'paper':
            return '1st player wins'
        else:
            return '2nd player wins'
    elif p1 == 'paper':
        if p2 == 'scissors':
            return '2nd player wins'
        else:
            return '1st player wins'
    else:
        return 'Invalid input'
player1 = input('First player: rock or paper or scissors: ')
player2 = input('Second player: rock or paper or scissors: ')
print(get_winner(player1, player2))

#another solve

def get_winner(p1, p2):
    if p1 == 'rock' and p2 == 'paper':
        return 'Second player wins'
    elif p1 == 'rock' and p2 == 'scissors':
        return 'First player wins'
    elif p1 == 'paper' and p2 == 'rock':
           return 'First player wins!'
    elif p1 == 'paper' and p2 == 'scissors':
       return'Second player wins!'
    elif p1 == 'scissors' and p2 == 'rock':
       return'Second player wins!'
    elif p1 == 'scissors' and p2 == 'paper':
       return 'First player wins!'
    else:
       return 'Tie'
player1 = input('First player: rock, paper or scissors: ')
player2 = input('Second Player: rock, paper or scissors: ')
print(get_winner(player1, player2))