# CTI 110
# P3LAB - Choose your own adventure
# adams
# 10/22/24

def main (): 
    print ("Create your own Adventure")
    go_home()

def go_home():
    print ("You decide to go home.")
    print ("But should you get some food?")  
    print ("1. Grab a Salad")
    print ("2. Get some Ramen")
    print ("3. Eat a bowl of cereal")
    choice = int(input())
    if choice == 1:
        get_salad()
    elif choice == 2:
        get_ramen()      
    elif choice == 3:
        get_cereal()
def get_salad():
    print("The salad🥬 is green 🥗🤮🤢 slime!🤮🤮⚰️")
    print("You a have been 🤢🤮SLIMED🤮🤢⚰️")

def get_ramen():
    print("The noodles🍜 rap🕸️🕸️🕸️ you up")
    print("You have been mumified🧟 by noodles🍲⚰️")

def get_cereal():
    print("Don't forget the 🍯🍯honey🍯🍯")
    print("Nice 🥛🥛choice your safe🥣🥣🥣.")    
    
