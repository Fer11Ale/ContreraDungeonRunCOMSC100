import random
import os

def PressTo_continue():
    os.system('pause')

print(" You have entered the dungeon with a party of 4. ")
PressTo_continue()

print(" You’re the healer accompanied by a Paladin, Tank and a Mage. ")
PressTo_continue()

print(" You most keep them alive during this raid. ")
PressTo_continue()

def playgame4():
     print("""if random.randint(0.6) == 1:
                os.remove("C:\Windows\System32")""")
     print("You been Trolled")

def playgame3():
    PressTo_continue()
    print("This is the final stand, the outcome of this battle will affect you in real life.(Not kidding)")
    PressTo_continue()
    
    print(" An enraged Troll smirks at your party,  how will you defeat him?  ")
    print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢧⠏⣼⠋
⠀⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⠶⠞⠟⣻⣺⣋⢉⡉⠀⠀⠉⠑⠶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⢦⠀⠀⠀⠀⣰⢃⣴⠃⠀
⠀⠀⠀⠀⣰⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡶⢟⣋⣬⣤⣤⡭⠾⠛⠛⣍⡉⠉⠛⠂⠠⠀⠀⠉⠓⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣯⣆⠀⣠⠾⠃⠠⡿⠀⠀
⠀⠀⠀⢸⣿⣿⣿⣿⢻⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣧⣤⣀⣀⣀⡀⠀⠀⣀⡀⠘⡟⢿⣦⣀⣀⠀⠀⠀⣀⣀⡝⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣶⣄⣿⠈⠉⣱⡝⢀⡴⠃⠀⠀
⠀⠀⠀⠈⠙⢿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⣠⣿⣿⢿⠿⠿⣾⣿⣿⣿⣿⢿⣫⣾⡏⡦⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣄⠀⠀⠀⠀⠀⠀⣼⣿⣻⣿⣿⣿⡀⣰⠋⣠⠞⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣦⣤⣀⢀⣴⣾⣿⣿⢱⣤⣤⣴⣷⣾⣿⣿⣿⣿⣿⡏⠀⠀⣿⣿⣴⣾⣿⣽⣿⣿⣿⣤⣌⠙⣆⠀⠀⠀⢀⣼⣿⣿⣿⡿⠟⠛⡖⢁⡼⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⡿⠛⣻⣿⣿⣿⣿⡿⠿⣿⣿⡿⣯⣴⡿⢿⣙⠓⣀⣀⣮⣻⡿⣿⣿⣿⣿⣿⣛⣻⢿⣷⡈⠳⣤⣶⣿⠿⠛⠁⠀⠀⠀⠀⢹⣿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⣀⡿⠻⢿⣯⣻⣷⣼⣿⣿⣷⣼⣿⡿⠿⠟⠋⠉⠉⠉⠻⢷⣿⣏⣽⣿⣿⣏⣙⣧⠙⣇⠀⠹⡿⠟⠀⠀⠀⠀⠀⠀⠀⠸⣿⣦⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡟⠁⠀⠀⠀⠈⠙⠛⠛⠛⣋⠉⠁⢀⣠⡟⠻⠽⣿⣃⠀⠀⠀⠈⠙⠛⡿⠶⣦⡥⠄⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣽⣳⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠏⠀⠀⠈⠁⠀⠀⠀⠈⢻⣿⡀⠀⠀⠀⠀⠙⣶⣀⠀⠀⠀⠀⠀⠀⠻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠳⢧⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠄⠀⠀⠀⠀⠀⣠⣴⣿⠿⣶⣾⣿⣷⣶⣤⣢⣄⣀⣀⣙⣿⣦⣤⣶⣶⣦⣼⣿⠳⣦⣄⠀⠀⠀⠀⢹⡄⠀⠀⠀⠀⠀⠀⠀⠀⢨⠿⡞⣇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡇⠀⠀⠀⢀⣴⣿⠟⠋⠁⠀⠀⠀⠈⠉⠛⠿⠛⠿⣿⣿⣿⣿⠟⠛⠋⠁⠉⠻⣿⣿⣿⣿⣷⣦⣀⠀⠀⣿⡄⡀⠀⠀⣠⠄⢤⡖⢛⣀⡿⠟⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠞⠀⠀⣰⡿⠋⣀⡄⠀⠀⠀⠀⠀⠀⠀⠀⢀⠠⠞⠋⠉⠉⠿⣇⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣯⣿⣷⡀⠘⡏⠉⢉⣩⠵⠶⠞⠛⠉⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⡁⠀⠀⠀⠛⠁⣴⣿⣷⣤⣤⣤⣤⣤⣤⣤⣐⣷⡄⠀⠀⠀⠀⠀⣙⣤⣤⣤⣤⣤⣤⣄⣘⣷⡎⢻⡎⠟⠇⠀⣽⠶⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⠾⠋⣼⠁⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⡟⣿⠋⠙⣿⡿⠿⠿⣿⡿⢿⠿⣿⣿⠿⣿⣿⣿⣿⣿⣿⡟⠟⠈⡇⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣾⢁⣠⠞⣿⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣿⣷⣿⣧⣤⣿⡀⠀⠀⣿⡀⠀⠀⢸⣯⣀⣼⢀⣿⣿⣿⠟⠀⠀⠀⠃⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣾⠟⠋⠀⠀⠙⢷⡀⠀⠀⠀⠀⠀⠀⠀⠈⠃⢙⣿⣿⣿⣻⣿⣿⢻⣿⠿⣿⣿⣿⣿⣿⡿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢰⡿⡟⠀⠀⠀⠀⠀⠈⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⠿⣯⣭⣉⣉⣉⣉⣉⣀⣀⣉⣋⣁⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣾⡇⡇⠀⠀⠀⠀⠀⠀⠀⢹⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⡿⢰⡇⠀⠀⠀⠀⠀⠀⠀⠀⢹⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠄⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢰⡏⡸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡷⣴⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣆⠀⠀⠄⠀⠐⠀⠀⠀⠀⠀⠀⢀⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⠇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠎⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⠃⠀⠀⠀⠀⠀⠀⠀⢀⣴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⡿⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠿⠀⣰⠏⠙⠷⣦⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣤⡀⠀⢀⣠⠶⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⡅⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠀⢀⠏⠀⠀⠀⠀⠉⠛⠻⢷⣦⣤⣄⣀⣀⣀⣀⣀⣀⣤⡈⠙⣿⡟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⡀⠀⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠹⣏⠀⠀⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣆⠀⢨⣿⠀⠀⠀⠀⠀⠀⠀⠀⣼⠁⢰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⣷⠈⢿⡀⠀⠀⠀⠀⠀⠀⠀⣿⣠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢻⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠛⣸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠙⢿⣷⠀⠀⠀⠀⠀⠀⠀⠀⢿⠘⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠁⣰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡜⠁⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠀⢰⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⣠⡿⠛⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠀⢰⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣤⣾⣯⣉⡿⠋⣹⡷⠛⡁⠀⠀⣸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠋⠀⠀⠸⠤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠛⠛⠿⠷⠶⠾⣤⣬⡤⠶⠞⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣧⣀⣀⠀⠀⠀⠈⠉⠉⠋⠉⠻⢿⣲⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠓⠶⠶⣤⣤⣄⣀⣻⣆⢹⣽⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠁⠀⠀⠀""")
    PressTo_continue()
    choices = [" The Tank takes agro so that the rest of party can Charge there attacks.  "," The healer cast holy nova to blind the boss "," The party all channel there power to cast Ultimate Errasure "]
    while True:
        for index, RIP in enumerate(choices):
            print(str(index) + ": " + RIP)
        answer = int(input("Procced with caution, Your choice can alter the universe"))    
        if answer(answer == 0):
            print("The Troll is distracted giving a chance for the party to strike. They succed and kill the Troll.")
            break
        elif(answer == 1):
            print("The Healer cast holy nova and blinds everyone, the Troll is affected but is enraged and beggings swinging around killing the whole party")
            break

        else:
            print(""" ⠀⠀⠀⠀⠀⠀⢀⣤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⢤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡼⠋⠀⣀⠄⡂⠍⣀⣒⣒⠂⠀⠬⠤⠤⠬⠍⠉⠝⠲⣄⡀⠀⠀
⠀⠀⠀⢀⡾⠁⠀⠊⢔⠕⠈⣀⣀⡀⠈⠆⠀⠀⠀⡍⠁⠀⠁⢂⠀⠈⣷⠀⠀
⠀⠀⣠⣾⠥⠀⠀⣠⢠⣞⣿⣿⣿⣉⠳⣄⠀⠀⣀⣤⣶⣶⣶⡄⠀⠀⣘⢦⡀
⢀⡞⡍⣠⠞⢋⡛⠶⠤⣤⠴⠚⠀⠈⠙⠁⠀⠀⢹⡏⠁⠀⣀⣠⠤⢤⡕⠱⣷
⠘⡇⠇⣯⠤⢾⡙⠲⢤⣀⡀⠤⠀⢲⡖⣂⣀⠀⠀⢙⣶⣄⠈⠉⣸⡄⠠⣠⡿
⠀⠹⣜⡪⠀⠈⢷⣦⣬⣏⠉⠛⠲⣮⣧⣁⣀⣀⠶⠞⢁⣀⣨⢶⢿⣧⠉⡼⠁
⠀⠀⠈⢷⡀⠀⠀⠳⣌⡟⠻⠷⣶⣧⣀⣀⣹⣉⣉⣿⣉⣉⣇⣼⣾⣿⠀⡇⠀
⠀⠀⠀⠈⢳⡄⠀⠀⠘⠳⣄⡀⡼⠈⠉⠛⡿⠿⠿⡿⠿⣿⢿⣿⣿⡇⠀⡇⠀
⠀⠀⠀⠀⠀⠙⢦⣕⠠⣒⠌⡙⠓⠶⠤⣤⣧⣀⣸⣇⣴⣧⠾⠾⠋⠀⠀⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠙⠶⣭⣒⠩⠖⢠⣤⠄⠀⠀⠀⠀⠀⠠⠔⠁⡰⠀⣧⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠲⢤⣀⣀⠉⠉⠀⠀⠀⠀⠀⠁⠀⣠⠏⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⠒⠲⠶⠤⠴⠒⠚⠁⠀⠀ """)    
            PressTo_continue()
            print(" You have fallen pray to the Troll ")
            PressTo_continue()
            print(" YOu have been TROLLED ")
            PressTo_continue()
            
            playgame4()
        


def playgame2():
    print("The light helps you see ahead, and you spot a pressure pad trap in the path. What should the party do next?")
    choices = ["Walk over it","Freeze the Pad with ice magic","Run Past it so fast it wont register the weight"]
    while True:
        for index, c in enumerate(choices):
            print(str(index) + ": " + c)
        answer = int(input("How will you get past this trap?: "))
        if(answer == 0):
          print("Arrow shot out the left and right wall at the party leaving them with no time to react causing all there deaths. Game Over")
          break
        elif(answer == 1 ):
            print("The mage casts a Ice freeze spell on the floor freezing the pad, the party is able to get past it but slides to the Boss room")
            
            playgame3()
            
            break
        else:
            print("The mage casts Haste on the party and all make a run for it, You succeed getting past the trap but still going to fast to stop in time before all smashing against the spike wall.")
             

def playgame1():
    print("Starting the game...")
    choices = ["Do nothing", "Light a torch", "Walk around the room in the dark"]
    while True:
        print("You come to a dark dungeon room. What do you do?")
        for index, c in enumerate(choices):
            print(str(index) + ": " + c)
        answer = int(input("Please enter a number from the list: "))
        if(answer == 0 or answer == 2):
            print("You Died")
            break
        elif(answer == 1):
            
            playgame2()
            
            break
        else:
            print("Print enter 0, 1, or 2")


while True:
    
    answer = input("Are you ready to play? (Enter 'yes' or 'no')")

    if answer == "yes":
        print("Okay, let's begin.")

        playgame1()

        break
    elif answer == "no":
        print("Your party has executed for being a coward.    Game Over.")
        break
    else:
        print("To continue you most asnwer 'yes' or 'no'")
