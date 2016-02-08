
#dices

def dice():
    pygame.draw.rect(screen, black, (1128,177,300,300))
    d = random.randint(1,6)
    if d == 1:
        screen.blit(dice1, [1150, 200])
        p1.position * 1
    elif d == 2:
        screen.blit(dice2, [1150, 200])
    elif d == 3:
        screen.blit(dice3, [1150, 200])
    elif d == 4:
        screen.blit(dice4, [1150, 200])
    elif d == 5:
        screen.blit(dice5, [1150, 200])
    else:
        screen.blit(dice6, [1150, 200])