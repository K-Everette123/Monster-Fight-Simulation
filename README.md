# Monster-Fight-Simulation
**Monster-Fight-Simulation** is a program that allows the to simulate fights against multiple monsters.

The combat mechanics of this simulation uses the random module to achieve damage between a minimum and maximum set by the program. This system is used for both the user and monsters.

For every monster killed the user gains experience pints, and after the user gains 20 experience points they gain 1 level.
Each level gives the user more damage against the monsters.

The program also uses a loot system. The loot list consists of a sword, shiny dagger, and shield. The sword and dagger give a boost to user damage, and the shield reduces damage of monsters to the player.



## Motivation
**Monster-Fight-Simulation** was created for an assignment given in the CS 230 class at Jacksonville State University.

##Requirements
* [Python 3.4.4 (Windows)](https://www.python.org/ftp/python/3.4.4/python-3.4.4.msi)
* [Python 3.4.4 (Mac)](https://www.python.org/ftp/python/3.4.4/python-3.4.4-macosx10.6.pkg)

## Download
* [Monster-Fight-Simulation](https://github.com/K-Everette123/Monster-Fight-Simulation/archive/master.zip)

## Usage
```$ git clone https://github.com/K-Everette123/Monster-Fight-Simulation.git
...```

## How-to use this program
To use this program complete the following steps:
* Download and install Python 3.4.4 for whichever OS you have.
* Download the Monster-Fight-Simulation repository.
* Un-zip the file.
* Run Monster-Fight-Simulation.py
* Follow the on screen instructions to play through the simulation.

## Editing the user or monster statisics

To change how powerful the user or monsters are edit the variable values in this section of code.
```
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
```
##Author
Kyle Everette

## License
See [LICENSE](https://github.com/K-Everette123/Monster-Fight-Simulation/blob/master/LICENSE.txt)
