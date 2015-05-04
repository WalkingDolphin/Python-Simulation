#Written for Python 2.7.8
import random
#Defining Variables
currentPopulation = 7.0
infected = 0
speedOfInfection = 0
speedPopulation = 0
amount = 0

#Calculation Function
def calc(current, speed):
    amount = current * speed
    infected = amount * 1000000000
    print("There are", infected, "people that got malaria.")
    
print("Ben and Toby's simulation")
print("                                                               ")
print("Mosquitos are spreading deadly diseases that kill hundreds of thousands of people each year.")
print("                                                               ")
print("Climate change provides better living conditions for mosquitos letting them thrive and kill more of our kind.")
print("                                                               ")
print("This simulation shows how climate change affects mosquitos and the diseases they spread.")
print("                                                               ")
done = False
while done == False:
    print("Type 11 to exit the simulation")
    userInput = input("How many years into the future do you want to go?: ")
    print("-----------------------------------------------------------")
    drought = random.randrange(0, 11)
    outbreak = random.randrange(0, 11)
    if userInput == 1:
        currentPopulation = 7.1
        print("You chose 2016 with a population of", currentPopulation, "billion.")
        if drought <= 5:
            speedOfInfection = 0.0002
            calc(currentPopulation, speedOfInfection)
        elif outbreak <= 2:
            speedOfInfection = 0.0005
            print("A major outbreak has occured!")
            calc(currentPopulation, speedOfInfection)
        else:
            speedOfInfection = 0.0001
            print("This year there was a drought so the mosquito population has dropped");
            calc(currentPopulation, speedOfInfection)

    elif userInput == 2:
        currentPopulation = 7.2
        print("You chose 2017 with a population of", currentPopulation, "billion.")
        if drought <= 5:
            speedOfInfection = 0.0002
            calc(currentPopulation, speedOfInfection)
        elif outbreak <= 2:
            speedOfInfection = 0.0005
            print("A major outbreak has occured!")
            calc(currentPopulation, speedOfInfection)
        else:
            speedOfInfection = 0.0001
            print("This year there was a drought so the mosquito population has dropped");
            calc(currentPopulation, speedOfInfection)
        
    elif userInput == 3:
        currentPopulation = 7.3
        print("You chose 2018 with a population of", currentPopulation, "billion.")
        if drought <= 5:
            speedOfInfection = 0.0003
            calc(currentPopulation, speedOfInfection)
        elif outbreak <= 2:
            speedOfInfection = 0.0005
            print("A major outbreak has occured!")
            calc(currentPopulation, speedOfInfection)
        else:
            speedOfInfection = 0.0001
            print("This year there was a drought so the mosquito population has dropped");
            calc(currentPopulation, speedOfInfection)

    elif userInput == 4:
        currentPopulation = 7.4
        print("You chose 2019 with a population of", currentPopulation, "billion.")
        if drought <= 5:
            speedOfInfection = 0.0003
            calc(currentPopulation, speedOfInfection)
        elif outbreak <= 2:
            speedOfInfection = 0.0005
            print("A major outbreak has occured!")
            calc(currentPopulation, speedOfInfection)
        else:
            speedOfInfection = 0.0001
            print("This year there was a drought so the mosquito population has dropped");
            calc(currentPopulation, speedOfInfection)

    elif userInput == 5:
        currentPopulation = 7.5
        print("You chose 2020 with a population of", currentPopulation, "billion.")
        if drought <= 5:
            speedOfInfection = 0.0003
            calc(currentPopulation, speedOfInfection)
        elif outbreak <= 2:
            speedOfInfection = 0.0005
            print("A major outbreak has occured!")
            calc(currentPopulation, speedOfInfection)
        else:
            speedOfInfection = 0.0001
            print("This year there was a drought so the mosquito population has dropped");
            calc(currentPopulation, speedOfInfection)

    elif userInput == 6:
        currentPopulation = 7.6
        print("You chose 2021 with a population of", currentPopulation, "billion.")
        if drought <= 5:
            speedOfInfection = 0.0003
            calc(currentPopulation, speedOfInfection)
        elif outbreak <= 2:
            speedOfInfection = 0.0005
            print("A major outbreak has occured!")
            calc(currentPopulation, speedOfInfection)
        else:
            speedOfInfection = 0.0001
            print("This year there was a drought so the mosquito population has dropped");
            calc(currentPopulation, speedOfInfection)

    elif userInput == 7:
        currentPopulation = 7.7
        print("You chose 2022 with a population of", currentPopulation, "billion.")
        if drought <= 5:
            speedOfInfection = 0.0003
            calc(currentPopulation, speedOfInfection)
        elif outbreak <= 2:
            speedOfInfection = 0.0005
            print("A major outbreak has occured!")
            calc(currentPopulation, speedOfInfection)
        else:
            speedOfInfection = 0.0001
            print("This year there was a drought so the mosquito population has dropped");
            calc(currentPopulation, speedOfInfection)

    elif userInput == 8:
        currentPopulation = 7.8
        print("You chose 2023 with a population of", currentPopulation, "billion.")
        if drought <= 5:
            speedOfInfection = 0.0003
            calc(currentPopulation, speedOfInfection)
        elif outbreak <= 2:
            speedOfInfection = 0.0005
            print("A major outbreak has occured!")
            calc(currentPopulation, speedOfInfection)
        else:
            speedOfInfection = 0.0001
            print("This year there was a drought so the mosquito population has dropped");
            calc(currentPopulation, speedOfInfection)

    elif userInput == 9:
        currentPopulation = 7.9
        print("You chose 2024 with a population of", currentPopulation, "billion.")
        if drought <= 5:
            speedOfInfection = 0.0003
            calc(currentPopulation, speedOfInfection)
        elif outbreak <= 2:
            speedOfInfection = 0.0005
            print("A major outbreak has occured!")
            calc(currentPopulation, speedOfInfection)
        else:
            speedOfInfection = 0.0001
            print("This year there was a drought so the mosquito population has dropped");
            calc(currentPopulation, speedOfInfection)

    elif userInput == 10:
        currentPopulation = 8.0
        print("You chose 2025 with a population of", currentPopulation, "billion.")
        if drought <= 5:
            speedOfInfection = 0.0003
            calc(currentPopulation, speedOfInfection)
        elif outbreak <= 2:
            speedOfInfection = 0.0005
            print("A major outbreak has occured!")
            calc(currentPopulation, speedOfInfection)
        else:
            speedOfInfection = 0.0001
            print("This year there was a drought so the mosquito population has dropped");
            calc(currentPopulation, speedOfInfection)
    
    elif userInput == 11:
        print("Thanks for using the simulation!")
        done = True

    else:
        print("That is not a valid value. Please try again.")

