import random

IS_light=["Locust", "Commando", "Stinger", "Jenner"]
IS_Med=["Wolverine", "Centurion", "Hunchback", "Shadow Hawk", "Phoenix Hawk"]
IS_Heav=["Marauder", "Catapult","Archer", "Warhammer", "Awesome", "Atlas", 
         "Battlemaster"]
CL_light=["Kit Fox", "Adder", "Fire Moth", "Piranha"]
CL_Med=["Stormcrow", "Nova", "Ice Ferret", "Shadow Cat" ]
CL_Heav=["Timber Wolf","Summoner", "Vulture", 
         "Hellbringer", "Dire Wolf", "Executioner", "Warhawk", "Ebon Jaguar",
         "Gargoyle"]
First_names = ["Kenji", "Haruka", "Takeshi", "Aiko", "Ryota", "Sakura", "Daichi", "Mei", "Hiroshi", "Yuki", 
               "Kaito", "Emiko", "Riku", "Ayumi", "Hikaru", "Satoshi", "Miyuki", 
                "Ren", "Yumi", "Takumi", "Jack", "Emily", "Connor", "Sarah", "Wyatt", "Megan", "Dalton", "Hannah", "Rhett", "Claire",
                "Klaus", "Ingrid", "Dieter", "Freya", "Matthias", "Astrid", "Gunnar", "Greta", "Lars", "Brigitte",
                "Wei", "Mei Lin", "Jun", "Xiaoling", "Bao", "Lian", "Tao", "Ying", "Hao", "Fang",
                "Rafael", "Elena", "Mateo", "Lucia", "Dario", "Isabella", "Tomas", "Chiara", "Andres", "Sofia", "Dave"]

IS_Last_names = ["Tanaka", "Yamamoto", "Kobayashi", "Matsumoto", "Fujimoto", "Nakamura", "Sato", "Suzuki", "Takahashi", "Yamaguchi",
              "Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez", "Martinez",
              "Schmidt", "Müller", "Weber", "Fischer", "Wagner", "Becker", "Hoffmann", "Schneider", "Koch", "Bauer",
              "Li", "Wang", "Zhang", "Liu", "Chen", "Yang", "Huang", "Zhao", "Wu", "Xu",
              "Gonzalez", "Perez", "Sanchez", "Ramirez", "Torres", "Flores", "Rivera", "Gomez", "Diaz"]
GB_Last_names =[ "Silva", "Gilmour", "Wayne", "DelVillar", "Devon", "Snuka"]
JF_Last_names = ["Pryde", "Chistu", "Buhallin", "Helmer", "Hazen", "Crichell"]
WF_Last_names = ["Kerensky", "Ward", "Radick", "Sender", "Vickers", "Conners", "Leroux", "Rhyde", "Isaac", "Ruby"]
SJ_Last_names = ["Bowen", "Moon", "Chrisholm", "Stiles", "Osis", "Furey", "Showers", "Nevversan"]
Gunnery_Ints = [3, 4, 4, 4, 5, 5, 6]
Piloting_Ints =[4, 5, 5, 5, 6, 6, 7]
def lance_comp(Lances):
    if Lances == "Recon":
        return ("Your lance will be: " + random.choice(IS_light) + ", " + 
            random.choice(IS_light) + ", " + random.choice(IS_light) + 
              ", " + "and " + random.choice(IS_light) + ". ")
    elif Lances == "Fire Support":
        return ("Your lance will be: " + random.choice(IS_Heav) + ", " + 
            random.choice(IS_light) + ", " + random.choice(IS_Heav) + 
              ", " + "and " + random.choice(IS_Heav) + ". ")
    elif Lances == "Heavy":
        return ("Your lance will be: " + random.choice(IS_Heav) + ", " + 
            random.choice(IS_Heav) + ", " + random.choice(IS_Heav) + 
              ", " + "and " + random.choice(IS_Heav) + ". ")
    elif Lances == "Command":
        return ("Your lance will be: " + random.choice(IS_Heav) + ", " + 
            random.choice(IS_Med) + ", " + random.choice(IS_Med) + 
              ", " + "and " + random.choice(IS_Med) + ". ")

    elif Lances == "Battle":
        return ("Your lance will be: " + random.choice(IS_Med) + ", " + 
            random.choice(IS_light) + ", " + random.choice(IS_Med) + 
              ", " + "and " + random.choice(IS_Heav) + ". ")





def star_comp(Stars):
    if Stars == "Fire Support":
        return ("Your star will be: " + random.choice(CL_Heav) + ", " + 
            random.choice(CL_Heav) + ", " + random.choice(CL_Med) + 
              ", " + "and " + random.choice(CL_light) + ", " + 
                "spearheaded by a " + random.choice(CL_Heav) + ". ")
    elif Stars == "Battle":
        return ("Your star will be: " + random.choice(CL_Med) + ", " + 
            random.choice(CL_Med) + ", " + random.choice(CL_Med) + 
              ", " + "and " + random.choice(CL_light) + ", " + 
                "spearheaded by a " + random.choice(CL_Heav) + ". ")

    elif Stars == "Command":
        return ("Your star will be: " + random.choice(CL_Heav) + ", " + 
            random.choice(CL_Med) + ", " + random.choice(CL_Med) + 
              ", " + "and " + random.choice(CL_light) + ", " + 
                "spearheaded by a " + random.choice(CL_Med) + ". ")
    elif Stars == "Heavy":
        return ("Your star will be: " + random.choice(CL_Heav) + ", " + 
            random.choice(CL_Heav) + ", " + random.choice(CL_Heav) + 
              ", " + "and " + random.choice(CL_Heav) + ", " + 
                "spearheaded by a " + random.choice(CL_Heav) + ". ")

    elif Stars == "Ad-hoc":
        return ("Your star will be: " + random.choice(CL_Heav) + ", " + 
            random.choice(CL_light) + ", " + random.choice(CL_Med) + 
              ", " + "and " + random.choice(CL_Med) + ", " + 
                "spearheaded by a " + random.choice(CL_Heav) + ". ")

    elif Stars == "Recon": 
        return ("Your star will be: " + random.choice(CL_light) + ", " + 
            random.choice(CL_light) + ", " + random.choice(CL_light) + 
              ", " + "and " + random.choice(CL_light) + ", " + 
                "spearheaded by a " + random.choice(CL_light) + ". ")

def IS_names():
    return "Your pilots will be: " + random.choice(First_names) + " " + random.choice(IS_Last_names) + ", " + random.choice(First_names) + " " + random.choice(IS_Last_names) + ", and " + random.choice(First_names) + " " + random.choice(IS_Last_names) + ". "

def CL_names(clan_choice):
    if clan_choice == "Ghost Bear":
        name_block = "Your pilots will be: " + random.choice(First_names) + ", " + random.choice(First_names) + ", " + random.choice(First_names) + " " + random.choice(GB_Last_names) + ", and " + random.choice(First_names) + " " + random.choice(GB_Last_names) + "." 
    elif clan_choice == "Jade Falcon":
        name_block = "Your pilots will be: " + random.choice(First_names) + ", " + random.choice(First_names) + ", " + random.choice(First_names) + " " + random.choice(JF_Last_names) + ", and " + random.choice(First_names) + " " + random.choice(JF_Last_names) + "."
    elif clan_choice == "Wolf":
        name_block = "Your pilots will be: " + random.choice(First_names) + ", " + random.choice(First_names) + ", " + random.choice(First_names) + " " + random.choice(WF_Last_names) + ", and " + random.choice(First_names) + " " + random.choice(WF_Last_names) + "."
    elif clan_choice == "Smoke Jaguar":
        name_block = "Your pilots will be: " + random.choice(First_names) + ", " + random.choice(First_names) + ", " + random.choice(First_names) + " " + random.choice(SJ_Last_names) + ", and " + random.choice(First_names) + " " + random.choice(SJ_Last_names) + "."
    return name_block

def PG_stat_cl():
    return "Your pilots have the following Pilot/Gunnery Skills: " + "P/G 1: " + str(random.choice(Piloting_Ints)) + "|" + str(random.choice(Gunnery_Ints)) + ", P/G 2: "  + str(random.choice(Piloting_Ints)) + "|" + str(random.choice(Gunnery_Ints)) + ", P/G 3: " + str(random.choice(Piloting_Ints)) + "|" + str(random.choice(Gunnery_Ints)) + ", P/G 4: " + str(random.choice(Piloting_Ints)) + "|" + str(random.choice(Gunnery_Ints)) + ", and your P/G: " + + "P/G 1: " + str(random.choice(Piloting_Ints)) + "|" + str(random.choice(Gunnery_Ints)) + "."

def PG_stat_is():
     return "Your pilots have the following Pilot/Gunnery Skills: " + "P/G 1: " + str(random.choice(Piloting_Ints)) + "|" + str(random.choice(Gunnery_Ints)) + ", P/G 2: "  + str(random.choice(Piloting_Ints)) + "|" + str(random.choice(Gunnery_Ints)) + ", P/G 3: " + str(random.choice(Piloting_Ints)) + "|" + str(random.choice(Gunnery_Ints)) + ", and your P/G: " + + "P/G 1: " + str(random.choice(Piloting_Ints)) + "|" + str(random.choice(Gunnery_Ints)) + "."
    
   