import random
import time




#Determine how much money does the user have extracting it form the txt file
file_path = 'C:\\Users\\Arturo Catalán\\Documents\\Python\\ruleta\\ruleta.txt'

with open(file_path, 'r') as file:
    line = file.readline()
    
line = line.split('=')
balance = float(line[1])

#Check if balance > 0

if balance == 0:
    add_balance = float(input("You have no money left\n How much do you want to add? $"))
    balance = add_balance
    with open(file_path, 'w') as file:
        file.write(f"balance={balance}")
    print(f"${add_balance} succesfully added!")



bet_amount = 0
bet = 10000

ALL_BETS = [
    ["Red", [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]],
    ["Black", [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]],
    ["Odd", [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]],
    ["Even", [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]],
    ["1 to 18", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]],
    ["19 to 36", [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]],
    ["1st Dozen", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]],
    ["2nd Dozen", [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]],
    ["3rd Dozen", [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]],
    ["Numbers",[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]] 
]

valid_numbers = ALL_BETS[-1][1]
valid_bets = [bet[0] for bet in ALL_BETS]


bet_amount = float(input("How much money do you want to bet? $"))

while bet_amount <= 0:
    print("Value must be greater than 0")
    
while bet_amount > balance:
    print(f"Insuficcient balance, you only have ${balance}")
    bet_amount = float(input("How much money do you want to bet?  $"))
        

bet = (input("Place your bet or type done if you are finished beting\n"  ))
if bet.lower()  == 'done':
    print("No more bets!")
    
while bet not in valid_bets and not (bet.isdigit() and int(bet) in valid_numbers):
    print("Invalid bet. Please try again.")
    bet = (input("Place your bet or type done if you are finished beting\n"  ))
    if bet.lower()  == 'done':
        print("No more bets!")


balance = balance - bet_amount
print(f"Succesfull betted ${bet_amount} on {bet}")

time.sleep(0.5)
print("Rolling!")
time.sleep(0.5)
ball_land = random.randint(0, 36)

RESET = "\033[0m"
GREEN = "\033[92m"
RED = "\033[91m"
BLACK = "\033[30m"

RED_COLOR = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]


if ball_land == 0:
    color_name = 'Green'
    color = GREEN

if ball_land in RED_COLOR:
    color_name = 'Red'
    color = RED
else:
    color_name = 'Black'
    color = BLACK


print(f"The ball landed on {color} {ball_land} {color_name}{RESET}")



if bet == color_name:
    winnings = bet_amount*2
    print(f"You won {GREEN}${winnings}{RESET}!")
    balance = balance + winnings


if bet and bet.isdigit() and int(bet) == ball_land:
    winnings = bet_amount * 35
    print(f"You won {GREEN}${winnings}{RESET}!")
    balance += winnings
elif bet and bet in [name for name, _ in ALL_BETS if ball_land in _]:
    if bet in ['Odd', 'Even', '1 to 18', '19 to 36']:
        winnings = bet_amount * 2
        print(f"You won {GREEN}${winnings}{RESET}!")
        balance += winnings
    elif bet in ['1st Dozen', '2nd Dozen', '3rd Dozen']:
        winnings = bet_amount * 3
        print(f"You won {GREEN}${winnings}{RESET}!")
        balance += winnings
else:
    print(f"You lost ${bet_amount}!")


with open(file_path, 'w') as file:
    file.write(f"balance={balance}")

print(f"Your new balance is {GREEN}${balance}{RESET}")


      



    
    
    
    
  





