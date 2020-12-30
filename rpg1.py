import random
import time
from os import system

##CONTROL FUNCTIONS##

def namecon(name):
    while True:
        if len(name) > 30:
            name = input("Please enter a shorter name. (30 characters max.)\n")

        elif name.replace(" ", "") == "":
            name = input("You DO have a name right??? Enter it:\n")

        else:
            break

##CLASSES AND JOBS##

class Equip():
    def __init__(self, name, typ, maxhp, maxmp, atk, df, spd, mag, mdf):
        self.name = name
        self.typ = typ
        self.maxhp = maxhp
        self.maxmp = maxmp
        self.atk = atk
        self.df = df
        self.spd = spd
        self.mag = mag
        self.mdf = mdf


class FullJob():
    def __init__(self, name, maxhp, maxmp, atk, df, spd, mag, mdf, spells, lvbons):
        self.name = name
        self.maxhp = maxhp
        self.hp = maxhp
        self.maxmp = maxmp
        self.mp = maxmp
        self.atk = atk
        self.df = df
        self.spd = spd
        self.mag = mag
        self.mdf = mdf

        self.spells = spells
        self.lvbons = lvbons



class Monster():
    def __init__(self, name, lv, maxhp, maxmp, atk, df, spd, mag, mdf, spells, pattern, exploot, goldloot):
        self.name = name
        self.lv = lv
        self.maxhp = maxhp
        self.hp = maxhp
        self.maxmp = maxmp
        self.mp = maxmp
        self.atk = atk
        self.df = df
        self.spd = spd
        self.mag = mag
        self.mdf = mdf

        self.status = ""

        self.spells = spells
        self.pattern = pattern
        self.exploot = exploot
        self.goldloot = goldloot

    def phase(self):
        def monstercast():
            moncastlist = list()
            for i in self.spells:
                if dmgspell.get(i).cost <= self.mp:
                    moncastlist.append(i)

            if len(moncastlist) > 0:
                cast(self, player, dmgspell.get(moncastlist[random.randrange(0,len(moncastlist))]))
            else:
                fight(self, player)
                        
        if self.pattern == "aggro": #aggro, mage, buffer/debuffer, special aggro, bosses separate
            fight(self, player) 
        elif self.pattern == "mage":
            if self.lv < player.lv and player.hp >= player.maxhp/2:
                monstercast()
            elif self.lv >= player.lv: 
                monstercast()
            else: 
                fight(self, player)


class Player():
    name = input("Please enter your name:\n")
    namecon(name)

    joblist = {"mage":FullJob("mage", 10, 20, 3, 4, 5, 7, 6, ["fire", "heal"], [2,4,1,2,3,5,4]),
    "fighter":FullJob("fighter", 20, 10, 7, 6, 5, 3, 4, [], [4,2,5,4,3,1,2]),
    "rogue":FullJob("rogue", 15, 15, 4, 4, 9, 4, 4, [], [2,2,4,3,5,4,3])}

    jobsel = input("Please select a job: \n* Fighter\n* Mage\n* Rogue\n").lower()
    jobtrig = jobsel in joblist.keys()

    while not jobtrig:
        jobsel = input("Invalid job. Please select again: \n* Fighter\n* Mage\n* Rogue\n").lower()
        job = joblist.get(jobsel) 
        jobtrig = jobsel in joblist.keys()   

    job = joblist.get(jobsel)

    weapon = "none"
    armor = "none"

    lv = 1
    maxhp = job.maxhp
    hp = maxhp
    maxmp = job.maxmp
    mp = maxmp
    atk = job.atk
    df = job.df
    spd = job.spd
    mag = job.mag
    mdf = job.mdf

    exp = 0
    expreq = 50
    gold = 0
    status = "OK"
    inv = ["red potion", "red potion", "sword"]
    spells = job.spells

    enemy = Monster("Slime", 0, 5, 5, 1, 1, 1, 1, 1, [] , "aggro", 10, 10)
    away = False
    
    def invset(self):
        dupinv = set()
        uniqinv = []
        tempinv = []

        for i in self.inv:
            tempinv.append(i.title() + " * {}".format(self.inv.count(i)))

        for i in tempinv:
            if i not in dupinv:
                dupinv.add(i)
                uniqinv.append(i)

        return uniqinv

    def lvup(self):
        def incre(exnum):
            return random.randint(1, self.job.lvbons[exnum])
        
        if self.exp >= self.expreq:
            self.lv += 1
            self.expreq = round(100*(self.lv**2)/2)
            self.exp = 0

            print("{} is now Level {}!\n".format(self.name, self.lv))
            time.sleep(1)
            self.maxhp += incre(0)
            self.maxmp += incre(1)
            self.atk += incre(2)
            self.df += incre(3)
            self.spd += incre(4)
            self.mag += incre(5)
            self.mdf += incre(6)

            print("New stats:\n Max HP: {}\n Max MP: {}\n Attack: {}\n Defense: {}\n Speed: {}\n Magic: {}\n Magic Defense: {}\n".format(self.maxhp, self.maxmp, self.atk, self.df, self.spd, self.mag, self.mdf))
            input("Press Enter to continue.")
            system('cls')

    def phase(self):
        def resetscreen():
            system("cls")
            print("{} - HP:{}/{}".format(self.enemy.name, self.enemy.hp, self.enemy.maxhp))
            print(" _ " * 30)
            print("{} - {} - LV{} - HP: {}/{} - MP: {}/{} - STATUS: {}".format(self.name, self.jobsel.title(), self.lv, self.hp, self.maxhp, self.mp, self.maxmp, self.status))
            print("""

            [1]FIGHT              [2]MAGIC
            [3]ITEM               [4]RUN
            
            """)
            print(" _ " * 30)

        def act():
            action = input("Please choose an action:\n")  
            if action == "1":
                fight(self, self.enemy)
                resetscreen()

            elif action == "2":
                if self.spells == []:
                    resetscreen()
                    print("You don't have any spells.\n")
                    time.sleep(2)
                    self.phase()
                    
                else:
                    for spellies in self.spells:
                        print(spellies.title())
                    i = input("Select the spell to cast:\n").lower()
                    if i in dmgspell.keys() and i in self.spells:
                        if dmgspell.get(i).cost <= self.mp:
                            cast(self, self.enemy, dmgspell.get(i))
                        else:
                            resetscreen()
                            print("Not enough MP!\n")
                            time.sleep(2)
                            self.phase()
                    elif i in healspell.keys() and i in self.spells:
                        if healspell.get(i).cost <= self.mp:
                            cast(self, self, healspell.get(i))
                        else:
                            resetscreen()
                            print("Not enough MP!\n")
                            time.sleep(2)
                            self.phase()
                    else:
                        resetscreen()
                        print("Please enter a correct spell.\n")
                        time.sleep(2)
                        self.phase()
                        
            
            elif action == "3":
                if self.inv == []:
                    resetscreen()
                    print("You don't have any items.\n")
                    time.sleep(2)
                    self.phase()
                else:
                    for itemies in self.invset():
                        print(itemies)
                    i = input("Select the item to use:\n")
                    if i in itemlist.keys() and i in self.inv:
                        useitem(self, itemlist.get(i))
                    else:
                        resetscreen()
                        print("Please choose a correct item.\n")
                        time.sleep(2)
                        self.phase()

            elif action == "4":
                self.away = run(self.enemy)

            else:
                resetscreen()
                print("Invalid action.\n")
                time.sleep(1)
                self.phase()
        
        resetscreen()
        act()
    

class Spell():
    def __init__(self, initdmg, hit, attribute, typ, name, cost):
        self.name = name
        self.typ = typ
        self.initdmg = initdmg
        self.hit = hit
        self.attribute = attribute
        self.cost = cost


class Item():
    def __init__(self, name, effect, power):
        self.name = name
        self.effect = effect
        self.power = power

class Area():
    def __init__(self, name, monlist, lootlist, boss, flavtxt):
        self.name = name
        self.monlist = monlist
        self.lootlist = lootlist
        self.boss = boss
        self.randomflav = ["exciting", "boring", "creepy", "sad", "taxing", "hard", "...weird"]
        self.flavtxt = flavtxt
        self.flavtxt += ["You wondered about why your parents named you {}.".format(player.name), "You mumbled a song to yourself. Feeling lonely?", "You pondered about your journey so far. Isn't it kind of {}?".format(self.randomflav[random.randrange(0,len(self.randomflav))])] 
        #first two = minor and major recovery, second two = idle, third two = item found, fourth two = town/city found 


##SETUP##

player = Player()

slime = Monster("Slime", 0, 5, 5, 1, 1, 2, 1, 1, [] , "aggro", 10, 5)
redslime = Monster("Red Slime", 1, 10, 10, 5, 5, 5, 5, 5, [] , "aggro", 30, 10)
oraslime = Monster("Orange Slime", 3, 15, 15, 8, 10, 10, 5, 3, [] , "aggro", 70, 20)

jam = Monster("Jam", 1, 10, 20, 2, 2, 4, 5, 8, ["jamburst"], "mage", 60, 10)
redjam = Monster("Strawberry Jam", 3, 20, 30, 5, 3, 8, 8, 9, ["jamburst", "fire"], "mage", 80, 20)

kingslime = Monster("King Slime", 5, 50, 20, 10, 15, 9, 10, 15, ["jamburst"] , "mage", 100, 200)

##DATABASE##

dmgspell = {"fire":Spell(10, 99, "fire","dmg","fire", 5),
"megafire":Spell(50, 85, "fire","dmg","megafire", 20),
"gigafire":Spell(100, 75,"fire","dmg","gigafire", 40),
"jamburst":Spell(8, 95, "none","dmg","jamburst", 5)}

healspell = {"heal":Spell(10, 100, "none","heal","heal", 5),
"megaheal":Spell(50, 100, "none","heal","megaheal", 20),
"gigaheal":Spell(100, 100, "none","heal","gigaheal", 40)}

itemlist = {"red potion":Item("red potion", "heal", 20),
"blue potion":Item("blue potion", "mpheal", 20)}

arealist = {"plains":Area("plains", [slime, redslime, jam, oraslime, redjam], ["red potion", "blue potion"], kingslime, ["You strolled around the green grass. Good relief!", "You chilled with some friendly slimes. Turns out not everyone is out for blood, huh?", "You started to dance out of boredom.", "Something incredible is about to happen!.. Or not.", "You found something lying on the tall grass.", "Ow! You tripped over something."])}

eqlist = {"none":Equip("none","none", 0, 0, 0, 0, 0, 0, 0),
"sword":Equip("sword","weapon", 0, 0, 3, 0, 0, 0, 0), 
"dagger":Equip("dagger","weapon", 0, 0, 1, 0, 2, 0, 0), 
"rod":Equip("rod","weapon", 0, 0, 1, 0, 0, 2, 0), 
"armor":Equip("armor","armor", 0, 0, 0, 3, 0, 0, 0)} 

##OVERWORLD FUNCTIONS##

explorelv = 0

def explore(area):
    system('cls')
    print("Exploring the {}!".format(area.name))
    time.sleep(1)
    monstercount = round(player.lv*2/random.randint(1,player.lv+1))
    expmonlist = []
    while monstercount > 0:
        flavour = area.flavtxt[random.randrange(0,len(area.flavtxt))]
        print(flavour)
        time.sleep(1)
        if flavour in area.randomflav or flavour == area.flavtxt[2] or flavour == area.flavtxt[3]:
            pass
        else: 
            if flavour == area.flavtxt[1] and player.hp != player.maxhp:
                print("Recovered some HP!")
                player.hp += round(player.maxhp/random.randint(5,10))
                if player.hp > player.maxhp:
                    player.hp = player.maxhp

            elif flavour == area.flavtxt[0] and player.mp != player.maxmp:
                print("Recovered some MP!")
                player.mp += round(player.maxmp/random.randint(5,10))
                if player.mp > player.maxmp:
                    player.mp = player.maxmp
                
            elif flavour == area.flavtxt[4] or flavour == area.flavtxt[5]:
                loot = area.lootlist[random.randrange(0, len(area.lootlist))]
                print("Picked up the {}!".format(loot))
                player.inv.append(loot)
            #city and shop

        time.sleep(2)
        monstercount -= 1

    for i in area.monlist:
        if i.lv <= player.lv:
            expmonlist.append(i)
    
    if player.lv >= area.boss.lv:
        print("You encounter the boss of the {}, {}!".format(area.name, area.boss.name))
        time.sleep(2)
        fightscreen(area.boss)
    else:
        fightscreen(expmonlist[random.randrange(0,len(expmonlist))])

    if input("Continue adventuring? y/n").lower() == "n":
        print("You returned to the hub.")
        time.sleep(2)
        hub()
    else:
        explore(area)

def hub():
    system('cls')

    def hubitem():
        system('cls')
        for i in player.invset():
            print(i)

        itemsel = input("\nPlease choose an item to use.\nPress enter to cancel.\n").lower()
        if itemsel in itemlist.keys() and itemsel in player.inv:
            useitem(player, itemlist.get(itemsel))
        elif itemsel == "":
            hub()
        else:
            print("Please enter correctly.")
            time.sleep(2)
            system('cls')
            hubitem()


    print("Welcome to the hub!")
    hubput = input("""What would you like to do?
    1 - View Stats
    2 - Use Item
    3 - Equip Weapon/Armor
    4 - Rest at the Inn (50G) 
    5 - Explore
    6 - Exit

    """)

    if hubput == "1":
        system('cls')
        input("""{}'s stats:
        LV: {}
        Job: {}
        Status: {}

        HP: {}/{}
        MP: {}/{}
        Attack: {}
        Defense: {}
        Speed: {}
        Magic: {}
        Magic Defense: {}

        Gold: {}
        {} Exp left to level up
        
        Press enter to continue.
        """.format(player.name, player.lv, player.job.name.capitalize(), player.status, player.hp, player.maxhp, player.mp, player.maxmp, player.atk, player.df, player.spd, player.mag, player.mdf, player.gold, player.expreq))
        hub()

    elif hubput == "2":
        hubitem()
        hub()

    elif hubput == "3":
        prestat = {"Max HP":player.maxhp, "Max MP":player.maxmp, "Attack":player.atk, "Defense":player.df, "Speed":player.spd, "Magic":player.mag, "Magic Defense":player.mdf}
        system('cls')
        for itemies in player.invset():
            print(itemies)
        print("\nEnter Remove to unequip all equipment.\n")
        eqinput = input("Please enter an item to equip.\n").lower()
        if eqinput in player.inv and eqinput in eqlist.keys():
            if eqlist.get(eqinput).typ == "armor":
                equipitem(eqlist.get(eqinput), eqlist.get(player.armor))
                if player.armor != "none":
                    player.inv.append(player.armor)
                player.armor = eqinput
                player.inv.remove(eqinput)
                
            elif eqlist.get(eqinput).typ == "weapon":
                equipitem(eqlist.get(eqinput), eqlist.get(player.weapon))
                if player.weapon != "none":
                    player.inv.append(player.weapon)
                player.weapon = eqinput
                player.inv.remove(eqinput)
                
            print("Equipped {}.".format(eqinput.capitalize()))
            poststat = {"Max HP":player.maxhp, "Max MP":player.maxmp, "Attack":player.atk, "Defense":player.df, "Speed":player.spd, "Magic":player.mag, "Magic Defense":player.mdf}
            time.sleep(1)
            for i in prestat.keys(): 
                if prestat.get(i) != poststat.get(i):
                    print("{}: {} --> {}".format(i, prestat.get(i), poststat.get(i)))
            input("\nPress enter to continue.\n")
            hub()
        elif eqinput == "remove":
            equipitem(eqlist.get("none"), eqlist.get(player.armor))
            equipitem(eqlist.get("none"), eqlist.get(player.weapon))
            print("Removed all equipment.")
            if player.armor != "none":
                player.inv.append(player.armor)
            if player.weapon != "none":    
                player.inv.append(player.weapon)
            player.armor = "none"
            player.weapon = "none"
            poststat = {"Max HP":player.maxhp, "Max MP":player.maxmp, "Attack":player.atk, "Defense":player.df, "Speed":player.spd, "Magic":player.mag, "Magic Defense":player.mdf}
            for i in prestat.keys(): 
                if prestat.get(i) != poststat.get(i):
                    print("{}: {} --> {}".format(i, prestat.get(i), poststat.get(i)))
            input("\nPress enter to continue.\n")
            hub()
        else:
            print("Please choose a correct item.")
            time.sleep(2)
            hub()
        
    
    elif hubput == "4":
        system('cls')
        innsel = input("Rest at the inn? y/n\n")
        if (innsel.lower() == "y" or innsel == "") and player.gold >= 50:
            print("{} slept at the inn.\n".format(player.name))
            time.sleep(1)
            player.hp = player.maxhp
            player.mp = player.maxmp
            print("Recovered all MP!")
            time.sleep(2)
        elif (innsel.lower() == "y" or innsel == "") and player.gold < 50:
            print("You are too poor to have a nice sleep.")
            time.sleep(2)
        else:
            pass
        hub()

    elif hubput == "5":
        #selecting area
        explore(arealist.get("plains"))

    elif hubput == "6":
        exitput = input("You will lose all progress. Continue? y/n\n")
        if exitput.lower() == "y":
            print("Goodbye!")
            time.sleep(2)
            quit()
        else:
            hub()

def equipitem(eqitem, previtem):
    player.atk = player.atk + eqitem.atk - previtem.atk
    player.df = player.df + eqitem.df - previtem.df
    player.spd = player.spd+ eqitem.spd - previtem.spd
    player.mdf = player.mdf + eqitem.mdf - previtem.mdf
    player.maxhp = player.maxhp + eqitem.maxhp - previtem.maxhp
    player.maxmp = player.maxmp + eqitem.maxmp - previtem.maxmp
    player.mag = player.mag + eqitem.mag - previtem.mag


##BATTLE FUNCTIONS##

def fight(user, target):
    print("{} attacks!\n".format(user.name))
    time.sleep(1)
    dmg = round(user.atk * (user.atk / (target.df + user.atk))) + random.randint(0,1) - random.randint(0,1)
    if dmg >= 1 and (user.spd/2 + user.atk/2) - (target.spd/2 + target.df/2) > 0 and random.randint(1,100) <= (user.spd/2 + user.atk/2) - (target.spd/2 + target.df/2):
        print("Critical hit!\n")
        time.sleep(1)
        target.hp -= 2*dmg 
    elif dmg >= 1:
        target.hp -= dmg
    else:
        dmg = 1
        target.hp -= 1
    if target.hp <= 0:
        target.hp = 0

    print("{} took {} damage!\n".format(target.name, str(dmg)))
    time.sleep(1)
        
def run(enemy):
    if player.spd > enemy.spd:
        print("{} ran away!\n".format(player.name))
        return True
    elif player.spd <= enemy.spd and random.randint(1,101) > 50:
        print("{} ran away!\n".format(player.name))
        return True
    else:
        print("{} couldn't run away!\n".format(player.name))
        return False

def cast(user, target, castspell):
    print("{} casts {}!\n".format(user.name, castspell.name.title()))
    time.sleep(1)
    dmg = round((castspell.initdmg + user.mag) * (user.mag / (target.mdf + user.mag)))
    heal = castspell.initdmg + user.mag
    
    if castspell.typ == "dmg":
        if random.randint(1,100) <= castspell.hit:
            if dmg >= 1 and (user.spd/3 + user.mag/3) - (target.spd/3 + target.mdf/3) > 0 and random.randint(1,100) <= (user.spd/3 + user.mag/3) - (target.spd/3 + target.mdf/3):
                print("Critical hit!\n")
                time.sleep(1)
                dmg = 2*dmg
                target.hp -= dmg
            elif dmg >= 1:
                target.hp -= dmg
            else:
                dmg = 1
                target.hp -= 1
            print("{} took {} damage!\n".format(target.name, str(dmg)))
        else:
            print("Miss!\n")
            time.sleep(1)

    elif castspell.typ == "heal":
        target.hp += heal
        print("{} recovered {} HP!\n".format(target.name, str(heal)))
    user.mp -= castspell.cost
    time.sleep(1)

def useitem(user, uitem):
    print("{} uses {}!\n".format(user.name, uitem.name))
    time.sleep(1)

    if uitem.effect == "heal":
        user.hp += uitem.power
        print("{} recovered {} HP!\n".format(user.name, str(uitem.power)))

    elif uitem.effect == "mpheal":
        user.mp += uitem.power
        print("{} recovered {} MP!\n".format(user.name, str(uitem.power)))

    #extra effects here

    user.inv.remove(uitem.name)
    time.sleep(1)


def battlecon(unit):
    def poolcheck(unit):
        if unit.hp > unit.maxhp:
            unit.hp = unit.maxhp
            
        if unit.mp > unit.maxmp:
            unit.mp = unit.maxmp

    if unit.hp > 0 and player.away == False:
        unit.phase()
        poolcheck(unit)

def fightscreen(enemy):
    player.enemy = enemy
    enemy.hp = enemy.maxhp
    enemy.mp = enemy.maxmp
    player.away = False
    system('cls')

    def wincon():   
            if enemy.hp <= 0:
                print("{} fell apart!\n".format(enemy.name))
                time.sleep(2)
                system('cls')
                print("YOU WON!\n")
                time.sleep(1)
                player.exp += enemy.exploot
                print("Gained {} EXP!\n".format(enemy.exploot))
                time.sleep(1)
                player.gold += enemy.goldloot
                print("Gained {}G!\n".format(enemy.goldloot))
                time.sleep(2)
                system('cls')
                player.lvup()
            elif player.hp <= 0:
                print("{} collapsed...\n".format(player.name))
                time.sleep(1)
                player.hp = 1
                player.gold = int(player.gold/2)
                print("Lost {}G.".format(int(player.gold/2)))
                time.sleep(2)
                hub()

    print("{} appears!\n".format(enemy.name))
    time.sleep(1)
    while enemy.hp > 0 and player.hp > 0:
        if player.away == True:
            player.away = False
            break
        else:
            if player.spd >= 2.5*enemy.spd:
                a = 1
                while a < player.spd/enemy.spd:
                    battlecon(player)
                    if enemy.hp <= 0:
                        break
                    a += 1
                battlecon(enemy)

            elif enemy.spd >= 2.5*player.spd:
                b = 1
                while b < enemy.spd/player.spd:
                    battlecon(enemy)
                    if enemy.hp <= 0:
                        break
                    b += 1
                battlecon(player)

            elif player.spd >= enemy.spd:
                battlecon(player)
                battlecon(enemy)
            else:
                battlecon(enemy)
                battlecon(player)
            
            wincon()
            



##MAIN##

def main():
    system('cls')
    print("Basic RPG by KiiroDora - v0.0.7")
    time.sleep(3)
    hub()

main()
