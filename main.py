"""
Higher or lower instagram follower_count game using gamedata.py file
This is day 14 from 100 days of python. it's ugly, but it works
"""
import art
import gamedata
import random
game_over = False
score = 0
print(art.logo)

# get a random name and # of follower_count
a = random.choice(gamedata.data)
b = random.choice(gamedata.data)

while not game_over:
    followB = b["follower_count"]
    followA = a["follower_count"]
    # re-select values until they do not match incase they are the same
    if a == b:
        while a == b:
            a = random.choice(gamedata.data)
            b = random.choice(gamedata.data)
    # checking values
    a_higher = False
    b_higher = False
    if followA > followB:
        # print(f'{a["name"]} has more follower_count with a total of {followA} million.')
        a_higher = True
    else:
        # print(f'{b["name"]} has more follower_count with a total of {followB} million.')
        b_higher = True
    # give two options:
    print(f'who has more followers?\nA: {a["name"]}\n{art.vs}\nB: {b["name"]} ?\n')

    # take input from the user
    guess = input('pick A or B:  ').lower()
    if guess == 'a' and a_higher or guess == 'b' and b_higher:
        score += 1
        print(f'GOOD GUESS! Your score is: {score}')
        if b_higher:
            a = b
            b = random.choice(gamedata.data)
            if a == b:
                while a == b:
                    b = random.choice(gamedata.data)
        else:
            b = random.choice(gamedata.data)
            if a == b:
                while a == b:
                    b = random.choice(gamedata.data)
    else:
        print(f'Wrong!\nYou scored: {score}!')
        game_over = True

print('\nGAME OVER.')
