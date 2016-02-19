'''
    Name: Monster-Fight-Simulation
    Author: Kyle Everette
    Date Last Modified: 2/17/16

    Simulates a fight between multiple monsters with a loot system.
'''
import random

roll = input("Type f to begin or q to quit: ")
print("\n")

p_health = 100                  #Initializes beginning variables
m_health = 40
kills = 0
exp = 0
level = 0
lp_dmg = 5                      #Player low and and high damage
hp_dmg = 30                     #Monster low and hight damage
lm_dmg = 1
hm_dmg = 5
item_dmg = 0
tuff = 0

loot_list = ["shiny_dagger", "shield", "sword"]            #Create loot list

while roll != "q":                                      #Creates main menu
    p_dmg = random.randint(lp_dmg, hp_dmg)
    m_dmg = random.randint(lm_dmg, hm_dmg)
    if roll != "f" and roll != "q":
        print("Invalid Choice")
        print("\n")
        roll = input("Type f to begin or q to quit: ")
        print("\n")
    else:
        if p_health >= 1:                               #Combat mechanics
            print("Number of kills: " + str(kills))
            print("\n")
            print("Your level: " + str(level))
            print("\n")
            print("Your experience: " + str(exp))
            print("\n")
            if m_health >= 1:
                p_health = p_health - (m_dmg + tuff)
                m_health = m_health - (p_dmg + item_dmg)
                print("The skeleton has hit you for " + str(m_dmg) + " damage")
                print("\n")
                print("Your health is: " + str(p_health))
                print("\n")
                print("You have hit the skeleton for " + str(p_dmg) + " damage")
                print("\n")
                print("Your enemies health is: " + str(m_health))
                print("\n")
                if m_health <= 0 and p_health <= 0:
                    print("You have both died in combat.")
                    print("\n")
                    print("GAME OVER")
                    print("\n")
                elif p_health <= 0:
                    print("You have died.")
                    print("\n")
                    print("GAME OVER")
                    print("\n")
                    roll = input("Type q to quit: ")
                    print("\n")
                elif m_health <= 0:                                             #Loot system
                    print("You've slayed the skeleton")
                    print("\n")
                    loot = random.randint(1, 10)
                    if loot_list[2] == "false" and loot_list[1] == "false":
                        if exp % 20:
                            level += 1
                            exp += 10
                            print("You have slayed the skeleton!")
                            print("\n")
                            print("You gain 10 experience points!")
                            print("\n")
                            print("You leveled up!")
                            print("\n")
                            roll = input("Type f to continue or q to quit: ")
                            print("\n")
                            m_health = 25
                            kills += 1
                        else:
                            exp += 10
                            print("You have slayed the skeleton!")
                            print("\n")
                            print("You gain 10 experience points!")
                            print("\n")
                            roll = input("Type f to continue or q to quit: ")
                            print("\n")
                            m_health = 25
                            kills += 1
                    elif loot_list[0] == "false" and loot_list[1] == "false":
                        if loot == 10:
                            print("The skeleton dropped a sword!")
                            print("\n")
                            loot_list.pop(2)
                            loot_list.insert(2, "false")
                            item_dmg = 10
                            if exp % 20:
                                level += 1
                                exp += 10
                                print("You have slayed the skeleton!")
                                print("\n")
                                print("You gain 10 experience points!")
                                print("\n")
                                print("You leveled up!")
                                print("\n")
                                roll = input("Type f to continue or q to quit: ")
                                print("\n")
                                m_health = 25
                                kills += 1
                            else:
                                exp += 10
                                print("You have slayed the skeleton!")
                                print("\n")
                                print("You gain 10 experience points!")
                                print("\n")
                                roll = input("Type f to continue or q to quit: ")
                                print("\n")
                                m_health = 25
                                kills += 1
                        else:
                            if exp % 20:
                                level += 1
                                exp += 10
                                print("You have slayed the skeleton!")
                                print("\n")
                                print("You gain 10 experience points!")
                                print("\n")
                                print("You leveled up!")
                                roll = input("Type f to continue or q to quit: ")
                                print("\n")
                                m_health = 25
                                kills += 1
                            else:
                                exp += 10
                                print("You have slayed the skeleton!")
                                print("\n")
                                print("You gain 10 experience points!")
                                print("\n")
                                roll = input("Type f to continue or q to quit: ")
                                print("\n")
                                m_health = 25
                                kills += 1
                    elif loot_list[2] == "false":
                        if loot == 8 or loot == 9:
                            print("The skeleton dropped a shield!")
                            print("\n")
                            tuff = -1
                            loot_list.pop(1)
                            loot_list.insert(1, "false")
                            if exp % 20:
                                level += 1
                                exp += 10
                                print("You have slayed the skeleton!")
                                print("\n")
                                print("You gain 10 experience points!")
                                print("\n")
                                print("You leveled up!")
                                print("\n")
                                roll = input("Type f to continue or q to quit: ")
                                print("\n")
                                m_health = 25
                                kills += 1
                            else:
                                exp += 10
                                print("You have slayed the skeleton!")
                                print("\n")
                                print("You gain 10 experience points!")
                                print("\n")
                                roll = input("Type f to continue or q to quit: ")
                                print("\n")
                                m_health = 25
                                kills += 1
                        else:
                            if exp % 20:
                                level += 1
                                exp += 10
                                print("You have slayed the skeleton!")
                                print("\n")
                                print("You gain 10 experience points!")
                                print("\n")
                                print("You leveled up!")
                                print("\n")
                                roll = input("Type f to continue or q to quit: ")
                                print("\n")
                                m_health = 25
                                kills += 1
                            else:
                                exp += 10
                                print("You have slayed the skeleton!")
                                print("\n")
                                print("You gain 10 experience points!")
                                print("\n")
                                roll = input("Type f to continue or q to quit: ")
                                print("\n")
                                m_health = 25
                                kills += 1
                    elif loot_list[0] == "false":
                        if loot == 8 or loot == 9:
                            print("The skeleton dropped a shield!")
                            print("\n")
                            tuff = -1
                            loot_list.pop(1)
                            loot_list.insert(1, "false")
                            if exp % 20:
                                level += 1
                                exp += 10
                                print("You have slayed the skeleton!")
                                print("\n")
                                print("You gain 10 experience points!")
                                print("\n")
                                print("You leveled up!")
                                print("\n")
                                roll = input("Type f to continue or q to quit: ")
                                print("\n")
                                m_health = 25
                                kills += 1
                            else:
                                exp += 10
                                print("You have slayed the skeleton!")
                                print("\n")
                                print("You gain 10 experience points!")
                                print("\n")
                                roll = input("Type f to continue or q to quit: ")
                                print("\n")
                                m_health = 25
                                kills += 1
                        elif loot == 10:
                            print("The skeleton dropped a sword!")
                            print("\n")
                            loot_list.pop(2)
                            loot_list.insert(2, "false")
                            item_dmg = 10
                            if exp % 20:
                                level += 1
                                exp += 10
                                print("You have slayed the skeleton!")
                                print("\n")
                                print("You gain 10 experience points!")
                                print("\n")
                                print("You leveled up!")
                                print("\n")
                                roll = input("Type f to continue or q to quit: ")
                                print("\n")
                                m_health = 25
                                kills += 1
                            else:
                                exp += 10
                                print("You have slayed the skeleton!")
                                print("\n")
                                print("You gain 10 experience points!")
                                print("\n")
                                roll = input("Type f to continue or q to quit: ")
                                print("\n")
                                m_health = 25
                                kills += 1
                        else:
                            if exp % 20:
                                level += 1
                                exp += 10
                                print("You have slayed the skeleton!")
                                print("\n")
                                print("You gain 10 experience points!")
                                print("\n")
                                print("You leveled up!")
                                print("\n")
                                roll = input("Type f to continue or q to quit: ")
                                print("\n")
                                m_health = 25
                                kills += 1
                            else:
                                exp += 10
                                print("You have slayed the skeleton!")
                                print("\n")
                                print("You gain 10 experience points!")
                                print("\n")
                                roll = input("Type f to continue or q to quit: ")
                                print("\n")
                                m_health = 25
                                kills += 1
                    else:    
                        if loot == 6 or loot == 7:
                            print("The skeleton dropped a shiny dagger!")
                            print("\n")
                            loot_list.pop(0)
                            loot_list.insert(0, "false")
                            item_dmg = 1
                            if exp % 20:
                                level += 1
                                exp += 10
                                print("You have slayed the skeleton!")
                                print("\n")
                                print("You gain 10 experience points!")
                                print("\n")
                                print("You leveled up!")
                                print("\n")
                                roll = input("Type f to continue or q to quit: ")
                                print("\n")
                                m_health = 25
                                kills += 1
                            else:
                                exp += 10
                                print("You have slayed the skeleton!")
                                print("\n")
                                print("You gain 10 experience points!")
                                print("\n")
                                roll = input("Type f to continue or q to quit: ")
                                print("\n")
                                m_health = 25
                                kills += 1
                        elif loot == 8 or loot == 9:
                            print("The skeleton has dropped a shield")
                            print("\n")
                            tuff = -1
                            loot_list.pop(1)
                            loot_list.insert(1, "false")
                            if exp % 20:
                                level += 1
                                exp += 10
                                print("You have slayed the skeleton!")
                                print("\n")
                                print("You gain 10 experience points!")
                                print("\n")
                                print("You leveled up!")
                                print("\n")
                                roll = input("Type f to continue or q to quit: ")
                                print("\n")
                                m_health = 25
                                kills += 1
                            else:
                                exp += 10
                                print("You have slayed the skeleton!")
                                print("\n")
                                print("You gain 10 experience points!")
                                print("\n")
                                roll = input("Type f to continue or q to quit: ")
                                print("\n")
                                m_health = 25
                                kills += 1
                        elif loot == 10:
                            print("The skeleton has dropped a sword")
                            print("\n")
                            loot_list.pop(2)
                            loot_list.insert(2, "false")
                            item_dmg = 10
                            if exp % 20:
                                level += 1
                                exp += 10
                                print("You have slayed the skeleton!")
                                print("\n")
                                print("You gain 10 experience points!")
                                print("\n")
                                print("You leveled up!")
                                print("\n")
                                roll = input("Type f to continue or q to quit: ")
                                print("\n")
                                m_health = 25
                                kills += 1
                            else:
                                exp += 10
                                print("You have slayed the skeleton!")
                                print("\n")
                                print("You gain 10 experience points!")
                                print("\n")
                                roll = input("Type f to continue or q to quit: ")
                                print("\n")
                                m_health = 25
                                kills += 1
                        else:
                            if exp % 20:
                                level += 1
                                exp += 10
                                print("You have slayed the skeleton!")
                                print("\n")
                                print("You gain 10 experience points!")
                                print("\n")
                                print("You leveled up!")
                                print("\n")
                                roll = input("Type f to continue or q to quit: ")
                                print("\n")
                                m_health = 25
                                kills += 1
                            else:
                                exp += 10
                                print("You have slayed the skeleton!")
                                print("\n")
                                print("You gain 10 experience points!")
                                print("\n")
                                roll = input("Type f to continue or q to quit: ")
                                print("\n")
                                m_health = 25
                                kills += 1
                else:
                    roll = input("Type f to continue or q to quit: ")
                    print("\n")
                    
            else:
                roll = input("Type f to continue or q to quit: ")
                print("\n")
        else:    
            roll = input("Type q to quit: ")
            print("\n")
            
    


