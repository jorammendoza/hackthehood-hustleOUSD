# hero.py for hero profile
import random
from ability import Ability
from armor import Armor

class Hero:
    def __init__(self, name, starting_health=100):
        '''Initialize Hero with a name and health values'''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []


    def battle(self, opponent):
    # '''Fight another hero and randomly declare a winner'''
        # Randomly choose winner
        print(f"{self.name} is battling {opponent.name}!")
        winner = random.choice([self.name, opponent.name])
        print(f"{winner} wins the battle!")

    def add_ability(self, ability):
        '''Appends an ability to the abilities list.'''
        self.abilities.append(ability)
        print(f"{ability.name} has been added to {self.name}'s ability list!")

    def sum_of_attacks(self):
        '''Add together all damage from all abilites' attack'''
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        '''Appends an armor to the armors list.'''
        self.armors.append(armor)
        print(f"{armor.name} has been added to {self.name}'s list")

    def defend(self):
        '''Adds together total block from all armors.'''
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block


if __name__ == "__main__":
    my_hero = Hero("Grace Hopper", 200)
    my_hero2 = Hero("Batman", 300)
    print(my_hero.name)            # Grace Hopper
    print(my_hero.current_health)  # 200


    my_hero.add_ability(Ability("Fireball", 30))
    my_hero.add_ability(Ability("Lightning", 50))
    my_hero.add_ability(Ability("Telekinesis", 60))
    print(my_hero.sum_of_attacks())

my_hero.battle(my_hero2)