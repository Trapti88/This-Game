# Author : - Trapti Meshram (Aliya)
# Making Date : 19/10/2022

import random
sy = ['Stone','Papar','Caeser']
ch = 1
c = 10
your_point = 0
computer_point = 0
count=0

while (ch<=10):
    cho = random.choice(sy)
    a = input('press S for Stone , P for Papar , C for Caeser\nyour choice:').capitalize()
    print("\n$$$$$$$$$$$$ TURN -",str(count+1),"$$$$$$$$$$$$$$$")
    print('computer choice: '+cho)
    if a == 'S' and cho == 'Papar':
        print('you win ')
        your_point = your_point + 1
    elif a == 'P' and cho == 'Papar':
        print('its a tie')
    elif a == 'C' and cho == 'Paper':
        print('you loose')
        computer_point = computer_point + 1

    elif a == 'S' and cho == 'Stone':
        print('its a tie')
    elif a == 'P' and cho == 'Stone':
        print('you loose')
        computer_point = computer_point + 1
    elif a == 'C' and cho == 'Stone':
        print('you win')
        your_point = your_point + 1
    elif a == 'S' and cho == 'Caeser':
        print('you loose')
        computer_point = computer_point + 1
    elif a == 'P' and cho == 'Caeser':
        print('you win')
        your_point = your_point + 1
    elif a == 'C' and cho == 'Caeser':
        print('its a tie')
    else:
        print('wrong input')
        c = c+1
    print('your point: ',your_point,'computer point: ',computer_point)

    c = c-1
    print(c, 'chances left')
    ch+=1
if your_point > computer_point:
    print('yay! you won')
else:
    print('oops! you lost')