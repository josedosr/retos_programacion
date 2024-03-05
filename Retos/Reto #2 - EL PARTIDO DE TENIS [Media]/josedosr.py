import time
from time import sleep

def tennis (points = ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1']):

    player_1 = 0
    player_2 = 0
    point_chart = ['Love', '15', '30', '40']
    finish = False

    print('Player 1 - Player 2')

    for point in points:
        
        player_1 += 1 if point.upper() == 'P1' else 0
        player_2 += 1 if point.upper() == 'P2' else 0
        
        if player_1 >= 3 and player_2 >= 3:
            if not finish and -1 <= (player_1 - player_2) <= 1:
                print('Deuce' if player_1 == player_2 else
                     'Ventaja Player 1' if player_1 > player_2 else 'Ventaja Player 2')
                sleep(1)
            
            else:
                finish = True

        else: 
            if player_1 < 4 and player_2 < 4:
                print(f'{point_chart[player_1]} - {point_chart[player_2]}')
                sleep(1)
            else:
                finish = True

    print("Los puntos jugados no son correctos" if not finish else
          "Ha ganado el P1" if player_1 > player_2 else "Ha ganado el P2")


tennis()


