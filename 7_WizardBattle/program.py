import random
import time
from actors import Wizard, Creature, SmallAnimal, Dragon


def main():
    print_header()
    game_loop()


def print_header():
    print('-----------------------------')
    print('      WIZARD GAME APP')
    print('-----------------------------')
    print('')


def game_loop():

    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Fox', 5),
        SmallAnimal('Deadly Snake', 12),
        Dragon('Dragon', 100, 25, True),
        Wizard('Evil Wizard', 500),
    ]

    hero = Wizard('Gandolf', 75)


    while True:

        active_creature = random.choice(creatures)
        print('A {} of Level {} has appeared out of a dark and foggy forest...'.format(
            active_creature.name,
            active_creature.level
        ))

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around?')
        cmd = cmd.lower()
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("The Wizard runs and take time to recover.")
                time.sleep(5)
                print("The Wizard returns revitalized")
        elif cmd == 'r':
            print('The Wizard {} has become unsure of his powers and flees.'.format(hero.name))
        elif cmd == 'l':
            for c in creatures:
                print("The wizard {} look around and a {} of level {}.".format(hero.name, c.name, c.level))
        else:
            print('OK, exiting game... bye!')
            break
        if not creatures:
            print('You have defeated all the creatures!!')
            break
        print()

if __name__ == '__main__':
    main()
