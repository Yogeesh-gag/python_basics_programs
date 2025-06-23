import random

stake=int(input("Enter the initial stake amount :"))
goal=int(input("Enter the goal amount :"))
trails=int(input("Enter number of trails :"))

def gambler_simulation(stake,goal,trails):
    total_bets=0
    total_wins=0

    for trail in range(trails):
        cash=stake
        while 0<cash<goal:
            total_bets+=1

            if random.random()<0.5:
                cash+=1
            else:
                cash-=1

        if cash==goal:
            total_wins+=1

    win_percentage=(total_wins/trails)*100
    loss_percentage=100-win_percentage

    print(f"\nTotal Trials       : {trails}")
    print(f"Total Wins         : {total_wins}")
    print(f"Total Losses       : {trails - total_wins}")
    print(f"Win Percentage     : {win_percentage:.2f}%")
    print(f"Loss Percentage    : {loss_percentage:.2f}%")
    print(f"Average Bets/Trial : {total_bets / trails:.2f}")

gambler_simulation(stake,goal,trails)