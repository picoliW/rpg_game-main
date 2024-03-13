goblins_killed_goal = 10
goblins_killed_reward = 25
dragons_killed_goal = 5
dragons_killed_reward = 5


def achievements_progress():
    from messagess.goblin_killed import goblins_killed
    from messagess.dragon_killed import dragons_killed
    global goblins_killed_goal
    global goblins_killed_reward

    if goblins_killed > goblins_killed_goal:
        goblins_killed = goblins_killed_goal
    if dragons_killed > dragons_killed_goal:
        dragons_killed = dragons_killed_goal
    
    print(f'Goblins killed {goblins_killed} / {goblins_killed_goal} - Reward: {goblins_killed_reward} gold')
    
    
    print(f'Dragons killed {dragons_killed} / {dragons_killed_goal} - Reward: {dragons_killed_reward}')

    

    from mainMenu import menu
    menu()