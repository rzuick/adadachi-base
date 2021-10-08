from constants import STATUS
import random
from adadachi  import Adadachi

class Player:
    def __init__(self):
        self.adadachi = None
        self.inventory = {
            "games": ["hide-n-seek", "tag", "go fish", "red rover"],
            "foods": ["banana cream pie", "carrot sticks", "mashed potatoes", "mac 'n cheese", "tater tots", "chocolate cake", "strawberries", "fried rice"],
        }

    def get_status(self):
        print(STATUS)

    def clean(self):
        pass
        if self.adadachi.poop_lvl > 0:
            print("Someone is a stinky. Time to clean them.")
        else:
            print(f"{self.adadachi.name} is all clean!")

    def feed(self):
        print(f"Time to eat! What should you feed {self.adadachi.name.capitalize()}?\n")
        print(self.inventory["foods"], "\n")
        food = input("Pick a food from the list: \n")
        if food == self.adadachi.personality["hates_food"]:
            print("Yuck! How could you feed that to them?\n")
        elif food == self.adadachi.personality["fav_food"]:
            print(f"Aww, thank you so much! {self.adadachi.name.capitalize()} loves {self.adadachi.personality['fav_food']}")
        else:
            print(f"{food.capitalize()} wasn't half bad.")

    def play_with_adadachi(self):
        pass