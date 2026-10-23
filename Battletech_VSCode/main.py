import random
import random_functions

#This is a love letter to Battletech, but also a tool. It helps you decide  
#what your faction is, and what Mechs to paint. 

Houses = ["Liao", "Kurita", "Davion", "Steiner", "Marik"]
Clans = ["Smoke Jaguar", "Ghost Bear", "Wolf", "Jade Falcon"]
Mercs = ["Wolf's Dragoons", "Gray Death Legion", "Kell Hounds", 
        "Eridani Light Horse"]
Lances = ["Recon", "Heavy", "Battle", "Fire Support", "Command"]
Stars = ["Fire Support", "Battle", "Command", "Heavy", "Ad-hoc", "Recon"]
IS_Ranks = ["Captain", "Lieutenant", "Colonel"]
CL_Ranks = ["Star Commander", "Star Captain", "Star Colonel"]

print("You are a Mechwarrior. You command avatars of power, and decide the " 
"fate of worlds.")
name = input("But even gods have names. What is yours? ")

print("So you are " + name + ".")
play_again = "yes"
while play_again == "yes":
    faction_input = input("Well, " + name + "." + 
    " Do you serve the Houses, Clans, or yourself? ")

    if faction_input == "Houses" or faction_input == "houses":
        print("Here is who you can serve.")
        print(Houses)
        house = input("Who will you march for, Mechwarrior? ")
        while house not in Houses:
            print("This house is neither existent, nor worthy of your service.")
            house = input("Who will you march for, Mechwarrior? ")
        print("You will serve the Great House of " + house + ".")
        lance = random.choice(Lances)
        print("You are now the designated Lieutenant of a " 
        + lance + " Lance, " + name + "." + " Serve us well.")
        print(random_functions.lance_comp(lance))
        print(random_functions.IS_names())
        print(random_functions.PG_stat_is())

    elif faction_input == "Clans" or faction_input == "clans":
        print("Aff, welcome home, Warrior.")
        print("Remind me, which clan do you hail from? Here are our homes.")
        print(Clans)
        clan_choice = input("So. Who are we? What name do we bear? ")
        while clan_choice not in Clans:
            print("This clan is too..weak for a warrior of your skill. Try again.")
            clan_choice = input("So. Who are we? What name do we bear? ")
        print("Ah, we serve Clan " + clan_choice + " then. A name worth bearing.")
        star = random.choice(Stars)
        print("You excelled in your trials, " + name + 
            "," " and have been made a Star Commander" 
            ".  You shall join one of our " + star 
            + " Stars. Lead them well, you've earned it.")
        print(random_functions.star_comp(star))
        print(random_functions.CL_names(clan_choice))
        print(random_functions.PG_stat_cl())
    elif faction_input == "Myself" or faction_input == "myself":
        print("No master but money rules you. A dangerous choice, but a free one.")
        print("Many legions exist. Here are the most dangerous.")
        print(Mercs)
        merc = input("Whose banner do you fly, Merc? ")
        while merc not in Mercs:
            print("This is not a worthy outfit. Try again.")
            merc = input("Whose banner do you fly, Merc? ")
        print("Ah. The " + merc + " Command. A fine and lethal formation.")
        lance = random.choice(Lances)
        print("Leading a " + lance + " Lance is no easy task." 
        " Let's see if you have the skill.")
        print("You are " + name + "." " You are a Lieutenant for " + merc + "."
        " The burden of duty is not new to you, and neither is death.")
        print(random_functions.lance_comp(lance))
        print(random_functions.IS_names())
        print(random_functions.PG_stat_is())
    else:
        print("That's not gonna fly.")

    play_again = input("Do you want to rewrite your story (yes/no)? ")
else:
    print("March on, and write your tale.")   



