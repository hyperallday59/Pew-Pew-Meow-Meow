import random
import pickle
from numpy import array
Actions = ("quit", "save", "load", "get", "use", "move")


Game_End = 0
name = input("what would you like to be called\n")
print("\nAfter months of training you finally return home to the Ninja Cat Village. You've been training to make your family proud and become the ninja you were always meant to be.\nBut... no one is in the village, it's as if it's been deserted.\n")
print("After searching the village for quite some time you find a letter. It's from your grandfather, the chief of Ninja Cat Village")
print(f"{name}, the evil ninja cats have invaded our lands stealing our Ninja gear and enslaving us. If you find this we must have all already been taken! Your final test to become a true shinobi will be saving our people and reclaiming our Ninja gear! Luckily I located the Evil Ninja Cat Mansion located deep in the bamboo forest. It's...")
print('the letter suddenly ends.\n\n"Dang it!" you exclaim\nThey must have invaded the village while your grandfather was writing the letter.')
print("\nYou waste no time gathering what little supplies you have and embark for the bamboo forest. After a day or two of treacherous hiking you've finally reached it!\nThe entrance to the bamboo forest!")

def main(hero):
    print("yay")