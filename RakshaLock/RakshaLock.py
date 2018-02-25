#Generator for Rakshasa Patron Warlock
import random

LVL = input("Player level?\n")

race = random.randint(0,8)
face = ""
forename = ""
surname = ""
occupation = ""
details = ""
plusSTR = 0
plusDEX = 0
plusCON = 0
SPEED = 0
STR = 0
DEX = 0
CON = 0
HPBoost = 0
HP = 0

if race <=0:
	face = "Dwarf"
	plusDEX = -1
	plusCON = 1
	SPEED = 25
	forename_in = open("Forename_Dwarf.txt")
	forename_list = forename_in.read().split('\n')
	forename = forename_list[random.randint(0,len(forename_list)-1)]
	surname_in = open("Surname_Dwarf.txt")
	surname_list = surname_in.read().split('\n')
	surname = surname_list[random.randint(0,len(surname_list)-1)]
elif race <=1:
	face = "Elf"
	plusDEX = 1
	plusCON = -1
	SPEED = 30
	forename_in = open("Forename_Elf.txt")
	forename_list = forename_in.read().split('\n')
	forename = forename_list[random.randint(0,len(forename_list)-1)]
	surname_in = open("Surname_Elf.txt")
	surname_list = surname_in.read().split('\n')
	surname = surname_list[random.randint(0,len(surname_list)-1)]
elif race <=2:
	face = "Halfling"
	plusDEX = 1
	plusSTR = -1
	SPEED = 30
	forename_in = open("Forename_Halfling.txt")
	forename_list = forename_in.read().split('\n')
	forename = forename_list[random.randint(0,len(forename_list)-1)]
	surname_in = open("Surname_Halfling.txt")
	surname_list = surname_in.read().split('\n')
	surname = surname_list[random.randint(0,len(surname_list)-1)]
elif race <=3:
	face = "Human"
	SPEED = 30
	forename_in = open("Forename_Human.txt")
	forename_list = forename_in.read().split('\n')
	forename = forename_list[random.randint(0,len(forename_list)-1)]
	surname_in = open("Surname_Human.txt")
	surname_list = surname_in.read().split('\n')
	surname = surname_list[random.randint(0,len(surname_list)-1)]
elif race <=4:
	face = "Dragonborn"
	plusSTR = 1
	plusCON = -1
	SPEED = 30
	forename_in = open("Forename_Dragonborn.txt")
	forename_list = forename_in.read().split('\n')
	forename = forename_list[random.randint(0,len(forename_list)-1)]
	surname_in = open("Surname_Dragonborn.txt")
	surname_list = surname_in.read().split('\n')
	surname = surname_list[random.randint(0,len(surname_list)-1)]
elif race <=5:
	face = "Gnome"
	SPEED = 25
	forename_in = open("Forename_Gnome.txt")
	forename_list = forename_in.read().split('\n')
	forename = forename_list[random.randint(0,len(forename_list)-1)]
	surname_in = open("Surname_Gnome.txt")
	surname_list = surname_in.read().split('\n')
	surname = surname_list[random.randint(0,len(surname_list)-1)]
elif race <=6:
	face = "Half-Elf"
	SPEED = 30
	forename_in = open(random.choice(["Forename_Elf.txt","Forename_Human.txt"]))
	forename_list = forename_in.read().split('\n')
	forename = forename_list[random.randint(0,len(forename_list)-1)]
	surname_in = open(random.choice(["Surname_Elf.txt","Surname_Human.txt"]))
	surname_list = surname_in.read().split('\n')
	surname = surname_list[random.randint(0,len(surname_list)-1)]
elif race <=7:
	face = "Half-Orc"
	plusSTR = 1
	plusDEX = -2
	plusCON = 1
	SPEED = 30
	forename_in = open(random.choice(["Forename_Orc.txt","Forename_Human.txt"]))
	forename_list = forename_in.read().split('\n')
	forename = forename_list[random.randint(0,len(forename_list)-1)]
	surname_in = open("Surname_Human.txt")
	surname_list = surname_in.read().split('\n')
	surname = surname_list[random.randint(0,len(surname_list)-1)]
else:
	face = "Tiefling"
	SPEED = 30
	forename_in = open(random.choice(["Forename_Tiefling.txt","Forename_Human.txt"]))
	forename_list = forename_in.read().split('\n')
	forename = forename_list[random.randint(0,len(forename_list)-1)]
	surname_in = open("Surname_Human.txt")
	surname_list = surname_in.read().split('\n')
	surname = surname_list[random.randint(0,len(surname_list)-1)]

while(STR<8 or DEX<8 or CON<8):
	STR_array = sorted([random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)])
	DEX_array = sorted([random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)])
	CON_array = sorted([random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)])
	STR = sum(STR_array[1:])+plusSTR
	DEX = sum(DEX_array[1:])+plusDEX
	CON = sum(DEX_array[1:])+plusCON

if CON <= 9:
	HPBoost = -1
elif CON<=11:
	HPBoost = 0
elif CON<=13:
	HPBoost = 1
elif CON<=15:
	HPBoost = 2
elif CON<=17:
	HPBoost = 3
else:
	HPBoost = 4

for x in range(0,LVL):
	HP = HP + random.randint(1,8) + HPBoost

job = random.randint(1,100) 
if job <=5:
	occupation = "academic"
	field = random.choice(["alchemy","astronomy","archival studies","arcana","botany","zoology","linguistics","history","philosophy","mathematics","medicine","engineering"])
	details = " specializing in " + field
elif job<=10:
	occupation = "adventurer"
elif job<=11:
	occupation = ""
	details = random.choice(["noble","industrialist","heir","aristocrat"])
elif job<=26:
	occupation = ""
	details = random.choice(["apothecary","locksmith","brewer","calligrapher","carpenter","cartographer","shoemaker","chef","baker","glassblower","jeweller","leatherworker","mason","potter","shipwright","blacksmith","mechanic","weaver"])
elif job<=31:
	occupation = ""
	details = random.choice(["burglar","gang enforcer","highway robber","sellsword","pickpocket","smuggler","grifter","con artist"])
elif job<=36:
	occupation = ""
	details = random.choice(["actor","dancer","comedian","juggler","instrumentalist","poet","acrobat","singer","storyteller","gladiator"])
elif job <=38: 
	occupation = ""
	details = random.choice(["hermit","exile","refugee"])
elif job <=43:
	occupation = "explorer"
elif job<=55:
	occupation = ""
	details = random.choice(["farmer","shepherd","beekeeper","farmer"])
elif job <=60:
	occupation = "hunter and trapper"
elif job<=75:
	occupation = ""
	details = random.choice(["farm laborer","factory worker","sex worker"])
elif job<=80:
	occupation = "merchant"
	goods = random.choice(["foreign luxuries","furs","spices","general goods","furniture","durable foods","weapons"])
	details = " selling " + goods
elif job<=85:
	occupation = ""
	details = random.choice(["union leader","alderman","councillor","governor","disgraced politician","ambassador","bureaucrat"])
elif job<=90:
	occupation = "priest"
elif job<=95:
	occupation = "sailor"
	ship = random.choice(["merchant ship","naval expidition","whaling ship","pirate ship","warship"])
	details = " on a " + ship
else:
	occupation = "soldier"
	rank = random.choice(["infantry","cavalry","captain","sargeant","commander","infantry","infantry"])
	details = ". Your rank was " + rank

land_in = open("Homelands.txt")
land_list = land_in.read().split('\n')
homeland = random.randint(0,len(land_list))

print face
print "Walk Speed: " + str(SPEED)
print "[STR, DEX, CON]: " + str([STR,DEX,CON])
print "HP: " + str(HP)
print "Your name is " + forename + " " + surname + ". You hail from " + land_list[homeland] + ". You are a/an " + occupation + details + "."