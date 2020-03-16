import random

def playGame(switch):
    doorChosen = random.randint(0, 2)
    doorWithCar = random.randint(0, 2)
    
    return (doorChosen == doorWithCar and not switch) or (doorChosen != doorWithCar and switch)

def main():
    totalTrials = 10
    timesWonSwitching = 0
    timesWonStaying = 0

    for j in range(6):
        for i in range(totalTrials):
            result = playGame(switch=True)
            if result:
                timesWonSwitching += 1
        
        for i in range(totalTrials):
            result = playGame(switch=False)
            if result:
                timesWonStaying += 1
        
        print("\nTRIALS: {}".format(totalTrials))
        print("Times won by switching: {} | {}%".format(timesWonSwitching, (float(timesWonSwitching) / totalTrials) * 100))
        print("Times won by staying: {} | {}%".format(timesWonStaying, (float(timesWonStaying) / totalTrials) * 100))
        totalTrials *= 10



if __name__ == "__main__":
    main()