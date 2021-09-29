import random
import math

def event4_1_00000001():
        print("Hello World!")

list_numbers = [15,14,13,12,10,8]        
ver = 0
i=0
kub_min = 0
value = 0
inventory = []
while (ver == 0):
    print("Welcome to Dungeon Masters!")
    print("It's a parody of  D&D")
    print("Try to enjoy it")
    # Next block about creating hero(race, name, class & etc)
    name_of_hero = input("What is your heroes name?\n")
    print("Unusually")
    print("Let's choose your race")
    race_of_hero = int(input("1 - Human, 2 - Orc, 3 - Elf\n"))
    print("Well choise")
    class_of_hero = int(input("1 - Warrior, 2 - Paladin, 3 - Druid\n"))
    print("Unexpectedly")
    height_of_hero = int(input("What height in cm?\n"))
    print("Ok")
    weight_of_hero = int(input("What weight in kg?\n"))
    print("Your wish is law")
    print("Now one last thing, your character?")
    character_of_hero = input("1 - Chaos, 2 - Order\n")
    character_of_hero2 = input("1 - Kind, 2 - Evil\n")
    # Next block about features(strength, constitution, wisdom, charisma, intelligence, dexterity)
    print("Please you Random? not Standart")
    version_of_choice = int(input("1 - Standart, 2 - Random\n"))
    if (version_of_choice == 1):
        print("Please choose one number to attribute")
        print("Choose number for strength")
        print(list_numbers)
        strength = int(input(""))
        if (strength == 15):
            list_numbers = [14,13,12,10,8]
            print("Choose number for constitution")
            print(list_numbers)
            constitution = int(input(""))
            if (constitution == 14):
                list_numbers = [13,12,10,8]
                print("Choose number for wisdom")
                print(list_numbers)
                wisdom = int(input(""))
                if (wisdom == 13):
                    list_numbers = [12,10,8]
                    print("Choose number for charisma")
                    print(list_numbers)
                    charisma = int(input(""))
                    if (charisma == 12):
                        list_numbers = [10,8]
                        print("Choose number for intelligence")
                        print(list_numbers)
                        intelligence = int(input(""))
                        if (intelligence == 10):
                            list_numbers = [8]
                            print("Choose number for dexterity")
                            dexterity = int(input(""))
                        if (intelligence == 8):
                            list_numbers = [10]
                            print("Choose number for dexterity")
                            dexterity = int(input(""))
                if (wisdom == 12):
                    list_numbers = [13,10,8]
                if (wisdom == 10):
                    list_numbers = [13,12,8]
                if (wisdom == 8):
                    list_numbers = [13,12,10]    
            if (constitution == 13):
                list_numbers = [14,12,10,8]
            if (constitution == 12):
                list_numbers = [14,13,12,8]
            if (constitution == 10):
                list_numbers = [14,13,12,8]
            if (constitution == 8):
                list_numbers = [14,13,12,10]
        if (strength == 14):
            list_numbers = [15,13,12,10,8]
            print("Choose number for constitution")
            print(list_numbers)
            constitution = int(input(""))
            if (constitution == 15):
                list_numbers = [13,12,10,8]
                print("Choose number for wisdom")
                print(list_numbers)
                wisdom = int(input(""))
                if (wisdom == 13):
                    list_numbers = [12,10,8]
                    print("Choose number for charisma")
                    print(list_numbers)
                    charisma = int(input(""))
                    if (charisma == 12):
                        list_numbers = [10,8]
                        print("Choose number for intelligence")
                        print(list_numbers)
                        intelligence = int(input(""))
                        if (intelligence == 10):
                            list_numbers = [8]
                            print("Choose number for dexterity")
                            dexterity = int(input(""))


            if (constitution == 13):
                list_numbers = [15,12,10,8]
                print("Choose number for wisdom")
                print(list_numbers)
                wisdom = int(input(""))
            if (constitution == 12):
                list_numbers = [15,13,10,8]
                print("Choose number for wisdom")
                print(list_numbers)
                wisdom = int(input(""))
            if (constitution == 10):
                list_numbers = [15,13,12,8]
                print("Choose number for wisdom")
                print(list_numbers)
                wisdom = int(input(""))
            if (constitution == 8):
                list_numbers = [15,13,12,10]
                print("Choose number for wisdom")
                print(list_numbers)
                wisdom = int(input(""))




        if (strength == 13):
            list_numbers = [15,14,12,10,8]
            print("Choose number for constitution")
            print(list_numbers)
            constitution = int(input(""))
            if (constitution == 14):
                list_numbers = [13,12,10,8]
                print("Choose number for wisdom")
                print(list_numbers)
                wisdom = int(input(""))
        if (strength == 12):
            list_numbers = [15,14,13,10,8]
            print("Choose number for constitution")
            print(list_numbers)
            constitution = int(input(""))
            if (constitution == 14):
                list_numbers = [13,12,10,8]
                print("Choose number for wisdom")
                print(list_numbers)
                wisdom = int(input(""))
        if (strength == 10):
            list_numbers = [15,14,13,12,8]
            print("Choose number for constitution")
            print(list_numbers)
            constitution = int(input(""))
            if (constitution == 14):
                list_numbers = [13,12,10,8]
                print("Choose number for wisdom")
                print(list_numbers)
                wisdom = int(input(""))
        if (strength == 8):
            list_numbers = [15,14,13,12,10]
            print("Choose number for constitution")
            print(list_numbers)
            constitution = int(input(""))
            if (constitution == 14):
                list_numbers = [13,12,10,8]
                print("Choose number for wisdom")
                print(list_numbers)
                wisdom = int(input(""))

    if (version_of_choice == 2):
        print("Your hero stats")
        while (i != 6):
            kub1 = random.randint(1,6)
            kub2 = random.randint(1,6)
            kub3 = random.randint(1,6)
            kub4 = random.randint(1,6)
            kub_min = min(kub1, kub2, kub3, kub4)
            value = kub1 + kub2 + kub3 + kub4 - kub_min
            if (i == 0):
                strength = value
                print("strength: ",strength)
            if (i == 1):
                constitution = value
                print("constitution: ",constitution)
            if (i == 2):
                wisdom = value
                print("wisdom: ",wisdom)
            if (i == 3):
                charisma = value
                print("charisma: ",charisma)
            if (i == 4):
                intelligence = value
                print("intelligence: ",intelligence)
            if (i == 5):
                dexterity = value
                print("dexterity: ",dexterity)
            i = i + 1
    #Next block about characteristic modifiers
    if (strength == 1):
        modifier_strength = -5
    if ((strength == 2) or (strength == 3)):
        modifier_strength = -4
    if ((strength == 4) or (strength == 5)):
        modifier_strength = -3
    if ((strength == 6) or (strength == 7)):
        modifier_strength = -2
    if ((strength == 8) or (strength == 9)):
        modifier_strength = -1
    if ((strength == 10) or (strength == 11)):
        modifier_strength = 0
    if ((strength == 12) or (strength == 13)):
        modifier_strength = 1
    if ((strength == 14) or (strength == 15)):
        modifier_strength = 2    
    if ((strength == 16) or (strength == 17)):
        modifier_strength = 3
    if ((strength == 18) or (strength == 19)):
        modifier_strength = 4
    if ((strength == 20) or (strength == 21)):
        modifier_strength = 5
    if ((strength == 22) or (strength == 23)):
        modifier_strength = 6
    if ((strength == 24) or (strength == 25)):
        modifier_strength = 7
    if ((strength == 26) or (strength == 27)):
        modifier_strength = 8
    if ((strength == 28) or (strength == 29)):
        modifier_strength = 9
    if (strength == 30):
        modifier_strength = 10

    if (constitution == 1):
        modifier_constitution = -5
    if ((constitution == 2) or (constitution == 3)):
        modifier_constitution = -4
    if ((constitution == 4) or (constitution == 5)):
        modifier_constitution = -3
    if ((constitution == 6) or (constitution == 7)):
        modifier_constitution = -2
    if ((constitution == 8) or (constitution == 9)):
        modifier_constitution = -1
    if ((constitution == 10) or (constitution == 11)):
        modifier_constitution = 0
    if ((constitution == 12) or (constitution == 13)):
        modifier_constitution = 1
    if ((constitution == 14) or (constitution == 15)):
        modifier_constitution = 2    
    if ((constitution == 16) or (constitution == 17)):
        modifier_constitution = 3
    if ((constitution == 18) or (constitution == 19)):
        modifier_constitution = 4
    if ((constitution == 20) or (constitution == 21)):
        modifier_constitution = 5
    if ((constitution == 22) or (constitution == 23)):
        modifier_constitution = 6
    if ((constitution == 24) or (constitution == 25)):
        modifier_constitution = 7
    if ((constitution == 26) or (constitution == 27)):
        modifier_constitution = 8
    if ((constitution == 28) or (constitution == 29)):
        modifier_constitution = 9
    if (constitution == 30):
        modifier_constitution = 10
    if (wisdom == 1):
        modifier_wisdom = -5
    if ((wisdom == 2) or (wisdom == 3)):
        modifier_wisdom = -4
    if ((wisdom == 4) or (wisdom == 5)):
        modifier_wisdom = -3
    if ((wisdom == 6) or (wisdom == 7)):
        modifier_wisdom = -2
    if ((wisdom == 8) or (wisdom == 9)):
        modifier_wisdom = -1
    if ((wisdom == 10) or (wisdom == 11)):
        modifier_wisdom = 0
    if ((wisdom == 12) or (wisdom == 13)):
        modifier_wisdom = 1
    if ((wisdom == 14) or (wisdom == 15)):
        modifier_wisdom = 2    
    if ((wisdom == 16) or (wisdom == 17)):
        modifier_wisdom = 3
    if ((wisdom == 18) or (wisdom == 19)):
        modifier_wisdom = 4
    if ((wisdom == 20) or (wisdom == 21)):
        modifier_wisdom = 5
    if ((wisdom == 22) or (wisdom == 23)):
        modifier_wisdom = 6
    if ((wisdom == 24) or (wisdom == 25)):
        modifier_wisdom = 7
    if ((wisdom == 26) or (wisdom == 27)):
        modifier_wisdom = 8
    if ((wisdom == 28) or (wisdom == 29)):
        modifier_wisdom = 9
    if (wisdom == 30):
        modifier_wisdom = 10
    if (charisma == 1):
        modifier_charisma = -5
    if ((charisma == 2) or (charisma == 3)):
        modifier_charisma = -4
    if ((charisma == 4) or (charisma == 5)):
        modifier_charisma = -3
    if ((charisma == 6) or (charisma == 7)):
        modifier_charisma = -2
    if ((charisma == 8) or (charisma == 9)):
        modifier_charisma = -1
    if ((charisma == 10) or (charisma == 11)):
        modifier_charisma = 0
    if ((charisma == 12) or (charisma == 13)):
        modifier_charisma = 1
    if ((charisma == 14) or (charisma == 15)):
        modifier_charisma = 2    
    if ((charisma == 16) or (charisma == 17)):
        modifier_charisma = 3
    if ((charisma == 18) or (charisma == 19)):
        modifier_charisma = 4
    if ((charisma == 20) or (charisma == 21)):
        modifier_charisma = 5
    if ((charisma == 22) or (charisma == 23)):
        modifier_charisma = 6
    if ((charisma == 24) or (charisma == 25)):
        modifier_charisma = 7
    if ((charisma == 26) or (charisma == 27)):
        modifier_charisma = 8
    if ((charisma == 28) or (charisma == 29)):
        modifier_charisma = 9
    if (charisma == 30):
        modifier_charisma = 10
    if (intelligence == 1):
        modifier_intelligence = -5
    if ((intelligence == 2) or (intelligence == 3)):
        modifier_intelligence = -4
    if ((intelligence == 4) or (intelligence == 5)):
        modifier_intelligence = -3
    if ((intelligence == 6) or (intelligence == 7)):
        modifier_intelligence = -2
    if ((intelligence == 8) or (intelligence == 9)):
        modifier_intelligence = -1
    if ((intelligence == 10) or (intelligence == 11)):
        modifier_intelligence = 0
    if ((intelligence == 12) or (intelligence == 13)):
        modifier_intelligence = 1
    if ((intelligence == 14) or (intelligence == 15)):
        modifier_intelligence = 2    
    if ((intelligence == 16) or (intelligence == 17)):
        modifier_intelligence = 3
    if ((intelligence == 18) or (intelligence == 19)):
        modifier_intelligence = 4
    if ((intelligence == 20) or (intelligence == 21)):
        modifier_intelligence = 5
    if ((intelligence == 22) or (intelligence == 23)):
        modifier_intelligence = 6
    if ((intelligence == 24) or (intelligence == 25)):
        modifier_intelligence = 7
    if ((intelligence == 26) or (intelligence == 27)):
        modifier_intelligence = 8
    if ((intelligence == 28) or (intelligence == 29)):
        modifier_intelligence = 9
    if (intelligence == 30):
        modifier_intelligence = 10
    if (dexterity == 1):
        modifier_dexterity = -5
    if ((dexterity == 2) or (dexterity == 3)):
        modifier_dexterity = -4
    if ((dexterity == 4) or (dexterity == 5)):
        modifier_dexterity = -3
    if ((dexterity == 6) or (dexterity == 7)):
        modifier_dexterity = -2
    if ((dexterity == 8) or (dexterity == 9)):
        modifier_dexterity = -1
    if ((dexterity == 10) or (dexterity == 11)):
        modifier_dexterity = 0
    if ((dexterity == 12) or (dexterity == 13)):
        modifier_dexterity = 1
    if ((dexterity == 14) or (dexterity == 15)):
        modifier_dexterity = 2    
    if ((dexterity == 16) or (dexterity == 17)):
        modifier_dexterity = 3
    if ((dexterity == 18) or (dexterity == 19)):
        modifier_dexterity = 4
    if ((dexterity == 20) or (dexterity == 21)):
        modifier_dexterity = 5
    if ((dexterity == 22) or (dexterity == 23)):
        modifier_dexterity = 6
    if ((dexterity == 24) or (dexterity == 25)):
        modifier_dexterity = 7
    if ((dexterity == 26) or (dexterity == 27)):
        modifier_dexterity = 8
    if ((dexterity == 28) or (dexterity == 29)):
        modifier_dexterity = 9
    if (dexterity == 30):
        modifier_dexterity = 10  

    print("Your modifiers")
    print("modifier_strength: ",modifier_strength)
    print("modifier_constitution: ",modifier_constitution)
    print("modifier_wisdom: ",modifier_wisdom)
    print("modifier_charisma: ",modifier_charisma)
    print("modifier_intelligence: ",modifier_intelligence)
    print("modifier_dexterity: ",modifier_dexterity)

    print("Let's start our journey: ")

    #Next block about journey
    print("It was a very beautiful village.\nThere are signs all along the street.\n On the first sign you see, you read that it is 'Saliero's Shop'.")
    print("Would you like to come in and buy something?")
    event4_3_1 = int(input("1 - Yes, 2 - No"))
    if (event4_3_1 == 1):
        print("You go into the shop. You see a lot of sword, bows and others.")
        equipment = int(input("What are you want? 1 - Sword, 2 - Bow, 3 - Shield, 4 - Nothing"))
        if (equipment == 1):
            print("This inexperienced merchant points to 3 swords")
            Answer4_3_1 = int(input("1 - Beginner's sword, 2 - Old sword, 3 - New Wooden Sword"))
            if (Answer4_3_1 == 1):
                print("Присматриваетесь к первому мечу. Простой, как раз для вас. Вы посмотрели")

                #Ситуация в магазине, торги , удача, первая проверка системы характеристик.

    ver = 1
    
