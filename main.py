import fantasynames as fnames
import os
from random import randrange,randint,choice
from os import system, name
import pickle
import time



def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')




class Ritual:
    def __init__(self):
        self.name = "None" # i.e. Dagger, Sword, Crown

        self.isPerformed = False



    def get_name(self):
        return self.name
    def set_name(self, x):
        self.name = x


    def get_isPerformed(self):
        return self.isPerformed
    def set_isPerformed(self, x):
        self.isPerformed = x




class Item:
    def __init__(self):
        self.name = "None" # i.e. Dagger, Sword, Crown
        self.adj = "None" # i.e. Greasy, Putrid, Glowing

        self.isOwned = False



    def get_name(self):
        return self.name
    def set_name(self, x):
        self.name = x


    def get_adj(self):
        return self.adj
    def set_adj(self, x):
        self.adj = x

    def get_isOwned(self):
        return self.isOwned
    def set_isOwned(self, x):
        self.isOwned = x

Ritual1 = Ritual()
Ritual2 = Ritual()
Ritual3 = Ritual()
Ritual4 = Ritual()

Item1 = Item()
Item2 = Item()
Item3 = Item()
Item4 = Item()
Item5 = Item()

def generateItems():
    possibleItems = ["Dagger", "Sword", "Crown", "Belt", "Pauldrons", "Helmet", "Shield", "Book", "Tome", "Legplate", "Vambrace", "Boots"]

    possibleAdj = ["Greasy", "Ashen", "Icy", "Molten", "Mossy", "Wooden", "Putrid", "Glowing", "Silver", "Nickel", "Copper", "Heavy", "Ethereal", "Tainted", "Blessed", "Sacred", "Holy", "Unholy", "Filthy", "Pristine", "Dull", "Foul", "Gilded"]




    Item.set_name(Item1, choice(possibleItems))
    Item.set_adj(Item1, choice(possibleAdj))
    Item.set_name(Item2, choice(possibleItems))
    Item.set_adj(Item2, choice(possibleAdj))
    Item.set_name(Item3, choice(possibleItems))
    Item.set_adj(Item3, choice(possibleAdj))
    Item.set_name(Item4, choice(possibleItems))
    Item.set_adj(Item4, choice(possibleAdj))
    Item.set_name(Item5, choice(possibleItems))
    Item.set_adj(Item5, choice(possibleAdj))





class TestObject:
    def __init__(self):
        self.name = "TestObjectName"

    def get_name(self):
        return self.name
    def set_name(self, x):
        self.name = x


TestObject1 = TestObject()


def LoadedSave():
    LoadedSave = 1

def NoLoadedSave():
    global LoadedSave
    LoadedSave = 0









class Enemy:
    def __init__(self):

        names = [fnames.elf(), fnames.human(), fnames.hobbit(), fnames.dwarf()]
        self.name = choice(names)
        ## CHARACTERISTICS
        self.WeaponSkill = randrange(30, 40)
        self.Strength = randrange(30, 40)
        self.Toughness = randrange(30, 40)
        self.Dexterity = randrange(30, 40)
        self.Charisma = randrange(30, 40)
        self.Intellect = randrange(30, 40)
        self.EnemyAttackStat = randrange(10,20)

        # Accuracy test will be to be lower than the accuracy stat so higher stats are better - i.e. 75 accuracy only needs to roll lower than 75 to hit
        self.EnemyAccuracy = randrange(25,100)

        # Attack Modifier will be added as bonus damage to a damage roll, the same king of damage roll (2d20?) that the PCs and Party will make

        self.EnemyAttackModifier = randrange(4,25)

        self.EnemyDamage = randrange(1,5)


        self.EnemyClass = "None"

        #self.Health = randrange(150, 500)
        self.Health = randrange(40, 110)
        #self.MaxHealth = 300
        self.MaxHealth = 125

        self.ArmourClass = randrange(25, 30)
        #self.ArmourClass = randrange(12,18)

        self.StatScore = self.WeaponSkill + self.Strength + self.Toughness + self.Dexterity + self.Charisma + self.Intellect + self.Health
        self.Initiative = randrange(1,20)   + randrange(1,6)
        self.Omen = ""
        self.Personality = ""


        self.NumberOfKills = 0

        self.reset()

        self.BattleTurn = 1
        self.Stage = 1


    def reset(self):
        self.name = fnames.elf()
        ## CHARACTERISTICS
        self.WeaponSkill = randrange(30, 40)
        self.Strength = randrange(30, 40)
        self.Toughness = randrange(30, 40)
        self.Dexterity = randrange(30, 40)
        self.Charisma = randrange(30, 40)
        self.Intellect = randrange(30, 40)
        self.EnemyAttackStat = randrange(10, 20)

        # Accuracy test will be to be lower than the accuracy stat so higher stats are better - i.e. 75 accuracy only needs to roll lower than 75 to hit
        self.EnemyAccuracy = randrange(40, 95)

        # Attack Modifier will be added as bonus damage to a damage roll, the same king of damage roll (2d20?) that the PCs and Party will make

        self.EnemyAttackModifier = randrange(4, 25)

        self.EnemyDamage = randrange(1, 5)

        self.EnemyClass = "None"



        self.Health = randrange(40, 110)
        self.MaxHealth = 125

        #self.ArmourClass = randrange(25,30)
        self.ArmourClass = randrange(12,18)
        self.StatScore = self.WeaponSkill + self.Strength + self.Toughness + self.Dexterity + self.Charisma + self.Intellect + self.Health
        self.Initiative = randrange(1, 20) + randrange(1,6) + randrange(1,4)
        self.Omen = ""
        self.Personality = ""


    def get_EnemyClass(self):
        return self.EnemyClass
    def set_EnemyClass(self, x):
        self.EnemyClass = x


    def get_Personality(self):
        return self.Personality
    def set_Personality(self, x):
        self.Personality = x
    def get_Health(self):
        return self.Health
    def set_Health(self, x):
        self.Health = x
    def get_ArmourClass(self):
        return self.ArmourClass
    def set_ArmourClass(self, x):
        self.ArmourClass = x
    def get_Initiative(self):
        return self.Initiative
    def set_Initiative(self, x):
        self.Initiative = x
    def get_Omen(self):
        return self.Omen
    def set_Omen(self, x):
        self.Omen = x

    def get_NumberOfKills(self):
        return self.NumberOfKills
    def set_NumberOfKills(self, x):
        self.NumberOfKills = x

    def get_EnemyAccuracy(self):
        return self.EnemyAccuracy
    def set_EnemyAccuracy(self, x):
        self.EnemyAccuracy = x
    def get_EnemyAttackModifier(self):
        return self.EnemyAttackModifier
    def set_EnemyAttackModifier(self, x):
        self.EnemyAttackModifier = x
    def get_MaxHealth(self):
        return self.MaxHealth
    def set_MaxHealth(self, x):
        self.MaxHealth = x

    def get_BattleTurn(self):
        return self.BattleTurn
    def set_BattleTurn(self, x):
        self.BattleTurn = x
    def get_Stage(self):
        return self.Stage
    def set_Stage(self, x):
        self.Stage = x


    def get_EnemyDamage(self):
        return self.EnemyDamage
    def set_EnemyDamage(self, x):
        self.EnemyDamage = x


    def get_name(self):
        return self.name



    def get_EnemyAttackStat(self):
        return self.EnemyAttackStat
    def get_EnemyAttackModifier(self):
        return self.EnemyAttackModifier
    def get_EnemyDamage(self):
        return self.EnemyDamage





        roll = randrange(1, 100)
        if roll > 33:
            rolledPersonality = choice(possiblePersonality)
            set_Personality(TestEnemy, rolledPersonality)
            levelMulti = Enemy.get_NumberOfKills(TestEnemy) + 1
            roll2 = randrange(1,100) - (2 * levelMulti)
            if 1 <= roll <= 33:
                roll3 = randrange(1,2)
                if roll3 == 1:
                    rolledOmen = choice(possibleOmen)
                    Enemy.set_Omen((TestEnemy, rolledOmen))
                    enemyDamage = Enemy.get_EnemyDamage(TestEnemy)
                    newEnemyDamage = enemyDamage + randrange(10,15)
                    Enemy.set_EnemyDamage(TestEnemy, newEnemyDamage)
                if roll3 == 2:
                    rolledOmen = choice(possibleOmen)
                    Enemy.set_Omen((TestEnemy, rolledOmen))
                    enemyHealth = get_Health(Enemy)
                    enemyHealthModded = enemyHealth + randrange(200, 300)




def assignEnemyPersonalityOmenClass():
        Enemy.set_Personality(TestEnemy, "")
        Enemy.set_Omen(TestEnemy, "")
        Enemy.set_EnemyClass(TestEnemy, "None")

        possiblePersonality = ["the Brave", "the Calm", "the Chaste", "the Content", "the Diligent", "the Fickle",
                               "the Forgiving", "the Generous", "the Gregarious", "the Honest", "the Humble",
                               "the Just",
                               "the Patient", "the Temperate", "the Trusting", "the Zealous", "the Compassionate",
                               "the Shy", "the Sinful", "the Pure", "the Heathen", "the Thief",
                               "the Murderer", "the Insane", "the Swan",
                               "the Lion", "the Stag", "the Raven", "the Mouse", "the Impure", "the Defiler",
                               "the Crooked", "the Weeping", "the Unrepentant", "the Uncharitable", "the Greedy",
                               "the Sick",
                               "the Hateful", "the Sweaty", "the Demon", "the Two-Faced", "the Liar",
                               "the Honest", "the Outcast", "the Lecherous", "the Ladykiller",
                               "the Maneater", "the Cannibal", "the Robber", "the Baron", "the Duke", "the Beautiful",
                               "the Rose", "the Dashing", "the Handsome", "the Colorful", "the Mindless", "the Weary",
                               "the First", "the Second", "the Third", "the Fourth", "the Obnoxious", "the Famous",
                               "the Infamous", "the Unforgiving", "the Unforgiven", "the Impartial", "the Mighty",
                               "the God King", "the Hellish", "the Defeated", "the Undefeated", "the Agonizing",
                               "the Jolly", "the Secretive", "the Stubborn", "the Persuader", "the Brute", "the Scientist",
                               "the Sorcerer", "the Witch Knight", "the Depressed", "the Small", "the Huge", "the Squealing",
                               "the Joyous", "the Sloppy", "the Pig",]

        possibleOmen = [", Cursed by the Raven God", ", Cursed by the Four Horned Stag",
                        ", Cursed by the Mad Toad King", ", Cursed by the Blood Witch"]





        roll = randrange(1, 100)
        if roll > 25:
            rolledPersonality = choice(possiblePersonality)
            Enemy.set_Personality(TestEnemy, rolledPersonality)
            enemyHealth = Enemy.get_Health(TestEnemy)
            enemyHealthModded = enemyHealth + randrange(15, 50)
            Enemy.set_Health(TestEnemy, enemyHealthModded)
            roll2 = randrange(1, 100)
            if roll < 10:
                rolledOmen = choice(possibleOmen)
                Enemy.set_Omen(TestEnemy, rolledOmen)
                enemyDamage = Enemy.get_Damage(TestEnemy)
                enemyDamageModded = enemyDamage + randrange(5, 15)
                Enemy.set_EnemyDamage(TestEnemy, enemyDamageModded)
            if roll > 90:
                rolledOmen = choice(possibleOmen)
                Enemy.set_Omen(TestEnemy, rolledOmen)
                enemyHealth = Enemy.get_Health(TestEnemy)
                enemyHealthModded = enemyHealth + randrange(50, 250)
                Enemy.set_Health(TestEnemy, enemyHealthModded)

        possibleClasses = ["Mercenary", "Assassin", "Witch Doctor", "Skulldugger", "Blackguard"]

        roll = randrange(100)
        if roll < 40 or roll > 94:
            time.sleep(1)
        if 41 <= roll <= 50:
            TestEnemy.set_EnemyClass("Blackguard")
            newEnemyDamage = Enemy.get_EnemyDamage(TestEnemy) + randrange(1,6) + randrange(1,6) + randrange(1,6)
            Enemy.set_EnemyDamage(TestEnemy, newEnemyDamage)
        if 51 <= roll <= 61:
            TestEnemy.set_EnemyClass("Mercenary")
            newEnemyHealth = Enemy.get_Health(TestEnemy) + randrange(1, 20) + randrange(1,20) + randrange(1,20) + randrange(1,20) + randrange(1,20)
            Enemy.set_Health(TestEnemy, newEnemyHealth)
        if 62 <= roll <= 72:
            TestEnemy.set_EnemyClass("Assassin")
            newEnemyAccuracy = Enemy.get_EnemyAccuracy(TestEnemy) + randrange(1, 6) + randrange(1, 6) + randrange(1,6) + randrange(1,6) + randrange(1,6)
            Enemy.set_EnemyAccuracy(TestEnemy, newEnemyAccuracy)
        if 73 <= roll <= 83:
            TestEnemy.set_EnemyClass("Witch Doctor")
            newArmourClass = Enemy.get_ArmourClass(TestEnemy) + randrange(1, 6)+ randrange(1, 6)
            Enemy.set_ArmourClass(TestEnemy, newArmourClass)
        if 84 <= roll <= 94:
            TestEnemy.set_EnemyClass("Skulldugger")
            newEnemyDamage = Enemy.get_EnemyDamage(TestEnemy) + randrange(1, 6)
            Enemy.set_EnemyDamage(TestEnemy, newEnemyDamage)
            newEnemyAccuracy = Enemy.get_EnemyAccuracy(TestEnemy) + randrange(1, 6) + randrange(1,6)+ randrange(1,6)
            Enemy.set_EnemyAccuracy(TestEnemy, newEnemyAccuracy)




class PartyMember:
    def __init__(self):

        ## GENDER AND AGE
        # Male is 1, Female is 0
        names = [fnames.elf(), fnames.human(), fnames.hobbit(), fnames.dwarf()]
        self.name = choice(names)
        self.age = randrange(18,79)

        ## CHARACTERISTICS
        self.WeaponSkill = randrange(10,20)
        self.Strength = randrange(10, 20)
        self.Toughness = randrange(10, 20)
        self.Dexterity = randrange(10, 20)
        self.Charisma = randrange(10, 20)
        self.Intellect = randrange(10, 20)
        self.Health = randrange(100, 250)
        self.MaxHealth = 250
        self.StatScore = self.WeaponSkill + self.Strength + self.Toughness + self.Dexterity + self.Charisma + self.Intellect + self.Health
        #classrandom = choice(poolsofSpecialMoves)
        self.hasPersonality = False
        self.Personality = ""
        self.ArmourClass = randrange(5,15)
        self.AttackModifier = randrange(2,10)
        self.isAlive = True




        self.SpecSlot1Name = "None"
        self.SpecSlot1Cost = 0
        self.SpecSlot1Damage = 0
        self.SpecSlot1Prob = 0
        self.SpecSlot1Desc = "N/A"
        self.SpecSlot1Num = 0

        self.SpecSlot2Name = "None"
        self.SpecSlot2Cost = 0
        self.SpecSlot2Damage = 0
        self.SpecSlot2Prob = 0
        self.SpecSlot2Desc = "N/A"
        self.SpecSlot2Num = 0


    def get_MaxHealth(self):
        return self.MaxHealth
    def set_MaxHealth(self, x):
        self.MaxHealth = x
    def get_SpecSlot1Name(self):
        return self.SpecSlot1Name
    def set_SpecSlot1Name(self, x):
        self.SpecSlot1Name = x
    def get_SpecSlot1Cost(self):
        return self.SpecSlot1Cost
    def set_SpecSlot1Cost(self, x):
        self.SpecSlot1Cost = x
    def get_SpecSlot1Damage(self):
        return self.SpecSlot1Damage
    def set_SpecSlot1Damage(self, x):
        self.SpecSlot1Damage = x
    def get_SpecSlot1Prob(self):
        return self.SpecSlot1Prob
    def set_SpecSlot1Prob(self, x):
        self.SpecSlot1Prob = x
    def get_SpecSlot1Desc(self):
        return self.SpecSlot1Desc
    def set_SpecSlot1Desc(self, x):
        self.SpecSlot1Desc = x

    def get_ArmourClass(self):
        return self.ArmourClass
    def set_ArmourClass(self, x):
        self.ArmourClass = x

    def get_SpecSlot1Num(self):
        return self.SpecSlot1Num
    def set_SpecSlot1Num(self, x):
        self.SpecSlot1Num = x

    def get_Initiative(self):
        return self.Initiative
    def set_Initiative(self, x):
        self.Initiative = x

   # getter method
    def get_Personality(self):
        return self.Personality
    # setter method
    def set_Personality(self, x):
        self.Personality = x

    def get_AttackModifier(self):
        return self.AttackModifier
    def set_AttackModifier(self, x):
        self.AttackModifier = x


    def get_isAlive(self):
        return self.isAlive
    def set_isAlive(self, x):
        self.isAlive = x

    # getter method
    def get_name(self):
        return self.name
    # setter method
    def set_name(self, x):
        self.name = x
    def get_age(self):
        return self.age
    def get_gender(self):
        return self.gender
    def get_WeaponSkill(self):
        return self.WeaponSkill
    def get_Strength(self):
        return self.Strength
    def get_Toughness(self):
        return self.Toughness
    def get_Dexterity(self):
        return self.Dexterity
    def get_Charisma(self):
        return self.Charisma
    def get_Intellect(self):
        return self.Intellect
    def get_Health(self):
        return self.Health
    def set_Health(self, x):
        self.Health = x

    def get_StatScore(self):
        return self.StatScore

class SpecialMoves:
    def __init__(self, age = 20, name = "John Doe"):
        self.name = "TestSpecialMove"
        self.cost = 1
        self.description = "Description."
        self.probability = .75
        self.damage = 50
        self.indexNumber = 0



    def get_name(self):
        return self.name
    def set_name(self, x):
        self.name = x
    def get_cost(self):
        return self.cost
    def set_cost(self, x):
        self.cost = x
    def get_description(self):
        return self.description
    def set_description(self, x):
        self.description = x
    def get_probability(self):
        return self.probability
    def set_probability(self, x):
        self.probability = x
    def get_damage(self):
        return self.damage
    def set_damage(self, x):
        self.damage = x
    def get_indexNumber(self):
        return self.indexNumber
    def set_indexNumber(self, x):
        self.indexNumber = x





def rollforPersonality():
    possiblePersonality = ["the Brave", "the Calm", "the Chaste", "the Content", "the Diligent", "the Fickle",
                           "the Forgiving", "the Generous", "the Gregarious", "the Honest", "the Humble", "the Just",
                           "the Patient", "the Temperate", "the Trusting", "the Zealous", "the Compassionate",
                           "the Shy",  "the Sinful", "the Pure", "the Heathen", "the Thief",
                           "the Murderer", "the Insane", "the Lionfish", "the Lamb", "the Ostrich", "the Swan",
                           "the Lion", "the Stag", "the Raven", "the Mouse", "the Kind", "the Sweet", "the Giving",
                           "the Scholar", "the Jester", "the Oaken", "the Good Spirited", "the Outlaw", "the Bandit",
                           "the Eccentric", "the Witty", "the Slow", "the Oaf", "the Alluring", "the Wealthy", "the Destitute",
                           "the Jolly", "the Happy", "the Serious", "the Sad", "the Faithful", "the Burly", "the Strong",
                           "the Bitter", "the Nosy", "the Smelly", "the Sleepy", "the Politicking", "the Squeamish", "the Tall",
                           "the Short", "the Mindless", "the Zen", "the Acrid", "the Handy", "the Poet", "the Paranoid",
                           "the Cultured", "the Inevitable", "the Salty", "the Sassy", "the Treasured", "the Learned",
                           "the Skinny", "the Fat", "the Unruly", "the Tremendous", "the Deaf", "the Mute", "the Blind",
                           "the Rude", "the Harmonious", "the Seer", "the All-Knowing", "the Mystic"]




    roll = randrange(0, 100)
    if roll < 40:
        NPC1.set_Personality(choice(possiblePersonality))
    roll = randrange(0, 100)
    if roll < 40:
        NPC2.set_Personality(choice(possiblePersonality))
    roll = randrange(0, 100)
    if roll < 40:
        NPC3.set_Personality(choice(possiblePersonality))


class PlayerCharacter:
    def __init__(self, age = 20, name = "John Doe"):

        ## GENDER AND AGE
        gender = randint(0, 1)
        # Male is 1, Female is 0
        if gender == 1:
            self.name = fnames.human('male')
            self.gender = "Male"
        if gender == 0:
            self.name = fnames.human('female')
            self.gender = "Female"
        self.age = randrange(16,79)

        self.playerclass = "Starved"

        self.hasMaiden = False

        self.Blood = randrange(1,100)
        self.Gold = randrange(1,100)

        self.LoadedSave = False

        ## CHARACTERISTICS
        self.attackStat = "None"
        self.attackModifier = 0

        self.WeaponSkill = randrange(10,20)
        self.Strength = randrange(10, 20)
        self.Toughness = randrange(10, 20)
        self.Dexterity = randrange(10, 20)
        self.Charisma = randrange(10, 20)
        self.Intellect = randrange(10, 20)

        self.Health = randrange(100, 250)
        self.MaxHealth = 250

        self.StatScore = self.WeaponSkill + self.Strength + self.Toughness + self.Dexterity + self.Charisma + self.Intellect + self.Health

        self.Initiative = 10
        self.ArmourClass = randrange(5,15)

        self.SpecialPoints = randrange(3,7)

        self.SlainEnemies = []

        self.reset()

        self.SpecSlot1Name = "None."
        self.SpecSlot1Cost = 0
        self.SpecSlot1Damage = 0
        self.SpecSlot1Prob = 0
        self.SpecSlot1Desc = "N/A"

        self.SpecSlot2Name = "None."
        self.SpecSlot2Cost = 0
        self.SpecSlot2Damage = 0
        self.SpecSlot2Prob = 0
        self.SpecSlot2Desc = "N/A"


    def get_SlainEnemies(self):
        return self.SlainEnemies
    def set_SlainEnemies(self, x):
        self.SlainEnemies = x

    def get_LoadedSave(self):
        return self.LoadedSave
    def set_LoadedSave(self, x):
        self.LoadedSave = x

    def get_Blood(self):
        return self.Blood
    def set_Blood(self, x):
        self.Blood = x

    def get_Gold(self):
        return self.Gold
    def set_Gold(self, x):
        self.Gold = x

    def get_hasMaiden(self):
        return self.hasMaiden
    def set_hasMaiden(self, x):
        self.hasMaiden = x

    def get_MaxHealth(self):
        return self.MaxHealth
    def set_MaxHealth(self, x):
        self.MaxHealth = x
    def get_Initiative(self):
        return self.Initiative
    def set_Initiative(self, x):
        self.Initiative = x
    def get_ArmourClass(self):
        return self.ArmourClass
    def set_ArmourClass(self, x):
        self.ArmourClass = x

    def set_attackStat(self, x):
        self.attackStat = x
    def get_attackStat(self):
        return self.attackStat

    def set_SpecialPoints(self, x):
        self.SpecialPoints = x
    def get_SpecialPoints(self):
        return self.SpecialPoints

    def set_attackModifier(self, x):
        self.attackModifier = x
    def get_attackModifier(self):
        return self.attackModifier

    def reset(self):
        ## GENDER AND AGE
        gender = randint(0, 1)
        # Male is 1, Female is 0
        if gender == 1:
            self.name = fnames.human('male')
            self.gender = "Male"
        if gender == 0:
            self.name = fnames.human('female')
            self.gender = "Female"
        self.age = randrange(16,79)

        self.playerclass = "Starved"

        self.hasMaiden = False


        ## CHARACTERISTICS
        self.WeaponSkill = randrange(10,20)
        self.Strength = randrange(10, 20)
        self.Toughness = randrange(10, 20)
        self.Dexterity = randrange(10, 20)
        self.Charisma = randrange(10, 20)
        self.Intellect = randrange(10, 20)

        self.Health = randrange(100, 250)
        self.MaxHealth = 250

        self.StatScore = self.WeaponSkill + self.Strength + self.Toughness + self.Dexterity + self.Charisma + self.Intellect + self.Health

    # getter method
    def get_name(self):
        return self.name
    # setter method
    def set_name(self, x):
        self.name = x

    def set_StatScore(self, x):
        self.StatScore = x
    def get_StatScore(self):
        return self.StatScore
    def get_WeaponSkill(self):
        return self.WeaponSkill
    def set_WeaponSkill(self, x):
        self.WeaponSkill = x
    def get_Strength(self):
        return self.Strength
    def set_Strength(self, x):
        self.Strength = x
    def get_Toughness(self):
        return self.Toughness
    def set_Toughness(self, x):
        self.Toughness = x
    def get_Dexterity(self):
        return self.Dexterity
    def set_Dexterity(self, x):
        self.Dexterity = x
    def get_Charisma(self):
        return self.Charisma
    def set_Charisma(self, x):
        self.Charisma = x
    def get_Intellect(self):
        return self.Intellect
    def set_Intellect(self, x):
        self.Intellect = x
    def get_Health(self):
        return self.Health
    def set_Health(self, x):
        self.Health = x

    def get_playerclass(self):
        return self.playerclass
    def set_playerclass(self, x):
        self.playerclass = x
    def get_age(self):
        return self.age
    def get_gender(self):
        return self.gender
    def set_gender(self, x):
        self.gender = x


class PlayerCharacterSave:
    def __init__(self, age = 20, name = "John Doe"):

        ## GENDER AND AGE
        gender = randint(0, 1)
        # Male is 1, Female is 0
        if gender == 1:
            self.name = fnames.human('male')
            self.gender = "Male"
        if gender == 0:
            self.name = fnames.human('female')
            self.gender = "Female"
        self.age = randrange(16,79)

        self.playerclass = "Starved"

        self.hasMaiden = False

        self.Blood = randrange(2000,5000)
        self.Gold = randrange(2000,5000)

        ## CHARACTERISTICS
        self.attackStat = "None"
        self.attackModifier = 0

        self.WeaponSkill = randrange(10,20)
        self.Strength = randrange(10, 20)
        self.Toughness = randrange(10, 20)
        self.Dexterity = randrange(10, 20)
        self.Charisma = randrange(10, 20)
        self.Intellect = randrange(10, 20)
        self.Health = randrange(100, 250)
        self.MaxHealth = 250
        self.StatScore = self.WeaponSkill + self.Strength + self.Toughness + self.Dexterity + self.Charisma + self.Intellect + self.Health

        self.Initiative = 10
        self.ArmourClass = randrange(5,15)

        self.SpecialPoints = randrange(3,7)

        self.SlainEnemies = []

        self.reset()

        self.SpecSlot1Name = "None."
        self.SpecSlot1Cost = 0
        self.SpecSlot1Damage = 0
        self.SpecSlot1Prob = 0
        self.SpecSlot1Desc = "N/A"

        self.SpecSlot2Name = "None."
        self.SpecSlot2Cost = 0
        self.SpecSlot2Damage = 0
        self.SpecSlot2Prob = 0
        self.SpecSlot2Desc = "N/A"


    def get_SlainEnemies(self):
        return self.SlainEnemies
    def set_SlainEnemies(self, x):
        self.SlainEnemies = x


    def get_Blood(self):
        return self.Blood
    def set_Blood(self, x):
        self.Blood = x

    def get_Gold(self):
        return self.Gold
    def set_Gold(self, x):
        self.Gold = x

    def get_hasMaiden(self):
        return self.hasMaiden
    def set_hasMaiden(self, x):
        self.hasMaiden = x

    def get_MaxHealth(self):
        return self.MaxHealth
    def set_MaxHealth(self, x):
        self.MaxHealth = x
    def get_Initiative(self):
        return self.Initiative
    def set_Initiative(self, x):
        self.Initiative = x
    def get_ArmourClass(self):
        return self.ArmourClass
    def set_ArmourClass(self, x):
        self.ArmourClass = x

    def set_attackStat(self, x):
        self.attackStat = x
    def get_attackStat(self):
        return self.attackStat

    def set_SpecialPoints(self, x):
        self.SpecialPoints = x
    def get_SpecialPoints(self):
        return self.SpecialPoints

    def set_attackModifier(self, x):
        self.attackModifier = x
    def get_attackModifier(self):
        return self.attackModifier

    def reset(self):
        ## GENDER AND AGE
        gender = randint(0, 1)
        # Male is 1, Female is 0
        if gender == 1:
            self.name = fnames.human('male')
            self.gender = "Male"
        if gender == 0:
            self.name = fnames.human('female')
            self.gender = "Female"
        self.age = randrange(16,79)

        self.playerclass = "Starved"

        self.hasMaiden = False


        ## CHARACTERISTICS
        self.WeaponSkill = randrange(10,20)
        self.Strength = randrange(10, 20)
        self.Toughness = randrange(10, 20)
        self.Dexterity = randrange(10, 20)
        self.Charisma = randrange(10, 20)
        self.Intellect = randrange(10, 20)
        self.Health = randrange(50, 150)
        self.StatScore = self.WeaponSkill + self.Strength + self.Toughness + self.Dexterity + self.Charisma + self.Intellect + self.Health

    # getter method
    def get_name(self):
        return self.name
    # setter method
    def set_name(self, x):
        self.name = x

    def set_StatScore(self, x):
        self.StatScore = x
    def get_StatScore(self):
        return self.StatScore
    def get_WeaponSkill(self):
        return self.WeaponSkill
    def set_WeaponSkill(self, x):
        self.WeaponSkill = x
    def get_Strength(self):
        return self.Strength
    def set_Strength(self, x):
        self.Strength = x
    def get_Toughness(self):
        return self.Toughness
    def set_Toughness(self, x):
        self.Toughness = x
    def get_Dexterity(self):
        return self.Dexterity
    def set_Dexterity(self, x):
        self.Dexterity = x
    def get_Charisma(self):
        return self.Charisma
    def set_Charisma(self, x):
        self.Charisma = x
    def get_Intellect(self):
        return self.Intellect
    def set_Intellect(self, x):
        self.Intellect = x
    def get_Health(self):
        return self.Health
    def set_Health(self, x):
        self.Health = x

    def get_playerclass(self):
        return self.playerclass
    def set_playerclass(self, x):
        self.playerclass = x
    def get_age(self):
        return self.age
    def get_gender(self):
        return self.gender
    def set_gender(self, x):
        self.gender = x


class Stage():
    def __init__(self):
        self.name = "TestStage"
        self.description = "Null description"
        self.number = 1

    # getter method
    def get_name(self):
        return self.name
    # setter method
    def set_name(self, x):
        self.name = x

    def get_description(self):
        return self.description
    def set_description(self, x):
        self.description = x

    def get_number(self):
        return self.number
    def set_number(self, x):
        self.number = x



NPC1 = PartyMember()
NPC2 = PartyMember()
NPC3 = PartyMember()
NPC4 = PartyMember()
TestEnemy = Enemy()
TestStage1 = Stage()
PC = PlayerCharacter()




BloodKnight = PartyMember()
RavenGuard = PartyMember()
FourHornedDruid = PartyMember()
PartyMember.set_Personality(BloodKnight, "the Blood Knight")
PartyMember.set_Personality(RavenGuard, "the Raven Guard")
PartyMember.set_Personality(FourHornedDruid, "the Four Horned Druid")


def ListParty():
    clear()
    print("\n")
    print(NPC1.get_name() + " " + str(NPC1.get_Personality()))
    print(str(NPC1.get_age()) + " years old.")
    #print("Weapon Skill: " + str(NPC1.get_WeaponSkill()))
    print("Strength: " + str(NPC1.get_Strength()) + "       Charisma: " + str(NPC1.get_Charisma()))
    print("Toughness: " + str(NPC1.get_Toughness()) + "      Intellect: " + str(NPC1.get_Intellect()))
    print("Dexterity: " + str(NPC1.get_Dexterity()) + "      Health: " + str(NPC1.get_Health()))
    print("StatScore: " + str(NPC1.get_StatScore()) + "      Attack Mod: " + str(NPC1.get_AttackModifier()))
    print("Armour Class: " + str(NPC1.get_ArmourClass()))
    slot1name = PartyMember.get_SpecSlot1Name(NPC1)
    if slot1name != "None":
        print("Special Move: " + slot1name)
    print("\n")
    print(NPC2.get_name() + " " + str(NPC2.get_Personality()))
    print(str(NPC2.get_age()) + " years old.")
    #print("Weapon Skill: " + str(NPC2.get_WeaponSkill()))
    print("Strength: " + str(NPC2.get_Strength()) + "       Charisma: " + str(NPC2.get_Charisma()))
    print("Toughness: " + str(NPC2.get_Toughness()) + "      Intellect: " + str(NPC2.get_Intellect()))
    print("Dexterity: " + str(NPC2.get_Dexterity()) + "      Health: " + str(NPC2.get_Health()))
    print("StatScore: " + str(NPC2.get_StatScore()) + "      Attack Mod: " + str(NPC2.get_AttackModifier()))
    print("Armour Class: " + str(NPC2.get_ArmourClass()))
    slot1name = PartyMember.get_SpecSlot1Name(NPC2)
    if slot1name != "None":
        print("Special Move: " + slot1name)
    print("\n")
    print(NPC3.get_name() + " " + str(NPC3.get_Personality()))
    print(str(NPC3.get_age()) + " years old.")
    #print("Weapon Skill: " + str(NPC3.get_WeaponSkill()))
    print("Strength: " + str(NPC3.get_Strength()) + "       Charisma: " + str(NPC3.get_Charisma()))
    print("Toughness: " + str(NPC3.get_Toughness()) + "      Intellect: " + str(NPC3.get_Intellect()))
    print("Dexterity: " + str(NPC3.get_Dexterity()) + "      Health: " + str(NPC3.get_Health()))
    print("StatScore: " + str(NPC3.get_StatScore()) + "      Attack Mod: " + str(NPC3.get_AttackModifier()))
    print("Armour Class: " + str(NPC3.get_ArmourClass()))
    slot1name = PartyMember.get_SpecSlot1Name(NPC3)
    if slot1name != "None":
        print("Special Move: " + slot1name)
    print("\n")


    print("(Press enter to continue)")
    key = input("")
    if key != "`":
        DescripAndInit()























def OldManIntellectChallenge():
    clear()
    print("The old man poses his riddle to you.")
    time.sleep(2)
    print("      Hmmm....")
    time.sleep(2)
    print("\n          ....Perhaps")
    time.sleep(2)
    IntellectMod = PlayerCharacter.get_Intellect(PC) / 4
    IntellectMod = round(IntellectMod)
    roll = randrange(1,20) + IntellectMod
    rolltarget = randrange(12,24)
    if roll >= rolltarget:
        clear()
        print("You solve the riddle! Well done!")
        time.sleep(3)
        possibleItems = ["necklace", "coin", "dagger", "satchel", "flower"]

        roll = randrange(1,2)
        if roll == 1:
            ACbonus = randrange(2, 8)
            newAC = PlayerCharacter.get_ArmourClass(PC) + ACbonus
            PlayerCharacter.set_ArmourClass(PC, newAC)
            print("The old man gives you a magical " + choice(
                possibleItems) + " which increases the player's Armour Class by " + str(ACbonus) + ".")
            time.sleep(5)
            clear()
        else:
            healthBonus = randrange(20, 80)
            newMaxHealth = PlayerCharacter.get_MaxHealth(PC) + healthBonus
            PlayerCharacter.set_MaxHealth(PC, newMaxHealth)

            newHealth = PlayerCharacter.get_Health(PC) + healthBonus
            PlayerCharacter.set_Health(PC, newHealth)

            print("The old man gives you a magical " + choice(
                possibleItems) + " which increases increased your Max Health and raises your Health by " + str(healthBonus) + ".")
            time.sleep(5)
            clear()


    elif roll < rolltarget:
        clear()
        print("You failed to solve the riddle! Embarrassing!")
        time.sleep(3)
        possibleExpressions = ["regretful", "amused", "ashamed", "tired", "happy", "sad"]
        print("The old man gives you a " + choice(possibleExpressions) + " look, then walks off into the distance.")
        time.sleep(5)
        clear()


def OldManStrengthChallenge():
    clear()
    print("Your party descends upon the old man, robbing him.")
    time.sleep(3)
    clear()
    print("          ....")
    time.sleep(2)
    clear()
    print("      ....")
    time.sleep(2)
    clear()
    print("  ....")
    time.sleep(2)
    roll = randrange(1,20) + ( PlayerCharacter.get_Strength(PC) / 4 )
    rolltarget = randrange(5,25)
    if roll >= rolltarget:
        clear()
        print("You beat and lash the old man until he gives up his valuables.")
        time.sleep(3)
        possibleItems = ["necklace", "coin", "dagger", "satchel", "flower"]


        roll = randrange(1, 2)
        if roll == 1:
            ACbonus = randrange(1, 4)
            newAC = PlayerCharacter.get_ArmourClass(PC) + ACbonus
            PlayerCharacter.set_ArmourClass(PC, newAC)
            print("The old man's backpack contained a magical " + choice(
                possibleItems) + " which increases the player's Armour Class by " + str(ACbonus) + ".")
            time.sleep(5)
            clear()
        else:
            healthBonus = randrange(20, 80)
            newMaxHealth = PlayerCharacter.get_MaxHealth(PC) + healthBonus
            PlayerCharacter.set_MaxHealth(PC, newMaxHealth)

            newHealth = PlayerCharacter.get_Health(PC) + healthBonus
            PlayerCharacter.set_Health(PC, newHealth)

            print("The old man's backpack contained a magical " + choice(
                possibleItems) + " which increases increased your Max Health and raises your Health by " + str(
                healthBonus) + ".")
            time.sleep(5)
            clear()
    else:
        clear()
        print("The old man is stronger than he looks, shouting and fighting back wildly until you find yourself bested.")


        newPChealth = PlayerCharacter.get_Health(PC) - randrange(1,30)
        PlayerCharacter.set_Health(PC, newPChealth)
        newNPChealth = PartyMember.get_Health(NPC1) - randrange(1,30)
        PartyMember.set_Health(NPC1, newNPChealth)
        newNPChealth = PartyMember.get_Health(NPC2) - randrange(1, 30)
        PartyMember.set_Health(NPC2, newNPChealth)
        newNPChealth = PartyMember.get_Health(NPC3) - randrange(1, 30)
        PartyMember.set_Health(NPC3, newNPChealth)

        time.sleep(1)
        possibleExpressions = ["regretful", "joyous", "shameful", "tired", "happy", "sad"]
        print("\nThe old man gives you a " + choice(possibleExpressions) + " look, then walks off into the distance.")
        time.sleep(5)
        clear()


def MaidenDexterityChallenge():
    roll = randrange(1, 20)
    rolltarget = randrange(15, 25)
    rollmod = PlayerCharacter.get_Dexterity(PC) / 4
    newroll = roll + rollmod
    time.sleep(1)
    if newroll > rolltarget:
        clear()
        print("You lie and deceive the fair maiden, tricking her into giving a Blessed relic.")
        time.sleep(3)
        possibleItems = ["amulet", "ring", "diary", "earring", "broach", "flower"]
        print("\nThe maiden gives you a Blessed " + choice(possibleItems) + ".")


        roll = randrange(1, 3)
        if roll == 1:
            SPbonus = randrange(1, 4)
            newSP = PlayerCharacter.get_SpecialPoints(PC) + SPbonus
            PlayerCharacter.set_SpecialPoints(PC, newSP)
            print("The Blessed " + choice(
                possibleItems) + " increases the player's Special Points by " + str(SPbonus) + ".")
            time.sleep(5)
            clear()
        elif roll == 2:
            attackModBonus = randrange(1, 3)
            newattackMod = PlayerCharacter.get_attackModifier(PC) + attackModBonus
            PlayerCharacter.set_attackModifier(PC, newattackMod)
            print("The Blessed " + choice(
                possibleItems) + " increases the player's Attack Modifier by " + str(newattackMod) + ", raising accuracy and damage.")
            time.sleep(5)
            clear()
        else:
            healthBonus = randrange(20, 80)
            newMaxHealth = PlayerCharacter.get_MaxHealth(PC) + healthBonus
            PlayerCharacter.set_MaxHealth(PC, newMaxHealth)

            newHealth = PlayerCharacter.get_Health(PC) + healthBonus
            PlayerCharacter.set_Health(PC, newHealth)

            print("The Blessed " + choice(
                possibleItems) + "increases the player's Max Health and Health by " + str(
                healthBonus) + ".")
            time.sleep(5)
            clear()

    else:
        clear()
        print("The maiden sobs when she realizes your treachery!")
        time.sleep(5)



def MysteriousStrangerRecruitment():
    clear()
    LobbyStatus()
    print("A mysterious stranger, shrouded in cloaks and bizarre garbs approaches your Party.")
    Stranger = PartyMember()
    newStrangerHealth = PartyMember.get_Health(Stranger) + 75
    PartyMember.set_Health(Stranger, newStrangerHealth)
    newStrangerAttackMod = PartyMember.get_AttackModifier(Stranger) + randrange(2,5)
    PartyMember.set_AttackModifier(Stranger, newStrangerAttackMod)
    newStrangerAC = PartyMember.get_ArmourClass(Stranger) + randrange(1, 4)
    PartyMember.set_ArmourClass(Stranger, newStrangerAC)
    chaMod = PlayerCharacter.get_Charisma(PC) / 5
    roll = randrange(1,100) - chaMod
    if roll < 80:
        time.sleep(3)
        print("After some banter, the stranger gives their name as " + PartyMember.get_name(Stranger) + ".")
        time.sleep(3)
        print("\nFurthermore, the stranger offers to join your Party, should you want their help.")
        time.sleep(2)
        print("\n")

        if PartyMember.get_Health(NPC1) > 0:
            print("1. " + PartyMember.get_name(NPC1) + " " + PartyMember.get_Personality(NPC1) + " (Health " + str(
                PartyMember.get_Health(NPC1)) + "/" + str(
                PartyMember.get_MaxHealth(NPC1)) + ")  Armour Class: " + str(PartyMember.get_ArmourClass(NPC1)))
            if PartyMember.get_SpecSlot1Name(NPC1) != "None":
                print("      Special: " + PartyMember.get_SpecSlot1Name(NPC1))
        else:
            print("1. " + PartyMember.get_name(NPC1) + " (Dead)")
        if PartyMember.get_Health(NPC2) > 0:
            print("2. " + PartyMember.get_name(NPC2) + " " + PartyMember.get_Personality(NPC1) + " (Health " + str(
                PartyMember.get_Health(NPC2)) + "/" + str(
                PartyMember.get_MaxHealth(NPC2)) + ")  Armour Class: " + str(PartyMember.get_ArmourClass(NPC2)))
            if PartyMember.get_SpecSlot1Name(NPC2) != "None":
                print("      Special: " + PartyMember.get_SpecSlot1Name(NPC2))
        else:
            print("2. " + PartyMember.get_name(NPC2) + " (Dead)")
        if PartyMember.get_Health(NPC3) > 0:
            print("3. " + PartyMember.get_name(NPC3) + " " + PartyMember.get_Personality(NPC1) + " (Health " + str(
                PartyMember.get_Health(NPC3)) + "/" + str(
                PartyMember.get_MaxHealth(NPC3)) + ")  Armour Class: " + str(PartyMember.get_ArmourClass(NPC3)))
            if PartyMember.get_SpecSlot1Name(NPC3) != "None":
                print("      Special: " + PartyMember.get_SpecSlot1Name(NPC3))
        else:
            print("3. " + PartyMember.get_name(NPC3) + " (Dead)")

        print("\n\nReplace Party Member or Decline: ")
        print("1. Replace " + PartyMember.get_name(NPC1))
        print("2. Replace " + PartyMember.get_name(NPC2))
        print("3. Replace " + PartyMember.get_name(NPC3))
        print("4. Decline the Stranger's Offer\n")
        key = input("")
        if key == "1":
            PartyMember.set_name(NPC1, PartyMember.get_name(Stranger))
            PartyMember.set_Health(NPC1, PartyMember.get_Health(Stranger))
            PartyMember.set_MaxHealth(NPC1, PartyMember.get_Health(Stranger))

            PartyMember.set_Personality(NPC1, PartyMember.get_Personality(Stranger))
            PartyMember.set_AttackModifier(NPC1, PartyMember.get_AttackModifier(Stranger))
            PartyMember.set_ArmourClass(NPC1, PartyMember.get_ArmourClass(Stranger))
            PartyMember.set_isAlive(NPC1, PartyMember.get_isAlive(Stranger))

            PartyMember.set_SpecSlot1Name(NPC1, PartyMember.get_SpecSlot1Name(Stranger))
            PartyMember.set_SpecSlot1Cost(NPC1, PartyMember.get_SpecSlot1Cost(Stranger))
            PartyMember.set_SpecSlot1Damage(NPC1, PartyMember.get_SpecSlot1Damage(Stranger))
            PartyMember.set_SpecSlot1Prob(NPC1, PartyMember.get_SpecSlot1Prob(Stranger))
            PartyMember.set_SpecSlot1Num(NPC1, PartyMember.get_SpecSlot1Num(Stranger))
            time.sleep(1)
            print(PartyMember.get_name(Stranger) + " has replaced Party Member slot 1!")
            time.sleep(3)
        if key == "2":
            PartyMember.set_name(NPC2, PartyMember.get_name(Stranger))
            PartyMember.set_Health(NPC2, PartyMember.get_Health(Stranger))
            PartyMember.set_MaxHealth(NPC2, PartyMember.get_Health(Stranger))

            PartyMember.set_Personality(NPC2, PartyMember.get_Personality(Stranger))
            PartyMember.set_AttackModifier(NPC2, PartyMember.get_AttackModifier(Stranger))
            PartyMember.set_ArmourClass(NPC2, PartyMember.get_ArmourClass(Stranger))
            PartyMember.set_isAlive(NPC2, PartyMember.get_isAlive(Stranger))

            PartyMember.set_SpecSlot1Name(NPC2, PartyMember.get_SpecSlot1Name(Stranger))
            PartyMember.set_SpecSlot1Cost(NPC2, PartyMember.get_SpecSlot1Cost(Stranger))
            PartyMember.set_SpecSlot1Damage(NPC2, PartyMember.get_SpecSlot1Damage(Stranger))
            PartyMember.set_SpecSlot1Prob(NPC2, PartyMember.get_SpecSlot1Prob(Stranger))
            PartyMember.set_SpecSlot1Num(NPC2, PartyMember.get_SpecSlot1Num(Stranger))
            time.sleep(1)
            print(PartyMember.get_name(Stranger) + " has replaced Party Member slot 2!")
            time.sleep(3)
        if key == "3":
            PartyMember.set_name(NPC3, PartyMember.get_name(Stranger))
            PartyMember.set_Health(NPC3, PartyMember.get_Health(Stranger))
            PartyMember.set_MaxHealth(NPC3, PartyMember.get_Health(Stranger))

            PartyMember.set_Personality(NPC3, PartyMember.get_Personality(Stranger))
            PartyMember.set_AttackModifier(NPC3, PartyMember.get_AttackModifier(Stranger))
            PartyMember.set_ArmourClass(NPC3, PartyMember.get_ArmourClass(Stranger))
            PartyMember.set_isAlive(NPC3, PartyMember.get_isAlive(Stranger))

            PartyMember.set_SpecSlot1Name(NPC3, PartyMember.get_SpecSlot1Name(Stranger))
            PartyMember.set_SpecSlot1Cost(NPC3, PartyMember.get_SpecSlot1Cost(Stranger))
            PartyMember.set_SpecSlot1Damage(NPC3, PartyMember.get_SpecSlot1Damage(Stranger))
            PartyMember.set_SpecSlot1Prob(NPC3, PartyMember.get_SpecSlot1Prob(Stranger))
            PartyMember.set_SpecSlot1Num(NPC3, PartyMember.get_SpecSlot1Num(Stranger))
            time.sleep(1)
            print(PartyMember.get_name(Stranger) + " has replaced Party Member slot 3!")
            time.sleep(3)
    else:
        time.sleep(3)
        print("After some attempts at finding a middle ground, the stranger is disinterested and wanders back into the distance.")
        time.sleep(4)

    print("\n(Press enter to continue)")
    key = input("")
    if key != "`":
        time.sleep(1)
    else:
        time.sleep(1)


def MysteriousStrangerRecruitment_Harder():
    clear()
    LobbyStatus()
    print("A mysterious stranger, shrouded in cloaks and bizarre garbs, responds to your recruitment posting.")
    Stranger = PartyMember()
    newStrangerHealth = PartyMember.get_Health(Stranger) + 75
    PartyMember.set_Health(Stranger, newStrangerHealth)
    newStrangerAttackMod = PartyMember.get_AttackModifier(Stranger) + randrange(2,5)
    PartyMember.set_AttackModifier(Stranger, newStrangerAttackMod)
    newStrangerAC = PartyMember.get_ArmourClass(Stranger) + randrange(1, 4)
    PartyMember.set_ArmourClass(Stranger, newStrangerAC)
    chaMod = PlayerCharacter.get_Charisma(PC) / 5
    roll = randrange(1,100) - chaMod
    if roll < 33:
        time.sleep(3)
        print("After some banter, the stranger gives their name as " + PartyMember.get_name(Stranger) + ".")
        time.sleep(3)
        print("\nFurthermore, the stranger offers to join your Party, should you want their help.")
        time.sleep(2)
        print("\n")

        if PartyMember.get_Health(NPC1) > 0:
            print("1. " + PartyMember.get_name(NPC1) + " " + PartyMember.get_Personality(NPC1) + " (Health " + str(
                PartyMember.get_Health(NPC1)) + "/" + str(
                PartyMember.get_MaxHealth(NPC1)) + ")  Armour Class: " + str(PartyMember.get_ArmourClass(NPC1)))
            if PartyMember.get_SpecSlot1Name(NPC1) != "None":
                print("      Special: " + PartyMember.get_SpecSlot1Name(NPC1))
        else:
            print(PartyMember.get_name(NPC1) + " (Dead)")
        if PartyMember.get_Health(NPC2) > 0:
            print("2. " + PartyMember.get_name(NPC2) + " " + PartyMember.get_Personality(NPC1) + " (Health " + str(
                PartyMember.get_Health(NPC2)) + "/" + str(
                PartyMember.get_MaxHealth(NPC2)) + ")  Armour Class: " + str(PartyMember.get_ArmourClass(NPC2)))
            if PartyMember.get_SpecSlot1Name(NPC2) != "None":
                print("      Special: " + PartyMember.get_SpecSlot1Name(NPC2))
        else:
            print(PartyMember.get_name(NPC2) + " (Dead)")
        if PartyMember.get_Health(NPC3) > 0:
            print("3. " + PartyMember.get_name(NPC3) + " " + PartyMember.get_Personality(NPC1) + " (Health " + str(
                PartyMember.get_Health(NPC3)) + "/" + str(
                PartyMember.get_MaxHealth(NPC3)) + ")  Armour Class: " + str(PartyMember.get_ArmourClass(NPC3)))
            if PartyMember.get_SpecSlot1Name(NPC3) != "None":
                print("      Special: " + PartyMember.get_SpecSlot1Name(NPC3))
        else:
            print(PartyMember.get_name(NPC3) + " (Dead)")

        print("\n\nReplace Party Member or Decline: ")
        print("1. Replace " + PartyMember.get_name(NPC1))
        print("2. Replace " + PartyMember.get_name(NPC2))
        print("3. Replace " + PartyMember.get_name(NPC3))
        print("4. Decline the Stranger's Offer\n")
        key = input("")
        if key == "1":
            PartyMember.set_name(NPC1, PartyMember.get_name(Stranger))
            #PartyMember.set_Strength(NPC1, PartyMember.get_Strength(Stranger))
            #PartyMember.set_Dexterity(NPC1, PartyMember.get_Dexterity(Stranger))
            #PartyMember.set_Charisma(NPC1, PartyMember.get_Charisma(Stranger))
            #PartyMember.set_Intellect(NPC1, PartyMember.get_Intellect(Stranger))
            PartyMember.set_Health(NPC1, PartyMember.get_Health(Stranger))
            PartyMember.set_MaxHealth(NPC1, PartyMember.get_Health(Stranger))

            PartyMember.set_Personality(NPC1, PartyMember.get_Personality(Stranger))
            PartyMember.set_AttackModifier(NPC1, PartyMember.get_AttackModifier(Stranger))
            PartyMember.set_ArmourClass(NPC1, PartyMember.get_ArmourClass(Stranger))
            PartyMember.set_isAlive(NPC1, PartyMember.get_isAlive(Stranger))

            PartyMember.set_SpecSlot1Name(NPC1, PartyMember.get_SpecSlot1Name(Stranger))
            PartyMember.set_SpecSlot1Cost(NPC1, PartyMember.get_SpecSlot1Cost(Stranger))
            PartyMember.set_SpecSlot1Damage(NPC1, PartyMember.get_SpecSlot1Damage(Stranger))
            PartyMember.set_SpecSlot1Prob(NPC1, PartyMember.get_SpecSlot1Prob(Stranger))
            PartyMember.set_SpecSlot1Num(NPC1, PartyMember.get_SpecSlot1Num(Stranger))
            time.sleep(1)
            print(PartyMember.get_name(Stranger) + " has replaced Party Member slot 1!")
            time.sleep(3)
        if key == "2":
            PartyMember.set_name(NPC2, PartyMember.get_name(Stranger))
            PartyMember.set_Strength(NPC2, PartyMember.get_Strength(Stranger))
            PartyMember.set_Dexterity(NPC2, PartyMember.get_Dexterity(Stranger))
            PartyMember.set_Charisma(NPC2, PartyMember.get_Charisma(Stranger))
            PartyMember.set_Intellect(NPC2, PartyMember.get_Intellect(Stranger))
            PartyMember.set_Health(NPC2, PartyMember.get_Health(Stranger))
            PartyMember.set_MaxHealth(NPC2, PartyMember.get_Health(Stranger))

            PartyMember.set_Personality(NPC2, PartyMember.get_Personality(Stranger))
            PartyMember.set_AttackModifier(NPC2, PartyMember.get_AttackModifier(Stranger))
            PartyMember.set_ArmourClass(NPC2, PartyMember.get_ArmourClass(Stranger))
            PartyMember.set_isAlive(NPC2, PartyMember.get_isAlive(Stranger))

            PartyMember.set_SpecSlot1Name(NPC2, PartyMember.get_SpecSlot1Name(Stranger))
            PartyMember.set_SpecSlot1Cost(NPC2, PartyMember.get_SpecSlot1Cost(Stranger))
            PartyMember.set_SpecSlot1Damage(NPC2, PartyMember.get_SpecSlot1Damage(Stranger))
            PartyMember.set_SpecSlot1Prob(NPC2, PartyMember.get_SpecSlot1Prob(Stranger))
            PartyMember.set_SpecSlot1Num(NPC2, PartyMember.get_SpecSlot1Num(Stranger))
            time.sleep(1)
            print(PartyMember.get_name(Stranger) + " has replaced Party Member slot 2!")
            time.sleep(3)
        if key == "3":
            PartyMember.set_name(NPC3, PartyMember.get_name(Stranger))
            PartyMember.set_Strength(NPC3, PartyMember.get_Strength(Stranger))
            PartyMember.set_Dexterity(NPC3, PartyMember.get_Dexterity(Stranger))
            PartyMember.set_Charisma(NPC3, PartyMember.get_Charisma(Stranger))
            PartyMember.set_Intellect(NPC3, PartyMember.get_Intellect(Stranger))
            PartyMember.set_Health(NPC3, PartyMember.get_Health(Stranger))
            PartyMember.set_MaxHealth(NPC3, PartyMember.get_Health(Stranger))

            PartyMember.set_Personality(NPC3, PartyMember.get_Personality(Stranger))
            PartyMember.set_AttackModifier(NPC3, PartyMember.get_AttackModifier(Stranger))
            PartyMember.set_ArmourClass(NPC3, PartyMember.get_ArmourClass(Stranger))
            PartyMember.set_isAlive(NPC3, PartyMember.get_isAlive(Stranger))

            PartyMember.set_SpecSlot1Name(NPC3, PartyMember.get_SpecSlot1Name(Stranger))
            PartyMember.set_SpecSlot1Cost(NPC3, PartyMember.get_SpecSlot1Cost(Stranger))
            PartyMember.set_SpecSlot1Damage(NPC3, PartyMember.get_SpecSlot1Damage(Stranger))
            PartyMember.set_SpecSlot1Prob(NPC3, PartyMember.get_SpecSlot1Prob(Stranger))
            PartyMember.set_SpecSlot1Num(NPC3, PartyMember.get_SpecSlot1Num(Stranger))
            time.sleep(1)
            print(PartyMember.get_name(Stranger) + " has replaced Party Member slot 3!")
            time.sleep(3)
    else:
        time.sleep(3)
        print("After some attempts at negotiating the terms of recruitment, the stranger is disinterested and wanders back into the distance.")
        time.sleep(4)

    print("\n(Press enter to continue)")
    key = input("")
    if key != "`":
        time.sleep(1)
    else:
        time.sleep(1)




def MaidenCharismaChallenge():
    roll = randrange(1,20)
    rolltarget = randrange(10,15)
    rollmod = PlayerCharacter.get_Charisma(PC) / 4
    newroll = roll + rollmod
    time.sleep(1)
    if newroll > rolltarget:
        clear()
        print("The fair maiden is very impressed with your manners at her dinner party.")
        possibleItems = ["longing", "shy", "nervous", "content", "contemplative", "quick"]
        time.sleep(3)
        print("\nThe maiden gives you a " + choice(possibleItems) + " glance.")
        time.sleep(2)
        print("\nWould you like the maiden to join your party?")
        print("1. Yes, have the maiden replace a Party Member.")
        print("2. No, thank the maiden for her hospitality and move on.\n")
        key = input("")
        if key == "1":
            clear()

            if PartyMember.get_Health(NPC1) > 0:
                print("1. " + PartyMember.get_name(NPC1) + " " + PartyMember.get_Personality(NPC1) + " (Health " + str(
                    PartyMember.get_Health(NPC1)) + "/" + str(
                    PartyMember.get_MaxHealth(NPC1)) + ")  Armour Class: " + str(PartyMember.get_ArmourClass(NPC1)))
                if PartyMember.get_SpecSlot1Name(NPC1) != "None":
                    print("      Special: " + PartyMember.get_SpecSlot1Name(NPC1))
            else:
                print(PartyMember.get_name(NPC1) + " (Dead)")
            if PartyMember.get_Health(NPC2) > 0:
                print("2. " + PartyMember.get_name(NPC2) + " " + PartyMember.get_Personality(NPC1) + " (Health " + str(
                    PartyMember.get_Health(NPC2)) + "/" + str(
                    PartyMember.get_MaxHealth(NPC2)) + ")  Armour Class: " + str(PartyMember.get_ArmourClass(NPC2)))
                if PartyMember.get_SpecSlot1Name(NPC2) != "None":
                    print("      Special: " + PartyMember.get_SpecSlot1Name(NPC2))
            else:
                print(PartyMember.get_name(NPC2) + " (Dead)")
            if PartyMember.get_Health(NPC3) > 0:
                print("3. " + PartyMember.get_name(NPC3) + " " + PartyMember.get_Personality(NPC1) + " (Health " + str(
                    PartyMember.get_Health(NPC3)) + "/" + str(
                    PartyMember.get_MaxHealth(NPC3)) + ")  Armour Class: " + str(PartyMember.get_ArmourClass(NPC3)))
                if PartyMember.get_SpecSlot1Name(NPC3) != "None":
                    print("      Special: " + PartyMember.get_SpecSlot1Name(NPC3))
            else:
                print(PartyMember.get_name(NPC3) + " (Dead)")


            time.sleep(1)
            print("\n\nReplace which Party Member?")
            key = input("")
            if key == "1":
                AbigailShapirath = PartyMember()
                PartyMember.set_name(AbigailShapirath, "Abigail Shapirath")
                newHealth = PartyMember.get_Health(AbigailShapirath) + 200
                PartyMember.set_Health(AbigailShapirath, newHealth)
                newMaxHealth = PartyMember.get_MaxHealth(AbigailShapirath) + 200
                PartyMember.set_MaxHealth(AbigailShapirath, newMaxHealth)

                PartyMember.set_name(NPC1, "Abigail Shapirath")
                #PartyMember.set_Initiative(NPC1, PartyMember.get_Initiative(AbigailShapirath))
                PartyMember.set_ArmourClass(NPC1, PartyMember.get_ArmourClass(AbigailShapirath))
                PartyMember.set_AttackModifier(NPC1, PartyMember.get_AttackModifier(AbigailShapirath))
                PartyMember.set_SpecSlot1Name(NPC1, "None")
                PartyMember.set_SpecSlot1Num(NPC1, 0)
                PartyMember.set_SpecSlot1Damage(NPC1, 0)
                PlayerCharacter.set_hasMaiden(PC, True)
            if key == "2":
                AbigailShapirath = PartyMember()
                PartyMember.set_name(AbigailShapirath, "Abigail Shapirath")
                newHealth = PartyMember.get_Health(AbigailShapirath) + 300
                PartyMember.set_Health(AbigailShapirath, newHealth)
                newMaxHealth = PartyMember.get_MaxHealth(AbigailShapirath) + 300
                PartyMember.set_MaxHealth(AbigailShapirath, newMaxHealth)

                PartyMember.set_name(NPC2, "Abigail Shapirath")
                #PartyMember.set_Initiative(NPC2, PartyMember.get_Initiative(AbigailShapirath))
                PartyMember.set_ArmourClass(NPC2, PartyMember.get_ArmourClass(AbigailShapirath))
                PartyMember.set_AttackModifier(NPC2, PartyMember.get_AttackModifier(AbigailShapirath))
                PartyMember.set_SpecSlot1Name(NPC2, "None")
                PartyMember.set_SpecSlot1Num(NPC2, 0)
                PartyMember.set_SpecSlot1Damage(NPC2, 0)
                PlayerCharacter.set_hasMaiden(PC, True)
            if key == "3":
                AbigailShapirath = PartyMember()
                PartyMember.set_name(AbigailShapirath, "Abigail Shapirath")
                newHealth = PartyMember.get_Health(AbigailShapirath) + 300
                PartyMember.set_Health(AbigailShapirath, newHealth)
                newMaxHealth = PartyMember.get_MaxHealth(AbigailShapirath) + 300
                PartyMember.set_MaxHealth(AbigailShapirath, newMaxHealth)

                PartyMember.set_name(NPC3, "Abigail Shapirath")
                #PartyMember.set_Initiative(NPC3, PartyMember.get_Initiative(AbigailShapirath))
                PartyMember.set_ArmourClass(NPC3, PartyMember.get_ArmourClass(AbigailShapirath))
                PartyMember.set_AttackModifier(NPC3, PartyMember.get_AttackModifier(AbigailShapirath))
                PartyMember.set_SpecSlot1Name(NPC3, PartyMember.get_SpecSlot1Name(HolyStrike))
                PartyMember.set_SpecSlot1Num(NPC3, SpecialMoves.get_indexNumber(HolyStrike))
                PartyMember.set_SpecSlot1Damage(NPC3, SpecialMoves.get_damage(HolyStrike))
                PartyMember.set_SpecSlot1Cost(NPC3, SpecialMoves.get_cost(HolyStrike))
                PartyMember.set_SpecSlot1Prob(NPC3, SpecialMoves.get_probability(HolyStrike))
                PlayerCharacter.set_hasMaiden(PC, True)
        elif key == 2:
            print("Thanking the maiden for her hospitality")
            possibleItems = ["longing", "shy", "nervous", "content", "contemplative", "quick"]
            time.sleep(3)
            print("\nThe maiden gives you a " + choice(possibleItems) + " glance.")
        else:
            print("Input unrecognized. Thanking the maiden for her hospitality")
            possibleItems = ["longing", "shy", "nervous", "content", "contemplative", "quick"]
            time.sleep(3)
            print("\nThe maiden gives you a " + choice(possibleItems) + " glance.")
        time.sleep(5)
    else:
        clear()
        print("You embarrass yourself in front of the maiden!")
        time.sleep(5)

        print("\n(Press enter to continue)")
        key = input("")
        if key != "`":
            time.sleep(1)
        else:
            time.sleep(1)


def swordStoneStrengthChallenge():
    roll = randrange(1, 20)
    rolltarget = randrange(10, 15)
    rollmod = PlayerCharacter.get_Strength(PC) / 4
    newroll = roll + rollmod
    time.sleep(1)
    if newroll > rolltarget:
        clear()
        print("You grapple with the sword, which seems firmly planted into the rock beneath.\n")
        time.sleep(2)
        print("      Hrrrrrrgh!")
        time.sleep(2)
        print("                     Gahhhhhhh!")
        time.sleep(2)
        print("\nThe sword comes unlodged in an instance, sending you flying back with it in hand.")
        time.sleep(2)
        possibleItems = ["Sarris Kingdom", "Valmaer Empire", "Erro Dynasty", "Aslam Caliphate"]
        print("\nThe sword glistens magically, and bears the insignia of the " + choice(possibleItems) + " on its hilt.")
        rollforattackMod = randrange(3,6)
        time.sleep(2)
        print("\nThe sword increases your AttackMod by " + str(rollforattackMod) + "!")
        newattackmod = PlayerCharacter.get_attackModifier(PC) + rollforattackMod
        PlayerCharacter.set_attackModifier(PC, newattackmod)
        time.sleep(3)

    else:
        clear()
        print("You grapple with the sword, which seems firmly planted into the rock beneath.\n")
        time.sleep(2)
        print("      Hrrrrrrgh!")
        time.sleep(2)
        print("                     Gahhhhhhh!")
        time.sleep(2)
        print("\nThe sword refuses to budge, taunting you from its comfortable lodging in the stone.")
        time.sleep(3)

    print("\n(Press enter to continue)")
    key = input("")
    if key != "`":
        time.sleep(1)
    else:
        time.sleep(1)


def swordStoneIntellectChallenge():
    roll = randrange(1, 20)
    rolltarget = randrange(17, 27)
    rollmod = PlayerCharacter.get_Intellect(PC) / 4
    newroll = roll + rollmod
    time.sleep(1)
    if newroll > rolltarget:
        clear()
        print("Only a fool would attempt brute strength on such a fine sword. Perhaps some potion of local roots and herbs could loose it?")
        time.sleep(4)
        print("      Hmmmm....")
        time.sleep(2)
        print("                     Searching.....")
        time.sleep(2)
        clear()
        print("After finding nearby reagents and mixing a potion, you pour it over the sword's sheath into the stone, which begins to gurgle.")
        time.sleep(4)
        print("\nHissing and frothing, the stone melts away until the sword is loose and dangling. You pluck it from the stone with ease!")
        time.sleep(4)
        possibleItems = ["Sarris Kingdom", "Valmaer Empire", "Erro Dynasty", "Aslam Caliphate"]
        print("\nThe sword glistens magically, and bears the insignia of the " + choice(possibleItems) + " on its hilt.")
        rollforattackMod = randrange(3,6)
        time.sleep(3)
        print("The sword increases your AttackMod by " + str(rollforattackMod) + "!")
        newattackmod = PlayerCharacter.get_attackModifier(PC) + rollforattackMod
        PlayerCharacter.set_attackModifier(PC, newattackmod)
        time.sleep(3)

    else:
        clear()
        print("Only a fool would attempt brute strength on such a fine sword. Perhaps some potion of local roots and herbs could loose it?")
        time.sleep(4)
        print("      Hmmmm....")
        time.sleep(2)
        print("                     Searching.....")
        time.sleep(2)
        clear()
        print("The homemade potion fizzles and bubbles, but ultimately only burns your hand lightly, doing nothing to loose the sword.")
        rollfordmg = randrange(1,20) + randrange(1,20)
        newPChealth = PlayerCharacter.get_Health(PC) - rollfordmg
        PlayerCharacter.set_Health(PC, newPChealth)
        time.sleep(4)
        print("You take " + str(rollfordmg) + " damage!")
        time.sleep(3)

    print("\n(Press enter to continue)")
    key = input("")
    if key != "`":
        time.sleep(1)
    else:
        time.sleep(1)


def randomEncounter():
    roll1 = randrange(1,100)
    if roll1 < 25:
        roll = randrange(1, 5)

        ## OLD MAN
        if roll == 1:
        #if roll == 1 or roll == 2:
            clear()
            LobbyStatus()
            print("An old man wanders up to your party. He looks weary but curious.")
            time.sleep(1)
            print("After some pleasantries, he asks the party to solve a riddle.")
            time.sleep(1)
            print("\n")
            print("1. Answer the Riddle (Intellect Challenge)")
            print("2. Rob the Old Man (Strength Challenge)\n")
            key = int(input(""))
            if key == 1:
                OldManIntellectChallenge()
            elif key == 2:
                OldManStrengthChallenge()
            else:
                print("Sorry, key not recognized. Attempting riddle!")
                OldManIntellectChallenge()

        ## FAIR MAIDEN
        elif roll == 2: #or roll == 2:
        #elif roll == 3 or roll ==4:
            if PlayerCharacter.get_hasMaiden(PC) == True:
                print("A fair maiden approaches and lends you a magic item. ")
                time.sleep(3)
                attackBonus = randrange(1,3)
                attackMod = PlayerCharacter.get_attackModifier(PC) + attackBonus
                print("It increases your Attack Modifier (increasing accuracy and damage) by " + str(attackBonus))
                time.sleep(3)

            if PlayerCharacter.get_hasMaiden(PC) == False:
                clear()
                LobbyStatus()
                print("A well endowed woman with a familiar-seeming face hails your party.\nAfter introductions, she requests that you accompany her for a traditional dinner.")
                print("\n")
                time.sleep(3)
                print("1. Attend the Maiden's Dinner (Charisma Challenge)")
                print("2. Deceive the Woman for Valuables (Dexterity Challenge)\n")
                key = input("")

                if key == "1":
                    MaidenCharismaChallenge()
                if key == "2":
                    MaidenDexterityChallenge()

        ## LADY IN A LAKE
        elif roll == 3: #or roll == 6:
            print("\nYou come across a Siren in a lake. She offers to bless you with the Gift of Power, allowing you to learn a new Special Attack.")
            time.sleep(2)
            print("\n\n1. Accept her Offer (Learn a Special Attack)\n2. Decline her Offer (Proceed to Next Battle)\n")
            time.sleep(2)
            key = input("")
            if key == "1":
                roll = randrange(1,100)
                if roll < 80:
                    learnSpecial()
                else:
                    print("The Siren betrays you, and her Blessing turns out to be a curse.")
                    time.sleep(2)
                    HealthLoss = randrange(2,75)
                    newHealth = PlayerCharacter.get_Health(PC) - HealthLoss
                    PlayerCharacter.set_Health(PC, newHealth)
                    print("Player Health decreased by " + str(HealthLoss))
            elif key == "2":
                print("You politely decline her offer.")
                time.sleep(2)

        ## SWORD IN THE STONE
        elif roll == 4:  # or roll == 6:
            clear()
            LobbyStatus()
            print("You pass by a Sword stuck in stone nearby. The local peasantry advises that myth says only a Strong hero can pry it from the rock.")
            time.sleep(4)
            print(
                "\n\n1. Try to Remove the Sword (Strength Challenge)\n2. Try to Devise an Alternate Means (Intellect Challenge)\n")
            key = input("")
            if key == "1":
                roll = randrange(1, 100)
                if roll < 92:
                    swordStoneStrengthChallenge()
                else:
                    print("\nAs you approach the sword, a strange hissing noise surrounds you, coming from all sides.")
                    time.sleep(3)
                    print("\nWhat's this? You turn around, but nothing is there!")
                    time.sleep(2)
                    print("\nTurning back around, you see the sword has transformed into a Python, which strikes out at you in an instant!")
                    time.sleep(3)
                    rolldmg = randrange(1,20) + randrange(1,20) + (5 * Stage.get_number(TestStage1)) - (PlayerCharacter.get_ArmourClass(PC) / 4)
                    rolldmg = round(rolldmg)
                    print("\nYou take " + str(rolldmg) + " damage.")
                    newPChealth = PlayerCharacter.get_Health(PC) - rolldmg
                    PlayerCharacter.set_Health(PC, newPChealth)
                    HealthLoss = randrange(2, 75)
                    newHealth = PlayerCharacter.get_Health(PC) - HealthLoss
                    PlayerCharacter.set_Health(PC, newHealth)
                    time.sleep(5)
            else:
                swordStoneIntellectChallenge()

        ## MYSTERIOUS STRANGER
        elif roll == 5:
            time.sleep(2)
            MysteriousStrangerRecruitment()








    else:
        print("")
        clear()







class Battle():
    def __init__(self):
        self.number = 0
        self.combatants = []
        self.loot = []




def tutorial():
    clear()
    print("Falchion is a game about vanquishing foes, managing Party Members, learning Special Attacks, and surviving as long as possible.")
    time.sleep(3)
    print("\nThe Player will create a character, choosing their class and receiving a starting Stat bonus based on that class.")
    time.sleep(4)
    print("\nThen, the Player will build a Party, consisting of 3 supporting Non-Player Characters (NPCs).")
    time.sleep(4)
    print("\nThe Player Character (PC) and Party Members will have an array of Stats, including Strength, Dexterity, Intellect, Charisma, Health, Armour Class, and more!")
    time.sleep(4)
    print("\nArmour Class makes a character harder to hit.\nHealth is how much damage a character can take before dying.\nAttackMod or Attack Modifier increases accuracy and damage.")
    time.sleep(4)
    print("\nInitiative helps a character move first in combat.\nSpecial Points are the points you spend on using Special Attacks.")
    time.sleep(4)
    print("\nAfter you win a battle, you will return to your Campfire and be given the chance to rest.")
    time.sleep(4)
    print("While resting at the Campfire, you will have a variety of options to make your Party stronger. Choose wisely! It could make the difference between survival and death.")
    time.sleep(4)
    print("\nAfter resting at the Campfire, you will depart for another journey. There is a chance of stumbling upon a Random Encounter while departing, but before the next battle.")
    time.sleep(4)
    print("\nRandom Encounters will offer the Player a choice of actions. Some choices pose easy challenges, some harder. Some will test one Stat, some will test another.")
    time.sleep(4)
    print("If you succeed in a Random Encounter, you will be rewarded with a considerable bonus.")
    time.sleep(3)
    print("\nWhile navigating the game, you will mostly need to type in a number (1-10) and hit enter, or just hit enter.")
    time.sleep(3)
    print("\nIf the game seems to be loading the next text slowly, try hitting the arrow keys -- don't hit enter or spam keys.")
    time.sleep(3)
    print("\nThat's all for now! Press any key to return to the Main Menu.\n")
    key = input("")
    if key != "`":
        MainMenu()
    else:
        MainMenu()



def initializeEntities():
    PC = PlayerCharacter()
    NPC1 = PartyMember()
    NPC2 = PartyMember()
    NPC3 = PartyMember()
    TestEnemy = Enemy()
    TestStage1 = Stage()


def MainMenu():
    clear()
    print("Loading...")
    clear()
    print("\n")
    clear()
    print("Loading...")
    clear()
    print("                           ")
    print("  ______      _      _____ _    _ _____ ____  _   _ ")
    print(" |  ____/\   | |    / ____| |  | |_   _/ __ \| \ | |")
    print(" | |__ /  \  | |   | |    | |__| | | || |  | |  \| |")
    print(" |  __/ /\ \ | |   | |    |  __  | | || |  | | . ` |")
    print(" | | / ____ \| |___| |____| |  | |_| || |__| | |\  |")
    print(" |_|/_/    \_\______\_____|_|  |_|_____\____/|_| \_|")
    print("")
    print("               Version 1.3 - Alpha")
    print("")
    print("                   by Spooky           ")
    print("\nFight Villains\n")
    print("         Learn Magic & Grow Stronger \n")
    print("                      Watch Evil Grow Stronger With Time      \n")
    print("                            ")
    print("1. New Game")
    print("2. Tutorial - Recommended for New Players")
    print("3. Config Game - Coming Soon")
    print("4. Exit Game - Coming Soon")
    print("5. Quick Start - Development Only")
    print("6. Load Game - Coming Soon")
    answered = input("\nPlease type a number to select an option.\n\n")
    if answered == "1":
        newgame()
    if answered == "5":

        buffEnemy()
        #LobbyStatus()
        buffEnemy()
        clear()
        LobbyStatus()
        #initializeEntities()
        PlayerCharacter.set_MaxHealth(PC, 1000)
        PlayerCharacter.set_Health(PC, 1000)
        PlayerCharacter.set_name(PC, "TestName for Save")

        #preBattle()


        SaveGame()
        InitiativeCheck()

    if answered == "2":
        tutorial()


        #buildparty()
        #levelUp()
        #DescripAndInit()

    if answered == "6":
        LoadGame()
        levelUp()
    else:
        exit()





PC = PlayerCharacter()
NPC1 = PartyMember()
NPC2 = PartyMember()
NPC3 = PartyMember()
TestEnemy = Enemy()
TestStage1 = Stage()

#if PlayerCharacter.get_LoadedSave(PC) == True:
#    with open("playerData.pkl", "rb") as inp:
#        PC = pickle.load(inp)


def newgame():

    clear()
    PC = PlayerCharacter()
    NPC1 = PartyMember()
    NPC2 = PartyMember()
    NPC3 = PartyMember()
    TestEnemy = Enemy()
    TestStage1 = Stage()

    generateItems()



    PCmaxhealth = PlayerCharacter.get_Health(PC)
    PlayerCharacter.set_MaxHealth(PC, PCmaxhealth)
    NPC1maxhealth = PartyMember.get_Health(NPC1)
    PartyMember.set_MaxHealth(NPC1, NPC1maxhealth)
    NPC2maxhealth = PartyMember.get_Health(NPC2)
    PartyMember.set_MaxHealth(NPC2, NPC2maxhealth)
    NPC3maxhealth = PartyMember.get_Health(NPC3)
    PartyMember.set_MaxHealth(NPC3, NPC3maxhealth)
    enemyMaxHealth = Enemy.get_Health(TestEnemy)
    Enemy.set_MaxHealth(TestEnemy, enemyMaxHealth)
    Stage.set_number(TestStage1, 1)
    #NPC4 = PartyMember()
    assignEnemyPersonalityOmenClass()



    Enemy.set_BattleTurn(TestEnemy,0)
    print("Choose a class or have one randomly selected for you.\n")
    print("1. I want to choose a class.")
    print("2. Choose one for me.")
    playerclass = input("\n")
    if playerclass == "1":
        chooseclassnewgame()
    else:
        randomclassnewgame()


def SaveGame():
    print("")
    clear()
    LobbyStatus()
    key = input("\nSave game? (1. Yes/2. No)\n")

    if key == "1":

        # PC = PlayerCharacter()
        # save_object(PC, "PC.pk1")

        TestObject1.set_name("TestObjectName-Steve")

        with open("testData.pkl", "wb") as outp:
            outp.seek(0)
            pickle.dump(TestObject1,outp)


        with open("playerData.pkl", "wb") as outp:
            outp.seek(0)
            pickle.dump(PC, outp)
        with open("partyData.pkl", "wb") as outp:
            outp.seek(0)
            pickle.dump(NPC1, outp)
            pickle.dump(NPC2, outp)
            pickle.dump(NPC3, outp)
        with open("stageData.pkl", "wb") as outp:
            outp.seek(0)
            pickle.dump(TestStage1, outp)
        with open("enemyData.pkl", "wb") as outp:
            outp.seek(0)
            pickle.dump(TestEnemy, outp)
        with open("specialData.pkl", "wb") as outp:
            outp.seek(0)
            pickle.dump(HolyStrike, outp)
            pickle.dump(IronMastery, outp)
            pickle.dump(FireStrike, outp)
            pickle.dump(SleepingGod, outp)
            pickle.dump(DemonMagic, outp)
            pickle.dump(AnimalFamiliar, outp)
            pickle.dump(WaterChain, outp)
            pickle.dump(PsychicBomb, outp)
            pickle.dump(ShieldBash, outp)
        with open("itemData.pkl", "wb") as outp:
            outp.seek(0)
            pickle.dump(Item1, outp)
            pickle.dump(Item2, outp)
            pickle.dump(Item3, outp)
            pickle.dump(Item4, outp)






        # PCNameSave = PlayerCharacter.get_name(PC)
        # PCNameSaveDump = pickle.dump(PCNameSave, open("PCNameSave", "wb"))
        # PCStrSave = PlayerCharacter.get_Strength(PC)
        # PCStrSaveDump = pickle.dump(PCStrSave, open("Save File", "wb"))
        # PCHealthSave = int(PlayerCharacter.get_Health(PC))
        # PCHealthSaveDump = pickle.dump(PCHealthSave, open("PCHealthSave", "wb"))

        print("\nSaving....")
        time.sleep(3)
        print("Saved game for " + PlayerCharacter.get_name(PC) +".")

        time.sleep(3)


    else:
        print("\nNot saving...")
        time.sleep(1)
    clear()
    LobbyStatus()


def LoadPCTest():
    with open("playerData.pkl", "rb") as inp:
        PC = pickle.load(inp)









def LoadGame():
    print("")
    clear()
    key = input("Load game? (1. Yes/2. No)\n")
    if key == "1":

        #load_object(PC, "PC.pk1")


        ImportedPC = PlayerCharacter


        with open("playerData.pkl", "rb") as inp:
            ImportedPC = pickle.load(inp)
        with open("partyData.pkl", "rb") as inp:
            ImportedNPC1 = pickle.load(inp)
            ImportedNPC2 = pickle.load(inp)
            ImportedNPC3 = pickle.load(inp)
        with open("stageData.pkl", "rb") as inp:
            ImportedStage = pickle.load(inp)
        with open("enemyData.pkl", "rb") as inp:
            ImportedEnemy = pickle.load(inp)

        with open("specialData.pkl", "rb") as inp:
            ImportedSpecial1 = pickle.load(inp)
            ImportedSpecial2 = pickle.load(inp)
            ImportedSpecial3 = pickle.load(inp)
            ImportedSpecial4 = pickle.load(inp)
            ImportedSpecial5 = pickle.load(inp)
            ImportedSpecial6 = pickle.load(inp)
            ImportedSpecial7 = pickle.load(inp)
            ImportedSpecial8 = pickle.load(inp)
            ImportedSpecial9 = pickle.load(inp)
        with open("itemData.pkl", "rb") as inp:
            ImportedItem1 = pickle.load(inp)
            ImportedItem2 = pickle.load(inp)
            ImportedItem3 = pickle.load(inp)
            ImportedItem4 = pickle.load(inp)



        PlayerCharacter.set_name(PC, PlayerCharacter.get_name(ImportedPC))
        PlayerCharacter.set_Health(PC, PlayerCharacter.get_Health(ImportedPC))
        PlayerCharacter.set_MaxHealth(PC, PlayerCharacter.get_MaxHealth(ImportedPC))
        PlayerCharacter.set_gender(PC, PlayerCharacter.get_gender(ImportedPC))
        PlayerCharacter.set_playerclass(PC, PlayerCharacter.get_playerclass(ImportedPC))
        PlayerCharacter.set_hasMaiden(PC, PlayerCharacter.get_hasMaiden(ImportedPC))
        PlayerCharacter.set_Gold(PC, PlayerCharacter.get_Gold(ImportedPC))
        PlayerCharacter.set_Blood(PC, PlayerCharacter.get_Blood(ImportedPC))
        PlayerCharacter.set_attackStat(PC, PlayerCharacter.get_attackStat(ImportedPC))
        PlayerCharacter.set_attackModifier(PC, PlayerCharacter.get_attackModifier(ImportedPC))
        PlayerCharacter.set_Strength(PC, PlayerCharacter.get_Strength(ImportedPC))
        PlayerCharacter.set_Toughness(PC, PlayerCharacter.get_Toughness(ImportedPC))
        PlayerCharacter.set_Dexterity(PC, PlayerCharacter.get_Dexterity(ImportedPC))
        PlayerCharacter.set_Charisma(PC, PlayerCharacter.get_Charisma(ImportedPC))
        PlayerCharacter.set_Intellect(PC, PlayerCharacter.get_Intellect(ImportedPC))
        PlayerCharacter.set_Initiative(PC, PlayerCharacter.get_Initiative(ImportedPC))
        PlayerCharacter.set_ArmourClass(PC, PlayerCharacter.get_ArmourClass(ImportedPC))
        PlayerCharacter.set_SpecialPoints(PC, PlayerCharacter.get_SpecialPoints(ImportedPC))


        PartyMember.set_name(NPC1, PartyMember.get_name(ImportedNPC1))
        PartyMember.set_isAlive(NPC1, PartyMember.get_isAlive(ImportedNPC1))
        PartyMember.set_ArmourClass(NPC1, PartyMember.get_ArmourClass(ImportedNPC1))
        PartyMember.set_AttackModifier(NPC1, PartyMember.get_AttackModifier(ImportedNPC1))
        PartyMember.set_Health(NPC1, PartyMember.get_Health(ImportedNPC1))
        PartyMember.set_MaxHealth(NPC1, PartyMember.get_MaxHealth(ImportedNPC1))
        PartyMember.set_Personality(NPC1, PartyMember.get_Personality(ImportedNPC1))
        PartyMember.set_SpecSlot1Name(NPC1, PartyMember.get_SpecSlot1Name(ImportedNPC1))
        PartyMember.set_SpecSlot1Num(NPC1, PartyMember.get_SpecSlot1Num(ImportedNPC1))
        PartyMember.set_SpecSlot1Damage(NPC1, PartyMember.get_SpecSlot1Damage(ImportedNPC1))
        PartyMember.set_SpecSlot1Prob(NPC1, PartyMember.get_SpecSlot1Prob(ImportedNPC1))
        PartyMember.set_SpecSlot1Cost(NPC1, PartyMember.get_SpecSlot1Cost(ImportedNPC1))

        PartyMember.set_name(NPC2, PartyMember.get_name(ImportedNPC2))
        PartyMember.set_isAlive(NPC2, PartyMember.get_isAlive(ImportedNPC2))
        PartyMember.set_ArmourClass(NPC2, PartyMember.get_ArmourClass(ImportedNPC2))
        PartyMember.set_AttackModifier(NPC2, PartyMember.get_AttackModifier(ImportedNPC2))
        PartyMember.set_Health(NPC2, PartyMember.get_Health(ImportedNPC2))
        PartyMember.set_MaxHealth(NPC2, PartyMember.get_MaxHealth(ImportedNPC2))
        PartyMember.set_Personality(NPC2, PartyMember.get_Personality(ImportedNPC2))
        PartyMember.set_SpecSlot1Name(NPC2, PartyMember.get_SpecSlot1Name(ImportedNPC2))
        PartyMember.set_SpecSlot1Num(NPC2, PartyMember.get_SpecSlot1Num(ImportedNPC2))
        PartyMember.set_SpecSlot1Damage(NPC2, PartyMember.get_SpecSlot1Damage(ImportedNPC2))
        PartyMember.set_SpecSlot1Prob(NPC2, PartyMember.get_SpecSlot1Prob(ImportedNPC2))
        PartyMember.set_SpecSlot1Cost(NPC2, PartyMember.get_SpecSlot1Cost(ImportedNPC2))

        PartyMember.set_name(NPC3, PartyMember.get_name(ImportedNPC3))
        PartyMember.set_isAlive(NPC3, PartyMember.get_isAlive(ImportedNPC3))
        PartyMember.set_ArmourClass(NPC3, PartyMember.get_ArmourClass(ImportedNPC3))
        PartyMember.set_AttackModifier(NPC3, PartyMember.get_AttackModifier(ImportedNPC3))
        PartyMember.set_Health(NPC3, PartyMember.get_Health(ImportedNPC3))
        PartyMember.set_MaxHealth(NPC3, PartyMember.get_MaxHealth(ImportedNPC3))
        PartyMember.set_Personality(NPC3, PartyMember.get_Personality(ImportedNPC3))
        PartyMember.set_SpecSlot1Name(NPC3, PartyMember.get_SpecSlot1Name(ImportedNPC3))
        PartyMember.set_SpecSlot1Num(NPC3, PartyMember.get_SpecSlot1Num(ImportedNPC3))
        PartyMember.set_SpecSlot1Damage(NPC3, PartyMember.get_SpecSlot1Damage(ImportedNPC3))
        PartyMember.set_SpecSlot1Prob(NPC3, PartyMember.get_SpecSlot1Prob(ImportedNPC3))
        PartyMember.set_SpecSlot1Cost(NPC3, PartyMember.get_SpecSlot1Cost(ImportedNPC3))

        Stage.set_number(TestStage1, Stage.get_number(ImportedStage))

        Enemy.set_NumberOfKills(TestEnemy, Enemy.get_NumberOfKills(ImportedEnemy))
        Enemy.set_BattleTurn(TestEnemy, Enemy.get_BattleTurn(ImportedEnemy))
        Enemy.set_Stage(TestEnemy, Enemy.get_Stage(ImportedEnemy))

        SpecialMoves.set_damage(HolyStrike, SpecialMoves.get_damage(ImportedSpecial1))
        SpecialMoves.set_damage(IronMastery, SpecialMoves.get_damage(ImportedSpecial2))
        SpecialMoves.set_damage(FireStrike, SpecialMoves.get_damage(ImportedSpecial3))
        SpecialMoves.set_damage(SleepingGod, SpecialMoves.get_damage(ImportedSpecial4))
        SpecialMoves.set_damage(DemonMagic, SpecialMoves.get_damage(ImportedSpecial5))
        SpecialMoves.set_damage(AnimalFamiliar, SpecialMoves.get_damage(ImportedSpecial6))
        SpecialMoves.set_damage(WaterChain, SpecialMoves.get_damage(ImportedSpecial7))
        SpecialMoves.set_damage(PsychicBomb, SpecialMoves.get_damage(ImportedSpecial8))
        SpecialMoves.set_damage(ShieldBash, SpecialMoves.get_damage(ImportedSpecial9))

        Item.set_name(Item1, Item.get_name(ImportedItem1))
        Item.set_adj(Item1, Item.get_adj(ImportedItem1))
        Item.set_name(Item2, Item.get_name(ImportedItem2))
        Item.set_adj(Item2, Item.get_adj(ImportedItem2))
        Item.set_name(Item3, Item.get_name(ImportedItem3))
        Item.set_adj(Item3, Item.get_adj(ImportedItem3))
        Item.set_name(Item4, Item.get_name(ImportedItem4))
        Item.set_adj(Item4, Item.get_adj(ImportedItem4))

        print("\nLoading....")
        time.sleep(3)
        LoadedSave()
        levelUp()
    else:
        print("\nNot loading...")
        time.sleep(3)
        levelUp()


def randomclassnewgame():
    warriordescription = "Warriors have a bonus to starting Health (+30 HP) and Strength (+2)."
    rangerdescription = "Rangers have a bonus to starting Health (+15 HP), Dexterity (+2) and Toughness (+2)."
    magiciandescription = "Magicians have a bonus to starting Dexterity (+3) and Intellect (+3)."
    roguedescription = "Rogues have a bonus to starting Health (+30 HP) and Dexterity (+2)."
    paladindescription = "Paladins have a bonus to Health (+20 HP) and Strength (+3)."
    classes = ["Warrior", "Ranger","Magician","Rogue","Paladin"]
    classesdescription = [warriordescription, rangerdescription, magiciandescription, roguedescription, paladindescription]
    classpicker = randrange(0,4)
    classpicker2 = randrange(0,4)
    classpicker3 = randrange(0,4)
    clear()
    print("  Hmmm... Perhaps you have the soul of a...")
    #print("\n")
    #print("      " + str(classes[classpicker2])+ "           ")
    time.sleep(1)
    #clear()
    #print("\n\n")
    #print("     " + str(classes[classpicker2]) + ".           ")
    #time.sleep(1)
    #clear()
    #print("\n\n")
    #print("    " + str(classes[classpicker2]) + "..           ")
    #time.sleep(1)
    #clear()
    #print("\n\n")
    #print("   " + str(classes[classpicker2]) + "...           ")
    #time.sleep(1)
    #clear()
    #print("    No..  Perhaps a...")
    #time.sleep(2)
    #clear()
    #print("\n\n")
    #print("                      " + str(classes[classpicker3]) + "       ")
    #time.sleep(1)
    #clear()
    #print("\n\n")
    #print("                      ." + str(classes[classpicker3]) + "      ")
    #time.sleep(1)
    #clear()
    #print("\n\n")
    #print("                      .." + str(classes[classpicker3]) + "      ")
    #time.sleep(1)
    #clear()
    #print("\n\n")
    #print("                      ..." + str(classes[classpicker3]) + "      ")
    time.sleep(1)
    clear()
    print("")
    print("You have the soul of a " + str(classes[classpicker])+ ". " + str(classesdescription[classpicker]) + "\n")
    if classpicker == 0:
        print("Health is " + str(PC.get_Health()))
        pchealth = PC.get_Health()
        PC.set_Health(pchealth + 30)
        print("Health increased to " + str(PC.get_Health()))
        PC.set_playerclass("Warrior")

        WarStrength = int(PlayerCharacter.get_Strength(PC))
        WarStrengthMod = WarStrength / 4
        PlayerCharacter.set_attackModifier(PC, WarStrengthMod)
        PlayerCharacter.set_attackStat(PC, "Strength")




        time.sleep(3)
        charactercreateClassChosen()
    if classpicker == 1:
        PlayerCharacter.set_playerclass(PC, "Ranger")
        PC.set_attackStat = "Dexterity"
        print(str(PlayerCharacter.get_playerclass(PC)))
        print("Health is " + str(PlayerCharacter.get_Health(PC)))
        pchealth = PlayerCharacter.get_Health(PC)
        PC.set_Health(pchealth + 15)
        print("Health increased to " + str(PlayerCharacter.get_Health(PC)))
        print("Dexterity is " + str(PlayerCharacter.get_Dexterity(PC)))
        pcdex = PlayerCharacter.get_Dexterity(PC)
        PC.set_Dexterity(pcdex + 2)
        print("Dexterity increased to " + str(PlayerCharacter.get_Dexterity(PC)))
        print("Toughness is " + str(PlayerCharacter.get_Toughness(PC)))
        pctough = PlayerCharacter.get_Toughness(PC)
        PC.set_Toughness(pctough + 2)
        print("Toughness increased to " + str(PlayerCharacter.get_Toughness(PC)))

        RanDex = int(PlayerCharacter.get_Dexterity(PC))
        RanDexMod = RanDex / 4
        PlayerCharacter.set_attackModifier(PC, RanDexMod)
        PlayerCharacter.set_attackStat(PC, "Dexterity")



        time.sleep(3)
        charactercreateClassChosen()
    if classpicker == 2:
        PlayerCharacter.set_playerclass(PC, "Magician")
        PC.set_attackStat = "Intellect"
        print(str(PlayerCharacter.get_playerclass(PC)))
        print("Dexterity is " + str(PlayerCharacter.get_Dexterity(PC)))
        pcDexterity = PlayerCharacter.get_Dexterity(PC)
        PC.set_Dexterity(pcDexterity + 3)
        print("Dexterity increased to " + str(PlayerCharacter.get_Dexterity(PC)))
        print("Intellect is " + str(PlayerCharacter.get_Intellect(PC)))
        pcIntellect = PlayerCharacter.get_Intellect(PC)
        PC.set_Intellect(pcIntellect + 3)
        print("Intellect increased to " + str(PlayerCharacter.get_Intellect(PC)))

        MagInt = int(PlayerCharacter.get_Intellect(PC))
        MagIntMod = MagInt / 4
        PlayerCharacter.set_attackModifier(PC, MagIntMod)
        PlayerCharacter.set_attackStat(PC, "Intellect")


        time.sleep(3)
        charactercreateClassChosen()
    if classpicker == 3:
        PlayerCharacter.set_playerclass(PC, "Rogue")
        PC.set_attackStat = "Dexterity"
        print(str(PlayerCharacter.get_playerclass(PC)))
        print("Health is " + str(PlayerCharacter.get_Health(PC)))
        pcHealth = PlayerCharacter.get_Health(PC)
        PC.set_Health(pcHealth + 30)
        print("Health increased to " + str(PlayerCharacter.get_Health(PC)))
        print("Dexterity is " + str(PlayerCharacter.get_Dexterity(PC)))
        pcDexterity = PlayerCharacter.get_Dexterity(PC)
        PC.set_Dexterity(pcDexterity + 2)
        print("Dexterity increased to " + str(PlayerCharacter.get_Dexterity(PC)))

        RogDex = int(PlayerCharacter.get_Dexterity(PC))
        RogDexMod = RogDex / 4
        PlayerCharacter.set_attackModifier(PC, RogDexMod)
        PlayerCharacter.set_attackStat(PC, "Dexterity")

        time.sleep(3)
        charactercreateClassChosen()
    if classpicker == 4:
        PlayerCharacter.set_playerclass(PC, "Paladin")
        PC.set_attackStat = "Toughness"
        print(str(PlayerCharacter.get_playerclass(PC)))
        print("Health is " + str(PlayerCharacter.get_Health(PC)))
        pcHealth = PlayerCharacter.get_Health(PC)
        PC.set_Health(pcHealth + 20)
        print("Health increased to " + str(PlayerCharacter.get_Health(PC)))
        print("Strength is " + str(PlayerCharacter.get_Strength(PC)))
        pcStrength = PlayerCharacter.get_Strength(PC)
        PC.set_Strength(pcStrength + 3)
        print("Strength increased to " + str(PlayerCharacter.get_Strength(PC)))

        PalTough = int(PlayerCharacter.get_Strength(PC))
        PalToughMod = PalTough / 4
        PlayerCharacter.set_attackModifier(PC, PalToughMod)
        PlayerCharacter.set_attackStat(PC, "Strength")

        time.sleep(3)
        charactercreateClassChosen()




def chooseclassnewgame():
    clear()
    print("Your traits are as follows: ")
    print("Weapon Skill: " + str(PlayerCharacter.get_WeaponSkill(PC)))
    print("Strength: " + str(PlayerCharacter.get_Strength(PC)))
    print("Toughness: " + str(PlayerCharacter.get_Toughness(PC)))
    print("Dexterity: " + str(PlayerCharacter.get_Dexterity(PC)))
    print("Charisma: " + str(PlayerCharacter.get_Charisma(PC)))
    print("Intellect: " + str(PlayerCharacter.get_Intellect(PC)))
    print("Health: " + str(PlayerCharacter.get_Health(PC)))
    print("StatScore: " + str(PlayerCharacter.get_StatScore(PC)))
    print("\n")
    print("Choose a class from the following selections. Select an option to learn more.")
    print("1. Warrior (STR)")
    print("2. Ranger (DEX)")
    print("3. Magician (INT)")
    print("4. Rogue (DEX)")
    print("5. Paladin (STR)")
    classselect = input("\n")
    if classselect == "1":
        clear()
        print("Warriors have a bonus to starting Health (+30 HP) and Strength (+2).")
        print("\nWould you like to play as a Warrior? (Yy/Nn)")
        confirmselect = input("\n")
        if confirmselect == "Y" or "y":
            clear()
            print("Health is " + str(PC.get_Health()))
            pchealth = PC.get_Health()
            PC.set_Health(pchealth + 30)
            print("Health increased to " + str(PC.get_Health()))
            PC.set_playerclass("Warrior")

            WarStrength = int(PlayerCharacter.get_Strength(PC))
            WarStrengthMod = WarStrength / 4
            PlayerCharacter.set_attackModifier(PC, WarStrengthMod)
            PC.set_attackStat("Strength")

            time.sleep(3)
            charactercreateClassChosen()
        else:
            chooseclassnewgame()

    if classselect == "2":
        clear()
        print("Rangers have a bonus to starting Health (+15 HP), Dexterity (+2) and Toughness (+2).")
        print("\nWould you like to play as a Ranger? (Yy/Nn)")
        confirmselect = input("\n")
        if confirmselect == "Y" or "y":
            clear()
            PlayerCharacter.set_playerclass(PC, "Ranger")



            print(str(PlayerCharacter.get_playerclass(PC)))
            print("Health is " + str(PlayerCharacter.get_Health(PC)))
            pchealth = PlayerCharacter.get_Health(PC)
            PC.set_Health(pchealth + 15)
            print("Health increased to " + str(PlayerCharacter.get_Health(PC)))
            print("Dexterity is " + str(PlayerCharacter.get_Dexterity(PC)))
            pcdex = PlayerCharacter.get_Dexterity(PC)
            PC.set_Dexterity(pcdex + 2)
            print("Dexterity increased to " + str(PlayerCharacter.get_Dexterity(PC)))
            print("Toughness is " + str(PlayerCharacter.get_Toughness(PC)))
            pctough = PlayerCharacter.get_Toughness(PC)
            PC.set_Toughness(pctough + 2)
            print("Toughness increased to " + str(PlayerCharacter.get_Toughness(PC)))

            RanDex = int(PlayerCharacter.get_Dexterity(PC))
            RanDexMod = RanDex / 4
            PlayerCharacter.set_attackModifier(PC, RanDexMod)
            PC.set_attackStat("Dexterity")

            time.sleep(3)
            charactercreateClassChosen()
        else:
            chooseclassnewgame()

    if classselect == "3":
        clear()
        print("Magicians have a bonus to starting Dexterity (+3) and Intellect (+3).")
        print("\nWould you like to play as a Magician? (Yy/Nn)")
        confirmselect = input("\n")
        if confirmselect == "Y" or "y":
            clear()
            PlayerCharacter.set_playerclass(PC, "Magician")




            print(str(PlayerCharacter.get_playerclass(PC)))
            print("Dexterity is " + str(PlayerCharacter.get_Dexterity(PC)))
            pcDexterity = PlayerCharacter.get_Dexterity(PC)
            PC.set_Dexterity(pcDexterity + 3)
            print("Dexterity increased to " + str(PlayerCharacter.get_Dexterity(PC)))
            print("Intellect is " + str(PlayerCharacter.get_Intellect(PC)))
            pcIntellect = PlayerCharacter.get_Intellect(PC)
            PC.set_Intellect(pcIntellect + 3)
            print("Intellect increased to " + str(PlayerCharacter.get_Intellect(PC)))

            MagInt = int(PlayerCharacter.get_Intellect(PC))
            MagIntMod = MagInt / 4
            PlayerCharacter.set_attackModifier(PC, MagIntMod)
            PC.set_attackStat("Intellect")

            time.sleep(3)
            charactercreateClassChosen()
        else:
            chooseclassnewgame()

    if classselect == "4":
        clear()
        print("Rogues have a bonus to starting Health (+30 HP) and Dexterity (+2).")
        print("\nWould you like to play as a Rogue? (Yy/Nn)")
        confirmselect = input("\n")
        if confirmselect == "Y" or "y":
            clear()
            PlayerCharacter.set_playerclass(PC, "Rogue")


            print(str(PlayerCharacter.get_playerclass(PC)))
            print("Health is " + str(PlayerCharacter.get_Health(PC)))
            pcHealth = PlayerCharacter.get_Health(PC)
            PC.set_Health(pcHealth + 30)
            print("Health increased to " + str(PlayerCharacter.get_Health(PC)))
            print("Dexterity is " + str(PlayerCharacter.get_Dexterity(PC)))
            pcDexterity = PlayerCharacter.get_Dexterity(PC)
            PC.set_Dexterity(pcDexterity + 2)
            print("Dexterity increased to " + str(PlayerCharacter.get_Dexterity(PC)))

            RogDex = int(PlayerCharacter.get_Dexterity(PC))
            RogDexMod = RogDex / 4
            PlayerCharacter.set_attackModifier(PC, RogDexMod)
            PC.set_attackStat("Dexterity")

            time.sleep(3)
            charactercreateClassChosen()
        else:
            chooseclassnewgame()

    if classselect == "5":
        clear()
        print("Paladins have a bonus to Health (+15 HP), Strength (+2) and Toughness (+2).")
        print("\nWould you like to play as a Paladin? (Yy/Nn)")
        confirmselect = input("\n")
        if confirmselect == "Y" or "y":
            clear()
            PlayerCharacter.set_playerclass(PC, "Paladin")
            print(str(PlayerCharacter.get_playerclass(PC)))
            print("Health is " + str(PlayerCharacter.get_Health(PC)))
            pcHealth = PlayerCharacter.get_Health(PC)
            PC.set_Health(pcHealth + 20)
            print("Health increased to " + str(PlayerCharacter.get_Health(PC)))
            print("Strength is " + str(PlayerCharacter.get_Strength(PC)))
            pcStrength = PlayerCharacter.get_Strength(PC)
            PC.set_Strength(pcStrength + 3)
            print("Strength increased to " + str(PlayerCharacter.get_Strength(PC)))


            PalTough = int(PlayerCharacter.get_Strength(PC))
            PalToughMod = PalTough / 4
            PlayerCharacter.set_attackModifier(PC, PalToughMod)
            PC.set_attackStat("Strength")

            time.sleep(3)
            charactercreateClassChosen()
        else:
            chooseclassnewgame()


def charactercreateClassChosen():

    attackMod = round(PlayerCharacter.get_attackModifier(PC))
    PlayerCharacter.set_attackModifier(PC, attackMod)

    clear()
    print("Here's what your character currently looks like:")
    print("\n")
    print("Name: " + str(PlayerCharacter.get_name(PC)))
    print("Class: " + str(PlayerCharacter.get_playerclass(PC)))
    print("Age: " + str(PlayerCharacter.get_age(PC)))
    print("\n")
    print("Class Skill: " + str(PlayerCharacter.get_attackStat(PC)))
    print("Attack Modifier (" + str(PlayerCharacter.get_attackStat(PC))+ " Based): " + str(PlayerCharacter.get_attackModifier(PC)))
    print("\n")
    #print("Weapon Skill: " + str(PlayerCharacter.get_WeaponSkill(PC)))
    print("Strength: " + str(PlayerCharacter.get_Strength(PC)))
    print("Toughness: " + str(PlayerCharacter.get_Toughness(PC)))
    print("Dexterity: " + str(PlayerCharacter.get_Dexterity(PC)))
    print("Charisma: " + str(PlayerCharacter.get_Charisma(PC)))
    print("Intellect: " + str(PlayerCharacter.get_Intellect(PC)))
    print("StatScore: " + str(PlayerCharacter.get_StatScore(PC)))
    print("\nOptions:\n1. Build Party\n2. Rename Character\n3. Restart Character Creation")
    selection = input("\nPlease choose an option: \n")
    if selection == "1":
        buildparty()
    elif selection == "2":
        clear()
        print("Renaming character. Please enter the desired name below:\n")
        newname = input("\n")
        PlayerCharacter.set_name(PC, newname)
        time.sleep(3)
        charactercreateClassChosen()
    elif selection == "3":
        newgame()
    else:
        charactercreateClassChosen()


enemyACdivision = Enemy.get_ArmourClass(TestEnemy) / 6


HolyStrike = SpecialMoves()
SpecialMoves.set_name(HolyStrike, "Holy Strike")
SpecialMoves.set_cost(HolyStrike, 2)
SpecialMoves.set_damage(HolyStrike, randrange(50,80))
SpecialMoves.set_probability(HolyStrike, 80)
SpecialMoves.set_indexNumber(HolyStrike, 77)
SpecialMoves.set_description(HolyStrike,
                             "A divinely inspired strike, enhanced with blessings from a God.")

IronMastery = SpecialMoves()
SpecialMoves.set_name(IronMastery, "Iron Mastery")
SpecialMoves.set_cost(IronMastery, 1)
SpecialMoves.set_damage(IronMastery, randrange(35,60))
SpecialMoves.set_probability(IronMastery, 90)
SpecialMoves.set_indexNumber(IronMastery, 25)
SpecialMoves.set_description(IronMastery,
                             "Decades of training informs muscle memory on exactly how to perform a deadly maneuver.")

FireStrike = SpecialMoves()
SpecialMoves.set_name(FireStrike, "Fire Strike")
SpecialMoves.set_cost(FireStrike, 2)
SpecialMoves.set_damage(FireStrike, randrange(70,125))
SpecialMoves.set_probability(FireStrike, 65)
SpecialMoves.set_indexNumber(FireStrike, 82)
SpecialMoves.set_description(FireStrike,
                             "A powerful fiery eruption scorches away at your enemies, but with wild unpredictability.")

ShieldBash = SpecialMoves()
SpecialMoves.set_name(ShieldBash, "Shield Bash")
SpecialMoves.set_cost(ShieldBash, 3)
SpecialMoves.set_damage(ShieldBash, randrange(150,175))
SpecialMoves.set_probability(ShieldBash, 60)
SpecialMoves.set_indexNumber(ShieldBash, 111)
SpecialMoves.set_description(ShieldBash,
                             "A hulking shove forward with the defender's shield pushes enemies back and wounds them in the process.")

PsychicBomb = SpecialMoves()
SpecialMoves.set_name(PsychicBomb, "Psychic Bomb")
SpecialMoves.set_cost(PsychicBomb, 5)
SpecialMoves.set_damage(PsychicBomb, randrange(300,350))
SpecialMoves.set_probability(PsychicBomb, 50)
SpecialMoves.set_indexNumber(PsychicBomb, 4444)
SpecialMoves.set_description(PsychicBomb,
                             "An excruciating wave of psychic horror explodes out of the user, wreaking havoc on the mind of the target.")

WaterChain = SpecialMoves()
SpecialMoves.set_name(WaterChain, "Water Chain")
SpecialMoves.set_cost(WaterChain, 3)
SpecialMoves.set_damage(WaterChain, randrange(90,120))
SpecialMoves.set_probability(WaterChain, 80)
SpecialMoves.set_indexNumber(WaterChain, 22)
SpecialMoves.set_description(WaterChain,
                             "Elemental magic lashes up from the surroundings to twist at enemies with chains of water.")

AnimalFamiliar = SpecialMoves()
SpecialMoves.set_name(AnimalFamiliar, "Animal Familiar")
SpecialMoves.set_cost(AnimalFamiliar, 2)
SpecialMoves.set_damage(AnimalFamiliar, randrange(80,100))
SpecialMoves.set_probability(AnimalFamiliar, 70)
SpecialMoves.set_indexNumber(AnimalFamiliar, 35)
SpecialMoves.set_description(AnimalFamiliar,
                             "An animal familiar accompanies this character, and fights viciously on their behalf in battle, if not unpredictably.")

DemonMagic = SpecialMoves()
SpecialMoves.set_name(DemonMagic, "Demon Magic")
SpecialMoves.set_cost(DemonMagic, 3)
SpecialMoves.set_damage(DemonMagic, randrange(140,160))
SpecialMoves.set_probability(DemonMagic, 50)
SpecialMoves.set_indexNumber(DemonMagic, 666)
SpecialMoves.set_description(DemonMagic,
                             "An incredibly unpredictable, but cheap, ability to channel Demonic magic and rend one's enemy with it.")

SleepingGod = SpecialMoves()
SpecialMoves.set_name(SleepingGod, "Prayer to the Sleeping God")
SpecialMoves.set_cost(SleepingGod, 1)
SpecialMoves.set_damage(SleepingGod, randrange(300,400))
SpecialMoves.set_probability(SleepingGod, 20)
SpecialMoves.set_indexNumber(SleepingGod, 99999)
SpecialMoves.set_description(SleepingGod,
                             "Foolishly pray that the All Powerful Sleeping God awakens from his endless slumber, and smites one's enemies with apocalyptic strength.")

def assignSpecials():

    firstroll = randrange(1,100)


    #NPC1
    if firstroll < 34:
        secondroll = randrange(1,9)
        # HolyStrike
        if secondroll == 1:
            PartyMember.set_SpecSlot1Name(NPC1, SpecialMoves.get_name(HolyStrike))
            PartyMember.set_SpecSlot1Cost(NPC1, SpecialMoves.get_cost(HolyStrike))
            PartyMember.set_SpecSlot1Damage(NPC1, SpecialMoves.get_damage(HolyStrike))
            PartyMember.set_SpecSlot1Prob(NPC1, SpecialMoves.get_probability(HolyStrike))
            PartyMember.set_SpecSlot1Desc(NPC1, SpecialMoves.get_description(HolyStrike))
            PartyMember.set_SpecSlot1Num(NPC1, SpecialMoves.get_indexNumber(HolyStrike))
        #IronMastery
        elif secondroll == 2:
            PartyMember.set_SpecSlot1Name(NPC1, SpecialMoves.get_name(IronMastery))
            PartyMember.set_SpecSlot1Cost(NPC1, SpecialMoves.get_cost(IronMastery))
            PartyMember.set_SpecSlot1Damage(NPC1, SpecialMoves.get_damage(IronMastery))
            PartyMember.set_SpecSlot1Prob(NPC1, SpecialMoves.get_probability(IronMastery))
            PartyMember.set_SpecSlot1Desc(NPC1, SpecialMoves.get_description(IronMastery))
            PartyMember.set_SpecSlot1Num(NPC1, SpecialMoves.get_indexNumber(IronMastery))
        # FireStrike
        elif secondroll == 3:
            PartyMember.set_SpecSlot1Name(NPC1, SpecialMoves.get_name(FireStrike))
            PartyMember.set_SpecSlot1Cost(NPC1, SpecialMoves.get_cost(FireStrike))
            PartyMember.set_SpecSlot1Damage(NPC1, SpecialMoves.get_damage(FireStrike))
            PartyMember.set_SpecSlot1Prob(NPC1, SpecialMoves.get_probability(FireStrike))
            PartyMember.set_SpecSlot1Desc(NPC1, SpecialMoves.get_description(FireStrike))
            PartyMember.set_SpecSlot1Num(NPC1, SpecialMoves.get_indexNumber(FireStrike))
        # WaterChain
        elif secondroll == 4:
            PartyMember.set_SpecSlot1Name(NPC1, SpecialMoves.get_name(WaterChain))
            PartyMember.set_SpecSlot1Cost(NPC1, SpecialMoves.get_cost(WaterChain))
            PartyMember.set_SpecSlot1Damage(NPC1, SpecialMoves.get_damage(WaterChain))
            PartyMember.set_SpecSlot1Prob(NPC1, SpecialMoves.get_probability(WaterChain))
            PartyMember.set_SpecSlot1Desc(NPC1, SpecialMoves.get_description(WaterChain))
            PartyMember.set_SpecSlot1Num(NPC1, SpecialMoves.get_indexNumber(WaterChain))
        # DemonMagic
        elif secondroll == 5:
            PartyMember.set_SpecSlot1Name(NPC1, SpecialMoves.get_name(DemonMagic))
            PartyMember.set_SpecSlot1Cost(NPC1, SpecialMoves.get_cost(DemonMagic))
            PartyMember.set_SpecSlot1Damage(NPC1, SpecialMoves.get_damage(DemonMagic))
            PartyMember.set_SpecSlot1Prob(NPC1, SpecialMoves.get_probability(DemonMagic))
            PartyMember.set_SpecSlot1Desc(NPC1, SpecialMoves.get_description(DemonMagic))
            PartyMember.set_SpecSlot1Num(NPC1, SpecialMoves.get_indexNumber(DemonMagic))
        # AnimalFamiliar
        elif secondroll == 6:
            PartyMember.set_SpecSlot1Name(NPC1, SpecialMoves.get_name(AnimalFamiliar))
            PartyMember.set_SpecSlot1Cost(NPC1, SpecialMoves.get_cost(AnimalFamiliar))
            PartyMember.set_SpecSlot1Damage(NPC1, SpecialMoves.get_damage(AnimalFamiliar))
            PartyMember.set_SpecSlot1Prob(NPC1, SpecialMoves.get_probability(AnimalFamiliar))
            PartyMember.set_SpecSlot1Desc(NPC1, SpecialMoves.get_description(AnimalFamiliar))
            PartyMember.set_SpecSlot1Num(NPC1, SpecialMoves.get_indexNumber(AnimalFamiliar))
        # PsychicBomb
        elif secondroll == 7:
            PartyMember.set_SpecSlot1Name(NPC1, SpecialMoves.get_name(PsychicBomb))
            PartyMember.set_SpecSlot1Cost(NPC1, SpecialMoves.get_cost(PsychicBomb))
            PartyMember.set_SpecSlot1Damage(NPC1, SpecialMoves.get_damage(PsychicBomb))
            PartyMember.set_SpecSlot1Prob(NPC1, SpecialMoves.get_probability(PsychicBomb))
            PartyMember.set_SpecSlot1Desc(NPC1, SpecialMoves.get_description(PsychicBomb))
            PartyMember.set_SpecSlot1Num(NPC1, SpecialMoves.get_indexNumber(PsychicBomb))
        # ShieldBash
        elif secondroll == 8:
            PartyMember.set_SpecSlot1Name(NPC1, SpecialMoves.get_name(ShieldBash))
            PartyMember.set_SpecSlot1Cost(NPC1, SpecialMoves.get_cost(ShieldBash))
            PartyMember.set_SpecSlot1Damage(NPC1, SpecialMoves.get_damage(ShieldBash))
            PartyMember.set_SpecSlot1Prob(NPC1, SpecialMoves.get_probability(ShieldBash))
            PartyMember.set_SpecSlot1Desc(NPC1, SpecialMoves.get_description(ShieldBash))
            PartyMember.set_SpecSlot1Num(NPC1, SpecialMoves.get_indexNumber(ShieldBash))
        # SleepingGod
        elif secondroll == 9:
            PartyMember.set_SpecSlot1Name(NPC1, SpecialMoves.get_name(SleepingGod))
            PartyMember.set_SpecSlot1Cost(NPC1, SpecialMoves.get_cost(SleepingGod))
            PartyMember.set_SpecSlot1Damage(NPC1, SpecialMoves.get_damage(SleepingGod))
            PartyMember.set_SpecSlot1Prob(NPC1, SpecialMoves.get_probability(SleepingGod))
            PartyMember.set_SpecSlot1Desc(NPC1, SpecialMoves.get_description(SleepingGod))
            PartyMember.set_SpecSlot1Num(NPC1, SpecialMoves.get_indexNumber(SleepingGod))
    # NPC2
    elif firstroll > 65:
        secondroll = randrange(1, 100)
        # HolyStrike
        if 0 <= secondroll <= 11:
            PartyMember.set_SpecSlot1Name(NPC2, SpecialMoves.get_name(HolyStrike))
            PartyMember.set_SpecSlot1Cost(NPC2, SpecialMoves.get_cost(HolyStrike))
            PartyMember.set_SpecSlot1Damage(NPC2, SpecialMoves.get_damage(HolyStrike))
            PartyMember.set_SpecSlot1Prob(NPC2, SpecialMoves.get_probability(HolyStrike))
            PartyMember.set_SpecSlot1Desc(NPC2, SpecialMoves.get_description(HolyStrike))
            PartyMember.set_SpecSlot1Num(NPC2, SpecialMoves.get_indexNumber(HolyStrike))
        # IronMastery
        elif 12 <= secondroll <= 23:
            PartyMember.set_SpecSlot1Name(NPC2, SpecialMoves.get_name(IronMastery))
            PartyMember.set_SpecSlot1Cost(NPC2, SpecialMoves.get_cost(IronMastery))
            PartyMember.set_SpecSlot1Damage(NPC2, SpecialMoves.get_damage(IronMastery))
            PartyMember.set_SpecSlot1Prob(NPC2, SpecialMoves.get_probability(IronMastery))
            PartyMember.set_SpecSlot1Desc(NPC2, SpecialMoves.get_description(IronMastery))
            PartyMember.set_SpecSlot1Num(NPC2, SpecialMoves.get_indexNumber(IronMastery))
        # FireStrike
        elif 24 <= secondroll <= 35:
            PartyMember.set_SpecSlot1Name(NPC2, SpecialMoves.get_name(FireStrike))
            PartyMember.set_SpecSlot1Cost(NPC2, SpecialMoves.get_cost(FireStrike))
            PartyMember.set_SpecSlot1Damage(NPC2, SpecialMoves.get_damage(FireStrike))
            PartyMember.set_SpecSlot1Prob(NPC2, SpecialMoves.get_probability(FireStrike))
            PartyMember.set_SpecSlot1Desc(NPC2, SpecialMoves.get_description(FireStrike))
            PartyMember.set_SpecSlot1Num(NPC2, SpecialMoves.get_indexNumber(FireStrike))
        # WaterChain
        elif 36 <= secondroll <= 47:
            PartyMember.set_SpecSlot1Name(NPC2, SpecialMoves.get_name(WaterChain))
            PartyMember.set_SpecSlot1Cost(NPC2, SpecialMoves.get_cost(WaterChain))
            PartyMember.set_SpecSlot1Damage(NPC2, SpecialMoves.get_damage(WaterChain))
            PartyMember.set_SpecSlot1Prob(NPC2, SpecialMoves.get_probability(WaterChain))
            PartyMember.set_SpecSlot1Desc(NPC2, SpecialMoves.get_description(WaterChain))
            PartyMember.set_SpecSlot1Num(NPC2, SpecialMoves.get_indexNumber(WaterChain))
        # DemonMagic
        elif 48 <= secondroll <= 59:
            PartyMember.set_SpecSlot1Name(NPC2, SpecialMoves.get_name(DemonMagic))
            PartyMember.set_SpecSlot1Cost(NPC2, SpecialMoves.get_cost(DemonMagic))
            PartyMember.set_SpecSlot1Damage(NPC2, SpecialMoves.get_damage(DemonMagic))
            PartyMember.set_SpecSlot1Prob(NPC2, SpecialMoves.get_probability(DemonMagic))
            PartyMember.set_SpecSlot1Desc(NPC2, SpecialMoves.get_description(DemonMagic))
            PartyMember.set_SpecSlot1Num(NPC2, SpecialMoves.get_indexNumber(DemonMagic))
        # AnimalFamiliar
        elif 60 <= secondroll <= 71:
            PartyMember.set_SpecSlot1Name(NPC2, SpecialMoves.get_name(AnimalFamiliar))
            PartyMember.set_SpecSlot1Cost(NPC2, SpecialMoves.get_cost(AnimalFamiliar))
            PartyMember.set_SpecSlot1Damage(NPC2, SpecialMoves.get_damage(AnimalFamiliar))
            PartyMember.set_SpecSlot1Prob(NPC2, SpecialMoves.get_probability(AnimalFamiliar))
            PartyMember.set_SpecSlot1Desc(NPC2, SpecialMoves.get_description(AnimalFamiliar))
            PartyMember.set_SpecSlot1Num(NPC2, SpecialMoves.get_indexNumber(AnimalFamiliar))
        # PsychicBomb
        elif 72 <= secondroll <= 83:
            PartyMember.set_SpecSlot1Name(NPC2, SpecialMoves.get_name(PsychicBomb))
            PartyMember.set_SpecSlot1Cost(NPC2, SpecialMoves.get_cost(PsychicBomb))
            PartyMember.set_SpecSlot1Damage(NPC2, SpecialMoves.get_damage(PsychicBomb))
            PartyMember.set_SpecSlot1Prob(NPC2, SpecialMoves.get_probability(PsychicBomb))
            PartyMember.set_SpecSlot1Desc(NPC2, SpecialMoves.get_description(PsychicBomb))
            PartyMember.set_SpecSlot1Num(NPC2, SpecialMoves.get_indexNumber(PsychicBomb))
        # ShieldBash
        elif 84 <= secondroll <= 92:
            PartyMember.set_SpecSlot1Name(NPC2, SpecialMoves.get_name(ShieldBash))
            PartyMember.set_SpecSlot1Cost(NPC2, SpecialMoves.get_cost(ShieldBash))
            PartyMember.set_SpecSlot1Damage(NPC2, SpecialMoves.get_damage(ShieldBash))
            PartyMember.set_SpecSlot1Prob(NPC2, SpecialMoves.get_probability(ShieldBash))
            PartyMember.set_SpecSlot1Desc(NPC2, SpecialMoves.get_description(ShieldBash))
            PartyMember.set_SpecSlot1Num(NPC2, SpecialMoves.get_indexNumber(ShieldBash))
        # SleepingGod
        elif 93 <= secondroll <= 100:
            PartyMember.set_SpecSlot1Name(NPC2, SpecialMoves.get_name(SleepingGod))
            PartyMember.set_SpecSlot1Cost(NPC2, SpecialMoves.get_cost(SleepingGod))
            PartyMember.set_SpecSlot1Damage(NPC2, SpecialMoves.get_damage(SleepingGod))
            PartyMember.set_SpecSlot1Prob(NPC2, SpecialMoves.get_probability(SleepingGod))
            PartyMember.set_SpecSlot1Desc(NPC2, SpecialMoves.get_description(SleepingGod))
            PartyMember.set_SpecSlot1Num(NPC2, SpecialMoves.get_indexNumber(SleepingGod))

    # NPC3
    else:
        secondroll = randrange(1, 100)
        # HolyStrike
        if 0 <= secondroll <= 11:
            PartyMember.set_SpecSlot1Name(NPC3, SpecialMoves.get_name(HolyStrike))
            PartyMember.set_SpecSlot1Cost(NPC3, SpecialMoves.get_cost(HolyStrike))
            PartyMember.set_SpecSlot1Damage(NPC3, SpecialMoves.get_damage(HolyStrike))
            PartyMember.set_SpecSlot1Prob(NPC3, SpecialMoves.get_probability(HolyStrike))
            PartyMember.set_SpecSlot1Desc(NPC3, SpecialMoves.get_description(HolyStrike))
            PartyMember.set_SpecSlot1Num(NPC3, SpecialMoves.get_indexNumber(HolyStrike))
        # IronMastery
        elif 12 <= secondroll <= 23:
            PartyMember.set_SpecSlot1Name(NPC3, SpecialMoves.get_name(IronMastery))
            PartyMember.set_SpecSlot1Cost(NPC3, SpecialMoves.get_cost(IronMastery))
            PartyMember.set_SpecSlot1Damage(NPC3, SpecialMoves.get_damage(IronMastery))
            PartyMember.set_SpecSlot1Prob(NPC3, SpecialMoves.get_probability(IronMastery))
            PartyMember.set_SpecSlot1Desc(NPC3, SpecialMoves.get_description(IronMastery))
            PartyMember.set_SpecSlot1Num(NPC3, SpecialMoves.get_indexNumber(IronMastery))
        # FireStrike
        elif 24 <= secondroll <= 35:
            PartyMember.set_SpecSlot1Name(NPC3, SpecialMoves.get_name(FireStrike))
            PartyMember.set_SpecSlot1Cost(NPC3, SpecialMoves.get_cost(FireStrike))
            PartyMember.set_SpecSlot1Damage(NPC3, SpecialMoves.get_damage(FireStrike))
            PartyMember.set_SpecSlot1Prob(NPC3, SpecialMoves.get_probability(FireStrike))
            PartyMember.set_SpecSlot1Desc(NPC3, SpecialMoves.get_description(FireStrike))
            PartyMember.set_SpecSlot1Num(NPC3, SpecialMoves.get_indexNumber(FireStrike))
        # WaterChain
        elif 36 <= secondroll <= 47:
            PartyMember.set_SpecSlot1Name(NPC3, SpecialMoves.get_name(WaterChain))
            PartyMember.set_SpecSlot1Cost(NPC3, SpecialMoves.get_cost(WaterChain))
            PartyMember.set_SpecSlot1Damage(NPC3, SpecialMoves.get_damage(WaterChain))
            PartyMember.set_SpecSlot1Prob(NPC3, SpecialMoves.get_probability(WaterChain))
            PartyMember.set_SpecSlot1Desc(NPC3, SpecialMoves.get_description(WaterChain))
            PartyMember.set_SpecSlot1Num(NPC3, SpecialMoves.get_indexNumber(WaterChain))
        # DemonMagic
        elif 48 <= secondroll <= 59:
            PartyMember.set_SpecSlot1Name(NPC3, SpecialMoves.get_name(DemonMagic))
            PartyMember.set_SpecSlot1Cost(NPC3, SpecialMoves.get_cost(DemonMagic))
            PartyMember.set_SpecSlot1Damage(NPC3, SpecialMoves.get_damage(DemonMagic))
            PartyMember.set_SpecSlot1Prob(NPC3, SpecialMoves.get_probability(DemonMagic))
            PartyMember.set_SpecSlot1Desc(NPC3, SpecialMoves.get_description(DemonMagic))
            PartyMember.set_SpecSlot1Num(NPC3, SpecialMoves.get_indexNumber(DemonMagic))
        # AnimalFamiliar
        elif 60 <= secondroll <= 71:
            PartyMember.set_SpecSlot1Name(NPC3, SpecialMoves.get_name(AnimalFamiliar))
            PartyMember.set_SpecSlot1Cost(NPC3, SpecialMoves.get_cost(AnimalFamiliar))
            PartyMember.set_SpecSlot1Damage(NPC3, SpecialMoves.get_damage(AnimalFamiliar))
            PartyMember.set_SpecSlot1Prob(NPC3, SpecialMoves.get_probability(AnimalFamiliar))
            PartyMember.set_SpecSlot1Desc(NPC3, SpecialMoves.get_description(AnimalFamiliar))
            PartyMember.set_SpecSlot1Num(NPC3, SpecialMoves.get_indexNumber(AnimalFamiliar))
        # PsychicBomb
        elif 72 <= secondroll <= 83:
            PartyMember.set_SpecSlot1Name(NPC3, SpecialMoves.get_name(PsychicBomb))
            PartyMember.set_SpecSlot1Cost(NPC3, SpecialMoves.get_cost(PsychicBomb))
            PartyMember.set_SpecSlot1Damage(NPC3, SpecialMoves.get_damage(PsychicBomb))
            PartyMember.set_SpecSlot1Prob(NPC3, SpecialMoves.get_probability(PsychicBomb))
            PartyMember.set_SpecSlot1Desc(NPC3, SpecialMoves.get_description(PsychicBomb))
            PartyMember.set_SpecSlot1Num(NPC3, SpecialMoves.get_indexNumber(PsychicBomb))
        # ShieldBash
        elif 84 <= secondroll <= 92:
            PartyMember.set_SpecSlot1Name(NPC3, SpecialMoves.get_name(ShieldBash))
            PartyMember.set_SpecSlot1Cost(NPC3, SpecialMoves.get_cost(ShieldBash))
            PartyMember.set_SpecSlot1Damage(NPC3, SpecialMoves.get_damage(ShieldBash))
            PartyMember.set_SpecSlot1Prob(NPC3, SpecialMoves.get_probability(ShieldBash))
            PartyMember.set_SpecSlot1Desc(NPC3, SpecialMoves.get_description(ShieldBash))
            PartyMember.set_SpecSlot1Num(NPC3, SpecialMoves.get_indexNumber(ShieldBash))
        # SleepingGod
        elif 93 <= secondroll <= 100:
            PartyMember.set_SpecSlot1Name(NPC3, SpecialMoves.get_name(SleepingGod))
            PartyMember.set_SpecSlot1Cost(NPC3, SpecialMoves.get_cost(SleepingGod))
            PartyMember.set_SpecSlot1Damage(NPC3, SpecialMoves.get_damage(SleepingGod))
            PartyMember.set_SpecSlot1Prob(NPC3, SpecialMoves.get_probability(SleepingGod))
            PartyMember.set_SpecSlot1Desc(NPC3, SpecialMoves.get_description(SleepingGod))
            PartyMember.set_SpecSlot1Num(NPC3, SpecialMoves.get_indexNumber(SleepingGod))





def stageSelect():

    possibleNames = ["The Dry Desert", "Haunted Mansion", "Temple of the Blood Witch", "Haunted Village", "Temple of the Raven God", "Temple of the Four Horned Stag", "Temple of the Mad Toad King", "Goulcrest Mansion", "a Wizard's Hut", "Taewe Jungle", "The Krosstoen Plains", "Ancient Ruins","Elven Ruins", "an Orc Warcamp", "a Dwarven Tunnelhead", "Dry Gulch Village" , "The Industrial District", "Red Hawk Villa",  "The Swampy Marshes", "The Pitch Black Caverns", "The Ruined Castle", "The Village Outskirts", "The Lord's Manor", "The Caravan", "Castle Ramparts", "Castle of the God King", "Swamp of the Mad Witch", ]
    stageName = choice(possibleNames)
    possibleDesc = ["A furious wind blows through the area, tearing at your armours and biting at your faces.",
                    "A strange moonlight peers in from above, an ominous omen if there ever was one.",
                    "An unfriendly pile of skeletons leer and guffaw at you from the distance, picking their teeth with daggers.",
                    "A calm ocean breeze pours in from the distance.", "The cold chills your bones, making you shiver and yearn for warmth.",
                    "The heat is unbearable, you sweat profusely and claw at your armour.",
                    "The night suffocates you as bats circle above and make terrible, wheezing noises, drawing closer.",
                    "A furious sun burns hot into your flesh from above, like an angered God.",
                    "A nearby body of water sends a breezy salt air through the area.",
                    "A premonition tells you this battle is of great consequence.",
                    "Your stomach turns at the sight of your surroundings.",
                    "You find your surroundings encouraging.",
                    "A thick mist envelops your surroundings.",
                    "Night refuses to break unto morn as eternal shadows threaten the land.",
                    "Witches cackle in the distance.",
                    "You feel far away from your Gods on this day.",
                    "You feel your Gods close to your heart on this day.",
                    "Smoke billows over the skies from nearby pillaging.",
                    "A noble Lord's camp in the nearby hills looks on at your plight with indifference.",

                    "These lands belong to the Sarris Kingdom.",
                    "These lands belong to the Valmaer Empire.",
                    "These lands belong to the Erro Dynasty.",
                    "These lands belong to the Aslam Caliphate.",
                    "These lands belong to the Sarris Kingdom.",
                    "These lands belong to the Valmaer Empire.",
                    "These lands belong to the Erro Dynasty.",
                    "These lands belong to the Aslam Caliphate.",


                    "This area seems to be of little significance at all.",
                    "There isn't much of note here.",
                    "This area seems to be of little significance at all.",
                    "There isn't much of note here.",
                    "This area seems to be of little significance at all.",
                    "There isn't much of note here.",
                    "This area seems to be of little significance at all.",
                    "There isn't much of note here.",
                    "This area seems to be of little significance at all.",
                    "There isn't much of note here.",
                    "This area seems to be of little significance at all.",
                    "There isn't much of note here.",
                    "This area seems to be of little significance at all.",
                    "There isn't much of note here.",
                    "This area seems to be of little significance at all.",
                    "There isn't much of note here.",
                    "This area seems to be of little significance at all.",
                    "There isn't much of note here.",
                    "This area seems to be of little significance at all.",
                    "There isn't much of note here.",
                    "This area seems to be of little significance at all.",
                    "There isn't much of note here.",
                    "This area seems to be of little significance at all.",
                    "There isn't much of note here.",
                    ]

    stageDesc = choice(possibleDesc)
    Stage.set_name(TestStage1, stageName)
    Stage.set_description(TestStage1, stageDesc)
    stageSetNum = Enemy.get_NumberOfKills(TestEnemy) + 1
    Stage.set_number(TestStage1, stageSetNum)






######################
##
## INITIATIVE AND INTRO LOOP
##
######################
def DescripAndInit():

    stageSelect()

    BattleTurn = 1
    #TestEnemy = Enemy()
    time.sleep(2)
    clear()

    possibleContinents = ["Faldria", "Luwhium", "Prules", "Eshye", "Ashain", "Lastrela", "Jaskotho"]
    rolledContinent = choice(possibleContinents)
    print(PlayerCharacter.get_name(PC) + " and a band of companions arrive to their destination after weeks of travel across the lands of " + rolledContinent + ".")
    time.sleep(2)
    print("\nFinally, " + PlayerCharacter.get_name(PC) + "'s band arrived to " + Stage.get_name(TestStage1) + ".")
    time.sleep(2)
    print("\n" + Stage.get_description(TestStage1))
    time.sleep(2)



    print("\n(Press enter to continue)")
    key = input("")
    if key != "`":
        time.sleep(2)
        clear()
        print(".......")
        time.sleep(1)
        print("               ........")
        time.sleep(1)
        print("      .........")
        time.sleep(1)
        clear()
        print("What's that!? An enemy approaches!!")
        print("\n(Press enter to continue)")
        key = input("")
        if key != "`":
            clear()
            enemyName = Enemy.get_name(TestEnemy)
            enemyPers = Enemy.get_Personality(TestEnemy)
            enemyOmen = Enemy.get_Omen(TestEnemy)
            enemyInit = Enemy.get_Initiative(TestEnemy)
            rollenemyInit = randrange(1,3)
            newenemyInit = enemyInit + rollenemyInit

            Enemy.set_Initiative(TestEnemy, newenemyInit)

            print("You are confronted by: \n")

            print("Enemy: " + Enemy.get_name(TestEnemy) + " " + Enemy.get_Personality(TestEnemy) + Enemy.get_Omen(
                TestEnemy))
            if Enemy.get_EnemyClass(TestEnemy) != "None":
                print("Class: " + Enemy.get_EnemyClass(TestEnemy))
            print("Health: " + str(Enemy.get_Health(TestEnemy)) + "/" + str(Enemy.get_MaxHealth(TestEnemy)))
            print("Armour Class: " + str(Enemy.get_ArmourClass(TestEnemy)))
            print("Accuracy: " + str(Enemy.get_EnemyAccuracy(TestEnemy)) + "\nBonus Damage: " + str(
                Enemy.get_EnemyDamage(TestEnemy)))

            time.sleep(7)
            #print("\n" + enemyName + " rolls a " + str(newenemyInit) + " for initiative.")
            #print("\n(Press enter to roll initiative for " + PlayerCharacter.get_name(PC) + ".)" )

            initRoll = randrange(1,20)
            initDexModifier = PlayerCharacter.get_Dexterity(PC) / 4
            initRollTotal = initRoll + initDexModifier
            initRollTotal = round(initRollTotal)
            #print("\n" + PlayerCharacter.get_name(PC) + " rolled a " + str(initRoll) + ", with a Dexterity modifier of +" + str(round(initDexModifier)) + ". (" + str(initRollTotal) + ")")
            #clear()
            #print("\nINITIATIVE")
            #print("\nEnemy: " + str(enemyInit) + "      PC: " + str(initRollTotal))
            #print("\n(Press enter to roll initiative for the party members)")


            PartyinitRoll = randrange(1,20)
            PartyinitModifier = randrange(-1,4)
            PartyinitTotal = PartyinitModifier + PartyinitRoll
            PartyinitSplit = PartyinitTotal / 5
            #print("\nThe other party members rolled a " + str(PartyinitRoll) + ", with a Fate modifier of " + str(PartyinitModifier)  + ". (" + str(PartyinitTotal) + ")")
            clear()


                    #print("\nINITIATIVE RESULTS")
                    #print("Enemy: " + enemyInit)
                    #print("PC: " + str(round(initRollTotal)))
                    #print("Party Members: " + str(PartyinitTotal))
                    #print("\n\nPlease select an option: ")
                    #print("1. Use PC Initiative (" + str(round(initRollTotal)) + ")")
                    #print("2. Use Party Members Initiative (" + str(PartyinitTotal) + ")")
                    #print("3. Split Party Members Initiative and Add to PC Initiative (" + str(initRollTotal) + " + " + str(PartyinitSplit) + ")")
                    #print("\n")
                    #key = input("")
                    #if key == "1":
                    #    PlayerCharacter.set_Initiative(PC, initRollTotal)
                    #    InitiativeCheck()
                    #if key == "2":
                    #    PlayerCharacter.set_Initiative(PC, PartyinitTotal)
                    #    InitiativeCheck()
                    #if key == "3":
                    #    addedInit = initRollTotal + PartyinitSplit
                    #    PlayerCharacter.set_Initiative(PC, addedInit)
                    #    InitiativeCheck()
                    #else:
                    #    print("Sorry, wrong input. ERR1")
                    #    PlayerCharacter.set_Initiative(PC, initRollTotal)
                    #    InitiativeCheck()
                #else#:
                 #       initgen = randrange(1,20) + randrange(1,4)
                  #      PlayerCharacter.set_Initiative((PC, initgen))
                   #     print("ERR2. Continuing")
                    #    time.sleep(2)
                     #   InitiativeCheck()

            InitiativeCheck()



def InitiativeCheck():


    if PlayerCharacter.get_Initiative(PC) > Enemy.get_Initiative(TestEnemy):
        clear()
        print("Player wins initiative.")
        time.sleep(1)
        print("Beginning combat...")
        time.sleep(3)
        GenericPCPhase()
    # if PC wins, give them a round to go first
    else:
        clear()
        print("Enemy wins initiative.")
        time.sleep(1)
        print("Beginning combat...")
        time.sleep(3)
    # if PC loses, do nothing and go to "Core" loop -- which Enemy goes first in by default
    CoreBattleLoopTest()




def CoreBattleLoopTest():



    clear()
    #print("(CoreBattleLoopTest)")
    time.sleep(3)
    clear()
    while PlayerCharacter.get_Health(PC) > 1 and Enemy.get_Health(TestEnemy) > 1:
        GenericEnemyPhase()
        GenericPCPhase()
        stageConditions()
    else:
        if PlayerCharacter.get_Health(PC) < 1:
            clear()
            BattleStatus()
            #print("PC has died in CoreBattleLoopTest!")
            time.sleep(2)
            playerDied()
        if Enemy.get_Health(TestEnemy) < 1:
            clear()
            BattleStatus()
            #print("Enemy has died in CoreBattleLoopTest!")
            time.sleep(2)
            enemyDied()









def playerDied():



    print("\n\n     GAME OVER       ")
    CurrentStage = Stage.get_number(TestStage1)
    print("\n\nYou were slain by " + Enemy.get_name(TestEnemy) + " in Stage " + str(CurrentStage) + " on Turn " + str(Enemy.get_BattleTurn(TestEnemy)) + ".")
    partyHealth =  PartyMember.get_Health(NPC1) + PartyMember.get_Health(NPC2) + PartyMember.get_Health(NPC3)
    enemyHealth = Enemy.get_Health(TestEnemy)
    time.sleep(3)
    print("\nYou died with " + str(PlayerCharacter.get_Gold(PC)) + " gold.")
    time.sleep(5)
    if partyHealth > enemyHealth:
        print("\nYour party survives, fleeing to the nearest civilization and telling tales of your glory.")
    else:
        print("\nYour party dies shortly after you, leaving naught but bones and rusting armour in your memory.")
    print("\n")
    time.sleep(5)
    print("Press enter to return to the Main Menu.")
    key = input("")
    if key != "`":
        MainMenu()
    else:
        MainMenu()



def dropGoldAndBlood():
    rollTable = randrange(1, 10)
    stageNumMod = 75
    if rollTable < 8:
        goldDrop = randrange(1, 100) + randrange(1, 100) + randrange(1, 100) + randrange(1, 100) + (stageNumMod * Stage.get_number(TestStage1))
        newGold = PlayerCharacter.get_Gold(PC) + goldDrop
        PlayerCharacter.set_Gold(PC, newGold)
        print(Enemy.get_name(TestEnemy) + " drops " + str(goldDrop) + " gold!")
        time.sleep(2)
    elif rollTable == 8:
        goldDrop = randrange(1, 200) + randrange(1, 200) + randrange(1, 200) + randrange(1, 200) + (stageNumMod * Stage.get_number(TestStage1))
        newGold = PlayerCharacter.get_Gold(PC) + goldDrop
        PlayerCharacter.set_Gold(PC, newGold)
        print(Enemy.get_name(TestEnemy) + " drops " + str(goldDrop) + " gold!")
        time.sleep(2)
    elif rollTable == 9:
        goldDrop = randrange(1, 300) + randrange(1, 300) + randrange(1, 300) + randrange(1, 300) + (stageNumMod * Stage.get_number(TestStage1))
        newGold = PlayerCharacter.get_Gold(PC) + goldDrop
        PlayerCharacter.set_Gold(PC, newGold)
        print(Enemy.get_name(TestEnemy) + " drops " + str(goldDrop) + " gold!")
        time.sleep(2)
    else:
        goldDrop = randrange(1, 400) + randrange(1, 400) + randrange(1, 400) + randrange(1, 400) + (stageNumMod * Stage.get_number(TestStage1))
        newGold = PlayerCharacter.get_Gold(PC) + goldDrop
        PlayerCharacter.set_Gold(PC, newGold)
        print(Enemy.get_name(TestEnemy) + " drops " + str(goldDrop) + " gold!")
        time.sleep(2)

    rollTable2 = randrange(1, 10)
    if rollTable2 < 8:
        bloodDrop = randrange(1, 100) + randrange(1, 100) + randrange(1, 100) + randrange(1, 100) + (75 * Stage.get_number(TestStage1))
        newBlood = PlayerCharacter.get_Blood(PC) + bloodDrop
        PlayerCharacter.set_Blood(PC, newBlood)
        print(Enemy.get_name(TestEnemy) + " spills " + str(bloodDrop) + " blood!")
        time.sleep(2)
    elif rollTable2 == 8:
        bloodDrop = randrange(1, 200) + randrange(1, 200) + randrange(1, 200) + randrange(1, 200) + (75 * Stage.get_number(TestStage1))
        newBlood = PlayerCharacter.get_Blood(PC) + bloodDrop
        PlayerCharacter.set_Blood(PC, newBlood)
        print(Enemy.get_name(TestEnemy) + " spills " + str(bloodDrop) + " blood!")
        time.sleep(2)
    elif rollTable2 == 9:
        bloodDrop = randrange(1, 300) + randrange(1, 300) + randrange(1, 300) + randrange(1, 300) + (75 * Stage.get_number(TestStage1))
        newBlood = PlayerCharacter.get_Blood(PC) + bloodDrop
        PlayerCharacter.set_Blood(PC, newBlood)
        print(Enemy.get_name(TestEnemy) + " spills " + str(bloodDrop) + " blood!")
        time.sleep(2)
    else:
        bloodDrop = randrange(1, 400) + randrange(1, 400) + randrange(1, 400) + randrange(1, 400) + (75 * Stage.get_number(TestStage1))
        newBlood = PlayerCharacter.get_Blood(PC) + bloodDrop
        PlayerCharacter.set_Blood(PC, newBlood)
        print(Enemy.get_name(TestEnemy) + " spills " + str(bloodDrop) + " blood!")
        time.sleep(2)

def enemyDied():



    newvalue = Enemy.get_NumberOfKills(TestEnemy) + 1
    Enemy.set_NumberOfKills(TestEnemy, newvalue)
    recordSlainEnemies()
    stagenum = Enemy.get_Stage(TestEnemy)
    time.sleep(4)
    clear()
    BattleStatus()
    print("\n")
    print("                STAGE CLEARED!       ")
    print("\n\nYour Party slayed " + Enemy.get_name(TestEnemy) + " in Stage " + str(newvalue) + " on Turn " + str(Enemy.get_BattleTurn(TestEnemy)) + ".")
    time.sleep(5)

    dropGoldAndBlood()

    print("\n(Press any key to continue)")
    key = input("")
    if key != "`":
        clear()
        LobbyStatus()
        time.sleep(3)
        if PlayerCharacter.get_Health(PC) < PlayerCharacter.get_MaxHealth(PC) or PartyMember.get_Health(NPC1) < PartyMember.get_MaxHealth(NPC1) or PartyMember.get_Health(NPC2) < PartyMember.get_MaxHealth(NPC2) or PartyMember.get_Health(NPC3) < PartyMember.get_MaxHealth(NPC3):
            print("You bandage your wounds with light supplies, but it's only a quick fix. ")
            time.sleep(3)
            rolls = 3
            total = 0
            while rolls > 1:
                rolldice = randrange(1, 20)
                total += rolldice
                rolls = rolls - 1

            levelmod = Stage.get_number(TestStage1) * 3

            total = total + levelmod


            if total + PlayerCharacter.get_Health(PC) >= PlayerCharacter.get_MaxHealth(PC):
                PlayerCharacter.set_Health(PC, PlayerCharacter.get_MaxHealth(PC))
            else:
                newPChealth = PlayerCharacter.get_Health(PC) + total
                PlayerCharacter.set_Health(PC, newPChealth)

            if total + PartyMember.get_Health(NPC1) >= PartyMember.get_MaxHealth(NPC1):
                PartyMember.set_Health(NPC1, PartyMember.get_MaxHealth(NPC1))
            else:
                NPC1health = PartyMember.get_Health(NPC1) + total
                PartyMember.set_Health(NPC1, NPC1health)
            if total + PartyMember.get_Health(NPC2) >= PartyMember.get_MaxHealth(NPC2):
                PartyMember.set_Health(NPC2, PartyMember.get_MaxHealth(NPC2))
            else:
                NPC2health = PartyMember.get_Health(NPC2) + total
                PartyMember.set_Health(NPC2, NPC2health)
            if total + PartyMember.get_Health(NPC3) >= PartyMember.get_MaxHealth(NPC3):
                PartyMember.set_Health(NPC3, PartyMember.get_MaxHealth(NPC3))
            else:
                NPC3health = PartyMember.get_Health(NPC3) + total
                PartyMember.set_Health(NPC3, NPC3health)
            clear()
            LobbyStatus()
            time.sleep(1)
            print("PC and Party Members are each healed for " + str(total) + " Health.")
            time.sleep(4)
        else:
            print("No need to bandage wounds, everyone is healthy.")
            time.sleep(3)
        clear()
        LobbyStatus()
        time.sleep(2)
        recoveredSP = randrange(1,3) + randrange(1,3)
        print("You gain " + str(recoveredSP) + " Special Points.")
        newSP = PlayerCharacter.get_SpecialPoints(PC) + recoveredSP
        PlayerCharacter.set_SpecialPoints(PC, newSP)
        time.sleep(4)
        clear()
        LobbyStatus()
        time.sleep(2)
        levelUp()

    else:
        levelUp()







    #print("\n")
    #time.sleep(2)
    #print("Press enter to return to the Main Menu.")
    #key = input("")
    #if key != "`":
    #    MainMenu()
    #else:
    #    MainMenu()




def buffEnemy():
    Enemy.reset(TestEnemy)

    newEnemyHealth = Enemy.get_Health(TestEnemy) + randrange(10,35) * Enemy.get_NumberOfKills(TestEnemy)
    Enemy.set_Health(TestEnemy, newEnemyHealth)

    enemyMaxHealth = Enemy.get_Health(TestEnemy)
    Enemy.set_MaxHealth(TestEnemy, enemyMaxHealth)


    enemyInit = int(Enemy.get_Initiative(TestEnemy))
    newInit = enemyInit + 1
    Enemy.set_Initiative(TestEnemy, newInit)

    newEnemyArmourClass = Enemy.get_ArmourClass(TestEnemy) + Enemy.get_NumberOfKills(TestEnemy)
    Enemy.set_ArmourClass(TestEnemy, newEnemyArmourClass)

    newEnemyDamage = Enemy.get_EnemyDamage(TestEnemy) + randrange(1, 3) + Enemy.get_NumberOfKills(TestEnemy) + Enemy.get_NumberOfKills(TestEnemy) + Enemy.get_NumberOfKills(TestEnemy)
    Enemy.set_EnemyDamage(TestEnemy, newEnemyDamage)

    newEnemyAccuracy = Enemy.get_EnemyAccuracy(TestEnemy) + randrange(1, 3) + Enemy.get_NumberOfKills(TestEnemy) + Enemy.get_NumberOfKills(TestEnemy)
    Enemy.set_EnemyAccuracy(TestEnemy, newEnemyAccuracy)


    Enemy.set_BattleTurn(TestEnemy, 0)



def GoldVictory():
    clear()
    LobbyStatus()
    print("\n\n     Congratulations! You earned enough gold to retire, with " + str(PlayerCharacter.get_Gold(PC)) + " coins to your name.\n     You and your friends live out the rest of your days in comfort.")
    time.sleep(20)
    key = input("")
    if key != "`":
        time.sleep(1)
        MainMenu()
    else:
        time.sleep(1)
        MainMenu()


def BloodVictory():
    clear()
    LobbyStatus()
    print("\n\n     Congratulations! You spilled enough blood to ascend, with " + str(PlayerCharacter.get_Gold(PC)) + " blood spilled in your wake.\n     You and your friends live out the rest of your days in glory.")
    time.sleep(20)
    key = input("")
    if key != "`":
        time.sleep(1)
        MainMenu()
    else:
        time.sleep(1)
        MainMenu()

def WinConditionCheck():
    gold = PlayerCharacter.get_Gold(PC)
    blood = PlayerCharacter.get_Blood(PC)
    needgold = 10000 - gold
    needblood = 10000 - blood
    if gold > 10000:
        GoldVictory()
    elif blood > 10000:
        BloodVictory()
    else:
        clear()
        LobbyStatus()
        time.sleep(1)
        print("You need " + str(needgold) + " gold for a Gold Victory, or " + str(needblood) + " blood for a Blood Victory.")
        time.sleep(3)
        print("\n(Press enter to continue)")
        key = input("")
        if key != "`":
            time.sleep(1)
        else:
            time.sleep(1)



def SavePCtoPCSave():
    PCNameSave = PlayerCharacter.get_name(PC)
    PCNameSaveDump = pickle.dump(PCNameSave, open("Save File", "wb"))
    print("\nSaving....")
    time.sleep(3)



def preBattle():


    SavePCtoPCSave()

    WinConditionCheck()

    clear()
    LobbyStatus()
    time.sleep(2)
    print("You prepare to depart for another battle...")
    time.sleep(5)
    # RESET TESTENEMY
    # RESET STAGE (EXCEPT NUMBER)
    # RESET ENEMY.BATTLETURNS 0
    StageNum = Stage.get_number(TestStage1) + 1
    Enemy.reset(TestEnemy)
    stageSelect()
    buffEnemy()



    randomEncounter()

    clear()
    LobbyStatus()
    print("\n(Press any key to depart)")
    key = input("")
    if key != "`":
        DescripAndInit()
    else:
        DescripAndInit()




def recordSlainEnemies():
    string1 = Enemy.get_name(TestEnemy)
    string2 = Enemy.get_Personality(TestEnemy)
    string3 = Enemy.get_Omen(TestEnemy)
    fulltitle = string1 + " " + string2 + " " + string3
    existingSlainList = []
    existingSlainList.append(str(PlayerCharacter.get_SlainEnemies(PC)))


    existingSlainList.append(fulltitle)
    PlayerCharacter.set_SlainEnemies(PC, existingSlainList)







def campfireHeal():
    rolls = 10
    total = 50
    while rolls > 1:
        rolldice = randrange(1, 10)
        total += rolldice
        rolls = rolls - 1
    clear()
    LobbyStatus()
    print("Everyone is healed for " + str(total) + " Health.")
    time.sleep(3)

    if total + PlayerCharacter.get_Health(PC) >= PlayerCharacter.get_MaxHealth(PC):
        PlayerCharacter.set_Health(PC, PlayerCharacter.get_MaxHealth(PC))
    else:
        newPChealth = PlayerCharacter.get_Health(PC) + total
        PlayerCharacter.set_Health(PC, newPChealth)

    if total + PartyMember.get_Health(NPC1) >= PartyMember.get_MaxHealth(NPC1):
        PartyMember.set_Health(NPC1, PartyMember.get_MaxHealth(NPC1))
    else:
        NPC1health = PartyMember.get_Health(NPC1) + total
        PartyMember.set_Health(NPC1, NPC1health)
    if total + PartyMember.get_Health(NPC2) >= PartyMember.get_MaxHealth(NPC2):
        PartyMember.set_Health(NPC2, PartyMember.get_MaxHealth(NPC2))
    else:
        NPC2health = PartyMember.get_Health(NPC2) + total
        PartyMember.set_Health(NPC2, NPC2health)
    if total + PartyMember.get_Health(NPC3) >= PartyMember.get_MaxHealth(NPC3):
        PartyMember.set_Health(NPC3, PartyMember.get_MaxHealth(NPC3))
    else:
        NPC3health = PartyMember.get_Health(NPC3) + total
        PartyMember.set_Health(NPC3, NPC3health)



def campfireRandomUpgrade():
    clear()
    LobbyStatus()
    print("Random Stat Upgrade selected.")
    time.sleep(2)
    print("Rolling For Upgrade...\n")
    time.sleep(3)
    roll2 = randrange(1, 6)

    ## MAXIMUM HEALTH UPGRADE
    if roll2 == 1:
        print("Max Health Upgrade!")
        print("\nIncreases Max Health by 125 and restores 75 Health to a single character")
        time.sleep(3)
        clear()
        LobbyStatus()
        print("Select a character to give Max Health Upgrade.")
        print("\n1. " + PlayerCharacter.get_name(PC) + " (PC) \n2. " + PartyMember.get_name(NPC1) +
              " (Party Member) \n3. " + PartyMember.get_name(NPC2) + " (Party Member) \n4. " +
              PartyMember.get_name(NPC3) + " (Party Member)\n")
        key = int(input(""))
        if key == 1:
            print("\nGiving upgrade to PC.")
            time.sleep(2)
            newPCmaxhealth = PlayerCharacter.get_MaxHealth(PC) + 125
            PlayerCharacter.set_MaxHealth(PC, newPCmaxhealth)
            newPChealth = PlayerCharacter.get_Health(PC) + 75
            PlayerCharacter.set_Health(PC, newPCmaxhealth)
        elif key == 2:
            print("\nGiving upgrade to " + PartyMember.get_name(NPC1) + ".")
            time.sleep(2)
            newNPCmaxhealth = PlayerCharacter.get_MaxHealth(NPC1) + 125
            PartyMember.set_MaxHealth(NPC1, newNPCmaxhealth)
            newNPChealth = PartyMember.get_Health(NPC1) + 75
            PartyMember.set_Health(NPC1, newNPChealth)
        elif key == 3:
            print("\nGiving upgrade to " + PartyMember.get_name(NPC2) + ".")
            time.sleep(2)
            newNPCmaxhealth = PlayerCharacter.get_MaxHealth(NPC2) + 125
            PartyMember.set_MaxHealth(NPC2, newNPCmaxhealth)
            newNPChealth = PartyMember.get_Health(NPC2) + 75
            PartyMember.set_Health(NPC2, newNPChealth)
        elif key == 4:
            print("\nGiving upgrade to " + PartyMember.get_name(NPC3) + ".")
            time.sleep(2)
            newNPCmaxhealth = PlayerCharacter.get_MaxHealth(NPC3) + 125
            PartyMember.set_MaxHealth(NPC3, newNPCmaxhealth)
            newNPChealth = PartyMember.get_Health(NPC3) + 75
            PartyMember.set_Health(NPC3, newNPChealth)
        else:
            print("Key not recognized, giving upgrade to PC.")
            time.sleep(2)
            newPCmaxhealth = PlayerCharacter.get_MaxHealth(PC) + 125
            PlayerCharacter.set_MaxHealth(PC, newPCmaxhealth)
            newPChealth = PlayerCharacter.get_Health(PC) + 75
            PlayerCharacter.set_Health(PC, newPCmaxhealth)

    ## ARMOUR CLASS UPGRADE
    if roll2 == 2:
        print("Armour Class Upgrade!")
        print("\nIncreases a character's Armour Class by 2d6.")
        time.sleep(3)
        clear()
        LobbyStatus()
        print("Select a character to give Armour Class Upgrade.")
        ACroll = randrange(1,6) + randrange(1,6)
        print("\n1. " + PlayerCharacter.get_name(PC) + " (PC) (Armour Class: " + str(PlayerCharacter.get_ArmourClass(PC)) +
              ")\n2. " + PartyMember.get_name(NPC1) + " (Party Member) (Armour Class: " + str(PartyMember.get_ArmourClass(NPC1)) +
              "\n3." + PartyMember.get_name(NPC2) + " (Party Member) (Armour Class: " + str(PartyMember.get_ArmourClass(NPC2)) +
              "\n4. " + PartyMember.get_name(NPC3) + " (Party Member) (Armour Class: " + str(PartyMember.get_ArmourClass(NPC3)))
        key = int(input(""))
        if key == 1:
            print("Giving upgrade to PC.")
            time.sleep(2)
            newPCarmourclass = PlayerCharacter.get_ArmourClass(PC) + ACroll
            PlayerCharacter.set_ArmourClass(PC, newPCarmourclass)
        elif key == 2:
            print("Giving upgrade to " + PartyMember.get_name(NPC1) + ".")
            time.sleep(2)
            newNPCarmourclass = PartyMember.get_ArmourClass(NPC1) + ACroll
            PartyMember.set_ArmourClass(NPC1, newNPCarmourclass)
        elif key == 3:
            print("Giving upgrade to " + PartyMember.get_name(NPC2) + ".")
            time.sleep(2)
            newNPCarmourclass = PartyMember.get_ArmourClass(NPC2) + ACroll
            PartyMember.set_ArmourClass(NPC2, newNPCarmourclass)
        elif key == 4:
            print("Giving upgrade to " + PartyMember.get_name(NPC3) + ".")
            time.sleep(2)
            newNPCarmourclass = PartyMember.get_ArmourClass(NPC3) + ACroll
            PartyMember.set_ArmourClass(NPC3, newNPCarmourclass)
        else:
            print("Key not recognized, giving upgrade to PC.")
            time.sleep(2)
            newPCarmourclass = PlayerCharacter.get_ArmourClass(PC) + ACroll
            PlayerCharacter.set_ArmourClass(PC, newPCarmourclass)
        print("Armour Class improved by " + str(ACroll) + "!")
        time.sleep(4)

    ## NEW EQUIPMENT UPGRADE
    if roll2 == 3:
        print("New Equipment")
        print("\nIncreases all characters Armour Class by 1d6.")
        time.sleep(3)

        ACroll = randrange(1,6)

        newPCarmourclass = PlayerCharacter.get_ArmourClass(PC) + ACroll
        PlayerCharacter.set_ArmourClass(PC, newPCarmourclass)
        newNPCarmourclass = PartyMember.get_ArmourClass(NPC1) + ACroll
        PartyMember.set_ArmourClass(NPC1, newNPCarmourclass)
        newNPCarmourclass = PartyMember.get_ArmourClass(NPC2) + ACroll
        PartyMember.set_ArmourClass(NPC2, newNPCarmourclass)
        newNPCarmourclass = PartyMember.get_ArmourClass(NPC3) + ACroll
        PartyMember.set_ArmourClass(NPC3, newNPCarmourclass)
        newPCarmourclass = PlayerCharacter.get_ArmourClass(PC) + ACroll
        PlayerCharacter.set_ArmourClass(PC, newPCarmourclass)

        print("Armour Class increased by " + str(ACroll) + "!")
        time.sleep(4)

        clear()
        LobbyStatus()

    ## NEW WEAPONS UPGRADE
    if roll2 == 4:
        print("New Weapons")
        print("\nIncreases all characters Attack Modifiers (increasing accuracy and damage) by 1d6.")
        time.sleep(3)
        roll1 = randrange(1,6)


        newPCattackmod = PlayerCharacter.get_attackModifier(PC) + roll1
        PlayerCharacter.set_attackModifier(PC, newPCattackmod)
        newNPCattackmod = PartyMember.get_AttackModifier(NPC1) + roll1
        PartyMember.set_AttackModifier(NPC1, newNPCattackmod)
        newNPCattackmod = PartyMember.get_AttackModifier(NPC2) + roll1
        PartyMember.set_AttackModifier(NPC2, newNPCattackmod)
        newNPCattackmod = PartyMember.get_AttackModifier(NPC3) + roll1
        PartyMember.set_AttackModifier(NPC3, newNPCattackmod)

        print("Attack Modifiers increased by " + str(roll1) + "! Accuracy and Damage improved.")
        time.sleep(4)

        clear()
        LobbyStatus()

    ## HEALTH CAP FOR ALL
    if roll2 == 5:
        print("Scroll of Health")
        print("\nIncreases all characters Max Health by 3d20.")
        increase = randrange(1,20) + randrange(1,20) + randrange(1,20)

        time.sleep(3)

        newPCmaxhealth = PlayerCharacter.get_MaxHealth(PC) + increase
        PlayerCharacter.set_MaxHealth(PC, newPCmaxhealth)
        newNPCMaxHealth = PartyMember.get_MaxHealth(NPC1) + increase
        PartyMember.set_MaxHealth(NPC1, newNPCMaxHealth)
        newNPCMaxHealth = PartyMember.get_MaxHealth(NPC2) + increase
        PartyMember.set_MaxHealth(NPC2, newNPCMaxHealth)
        newNPCMaxHealth = PartyMember.get_MaxHealth(NPC3) + increase
        PartyMember.set_MaxHealth(NPC3, newNPCMaxHealth)

        print("Health increased by " + str(increase))
        time.sleep(4)

        clear()
        LobbyStatus()

    ## SPECIAL POINTS
    if roll2 == 6:
        print("Vial of Goddess's Tears")
        print("\nIncreases Special Points by 2d6.")
        increase = randrange(1,6) + randrange(1,6)

        time.sleep(3)

        newSP = PlayerCharacter.get_SpecialPoints(PC) + increase
        PlayerCharacter.set_SpecialPoints(PC, newSP)


        print("Special Points increased by " + str(increase))
        time.sleep(4)

        clear()
        LobbyStatus()



    ## ALL PC STATS UP BY 2d6
    if roll2 == 7:
        print("Sacred Boar's Tusk")
        print("\nIncreases most PC stats by 2d6")
        increase = randrange(1,6) + randrange(1,6)

        time.sleep(3)

        newSP = PlayerCharacter.get_SpecialPoints(PC) + increase
        PlayerCharacter.set_SpecialPoints(PC, newSP)
        newPCmaxhealth = PlayerCharacter.get_MaxHealth(PC) + increase
        PlayerCharacter.set_MaxHealth(PC, newPCmaxhealth)
        newNPCMaxHealth = PartyMember.get_AttackModifier(NPC1) + increase
        PartyMember.set_MaxHealth(NPC1, newNPCMaxHealth)
        newNPCMaxHealth = PartyMember.get_AttackModifier(NPC2) + increase
        PartyMember.set_MaxHealth(NPC2, newNPCMaxHealth)
        newNPCMaxHealth = PartyMember.get_AttackModifier(NPC3) + increase
        PartyMember.set_MaxHealth(NPC3, newNPCMaxHealth)
        newPCattackmod = PlayerCharacter.get_attackModifier(PC) + roll1
        PlayerCharacter.set_attackModifier(PC, newPCattackmod)
        newNPCattackmod = PartyMember.get_AttackModifier(NPC1) + roll2
        PartyMember.set_AttackModifier(NPC1, newNPCattackmod)
        newNPCattackmod = PartyMember.get_AttackModifier(NPC2) + roll3
        PartyMember.set_AttackModifier(NPC2, newNPCattackmod)
        newNPCattackmod = PartyMember.get_AttackModifier(NPC3) + roll4
        PartyMember.set_AttackModifier(NPC3, newNPCattackmod)
        newStrength = PlayerCharacter.get_Strength(PC) + increase
        PlayerCharacter.set_Strength(PC, newStrength)
        newDexterity = PlayerCharacter.get_Dexterity(PC) + increase
        PlayerCharacter.set_Dexterity(PC, newDexterity)
        newArmourClass = PlayerCharacter.get_ArmourClass(PC) + increase
        PlayerCharacter.set_ArmourClass(PC, newArmourClass)
        newInitiative = PlayerCharacter.get_Initiative(PC) + increase
        PlayerCharacter.set_Initiative(PC, newInitiative)


        print("Special Points, Max Health, Health, Attack Modifier, Strength, Dexterity, Armour Class and Initiative increased by " + str(increase))
        time.sleep(2)

        clear()
        LobbyStatus()

    ## NEW EQUIPMENT UPGRADE
    if roll2 == 8:
        print("New Compass")
        print("\nIncreases Player Character initiative by 1d6.")
        time.sleep(3)

        initRoll = randrange(1,6)
        newPCinit = PlayerCharacter.get_Initiative(PC) + initRoll
        PlayerCharacter.set_Initiative(PC, newPCinit)
        print("Initiative increased by " + str(initRoll) +"!")
        time.sleep(4)

        clear()
        LobbyStatus()


    #print("Ending campfireRandomUpgrade()")
    time.sleep(1)



def campfireMaxHealth():
    clear()
    LobbyStatus()
    print("Max Health Upgrade!")
    print("\nIncreases Max Health by 40 and restores 40 Health to a single character")
    time.sleep(3)
    clear()
    LobbyStatus()
    print("Select a character to give Max Health Upgrade.")
    print("\n1. " + PlayerCharacter.get_name(PC) + " (PC) \n2. " + PartyMember.get_name(NPC1) +
          " (Party Member) \n3. " + PartyMember.get_name(NPC2) + " (Party Member) \n4. " +
          PartyMember.get_name(NPC3) + " (Party Member)\n")
    amount =  40
    key = int(input(""))
    if key == 1:
        print("\nGiving upgrade to PC.")
        time.sleep(2)
        newPCmaxhealth = PlayerCharacter.get_MaxHealth(PC) + amount
        PlayerCharacter.set_MaxHealth(PC, newPCmaxhealth)
        newPChealth = PlayerCharacter.get_Health(PC) + amount
        PlayerCharacter.set_Health(PC, newPCmaxhealth)
    elif key == 2:
        print("\nGiving upgrade to " + PartyMember.get_name(NPC1) + ".")
        time.sleep(2)
        newNPCmaxhealth = PlayerCharacter.get_MaxHealth(NPC1) + amount
        PartyMember.set_MaxHealth(NPC1, newNPCmaxhealth)
        newNPChealth = PartyMember.get_Health(NPC1) + amount
        PartyMember.set_Health(NPC1, newNPChealth)
    elif key == 3:
        print("\nGiving upgrade to " + PartyMember.get_name(NPC2) + ".")
        time.sleep(2)
        newNPCmaxhealth = PlayerCharacter.get_MaxHealth(NPC2) + amount
        PartyMember.set_MaxHealth(NPC2, newNPCmaxhealth)
        newNPChealth = PartyMember.get_Health(NPC2) + amount
        PartyMember.set_Health(NPC2, newNPChealth)
    elif key == 4:
        print("\nGiving upgrade to " + PartyMember.get_name(NPC3) + ".")
        time.sleep(2)
        newNPCmaxhealth = PlayerCharacter.get_MaxHealth(NPC3) + amount
        PartyMember.set_MaxHealth(NPC3, newNPCmaxhealth)
        newNPChealth = PartyMember.get_Health(NPC3) + amount
        PartyMember.set_Health(NPC3, newNPChealth)
    else:
        print("Key not recognized, giving upgrade to PC.")
        time.sleep(2)
        newPCmaxhealth = PlayerCharacter.get_MaxHealth(PC) + amount
        PlayerCharacter.set_MaxHealth(PC, newPCmaxhealth)
        newPChealth = PlayerCharacter.get_Health(PC) + amount
        PlayerCharacter.set_Health(PC, newPCmaxhealth)

def campfireAM():
    rolls = 1
    total = 0
    rolldice = randrange(1, 3)
    total = rolldice

    print("\nWeapons Upgrade!")
    time.sleep(2)

    newPCAM = PlayerCharacter.get_attackModifier(PC) + total
    PlayerCharacter.set_attackModifier(PC, newPCAM)

    NPC1AM = PartyMember.get_AttackModifier(NPC1) + total
    PartyMember.set_AttackModifier(NPC1, NPC1AM)
    NPC2AM = PartyMember.get_AttackModifier(NPC2) + total
    PartyMember.set_AttackModifier(NPC2, NPC2AM)
    NPC3AM = PartyMember.get_AttackModifier(NPC3) + total
    PartyMember.set_AttackModifier(NPC3, NPC3AM)


    clear()
    LobbyStatus()
    print("Everyone's Attack Modifier is increased by " + str(total) + "!")
    time.sleep(3)




    clear()
    LobbyStatus()


def campfireAC():
    rolls = 1
    total = 0
    rolldice = randrange(1, 3)
    total = rolldice

    print("\nArmour Upgrade!")
    time.sleep(2)

    newPCAC = PlayerCharacter.get_ArmourClass(PC) + total
    PlayerCharacter.set_ArmourClass(PC, newPCAC)

    NPC1AC = PartyMember.get_ArmourClass(NPC1) + total
    PartyMember.set_ArmourClass(NPC1, NPC1AC)
    NPC2AC = PartyMember.get_ArmourClass(NPC2) + total
    PartyMember.set_ArmourClass(NPC2, NPC2AC)
    NPC3AC = PartyMember.get_ArmourClass(NPC3) + total
    PartyMember.set_ArmourClass(NPC3, NPC3AC)


    clear()
    LobbyStatus()
    print("Everyone's Armour Class is increased by " + str(total) + "!")
    time.sleep(3)




    clear()
    LobbyStatus()


def campfireTrainCore():
    clear()
    LobbyStatus()

    rollinc = randrange(1,4)
    print("Select a Core Stat to train and increase by 1d4:\n")
    print("1. Strength (" + str(PlayerCharacter.get_Strength(PC)) + ")")
    print("2. Dexterity (" + str(PlayerCharacter.get_Dexterity(PC)) + ")")
    print("3. Charisma (" + str(PlayerCharacter.get_Charisma(PC)) + ")")
    print("4. Intellect (" + str(PlayerCharacter.get_Intellect(PC)) + ")\n")
    key = input("")
    if key == "1":
        newStr = PlayerCharacter.get_Strength(PC) + rollinc
        PlayerCharacter.set_Strength(PC, newStr)
        time.sleep(1)
        print("\nStrength increased by " + str(rollinc) + "!")
        time.sleep(4)
    if key == "2":
        newDex = PlayerCharacter.get_Dexterity(PC) + rollinc
        PlayerCharacter.set_Dexterity(PC, newDex)
        time.sleep(1)
        print("\nDexterity increased by " + str(rollinc) + "!")
        time.sleep(4)
    if key == "3":
        newCha = PlayerCharacter.get_Charisma(PC) + rollinc
        PlayerCharacter.set_Charisma(PC, newCha)
        time.sleep(1)
        print("\nCharisma increased by " + str(rollinc) + "!")
        time.sleep(4)
    if key == "4":
        newInt = PlayerCharacter.get_Intellect(PC) + rollinc
        PlayerCharacter.set_Intellect(PC, newInt)
        time.sleep(1)
        print("\nIntellect increased by " + str(rollinc) + "!")
        time.sleep(4)


def buyItem1():
    clear()
    Item.set_isOwned(Item1, True)
    newGold = PlayerCharacter.get_Gold(PC) - 1000
    PlayerCharacter.set_Gold(PC, newGold)
    print("Gold reduced to " + str(newGold) + ".")
    time.sleep(1)
    print("You purchase the " + Item.get_adj(Item1) +  " "    + Item.get_name(Item1) + "!")
    time.sleep(1)
    print("     Increases AttackMod for a single character by 10.")
    print("\n")
    time.sleep(1)
    print("1. " + PlayerCharacter.get_name(PC) + ": " + str(PlayerCharacter.get_attackModifier(PC)))
    print("2. " + PartyMember.get_name(NPC1) + ": " + str(PartyMember.get_AttackModifier(NPC1)))
    print("3. " + PartyMember.get_name(NPC2) + ": " + str(PartyMember.get_AttackModifier(NPC2)))
    print("4. " + PartyMember.get_name(NPC3) + ": " + str(PartyMember.get_AttackModifier(NPC3)))
    print("\n")
    print("Give the " + Item.get_adj(Item1) +  " "    + Item.get_name(Item1) + " to which character?")
    key = input("")
    if key == "1":
        newAM = PlayerCharacter.get_attackModifier(PC) + 10
        PlayerCharacter.set_attackModifier(PC, newAM)
        print("\n" + PlayerCharacter.get_name(PC) + "'s AttackMod increased to " + str(PlayerCharacter.get_attackModifier(PC)) +"!")
    if key == "2":
        newAM = PartyMember.get_AttackModifier(NPC1) + 10
        PartyMember.set_AttackModifier(NPC1, newAM)
        print("\n" + PartyMember.get_name(NPC1) + "'s AttackMod increased to " + str(PartyMember.get_AttackModifier(NPC1)) + "!")
    if key == "3":
        newAM = PartyMember.get_AttackModifier(NPC2) + 10
        PartyMember.set_AttackModifier(NPC2, newAM)
        print("\n" + PartyMember.get_name(NPC2) + "'s AttackMod increased to " + str(PartyMember.get_AttackModifier(NPC2)) + "!")
    if key == "4":
        newAM = PartyMember.get_AttackModifier(NPC3) + 10
        PartyMember.set_AttackModifier(NPC3, newAM)
        print("\n" + PartyMember.get_name(NPC3) + "'s AttackMod increased to " + str(PartyMember.get_AttackModifier(NPC3)) + "!")
    time.sleep(5)
    print("\n(Press enter to continue)")
    key = input("")
    if key != "`":
        time.sleep(1)
    else:
        time.sleep(1)



def buyItem2():
    clear()
    Item.set_isOwned(Item2, True)
    newGold = PlayerCharacter.get_Gold(PC) - 1250
    PlayerCharacter.set_Gold(PC, newGold)
    print("Gold reduced to " + str(newGold) + ".")
    time.sleep(1)
    print("You purchase the " + Item.get_adj(Item2) +  " "    + Item.get_name(Item2) + "!")
    time.sleep(1)
    print("     Increases Armour Class for a single character by 10.")
    print("\n")
    time.sleep(1)
    print("1. " + PlayerCharacter.get_name(PC) + ": " + str(PlayerCharacter.get_ArmourClass(PC)))
    print("2. " + PartyMember.get_name(NPC1) + ": " + str(PartyMember.get_ArmourClass(NPC1)))
    print("3. " + PartyMember.get_name(NPC2) + ": " + str(PartyMember.get_ArmourClass(NPC2)))
    print("4. " + PartyMember.get_name(NPC3) + ": " + str(PartyMember.get_ArmourClass(NPC3)))
    print("\n")
    print("Give the " + Item.get_adj(Item2) +  " "    + Item.get_name(Item2) + " to which character?")
    key = input("")
    if key == "1":
        newAM = PlayerCharacter.get_ArmourClass(PC) + 10
        PlayerCharacter.set_ArmourClass(PC, newAM)
        print("\n" + PlayerCharacter.get_name(PC) + "'s Armour Class increased to " + str(PlayerCharacter.get_ArmourClass(PC)) +"!")
    if key == "2":
        newAM = PartyMember.get_ArmourClass(NPC1) + 10
        PartyMember.set_ArmourClass(NPC1, newAM)
        print("\n" + PartyMember.get_name(NPC1) + "'s Armour Class increased to " + str(PartyMember.get_ArmourClass(NPC1)) + "!")
    if key == "3":
        newAM = PartyMember.get_ArmourClass(NPC2) + 10
        PartyMember.set_ArmourClass(NPC2, newAM)
        print("\n" + PartyMember.get_name(NPC2) + "'s Armour Class increased to " + str(PartyMember.get_ArmourClass(NPC2)) + "!")
    if key == "4":
        newAM = PartyMember.get_ArmourClass(NPC3) + 10
        PartyMember.set_ArmourClass(NPC3, newAM)
        print("\n" + PartyMember.get_name(NPC3) + "'s Armour Class increased to " + str(PartyMember.get_ArmourClass(NPC3)) + "!")
    time.sleep(5)
    print("(Press enter to continue)")
    key = input("")
    if key != "`":
        time.sleep(1)
    else:
        time.sleep(1)



def buyItem3():
    clear()
    Item.set_isOwned(Item3, True)
    newGold = PlayerCharacter.get_Gold(PC) - 1250
    PlayerCharacter.set_Gold(PC, newGold)
    print("Gold reduced to " + str(newGold) + ".")
    time.sleep(1)
    print("You purchase the " + Item.get_adj(Item3) +  " "    + Item.get_name(Item3) + "!")
    time.sleep(1)
    print("     Increases Health and Max Health for a single character by 200.")
    print("\n")
    time.sleep(1)
    print("1. " + PlayerCharacter.get_name(PC) + ": " + str(PlayerCharacter.get_Health(PC)) + "/"+ str(PlayerCharacter.get_MaxHealth(PC)))
    print("2. " + PartyMember.get_name(NPC1) + ": " + str(PartyMember.get_Health(NPC1)) + "/"+ str(PartyMember.get_MaxHealth(NPC1)))
    print("3. " + PartyMember.get_name(NPC2) + ": " + str(PartyMember.get_Health(NPC2)) + "/"+ str(PartyMember.get_MaxHealth(NPC2)))
    print("4. " + PartyMember.get_name(NPC3) + ": " + str(PartyMember.get_Health(NPC3)) + "/"+  str(PartyMember.get_MaxHealth(NPC3)))
    print("\n")
    print("Give the " + Item.get_adj(Item3) +  " "    + Item.get_name(Item3) + " to which character?")

    key = input("")
    if key == "1":
        newMaxHP = PlayerCharacter.get_MaxHealth(PC) + 200
        PlayerCharacter.set_MaxHealth(PC, newMaxHP)
        newHP = PlayerCharacter.get_Health(PC) + 200
        PlayerCharacter.set_Health(PC, newHP)
        print("\n" + PlayerCharacter.get_name(PC) + "'s Health increased to " + str(PlayerCharacter.get_Health(PC)) +" and Max Health increased to " + str(PlayerCharacter.get_MaxHealth(PC)) + "!")
    if key == "2":
        newMaxHP = PartyMember.get_MaxHealth(NPC1) + 200
        PartyMember.set_MaxHealth(NPC1, newMaxHP)
        newHP = PartyMember.get_Health(NPC1) + 200
        PartyMember.set_Health(NPC1, newHP)
        print("\n" + PartyMember.get_name(NPC1) + "'s Health increased to " + str(
            PartyMember.get_Health(NPC1)) + " and Max Health increased to " + str(
            PartyMember.get_MaxHealth(NPC1)) + "!")
    if key == "3":
        newMaxHP = PartyMember.get_MaxHealth(NPC2) + 200
        PartyMember.set_MaxHealth(NPC2, newMaxHP)
        newHP = PartyMember.get_Health(NPC2) + 200
        PartyMember.set_Health(NPC2, newHP)
        print("\n" + PartyMember.get_name(NPC2) + "'s Health increased to " + str(
            PartyMember.get_Health(NPC2)) + " and Max Health increased to " + str(
            PartyMember.get_MaxHealth(NPC2)) + "!")
    if key == "4":
        newMaxHP = PartyMember.get_MaxHealth(NPC3) + 200
        PartyMember.set_MaxHealth(NPC3, newMaxHP)
        newHP = PartyMember.get_Health(NPC3) + 200
        PartyMember.set_Health(NPC3, newHP)
        print("\n" + PartyMember.get_name(NPC3) + "'s Health increased to " + str(
            PartyMember.get_Health(NPC3)) + " and Max Health increased to " + str(
            PartyMember.get_MaxHealth(NPC3)) + "!")
    time.sleep(5)
    print("\n(Press enter to continue)")
    key = input("")
    if key != "`":
        time.sleep(1)
    else:
        time.sleep(1)


def buyItem4():
    clear()
    Item.set_isOwned(Item4, True)
    newGold = PlayerCharacter.get_Gold(PC) - 1500
    PlayerCharacter.set_Gold(PC, newGold)
    print("Gold reduced to " + str(newGold) + ".")
    time.sleep(1)
    print("You purchase the " + Item.get_adj(Item3) +  " "    + Item.get_name(Item3) + "!")
    time.sleep(1)
    print("     Increases Player Initiative by 7.")
    time.sleep(1)

    newInit = PlayerCharacter.get_Initiative(PC) + 7
    PlayerCharacter.set_Initiative(PC, newInit)
    print("\n" + PlayerCharacter.get_name(PC) + "'s Initiative increased to " + str(PlayerCharacter.get_Initiative(PC)) + ".")


    time.sleep(5)
    print("\n(Press enter to continue)")
    key = input("")
    if key != "`":
        time.sleep(1)
    else:
        time.sleep(1)

def buyRitual5():
    #rint("\n8. Exchange 3000 Gold for 1500 Blood Points")
    print("You turn in 3000 blood.")
    time.sleep(2)
    newBlood = PlayerCharacter.get_Blood(PC) - 3000
    newGold = PlayerCharacter.get_Blood(PC) + 1500
    PlayerCharacter.set_Gold(PC, newGold)
    PlayerCharacter.set_Blood(PC, newBlood)
    print("You receive 1500 gold for " + str(newGold) + " total.\n")
    time.sleep(2)
    print("(Press enter to continue)")
    key = input("")
    if key != "`":
        time.sleep(1)
        bloodShop()
    else:
        time.sleep(1)
        bloodShop()

def buyRitual3():
    clear()
    newBlood = PlayerCharacter.get_Blood(PC) - 2500
    PlayerCharacter.set_Blood(PC, newBlood)
    time.sleep(1)
    Ritual.get_isPerformed(Ritual3) == True
    print("Blood reduced to " + str(newBlood) + ".")
    time.sleep(2)
    print("\nYou perform the Sacrament of the Four Horned Stag!")


    time.sleep(2)
    print("     Replace a Party Member with a Four Horned Druid, with 20 more AttackMod than the Party Member sacrificed.")
    print("\n")
    time.sleep(1)
    #print("1. " + PlayerCharacter.get_name(PC) + ": " + str(PlayerCharacter.get_Health(PC)) + "/" + str(PlayerCharacter.get_MaxHealth(PC)))
    print("1. " + PartyMember.get_name(NPC1) + ": " + str(PartyMember.get_AttackModifier(NPC1)))
    print("2. " + PartyMember.get_name(NPC2) + ": " + str(PartyMember.get_AttackModifier(NPC2)))
    print("3. " + PartyMember.get_name(NPC3) + ": " + str(PartyMember.get_AttackModifier(NPC3)))
    print("\n")
    print("Sacrifice which character?")
    FourHornedDruid = PartyMember()
    key = input("")
    if key == "1":
        newAM = PartyMember.get_AttackModifier(NPC1) + 20
        PartyMember.set_name(NPC1, PartyMember.get_name(FourHornedDruid))
        PartyMember.set_isAlive(NPC1, True)
        PartyMember.set_ArmourClass(NPC1, PartyMember.get_ArmourClass(FourHornedDruid))
        PartyMember.set_AttackModifier(NPC1, newAM)
        PartyMember.set_Health(NPC1, PartyMember.get_Health(FourHornedDruid))
        PartyMember.set_MaxHealth(NPC1, PartyMember.get_Health(FourHornedDruid))

        PartyMember.set_Personality(NPC1, "the Four Horned Druid")
        PartyMember.set_SpecSlot1Name(NPC1, "None")
        PartyMember.set_SpecSlot1Damage(NPC1, 0)
        PartyMember.set_SpecSlot1Prob(NPC1, 1)
        print("\n" + PartyMember.get_name(NPC1) + "'s AttackMod increased to " + str(PartyMember.get_AttackModifier(NPC1)) + "!")
    if key == "2":
        newAM = PartyMember.get_AttackModifier(NPC2) + 20
        PartyMember.set_name(NPC2, PartyMember.get_name(FourHornedDruid))
        PartyMember.set_isAlive(NPC2, True)
        PartyMember.set_ArmourClass(NPC2, PartyMember.get_ArmourClass(FourHornedDruid))
        PartyMember.set_AttackModifier(NPC2, newAM)
        PartyMember.set_Health(NPC2, PartyMember.get_Health(FourHornedDruid))
        PartyMember.set_MaxHealth(NPC2, PartyMember.get_Health(FourHornedDruid))

        PartyMember.set_Personality(NPC2, "the Four Horned Druid")
        PartyMember.set_SpecSlot1Name(NPC2, "None")
        PartyMember.set_SpecSlot1Damage(NPC2, 0)
        PartyMember.set_SpecSlot1Prob(NPC2, 1)
        print("\n" + PartyMember.get_name(NPC2) + "'s AttackMod increased to " + str(
            PartyMember.get_AttackModifier(NPC2)) + "!")
    if key == "3":
        newAM = PartyMember.get_AttackModifier(NPC3) + 20
        PartyMember.set_name(NPC3, PartyMember.get_name(FourHornedDruid))
        PartyMember.set_isAlive(NPC3, True)
        PartyMember.set_ArmourClass(NPC3, PartyMember.get_ArmourClass(FourHornedDruid))
        PartyMember.set_AttackModifier(NPC3, newAM)
        PartyMember.set_Health(NPC3, PartyMember.get_Health(FourHornedDruid))
        PartyMember.set_MaxHealth(NPC3, PartyMember.get_Health(FourHornedDruid))

        PartyMember.set_Personality(NPC2, "the Four Horned Druid")
        PartyMember.set_SpecSlot1Name(NPC2, "None")
        PartyMember.set_SpecSlot1Damage(NPC2, 0)
        PartyMember.set_SpecSlot1Prob(NPC2, 1)

        print("\n" + PartyMember.get_name(NPC3) + "'s AttackMod increased to " + str(
            PartyMember.get_AttackModifier(NPC3)) + "!")


def buyRitual2():
    clear()
    Ritual.get_isPerformed(Ritual2) == True
    newBlood = PlayerCharacter.get_Blood(PC) - 2500
    PlayerCharacter.set_Blood(PC, newBlood)
    time.sleep(1)
    print("Blood reduced to " + str(newBlood) + ".")
    print("\nYou perform the Ceremony of the Raven God!")

    time.sleep(2)
    print("     Replace a Party Member with a Raven Guard, with 20 more Armour Class than the Party Member sacrificed.")
    print("\n")
    time.sleep(1)
    #print("1. " + PlayerCharacter.get_name(PC) + ": " + str(PlayerCharacter.get_Health(PC)) + "/" + str(PlayerCharacter.get_MaxHealth(PC)))
    print("1. " + PartyMember.get_name(NPC1) + ": " + str(PartyMember.get_ArmourClass(NPC1)))
    print("2. " + PartyMember.get_name(NPC2) + ": " + str(PartyMember.get_ArmourClass(NPC2)))
    print("3. " + PartyMember.get_name(NPC3) + ": " + str(PartyMember.get_ArmourClass(NPC3)))
    print("\n")
    print("Sacrifice which character?")
    RavenGuard = PartyMember()
    key = input("")
    if key == "1":
        newAC = PartyMember.get_ArmourClass(NPC1) + 20
        PartyMember.set_name(NPC1, PartyMember.get_name(RavenGuard))
        PartyMember.set_isAlive(NPC1, True)
        PartyMember.set_ArmourClass(NPC1, newAC)
        PartyMember.set_AttackModifier(NPC1, PartyMember.get_AttackModifier(RavenGuard))
        PartyMember.set_Health(NPC1, PartyMember.get_Health(RavenGuard))
        PartyMember.set_MaxHealth(NPC1, PartyMember.get_Health(RavenGuard))

        PartyMember.set_Personality(NPC1, "the Raven Guard")
        PartyMember.set_SpecSlot1Name(NPC1, "None")
        PartyMember.set_SpecSlot1Damage(NPC1, 0)
        PartyMember.set_SpecSlot1Prob(NPC1, 1)

        print("\n" + PartyMember.get_name(NPC1) + "'s Armour Class increased to " + str(PartyMember.get_ArmourClass(NPC1)) + "!")
    if key == "2":
        newAC = PartyMember.get_ArmourClass(NPC2) + 20
        PartyMember.set_name(NPC2, PartyMember.get_name(RavenGuard))
        PartyMember.set_isAlive(NPC2, True)
        PartyMember.set_ArmourClass(NPC2, newAC)
        PartyMember.set_AttackModifier(NPC2, PartyMember.get_AttackModifier(RavenGuard))
        PartyMember.set_Health(NPC2, PartyMember.get_Health(RavenGuard))
        PartyMember.set_MaxHealth(NPC2, PartyMember.get_Health(RavenGuard))

        PartyMember.set_Personality(NPC2, "the Raven Guard")
        PartyMember.set_SpecSlot1Name(NPC2, "None")
        PartyMember.set_SpecSlot1Damage(NPC2, 0)
        PartyMember.set_SpecSlot1Prob(NPC2, 1)

        print("\n" + PartyMember.get_name(NPC2) + "'s Armour Class increased to " + str(
            PartyMember.get_ArmourClass(NPC2)) + "!")
    if key == "3":
        newAC = PartyMember.get_ArmourClass(NPC3) + 20
        PartyMember.set_name(NPC3, PartyMember.get_name(RavenGuard))
        PartyMember.set_isAlive(NPC3, True)
        PartyMember.set_ArmourClass(NPC3, newAC)
        PartyMember.set_AttackModifier(NPC3, PartyMember.get_AttackModifier(RavenGuard))
        PartyMember.set_Health(NPC3, PartyMember.get_Health(RavenGuard))
        PartyMember.set_MaxHealth(NPC3, PartyMember.get_Health(RavenGuard))

        PartyMember.set_Personality(NPC3, "the Raven Guard")
        PartyMember.set_SpecSlot1Name(NPC3, "None")
        PartyMember.set_SpecSlot1Damage(NPC3, 0)
        PartyMember.set_SpecSlot1Prob(NPC3, 1)

        print("\n" + PartyMember.get_name(NPC3) + "'s Armour Class increased to " + str(
            PartyMember.get_ArmourClass(NPC3)) + "!")


def buyRitual4():
    clear()
    newBlood = PlayerCharacter.get_Blood(PC) - 3000
    PlayerCharacter.set_Blood(PC, newBlood)
    time.sleep(1)
    Ritual.get_isPerformed(Ritual4) == True
    print("Blood reduced to " + str(newBlood) + ".")
    time.sleep(2)
    print("You perform the Parade of the Mad Toad King!")
    time.sleep(3)

    newSP = PlayerCharacter.get_SpecialPoints(PC) + 100
    PlayerCharacter.set_SpecialPoints(PC, newSP)


    print("\nSpecial Points increased to " + str(newSP) + "!")
    time.sleep(4)



def buyRitual1():
    clear()
    newBlood = PlayerCharacter.get_Blood(PC) - 2000
    PlayerCharacter.set_Blood(PC, newBlood)
    Ritual.get_isPerformed(Ritual1) == True
    print("Blood reduced to " + str(newBlood) + ".")
    time.sleep(2)
    print("\nYou perform the Rite of the Blood Witch!")

    time.sleep(1)
    print("     Replace a Party Member with a Blood Knight, with 400 more Health and Max Health than the Party Member sacrificed.")
    print("\n")
    time.sleep(1)
    #print("1. " + PlayerCharacter.get_name(PC) + ": " + str(PlayerCharacter.get_Health(PC)) + "/" + str(PlayerCharacter.get_MaxHealth(PC)))
    print("1. " + PartyMember.get_name(NPC1) + ": " + str(PartyMember.get_Health(NPC1)) + "/" + str(
        PartyMember.get_MaxHealth(NPC1)))
    print("2. " + PartyMember.get_name(NPC2) + ": " + str(PartyMember.get_Health(NPC2)) + "/" + str(
        PartyMember.get_MaxHealth(NPC2)))
    print("3. " + PartyMember.get_name(NPC3) + ": " + str(PartyMember.get_Health(NPC3)) + "/" + str(
        PartyMember.get_MaxHealth(NPC3)))
    print("\n")
    print("Sacrifice which character?")
    BloodKnight = PartyMember()
    key = input("")
    if key == "1":
        newMaxHP = PartyMember.get_MaxHealth(NPC1) + 400
        newHP = PartyMember.get_Health(NPC1) + 400
        PartyMember.set_name(NPC1, PartyMember.get_name(BloodKnight))
        PartyMember.set_isAlive(NPC1, True)
        PartyMember.set_ArmourClass(NPC1, PartyMember.get_ArmourClass(BloodKnight))
        PartyMember.set_AttackModifier(NPC1, PartyMember.get_AttackModifier(BloodKnight))
        PartyMember.set_Health(NPC1, newHP)
        PartyMember.set_MaxHealth(NPC1, newMaxHP)

        PartyMember.set_Personality(NPC1, "the Blood Knight")
        PartyMember.set_SpecSlot1Name(NPC1, "None")
        PartyMember.set_SpecSlot1Damage(NPC1, 0)
        PartyMember.set_SpecSlot1Prob(NPC1, 1)
        print("\n" + PartyMember.get_name(NPC1) + "'s Health increased to " + str(PartyMember.get_Health(NPC1)) + " and Max Health increased to " + str(PartyMember.get_MaxHealth(NPC1)) + "!")
    if key == "2":
        newMaxHP = PartyMember.get_MaxHealth(NPC2) + 400
        newHP = PartyMember.get_Health(NPC2) + 400
        PartyMember.set_name(NPC2, PartyMember.get_name(BloodKnight))
        PartyMember.set_isAlive(NPC2, True)
        PartyMember.set_ArmourClass(NPC2, PartyMember.get_ArmourClass(BloodKnight))
        PartyMember.set_AttackModifier(NPC2, PartyMember.get_AttackModifier(BloodKnight))
        PartyMember.set_Health(NPC2, newHP)
        PartyMember.set_MaxHealth(NPC2, newMaxHP)

        PartyMember.set_Personality(NPC2, "the Blood Knight")
        PartyMember.set_SpecSlot1Name(NPC2, "None")
        PartyMember.set_SpecSlot1Damage(NPC2, 0)
        PartyMember.set_SpecSlot1Prob(NPC2, 1)
        print("\n" + PartyMember.get_name(NPC2) + "'s Health increased to " + str(PartyMember.get_Health(NPC2)) + " and Max Health increased to " + str(PartyMember.get_MaxHealth(NPC2)) + "!")
    if key == "3":
        newMaxHP = PartyMember.get_MaxHealth(NPC3) + 400
        newHP = PartyMember.get_Health(NPC3) + 400
        PartyMember.set_name(NPC3, PartyMember.get_name(BloodKnight))
        PartyMember.set_isAlive(NPC3, True)
        PartyMember.set_ArmourClass(NPC3, PartyMember.get_ArmourClass(BloodKnight))
        PartyMember.set_AttackModifier(NPC3, PartyMember.get_AttackModifier(BloodKnight))
        PartyMember.set_Health(NPC3, newHP)
        PartyMember.set_MaxHealth(NPC3, newMaxHP)

        PartyMember.set_Personality(NPC3, "the Blood Knight")
        PartyMember.set_SpecSlot1Name(NPC3, "None")
        PartyMember.set_SpecSlot1Damage(NPC3, 0)
        PartyMember.set_SpecSlot1Prob(NPC3, 1)
        print("\n" + PartyMember.get_name(NPC3) + "'s Health increased to " + str(PartyMember.get_Health(NPC3)) + " and Max Health increased to " + str(PartyMember.get_MaxHealth(NPC3)) + "!")



def bloodShop():

    clear()
    print("                 BLOOD ALTAR          ")
    print("\n")
    print("Blood: " + str(PlayerCharacter.get_Blood(PC)))
    print("\nBlood Rituals performed at the Blood Altar sacrifice a random Party Member for an upgraded one.")
    print("\n")
    if Ritual.get_isPerformed(Ritual1) == False:
        print("1. Rite of the Blood Witch")
        print("     2,000 Blood")
        print("     Replace a Party Member with a Blood Knight, with 400 more Health and Max Health than the Party Member sacrificed.")
    else:
        print("1. Already Performed")

    if Ritual.get_isPerformed(Ritual2) == False:
        print("\n2. Ceremony of the Raven God")
        print("     2,500 Blood")
        print("     Replace a Party Member with a Raven Guard, with 20 more Armour Class than the Party Member sacrificed.")
    else:
        print("\n2. Already Performed")
    if Ritual.get_isPerformed(Ritual3) == False:
        print("\n3. Sacrament of the Four Horned Stag")
        print("     2,500 Blood")
        print("     Replace a Party Member with a Four Horned Druid, with 20 more AttackMod than the Party Member sacrificed.")
    else:
        print("\n3. Already Performed")
    if Ritual.get_isPerformed(Ritual4) == False:
        print("\n4. Parade of the Mad Toad King")
        print("     3,000 Blood")
        print("     Increases Special Points by 100.")
    else:
        print("\n4. Empty")
        #print("5. " + Item.get_name(Item1))
        #print("2,000 Gold Coins")
        #print("     Increases AttackMod for a single character by 10.")
    print("\n8. Exchange 3,000 Blood for 1,500 Gold")
    print("\n9. (Return to Campfire)")
    print("_______________________________________________")
    print("\n")
    key = input("")
    if key == "1" and Ritual.get_isPerformed(Ritual1) == False:
        buyRitual1()
    if key == "2" and Ritual.get_isPerformed(Ritual2) == False:
        buyRitual2()
    if key == "3" and Ritual.get_isPerformed(Ritual3) == False:
        buyRitual3()
    if key == "4" and Ritual.get_isPerformed(Ritual4) == False:
        buyRitual4()
    blood = PlayerCharacter.get_Blood(PC)
    if key == "8" and blood > 2999:
        buyRitual5()
    if key == "9":
        clear()
        LobbyStatus()
        levelUp()
    else:
        clear()
        LobbyStatus()
        levelUp()

def buyItem5():
    #rint("\n8. Exchange 3000 Gold for 1500 Blood Points")
    print("You turn in 3000 gold.")
    time.sleep(2)
    newGold = PlayerCharacter.get_Gold(PC) - 3000
    newBlood = PlayerCharacter.get_Blood(PC) + 1500
    PlayerCharacter.set_Gold(PC, newGold)
    PlayerCharacter.set_Blood(PC, newBlood)
    print("You receive 1500 blood for " + str(newBlood) + " total.\n")
    time.sleep(2)
    print("(Press enter to continue)")
    key = input("")
    if key != "`":
        time.sleep(1)
        itemShop()
    else:
        time.sleep(1)
        itemShop()


def itemShop():
    clear()
    print("                 ITEM SHOP          ")
    print("\n")
    print("Gold: " + str(PlayerCharacter.get_Gold(PC)))
    print("\n")
    if Item.get_isOwned(Item1) == False:
        print("1. " + Item.get_adj(Item1) +  " "    + Item.get_name(Item1))
        print("     1,000 Gold Coins")
        print("     Increases AttackMod for a single character by 10.")
    else:
        print("1. Empty")

    if Item.get_isOwned(Item2) == False:
        print("\n2. " + Item.get_adj(Item2) +  " "    + Item.get_name(Item2))
        print("     1,250 Gold Coins")
        print("     Increases Armour Class for a single character by 10.")
    else:
        print("\n2. Empty")
    if Item.get_isOwned(Item3) == False:
        print("\n3. " + Item.get_adj(Item3) +  " "    + Item.get_name(Item3))
        print("     1,250 Gold Coins")
        print("     Increases Health and Max Health for a single character by 200.")
    else:
        print("\n3. Empty")
    if Item.get_isOwned(Item4) == False:
        print("\n4. " + Item.get_adj(Item4) +  " "    + Item.get_name(Item4))
        print("     1,500 Gold Coins")
        print("     Increases Player Initiative by 7.")
    else:
        print("\n4. Empty")
        #print("5. " + Item.get_name(Item1))
        #print("2,000 Gold Coins")
        #print("     Increases AttackMod for a single character by 10.")
    print("\n8. Exchange 3000 Gold for 1500 Blood")
    print("\n9. (Return to Campfire)")
    print("_______________________________________________")
    print("\n")
    key = input("")
    if key == "1" and Item.get_isOwned(Item1) == False:
        buyItem1()
    if key == "2" and Item.get_isOwned(Item2) == False:
        buyItem2()
    if key == "3" and Item.get_isOwned(Item3) == False:
        buyItem3()
    if key == "4" and Item.get_isOwned(Item4) == False:
        buyItem4()
    gold = PlayerCharacter.get_Gold(PC)
    if key == "8" and gold > 2999:
        buyItem5()
    if key == "8" and gold < 3000:
        clear()
        LobbyStatus()
        levelUp()
    if key == "9":
        clear()
        LobbyStatus()
        levelUp()
    else:
        clear()
        LobbyStatus()
        levelUp()







def levelUp():

    clear()
    LobbyStatus()

    SaveGame()
    print("1. Rest at the Campfire\n     (Restore 50 + 10d10 Health to Everyone)")
    print("2. Search for Loot Nearby\n     (Receive Random Stat Upgrade)")
    print("3. Study the Runes Nearby\n     (Learn Choice of Special Attack)")
    print("4. Seek an Armourer\n     (Improve Armour Class 1d3)")
    print("5. Seek a Weaponsmith\n     (Improve Attack Modifier 1d3)")
    print("6. Buy an Amulet\n     (Increase Max Health +40 for Choice of Character)")
    print("7. Train a Chosen Core Stat\n     (Strength, Dexterity, Charisma, or Intellect)")
    print("8. Post a Recruitment Ad\n     (Chance to Replace Party Member with Stranger)")
    gold = PlayerCharacter.get_Gold(PC)
    blood = PlayerCharacter.get_Blood(PC)
    if gold > 1000:
        print("9. Item Shop")

    else:
        print("9. Locked\n     (Earn More Gold)")

    if blood > 2000:
        print("10. Blood Altar")
    else:
        print("10. Locked\n     (Spill More Blood)")


    print("\n\n(Please select an option.)")
    intkey = input("")
    if intkey == "1":
        campfireHeal()
    if intkey == "2":
        campfireRandomUpgrade()
    if intkey == "3":
        learnSpecial()
    if intkey == "4":
        campfireAC()
    if intkey == "5":
        campfireAM()
    if intkey == "6":
        campfireMaxHealth()
    if intkey == "7":
        campfireTrainCore()
    if intkey == "8":
        MysteriousStrangerRecruitment_Harder()
    if intkey == "9" and gold >= 1000:
        itemShop()
    if intkey == "9" and gold < 1000:
        print("\nNot enough gold!")
        time.sleep(3)
        clear()
        LobbyStatus()
        levelUp()
    if intkey == "10" and blood >= 2000:
        bloodShop()
    if intkey == "10" and blood < 2000:
        print("\nNot enough blood!")
        time.sleep(3)
        clear()
        LobbyStatus()
        levelUp()

    clear()
    LobbyStatus()
    print("Campfire session completed!")
    time.sleep(5)
    clear()
    preBattle()




def HolyStrikeCharacterPicker():
    clear()
    print("     TRAINING HOLY STRIKE  ")
    print("\nSelect a Party Member to Teach Holy Strike:")
    print("1. "+ PartyMember.get_name(NPC1) + ": " + PartyMember.get_SpecSlot1Name(NPC1))
    print("2. " + PartyMember.get_name(NPC2) + ": " + PartyMember.get_SpecSlot1Name(NPC2))
    print("3. " + PartyMember.get_name(NPC3) + ": " + PartyMember.get_SpecSlot1Name(NPC3))
    print("")
    key = int(input(""))
    if key == 1:
        PartyMember.set_SpecSlot1Name(NPC1, "Holy Strike")
        PartyMember.set_SpecSlot1Prob(NPC1, SpecialMoves.get_probability(HolyStrike))
        PartyMember.set_SpecSlot1Cost(NPC1, SpecialMoves.get_cost(HolyStrike))
        PartyMember.set_SpecSlot1Num(NPC1, SpecialMoves.get_indexNumber(HolyStrike))
        PartyMember.set_SpecSlot1Damage(NPC1, SpecialMoves.get_damage(HolyStrike))
        clear()
        print(PartyMember.get_name(NPC1) + " learned Holy Strike!")
        time.sleep(3)
        clear()

    elif key == 2:
        PartyMember.set_SpecSlot1Name(NPC2, "Holy Strike")
        PartyMember.set_SpecSlot1Prob(NPC2, SpecialMoves.get_probability(HolyStrike))
        PartyMember.set_SpecSlot1Cost(NPC2, SpecialMoves.get_cost(HolyStrike))
        PartyMember.set_SpecSlot1Num(NPC2, SpecialMoves.get_indexNumber(HolyStrike))
        PartyMember.set_SpecSlot1Damage(NPC2, SpecialMoves.get_damage(HolyStrike))
        clear()
        print(PartyMember.get_name(NPC2) + " learned Holy Strike!")
        time.sleep(3)
        clear()
    elif key == 3:
        PartyMember.set_SpecSlot1Name(NPC3, "Holy Strike")
        PartyMember.set_SpecSlot1Prob(NPC3, SpecialMoves.get_probability(HolyStrike))
        PartyMember.set_SpecSlot1Cost(NPC3, SpecialMoves.get_cost(HolyStrike))
        PartyMember.set_SpecSlot1Num(NPC3, SpecialMoves.get_indexNumber(HolyStrike))
        PartyMember.set_SpecSlot1Damage(NPC3, SpecialMoves.get_damage(HolyStrike))
        clear()
        print(PartyMember.get_name(NPC3) + " learned Holy Strike!")
        time.sleep(3)
        clear()
    preBattle()

def IronMasteryCharacterPicker():
    clear()
    print("     TRAINING IRON MASTERY  ")
    print("\nSelect a Party Member to Teach Iron Mastery:")
    print("1. "+ PartyMember.get_name(NPC1) + ": " + PartyMember.get_SpecSlot1Name(NPC1))
    print("2. " + PartyMember.get_name(NPC2) + ": " + PartyMember.get_SpecSlot1Name(NPC2))
    print("3. " + PartyMember.get_name(NPC3) + ": " + PartyMember.get_SpecSlot1Name(NPC3))
    print("")
    key = int(input(""))
    if key == 1:
        PartyMember.set_SpecSlot1Name(NPC1, "Iron Mastery")
        PartyMember.set_SpecSlot1Prob(NPC1, SpecialMoves.get_probability(IronMastery))
        PartyMember.set_SpecSlot1Cost(NPC1, SpecialMoves.get_cost(IronMastery))
        PartyMember.set_SpecSlot1Num(NPC1, SpecialMoves.get_indexNumber(IronMastery))
        PartyMember.set_SpecSlot1Damage(NPC1, SpecialMoves.get_damage(IronMastery))
        clear()
        print(PartyMember.get_name(NPC1) + " learned Iron Mastery!")
        time.sleep(3)
        clear()
    elif key == 2:
        PartyMember.set_SpecSlot1Name(NPC2, "Iron Mastery")
        PartyMember.set_SpecSlot1Prob(NPC2, SpecialMoves.get_probability(IronMastery))
        PartyMember.set_SpecSlot1Cost(NPC2, SpecialMoves.get_cost(IronMastery))
        PartyMember.set_SpecSlot1Num(NPC2, SpecialMoves.get_indexNumber(IronMastery))
        PartyMember.set_SpecSlot1Damage(NPC2, SpecialMoves.get_damage(IronMastery))
        clear()
        print(PartyMember.get_name(NPC2) + " learned Iron Mastery!")
        time.sleep(3)
        clear()
    elif key == 3:
        PartyMember.set_SpecSlot1Name(NPC3, "Iron Mastery")
        PartyMember.set_SpecSlot1Prob(NPC3, SpecialMoves.get_probability(IronMastery))
        PartyMember.set_SpecSlot1Cost(NPC3, SpecialMoves.get_cost(IronMastery))
        PartyMember.set_SpecSlot1Num(NPC3, SpecialMoves.get_indexNumber(IronMastery))
        PartyMember.set_SpecSlot1Damage(NPC3, SpecialMoves.get_damage(IronMastery))
        clear()
        print(PartyMember.get_name(NPC3) + " learned Iron Mastery!")
        time.sleep(3)
        clear()
    preBattle()


def ShieldBashCharacterPicker():
    clear()
    print("     TRAINING SHIELD BASH  ")
    print("\nSelect a Party Member to Teach Shield Bash:")
    print("1. "+ PartyMember.get_name(NPC1) + ": " + PartyMember.get_SpecSlot1Name(NPC1))
    print("2. " + PartyMember.get_name(NPC2) + ": " + PartyMember.get_SpecSlot1Name(NPC2))
    print("3. " + PartyMember.get_name(NPC3) + ": " + PartyMember.get_SpecSlot1Name(NPC3))
    print("")
    key = int(input(""))
    if key == 1:
        PartyMember.set_SpecSlot1Name(NPC1, "Shield Bash")
        PartyMember.set_SpecSlot1Prob(NPC1, SpecialMoves.get_probability(ShieldBash))
        PartyMember.set_SpecSlot1Cost(NPC1, SpecialMoves.get_cost(ShieldBash))
        PartyMember.set_SpecSlot1Num(NPC1, SpecialMoves.get_indexNumber(ShieldBash))
        PartyMember.set_SpecSlot1Damage(NPC1, SpecialMoves.get_damage(ShieldBash))
        clear()
        print(PartyMember.get_name(NPC1) + " learned Shield Bash!")
        time.sleep(3)
        clear()
    elif key == 2:
        PartyMember.set_SpecSlot1Name(NPC2, "Shield Bash")
        PartyMember.set_SpecSlot1Prob(NPC2, SpecialMoves.get_probability(ShieldBash))
        PartyMember.set_SpecSlot1Cost(NPC2, SpecialMoves.get_cost(ShieldBash))
        PartyMember.set_SpecSlot1Num(NPC2, SpecialMoves.get_indexNumber(ShieldBash))
        PartyMember.set_SpecSlot1Damage(NPC2, SpecialMoves.get_damage(ShieldBash))
        clear()
        print(PartyMember.get_name(NPC2) + " learned Shield Bash!")
        time.sleep(3)
        clear()
    elif key == 3:
        PartyMember.set_SpecSlot1Name(NPC3, "Shield Bash")
        PartyMember.set_SpecSlot1Prob(NPC3, SpecialMoves.get_probability(ShieldBash))
        PartyMember.set_SpecSlot1Cost(NPC3, SpecialMoves.get_cost(ShieldBash))
        PartyMember.set_SpecSlot1Num(NPC3, SpecialMoves.get_indexNumber(ShieldBash))
        PartyMember.set_SpecSlot1Damage(NPC3, SpecialMoves.get_damage(ShieldBash))
        clear()
        print(PartyMember.get_name(NPC3) + " learned Shield Bash!")
        time.sleep(3)
        clear()
    preBattle()
def PsychicBombCharacterPicker():
    clear()
    print("     TRAINING PSYCHIC BOMB  ")
    print("\nSelect a Party Member to Teach Psychic Bomb:")
    print("1. "+ PartyMember.get_name(NPC1) + ": " + PartyMember.get_SpecSlot1Name(NPC1))
    print("2. " + PartyMember.get_name(NPC2) + ": " + PartyMember.get_SpecSlot1Name(NPC2))
    print("3. " + PartyMember.get_name(NPC3) + ": " + PartyMember.get_SpecSlot1Name(NPC3))
    print("")
    key = int(input(""))
    if key == 1:
        PartyMember.set_SpecSlot1Name(NPC1, "Psychic Bomb")
        PartyMember.set_SpecSlot1Prob(NPC1, SpecialMoves.get_probability(PsychicBomb))
        PartyMember.set_SpecSlot1Cost(NPC1, SpecialMoves.get_cost(PsychicBomb))
        PartyMember.set_SpecSlot1Num(NPC1, SpecialMoves.get_indexNumber(PsychicBomb))
        PartyMember.set_SpecSlot1Damage(NPC1, SpecialMoves.get_damage(PsychicBomb))
        clear()
        LobbyStatus()
        print(PartyMember.get_name(NPC1) + " learned Psychic Bomb!")
        time.sleep(3)
        clear()
    elif key == 2:
        PartyMember.set_SpecSlot1Name(NPC2, "Psychic Bomb")
        PartyMember.set_SpecSlot1Prob(NPC2, SpecialMoves.get_probability(PsychicBomb))
        PartyMember.set_SpecSlot1Cost(NPC2, SpecialMoves.get_cost(PsychicBomb))
        PartyMember.set_SpecSlot1Num(NPC2, SpecialMoves.get_indexNumber(PsychicBomb))
        PartyMember.set_SpecSlot1Damage(NPC2, SpecialMoves.get_damage(PsychicBomb))
        clear()
        LobbyStatus()
        print(PartyMember.get_name(NPC2) + " learned Psychic Bomb!")
        time.sleep(3)
        clear()
    elif key == 3:
        PartyMember.set_SpecSlot1Name(NPC3, "Psychic Bomb")
        PartyMember.set_SpecSlot1Prob(NPC3, SpecialMoves.get_probability(PsychicBomb))
        PartyMember.set_SpecSlot1Cost(NPC3, SpecialMoves.get_cost(PsychicBomb))
        PartyMember.set_SpecSlot1Num(NPC3, SpecialMoves.get_indexNumber(PsychicBomb))
        PartyMember.set_SpecSlot1Damage(NPC3, SpecialMoves.get_damage(PsychicBomb))
        clear()
        LobbyStatus()
        print(PartyMember.get_name(NPC3) + " learned Psychic Bomb!")
        time.sleep(3)
        clear()
    preBattle()


def WaterChainCharacterPicker():
    clear()
    print("     TRAINING WATER CHAIN  ")
    print("\nSelect a Party Member to Teach Water Chain:")
    print("1. "+ PartyMember.get_name(NPC1) + ": " + PartyMember.get_SpecSlot1Name(NPC1))
    print("2. " + PartyMember.get_name(NPC2) + ": " + PartyMember.get_SpecSlot1Name(NPC2))
    print("3. " + PartyMember.get_name(NPC3) + ": " + PartyMember.get_SpecSlot1Name(NPC3))
    print("")
    key = int(input(""))
    if key == 1:
        PartyMember.set_SpecSlot1Name(NPC1, "Water Chain")
        PartyMember.set_SpecSlot1Prob(NPC1, SpecialMoves.get_probability(WaterChain))
        PartyMember.set_SpecSlot1Cost(NPC1, SpecialMoves.get_cost(WaterChain))
        PartyMember.set_SpecSlot1Num(NPC1, SpecialMoves.get_indexNumber(WaterChain))
        PartyMember.set_SpecSlot1Damage(NPC1, SpecialMoves.get_damage(WaterChain))
        clear()
        print(PartyMember.get_name(NPC1) + " learned Water Chain!")
        time.sleep(3)
        clear()
    elif key == 2:
        PartyMember.set_SpecSlot1Name(NPC2, "Water Chain")
        PartyMember.set_SpecSlot1Prob(NPC2, SpecialMoves.get_probability(WaterChain))
        PartyMember.set_SpecSlot1Cost(NPC2, SpecialMoves.get_cost(WaterChain))
        PartyMember.set_SpecSlot1Num(NPC2, SpecialMoves.get_indexNumber(WaterChain))
        PartyMember.set_SpecSlot1Damage(NPC2, SpecialMoves.get_damage(WaterChain))
        clear()
        print(PartyMember.get_name(NPC2) + " learned Water Chain!")
        time.sleep(3)
        clear()
    elif key == 3:
        PartyMember.set_SpecSlot1Name(NPC3, "Water Chain")
        PartyMember.set_SpecSlot1Prob(NPC3, SpecialMoves.get_probability(WaterChain))
        PartyMember.set_SpecSlot1Cost(NPC3, SpecialMoves.get_cost(WaterChain))
        PartyMember.set_SpecSlot1Num(NPC3, SpecialMoves.get_indexNumber(WaterChain))
        PartyMember.set_SpecSlot1Damage(NPC3, SpecialMoves.get_damage(WaterChain))
        clear()
        print(PartyMember.get_name(NPC3) + " learned Water Chain!")
        time.sleep(3)
        clear()
    preBattle()

def FireStrikeCharacterPicker():
    clear()
    print("     TRAINING FIRE STRIKE  ")
    print("\nSelect a Party Member to Teach Fire Strike:")
    print("1. "+ PartyMember.get_name(NPC1) + ": " + PartyMember.get_SpecSlot1Name(NPC1))
    print("2. " + PartyMember.get_name(NPC2) + ": " + PartyMember.get_SpecSlot1Name(NPC2))
    print("3. " + PartyMember.get_name(NPC3) + ": " + PartyMember.get_SpecSlot1Name(NPC3))
    print("")
    key = int(input(""))
    if key == 1:
        PartyMember.set_SpecSlot1Name(NPC1, "Fire Strike")
        PartyMember.set_SpecSlot1Prob(NPC1, SpecialMoves.get_probability(FireStrike))
        PartyMember.set_SpecSlot1Cost(NPC1, SpecialMoves.get_cost(FireStrike))
        PartyMember.set_SpecSlot1Num(NPC1, SpecialMoves.get_indexNumber(FireStrike))
        PartyMember.set_SpecSlot1Damage(NPC1, SpecialMoves.get_damage(FireStrike))
        clear()
        print(PartyMember.get_name(NPC1) + " learned Fire Strike!")
        time.sleep(3)
        clear()
    elif key == 2:
        PartyMember.set_SpecSlot1Name(NPC2, "Fire Strike")
        PartyMember.set_SpecSlot1Prob(NPC2, SpecialMoves.get_probability(FireStrike))
        PartyMember.set_SpecSlot1Cost(NPC2, SpecialMoves.get_cost(FireStrike))
        PartyMember.set_SpecSlot1Num(NPC2, SpecialMoves.get_indexNumber(FireStrike))
        PartyMember.set_SpecSlot1Damage(NPC2, SpecialMoves.get_damage(FireStrike))
        clear()
        print(PartyMember.get_name(NPC2) + " learned Fire Strike!")
        time.sleep(3)
        clear()
    elif key == 3:
        PartyMember.set_SpecSlot1Name(NPC3, "Fire Strike")
        PartyMember.set_SpecSlot1Prob(NPC3, SpecialMoves.get_probability(FireStrike))
        PartyMember.set_SpecSlot1Cost(NPC3, SpecialMoves.get_cost(FireStrike))
        PartyMember.set_SpecSlot1Num(NPC3, SpecialMoves.get_indexNumber(FireStrike))
        PartyMember.set_SpecSlot1Damage(NPC3, SpecialMoves.get_damage(FireStrike))
        clear()
        print(PartyMember.get_name(NPC3) + " learned Fire Strike!")
        time.sleep(3)
        clear()
    preBattle()
def AnimalFamiliarCharacterPicker():
    clear()
    print("     TRAINING ANIMAL FAMILIAR  ")
    print("\nSelect a Party Member to Teach Animal Familiar:")
    print("1. "+ PartyMember.get_name(NPC1) + ": " + PartyMember.get_SpecSlot1Name(NPC1))
    print("2. " + PartyMember.get_name(NPC2) + ": " + PartyMember.get_SpecSlot1Name(NPC2))
    print("3. " + PartyMember.get_name(NPC3) + ": " + PartyMember.get_SpecSlot1Name(NPC3))
    print("")
    key = int(input(""))
    if key == 1:
        PartyMember.set_SpecSlot1Name(NPC1, "Animal Familiar")
        PartyMember.set_SpecSlot1Prob(NPC1, SpecialMoves.get_probability(AnimalFamiliar))
        PartyMember.set_SpecSlot1Cost(NPC1, SpecialMoves.get_cost(AnimalFamiliar))
        PartyMember.set_SpecSlot1Num(NPC1, SpecialMoves.get_indexNumber(AnimalFamiliar))
        PartyMember.set_SpecSlot1Damage(NPC1, SpecialMoves.get_damage(AnimalFamiliar))
        clear()
        print(PartyMember.get_name(NPC1) + " learned Animal Familiar!")
        time.sleep(3)
        clear()
    elif key == 2:
        PartyMember.set_SpecSlot1Name(NPC2, "Animal Familiar")
        PartyMember.set_SpecSlot1Prob(NPC2, SpecialMoves.get_probability(AnimalFamiliar))
        PartyMember.set_SpecSlot1Cost(NPC2, SpecialMoves.get_cost(AnimalFamiliar))
        PartyMember.set_SpecSlot1Num(NPC2, SpecialMoves.get_indexNumber(AnimalFamiliar))
        PartyMember.set_SpecSlot1Damage(NPC2, SpecialMoves.get_damage(AnimalFamiliar))
        clear()
        print(PartyMember.get_name(NPC2) + " learned Animal Familiar!")
        time.sleep(3)
        clear()
    elif key == 3:
        PartyMember.set_SpecSlot1Name(NPC3, "Animal Familiar")
        PartyMember.set_SpecSlot1Prob(NPC3, SpecialMoves.get_probability(AnimalFamiliar))
        PartyMember.set_SpecSlot1Cost(NPC3, SpecialMoves.get_cost(AnimalFamiliar))
        PartyMember.set_SpecSlot1Num(NPC3, SpecialMoves.get_indexNumber(AnimalFamiliar))
        PartyMember.set_SpecSlot1Damage(NPC3, SpecialMoves.get_damage(AnimalFamiliar))
        clear()
        print(PartyMember.get_name(NPC3) + " learned Animal Familiar!")
        time.sleep(3)
        clear()
    preBattle()

def DemonMagicCharacterPicker():
    clear()
    print("     TRAINING DEMON MAGIC  ")
    print("\nSelect a Party Member to Teach Demon Magic:")
    print("1. "+ PartyMember.get_name(NPC1) + ": " + PartyMember.get_SpecSlot1Name(NPC1))
    print("2. " + PartyMember.get_name(NPC2) + ": " + PartyMember.get_SpecSlot1Name(NPC2))
    print("3. " + PartyMember.get_name(NPC3) + ": " + PartyMember.get_SpecSlot1Name(NPC3))
    print("")
    key = int(input(""))
    if key == 1:
        PartyMember.set_SpecSlot1Name(NPC1, "Demon Magic")
        PartyMember.set_SpecSlot1Prob(NPC1, SpecialMoves.get_probability(DemonMagic))
        PartyMember.set_SpecSlot1Cost(NPC1, SpecialMoves.get_cost(DemonMagic))
        PartyMember.set_SpecSlot1Num(NPC1, SpecialMoves.get_indexNumber(DemonMagic))
        PartyMember.set_SpecSlot1Damage(NPC1, SpecialMoves.get_damage(DemonMagic))
        clear()
        print(PartyMember.get_name(NPC1) + " learned Demon Magic!")
        time.sleep(3)
        clear()
    elif key == 2:
        PartyMember.set_SpecSlot1Name(NPC2, "Demon Magic")
        PartyMember.set_SpecSlot1Prob(NPC2, SpecialMoves.get_probability(DemonMagic))
        PartyMember.set_SpecSlot1Cost(NPC2, SpecialMoves.get_cost(DemonMagic))
        PartyMember.set_SpecSlot1Num(NPC2, SpecialMoves.get_indexNumber(DemonMagic))
        PartyMember.set_SpecSlot1Damage(NPC2, SpecialMoves.get_damage(DemonMagic))
        clear()
        print(PartyMember.get_name(NPC2) + " learned Demon Magic!")
        time.sleep(3)
        clear()
    elif key == 3:
        PartyMember.set_SpecSlot1Name(NPC3, "Demon Magic")
        PartyMember.set_SpecSlot1Prob(NPC3, SpecialMoves.get_probability(DemonMagic))
        PartyMember.set_SpecSlot1Cost(NPC3, SpecialMoves.get_cost(DemonMagic))
        PartyMember.set_SpecSlot1Num(NPC3, SpecialMoves.get_indexNumber(DemonMagic))
        PartyMember.set_SpecSlot1Damage(NPC3, SpecialMoves.get_damage(DemonMagic))
        clear()
        print(PartyMember.get_name(NPC3) + " learned Demon Magic!")
        time.sleep(3)
        clear()
    preBattle()
def SleepingGodCharacterPicker():
    clear()
    print("     TRAINING SLEEPING GOD  ")
    print("\nSelect a Party Member to Teach Sleeping God:")
    print("1. "+ PartyMember.get_name(NPC1) + ": " + PartyMember.get_SpecSlot1Name(NPC1))
    print("2. " + PartyMember.get_name(NPC2) + ": " + PartyMember.get_SpecSlot1Name(NPC2))
    print("3. " + PartyMember.get_name(NPC3) + ": " + PartyMember.get_SpecSlot1Name(NPC3))
    print("")
    key = int(input(""))
    if key == 1:
        PartyMember.set_SpecSlot1Name(NPC1, "Sleeping God")
        PartyMember.set_SpecSlot1Prob(NPC1, SpecialMoves.get_probability(SleepingGod))
        PartyMember.set_SpecSlot1Cost(NPC1, SpecialMoves.get_cost(SleepingGod))
        PartyMember.set_SpecSlot1Num(NPC1, SpecialMoves.get_indexNumber(SleepingGod))
        PartyMember.set_SpecSlot1Damage(NPC1, SpecialMoves.get_damage(SleepingGod))
        clear()
        print(PartyMember.get_name(NPC1) + " learned Sleeping God!")
        time.sleep(3)
        clear()
    elif key == 2:
        PartyMember.set_SpecSlot1Name(NPC2, "Sleeping God")
        PartyMember.set_SpecSlot1Prob(NPC2, SpecialMoves.get_probability(SleepingGod))
        PartyMember.set_SpecSlot1Cost(NPC2, SpecialMoves.get_cost(SleepingGod))
        PartyMember.set_SpecSlot1Num(NPC2, SpecialMoves.get_indexNumber(SleepingGod))
        PartyMember.set_SpecSlot1Damage(NPC2, SpecialMoves.get_damage(SleepingGod))
        clear()
        print(PartyMember.get_name(NPC2) + " learned Sleeping God!")
        time.sleep(3)
        clear()
    elif key == 3:
        PartyMember.set_SpecSlot1Name(NPC3, "Sleeping God")
        PartyMember.set_SpecSlot1Prob(NPC3, SpecialMoves.get_probability(SleepingGod))
        PartyMember.set_SpecSlot1Cost(NPC3, SpecialMoves.get_cost(SleepingGod))
        PartyMember.set_SpecSlot1Num(NPC3, SpecialMoves.get_indexNumber(SleepingGod))
        PartyMember.set_SpecSlot1Damage(NPC3, SpecialMoves.get_damage(SleepingGod))
        clear()
        print(PartyMember.get_name(NPC3) + " learned Sleeping God!")
        time.sleep(3)
        clear()
    preBattle()

def learnSpecial2():
    clear()
    print("")
    print("         ...         ")
    clear()
    print("")
    print("          ...         ")
    clear()
    print("")
    print("           ...         ")
    clear()
    print("")
    print("          ...         ")
    clear()
    print("")
    print("         ...         ")
    clear()
    print("")
    print("       ...         ")
    clear()
    print("      SPECIALS LIST:      \n")
    print("\n1. Holy Strike")
    print("     A divinely inspired strike, enhanced with blessings from a God.\n     " + str(SpecialMoves.get_cost(HolyStrike))  + " Cost, "+ str(SpecialMoves.get_damage(HolyStrike)) + " Damage, " + str(SpecialMoves.get_probability(HolyStrike)) + "% Accuracy.")
    print("\n2. Iron Mastery")
    print("     Decades of training informs muscle memory on exactly how to perform a deadly maneuver.\n     " + str(SpecialMoves.get_cost(IronMastery)) + " Cost, "+ str(SpecialMoves.get_damage(IronMastery)) + " Damage, " + str(SpecialMoves.get_probability(IronMastery)) + "% Accuracy.")
    print("\n3. Fire Strike")
    print("     A powerful fiery eruption scorches away at your enemies, but with wild unpredictability.\n     " + str(SpecialMoves.get_cost(FireStrike)) + " Cost, "+ str(SpecialMoves.get_damage(FireStrike)) + " Damage, " + str(SpecialMoves.get_probability(FireStrike)) + "% Accuracy.")
    print("\n4. Sleeping God")
    print("     Foolishly pray that the All Powerful Sleeping God awakens from his endless slumber, and smites one's enemies with apocalyptic strength.\n     " + str(SpecialMoves.get_cost(SleepingGod)) + " Cost, "+ str(SpecialMoves.get_damage(SleepingGod)) + " Damage, " + str(SpecialMoves.get_probability(SleepingGod)) + "% Accuracy.")
    print("\n5. Demon Magic")
    print("     An incredibly unpredictable, but cheap, ability to channel Demonic magic and rend one's enemy with it.\n     " + str(SpecialMoves.get_cost(DemonMagic)) + " Cost, "+ str(SpecialMoves.get_damage(DemonMagic)) + " Damage, " + str(SpecialMoves.get_probability(DemonMagic)) + "% Accuracy.")
    print("\n6. Animal Familiar")
    print("     An animal familiar accompanies this character, and fights viciously on their behalf in battle, if not unpredictably.\n     " + str(SpecialMoves.get_cost(AnimalFamiliar)) + " Cost, "+ str(SpecialMoves.get_damage(AnimalFamiliar)) + " Damage, " + str(SpecialMoves.get_probability(AnimalFamiliar)) + "% Accuracy.")
    print("\n7. Water Chain")
    print("     Elemental magic lashes up from the surroundings to twist at enemies with chains of water.\n     " + str(SpecialMoves.get_cost(WaterChain)) + " Cost, "+ str(SpecialMoves.get_damage(WaterChain)) + " Damage, " + str(SpecialMoves.get_probability(WaterChain)) + "% Accuracy.")
    print("\n8. Psychic Bomb")
    print("     An excruciating wave of psychic horror explodes out of the user, wreaking havoc on the mind of the target.\n     " + str(SpecialMoves.get_cost(PsychicBomb)) + " Cost, "+ str(SpecialMoves.get_damage(PsychicBomb)) + " Damage, " + str(SpecialMoves.get_probability(PsychicBomb)) + "% Accuracy.")
    print("\n9. Shield Bash")
    print("     A hulking shove forward with the defender's shield pushes enemies back and wounds them in the process.\n     " + str(SpecialMoves.get_cost(ShieldBash)) + " Cost, "+ str(SpecialMoves.get_damage(ShieldBash)) + " Damage, " + str(SpecialMoves.get_probability(ShieldBash)) + "% Accuracy.")
    print("\nPlease type the corresponding number for the Special you would like to learn.\n")
    key = int(input(""))
    if key == 1:
        HolyStrikeCharacterPicker()
    if key == 2:
        IronMasteryCharacterPicker()
    if key == 3:
        FireStrikeCharacterPicker()
    if key == 4:
        SleepingGodCharacterPicker()
    if key == 5:
        DemonMagicCharacterPicker()
    if key == 6:
        AnimalFamiliarCharacterPicker()
    if key == 7:
        WaterChainCharacterPicker()
    if key == 8:
        PsychicBombCharacterPicker()
    if key == 9:
        ShieldBashCharacterPicker()
    else:
        learnSpecial2()




def learnSpecial():
    clear()
    NPC1isAlive = PartyMember.get_isAlive(NPC1)
    NPC2isAlive = PartyMember.get_isAlive(NPC2)
    NPC3isAlive = PartyMember.get_isAlive(NPC3)


    print("Known Special Attacks: ")
    print("Special Points: " + str(PlayerCharacter.get_SpecialPoints(PC)) + "\n\n")
    print(PartyMember.get_name(NPC1) + ": " + PartyMember.get_SpecSlot1Name(NPC1))
    print(PartyMember.get_name(NPC2) + ": " + PartyMember.get_SpecSlot1Name(NPC2))
    print(PartyMember.get_name(NPC3) + ": " + PartyMember.get_SpecSlot1Name(NPC3))
    print("\n(Press any key to learn a new Special Attack)")
    key = input("")
    if key != "`":
        learnSpecial2()
    else:
        learnSpecial2()


def LobbyStatus():


    CurrentStage = Stage.get_number(TestStage1)
    CurrentTurn = Enemy.get_BattleTurn(TestEnemy)
    CurrentStageName = Stage.get_name(TestStage1)
    UpperStageName = CurrentStageName.upper()

    # print("BATTLE TEXT STATUS PLACEHOLDER -----------------------")
    #print(str(slain))
    print("")
    print("PC: " + PlayerCharacter.get_name(PC) + " - " + PlayerCharacter.get_playerclass(PC))
    print("   Health: " + str(PlayerCharacter.get_Health(PC)) + "/" + str(PlayerCharacter.get_MaxHealth(PC)))
    print("   Armour Class: " + str(PlayerCharacter.get_ArmourClass(PC)) + "   STR: " + str(PlayerCharacter.get_Strength(PC)) + "   INT: " + str(PlayerCharacter.get_Intellect(PC)))
    print("   AttackMod: " + str(PlayerCharacter.get_attackModifier(PC)) + "      DEX: " + str(PlayerCharacter.get_Dexterity(PC)) + "   CHA: " + str(PlayerCharacter.get_Charisma(PC)))
    print("   Special Points: " + str(PlayerCharacter.get_SpecialPoints(PC)) + "      Gold: " + str(PlayerCharacter.get_Gold(PC)))
    print("                          Blood: " + str(PlayerCharacter.get_Blood(PC)))
    print("Party: ")
    if PartyMember.get_Health(NPC1) > 0:
        print(PartyMember.get_name(NPC1) + " " + PartyMember.get_Personality(NPC1) + "\n   Health: " + str(PartyMember.get_Health(NPC1)) + "/" + str(
            PartyMember.get_MaxHealth(NPC1)) + "\n   Armour Class: " + str(PartyMember.get_ArmourClass(NPC1)) + "\n   AttackMod: " + str(PartyMember.get_AttackModifier(NPC1)))
    else:
        print(PartyMember.get_name(NPC1) + "\n   (Dead)")
    if PartyMember.get_SpecSlot1Name(NPC1) != "None":
        print("      Special: " + PartyMember.get_SpecSlot1Name(NPC1))
    if PartyMember.get_Health(NPC2) > 0:
        print(PartyMember.get_name(NPC2)  + " " + PartyMember.get_Personality(NPC2) +  "\n   Health: " + str(PartyMember.get_Health(NPC2)) + "/" + str(
            PartyMember.get_MaxHealth(NPC2)) + "\n   Armour Class: " + str(PartyMember.get_ArmourClass(NPC2)) + "\n   AttackMod: " + str(PartyMember.get_AttackModifier(NPC2)))
    else:
        print(PartyMember.get_name(NPC2) + "\n   (Dead)")
    if PartyMember.get_SpecSlot1Name(NPC2) != "None":
        print("      Special: " + PartyMember.get_SpecSlot1Name(NPC2))
    if PartyMember.get_Health(NPC3) > 0:
        print(PartyMember.get_name(NPC3)  + " " + PartyMember.get_Personality(NPC3) +  "\n   Health: " + str(PartyMember.get_Health(NPC3)) + "/" + str(
            PartyMember.get_MaxHealth(NPC3)) +  "\n   Armour Class: " + str(PartyMember.get_ArmourClass(NPC3)) + "\n   AttackMod: " + str(PartyMember.get_AttackModifier(NPC3)))
    else:
        print(PartyMember.get_name(NPC3) + "\n   (Dead)")
    if PartyMember.get_SpecSlot1Name(NPC3) != "None":
        print("      Special: " + PartyMember.get_SpecSlot1Name(NPC3))
    print("\n             CAMPFIRE        \n")
    print("                .(")
    print("               /%/\\")
    print("              (%(%))")
    print("             .-'..`-.")
    print("             `-'.'`")
    print("\n")
    print("         Enemies Slain: " + str(Enemy.get_NumberOfKills(TestEnemy)))
    print("_______________________________________________\n")

    time.sleep(3)


def EnemyWinInitiative():
    clear()
    print("\n")
    print(Enemy.get_name(TestEnemy) + " (Enemy) wins initiative. ")
    time.sleep(3)
    clear()
    enemyHealth = Enemy.get_Health(TestEnemy)
    BattleStatus()
    print("")



def PCWinInitiative():
    clear()
    print("\n")
    print(PlayerCharacter.get_name(PC) + " (PC) wins initiative. ")
    time.sleep(2)



#############################
##
##    GENERIC PC ROUND
##
##############################
def GenericPCPhase():




    newBattleTurn = Enemy.get_BattleTurn(TestEnemy) + 1
    Enemy.set_BattleTurn(TestEnemy, newBattleTurn)

    clear()
    BattleStatus()
    if PlayerCharacter.get_Health(PC) > 0 and Enemy.get_Health(TestEnemy) > 0:
        print("Player turn. " + PlayerCharacter.get_name(PC) + "'s party goes first.\n")
        time.sleep(2)

        NPC1isAlive = PartyMember.get_isAlive(NPC1)
        if NPC1isAlive == True:
            NPC1roll = randrange(1,20)
            NPC1rollbonus = int(PartyMember.get_AttackModifier(NPC1))
            NPC1totalroll = NPC1roll + NPC1rollbonus
            enemyAC = Enemy.get_ArmourClass(TestEnemy)
            dmgroll1 = randrange(1,20)
            dmgroll2 = randrange(1,20)
            totaldmg = dmgroll1 + dmgroll2 * 3 + (2 * PartyMember.get_AttackModifier(NPC1)) + (2 * Stage.get_number(TestStage1))
            if NPC1totalroll >= enemyAC:
                print(PartyMember.get_name(NPC1) + " hits for " + str(totaldmg) + " points of damage.")
                time.sleep(1)
                print("(" + str(NPC1roll) + " + " + str(NPC1rollbonus) + " = " + str(NPC1totalroll) + " vs. " + str(enemyAC) + ")")
                #clear()
                #BattleStatus()
                if totaldmg > Enemy.get_Health(TestEnemy):
                    newenemyHealth = Enemy.get_Health(TestEnemy) - totaldmg
                    Enemy.set_Health(TestEnemy, newenemyHealth)
                    #clear()
                    #BattleStatus()
                    print(PartyMember.get_name(NPC1) + " slayed " + Enemy.get_name(TestEnemy) + ".")
                    time.sleep(3)
                    enemyDied()
                else:
                    newenemyHealth = Enemy.get_Health(TestEnemy) - totaldmg
                    Enemy.set_Health(TestEnemy, newenemyHealth)
                time.sleep(2)
            else:
                print(PartyMember.get_name(NPC1) + " misses.")
                time.sleep(1)
                print("(" + str(NPC1roll) + " + " + str(NPC1rollbonus) + " = " + str(NPC1totalroll) + " vs. " + str(enemyAC) + ")")
                time.sleep(1)
            time.sleep(3)
        else:
            print(PartyMember.get_name(NPC1) + " is dead...")

        NPC2isAlive = PartyMember.get_isAlive(NPC2)
        if NPC2isAlive == True:
            NPC2roll = randrange(1,20)
            NPC2rollbonus = PartyMember.get_AttackModifier(NPC2)
            NPC2totalroll = NPC2roll + NPC2rollbonus
            enemyAC = Enemy.get_ArmourClass(TestEnemy)
            dmgroll1 = randrange(1,20)
            dmgroll2 = randrange(1,20)
            totaldmg = dmgroll1 + dmgroll2 * 3 + (2 * PartyMember.get_AttackModifier(NPC1)) + (2 * Stage.get_number(TestStage1))
            if NPC2totalroll >= enemyAC:
                print(PartyMember.get_name(NPC2) + " hits for " + str(totaldmg) + " points of damage.")
                time.sleep(1)
                print("(" + str(NPC2roll) + " + " + str(NPC2rollbonus) + " = " + str(NPC2totalroll) + " vs. " + str(enemyAC) + ")")

                #clear()
                #BattleStatus()
                if totaldmg > Enemy.get_Health(TestEnemy):
                    newenemyHealth = Enemy.get_Health(TestEnemy) - totaldmg
                    Enemy.set_Health(TestEnemy, newenemyHealth)
                    #clear()
                    #BattleStatus()
                    print(PartyMember.get_name(NPC2) + " slayed " + Enemy.get_name(TestEnemy) + ".")
                    time.sleep(3)
                    enemyDied()
                else:
                    newenemyHealth = Enemy.get_Health(TestEnemy) - totaldmg
                    Enemy.set_Health(TestEnemy, newenemyHealth)
                time.sleep(2)
            else:
                print(PartyMember.get_name(NPC2) + " misses.")
                time.sleep(1)
                print("(" + str(NPC2roll) + " + " + str(NPC2rollbonus) + " = " + str(NPC2totalroll) + " vs. " + str(enemyAC) + ")")
                time.sleep(1)
            time.sleep(2)
        else:
            print(PartyMember.get_name(NPC2) + " is dead...")

        NPC3isAlive = PartyMember.get_isAlive(NPC3)
        if NPC3isAlive == True:
            NPC3roll = randrange(1, 20)
            NPC3rollbonus = PartyMember.get_AttackModifier(NPC3)
            NPC3totalroll = NPC3roll + NPC3rollbonus
            enemyAC = Enemy.get_ArmourClass(TestEnemy)
            dmgroll1 = randrange(1, 20)
            dmgroll2 = randrange(1, 20)
            totaldmg = dmgroll1 + dmgroll2 * 3 + (2 * PartyMember.get_AttackModifier(NPC1)) + (2* Stage.get_number(TestStage1))
            if NPC3totalroll >= enemyAC:
                print(PartyMember.get_name(NPC3) + " hits for " + str(totaldmg) + " points of damage.")
                time.sleep(1)
                print("(" + str(NPC3roll) + " + " + str(NPC3rollbonus) + " = " + str(NPC3totalroll) + " vs. " + str(enemyAC) + ")")

                #clear()
                #BattleStatus()
                if totaldmg > Enemy.get_Health(TestEnemy):
                    newEnemyHealth = Enemy.get_Health(TestEnemy) - totaldmg
                    Enemy.set_Health(TestEnemy, newEnemyHealth)
                    #clear()
                    #BattleStatus()
                    print(PartyMember.get_name(NPC3) + " slayed " + Enemy.get_name(TestEnemy) + ".")
                    time.sleep(3)
                    enemyDied()
                else:
                    newenemyHealth = Enemy.get_Health(TestEnemy) - totaldmg
                    Enemy.set_Health(TestEnemy, newenemyHealth)
                time.sleep(5)
                clear()
            else:
                print(PartyMember.get_name(NPC3) + " misses.")
                time.sleep(1)
                print("(" + str(NPC3roll) + " + " + str(NPC3rollbonus) + " = " + str(NPC3totalroll) + " vs. " + str(enemyAC) + ")")
                time.sleep(1)
                clear()
            time.sleep(4)
        else:
            print(PartyMember.get_name(NPC3) + " is dead...")


        if Enemy.get_Health(TestEnemy) < 1:
            time.sleep(4)
            enemyDied()
        else:
            time.sleep(2)
            clear()

        BattleStatus()
        print(PlayerCharacter.get_name(PC) + "'s turn.")
        print("1. Normal Attack")
        print("2. Special Attack")
        print("3. Try to Escape (2d20 Damage on Failure)\n")
        key = input("")
        if key == "1":
            print("\n"+ PlayerCharacter.get_name(PC) + " attacks " + Enemy.get_name(TestEnemy) + "!")
            time.sleep(2)
            roll = randrange(1,20)
            rollbonus = PlayerCharacter.get_attackModifier(PC)
            rollTotal = roll + rollbonus
            enemyAC = Enemy.get_ArmourClass(TestEnemy)
            if rollTotal >= enemyAC:
                print("The attack hits!")
                time.sleep(2)
                dmgroll1 = randrange(1, 20)
                dmgroll2 = randrange(1, 20)
                totaldmg = dmgroll1 * 3 + dmgroll2 * 3 + ( 2 *  Stage.get_number(TestStage1))
                print(PlayerCharacter.get_name(PC) + " hits " + Enemy.get_name(TestEnemy) + " for " + str(totaldmg) + " total damage.")
                newenemyHealth = Enemy.get_Health(TestEnemy) - totaldmg
                Enemy.set_Health(TestEnemy, newenemyHealth)
                time.sleep(2)
                clear()
                BattleStatus()
                if totaldmg > Enemy.get_Health(TestEnemy):
                    newEnemyHealth = Enemy.get_Health(TestEnemy) - totaldmg
                    Enemy.set_Health(TestEnemy, newEnemyHealth)
                    #clear()
                    #BattleStatus()
                    print(PartyMember.get_name(NPC3) + " slayed " + Enemy.get_name(TestEnemy) + ".")
                    time.sleep(4)
                    enemyDied()
                time.sleep(5)
                clear()

                ##############################TestBattle1_Phase5()#############################################
            else:
                print("The attack misses!")
                time.sleep(2)
                ################################TestBattle1_Phase5()#############################################



        if key == "2":
            clear()
            NPC1isAlive = PartyMember.get_isAlive(NPC1)
            NPC2isAlive = PartyMember.get_isAlive(NPC2)
            NPC3isAlive = PartyMember.get_isAlive(NPC3)
            print("Available Special Attacks: ")
            print("Special Points: " + str(PlayerCharacter.get_SpecialPoints(PC)) + "\n\n")
            if PartyMember.get_SpecSlot1Name(NPC1) != "None" and NPC1isAlive == True:
                print(PartyMember.get_name(NPC1) + ": " + PartyMember.get_SpecSlot1Name(NPC1))
                print("Cost: " + str(PartyMember.get_SpecSlot1Cost(NPC1)) + "  Damage: " + str(
                    PartyMember.get_SpecSlot1Damage(NPC1)))
                print("Accuracy: " + str(PartyMember.get_SpecSlot1Prob(NPC1)))
                print(PartyMember.get_SpecSlot1Desc(NPC1))
                print("Sacred Number:")
                print(str(PartyMember.get_SpecSlot1Num(NPC1)))

            print("\n")
            if PartyMember.get_SpecSlot1Name(NPC2) != "None" and NPC2isAlive == True:
                print(PartyMember.get_name(NPC2) + ": " + PartyMember.get_SpecSlot1Name(NPC2))
                print("Cost: " + str(PartyMember.get_SpecSlot1Cost(NPC2)) + "  Damage: " + str(
                    PartyMember.get_SpecSlot1Damage(NPC2)))
                print("Accuracy: " + str(PartyMember.get_SpecSlot1Prob(NPC2)))
                print(PartyMember.get_SpecSlot1Desc(NPC2))
                print("Sacred Number: ")
                print(str(PartyMember.get_SpecSlot1Num(NPC2)))
            print("\n")
            if PartyMember.get_SpecSlot1Name(NPC3) != "None" and NPC3isAlive == True:
                print(PartyMember.get_name(NPC3) + ": " + PartyMember.get_SpecSlot1Name(NPC3))
                print("Cost: " + str(PartyMember.get_SpecSlot1Cost(NPC3)) + "  Damage: " + str(
                    PartyMember.get_SpecSlot1Damage(NPC3)))
                print("Accuracy: " + str(PartyMember.get_SpecSlot1Prob(NPC3)))
                print(PartyMember.get_SpecSlot1Desc(NPC3))
                print("Sacred Number: ")
                print(str(PartyMember.get_SpecSlot1Num(NPC3)))



            print("\n\n1. Use a Special Attack")
            print("2. Normal Attack")
            print("3. Try to Escape (2d20 Damage on Failure)")

            key = input("")
            if key == "1":
                print("\nPlease type the exact 'Sacred Number' of the Special Attack to use: ")
                key = int(input(""))


                ## HOLY STRIKE CAST
                if key == 77:
                    if PlayerCharacter.get_SpecialPoints(PC) >= SpecialMoves.get_cost(HolyStrike):
                        newSP = PlayerCharacter.get_SpecialPoints(PC) - SpecialMoves.get_cost(HolyStrike)
                        PlayerCharacter.set_SpecialPoints(PC, newSP)

                        #NPC1
                        if PartyMember.get_SpecSlot1Name(NPC1) == "Holy Strike":
                            clear()
                            BattleStatus()
                            print(PartyMember.get_name(NPC1) + " uses Holy Strike!")
                            time.sleep(5)
                            roll = randrange(1,100)
                            rolltarget = SpecialMoves.get_probability(HolyStrike) - enemyACdivision
                            if roll <= rolltarget:
                                damage = SpecialMoves.get_damage(HolyStrike)
                                modifier = PartyMember.get_AttackModifier(NPC1)
                                dmgtotal = damage + modifier
                                clear()
                                BattleStatus()
                                print("Holy Strike hits for " + str(dmgtotal) + "!")
                                time.sleep(5)
                                newEnemyHealth = Enemy.get_Health(TestEnemy) - dmgtotal
                                Enemy.set_Health(TestEnemy, newEnemyHealth)
                                ##########################TestBattle1_Phase5()#################################
                            else:
                                clear()
                                BattleStatus()
                                print("Holy Strikes misses!")
                                time.sleep(5)
                                #############################TestBattle1_Phase5()#############################
                        #NPC2
                        elif PartyMember.get_SpecSlot1Name(NPC2) == "Holy Strike":
                            clear()
                            BattleStatus()
                            print(PartyMember.get_name(NPC2) + " uses Holy Strike!")
                            time.sleep(5)
                            roll = randrange(1,100)
                            rolltarget = SpecialMoves.get_probability(HolyStrike) - enemyACdivision
                            if roll <= rolltarget:
                                damage = SpecialMoves.get_damage(HolyStrike)
                                modifier = PartyMember.get_AttackModifier(NPC2)
                                dmgtotal = damage + modifier
                                clear()
                                BattleStatus()
                                print("Holy Strike hits for " + str(dmgtotal) + "!")
                                time.sleep(5)
                                newEnemyHealth = Enemy.get_Health(TestEnemy) - dmgtotal
                                Enemy.set_Health(TestEnemy, newEnemyHealth)
                                #############################TestBattle1_Phase5()#############################
                            else:
                                clear()
                                BattleStatus()
                                print("Holy Strikes misses!")
                                time.sleep(5)
                                #############################TestBattle1_Phase5()#############################
                        # NPC3
                        elif PartyMember.get_SpecSlot1Name(NPC3) == "Holy Strike":
                            clear()
                            BattleStatus()
                            print(PartyMember.get_name(NPC3) + " uses Holy Strike!")
                            time.sleep(5)
                            roll = randrange(1,100)
                            rolltarget = SpecialMoves.get_probability(HolyStrike) - enemyACdivision
                            if roll <= rolltarget:
                                damage = SpecialMoves.get_damage(HolyStrike)
                                modifier = PartyMember.get_AttackModifier(NPC3)
                                dmgtotal = damage + modifier
                                clear()
                                BattleStatus()
                                print("Holy Strike hits for " + str(dmgtotal) + "!")
                                time.sleep(5)
                                newEnemyHealth = Enemy.get_Health(TestEnemy) - dmgtotal
                                Enemy.set_Health(TestEnemy, newEnemyHealth)
                                #############################TestBattle1_Phase5()#############################
                            else:
                                clear()
                                BattleStatus()
                                print("Holy Strikes misses!")
                                time.sleep(5)
                                #############################TestBattle1_Phase5()#############################
                        else:
                            clear()
                            BattleStatus()
                            print("Somebody in the party used Holy Strike!")
                            roll = randrange(1, 100)
                            rolltarget = SpecialMoves.get_probability(HolyStrike)  - enemyACdivision
                            if roll <= rolltarget:
                                damage = SpecialMoves.get_damage(HolyStrike)
                                modifier = 0
                                dmgtotal = damage + modifier
                                clear()
                                BattleStatus()
                                print("Holy Strike hits for " + str(dmgtotal) + "!")
                                time.sleep(5)
                                newEnemyHealth = Enemy.get_Health(TestEnemy) - dmgtotal
                                Enemy.set_Health(TestEnemy, newEnemyHealth)
                                #############################TestBattle1_Phase5()#############################
                            else:
                                clear()
                                BattleStatus()
                                print("Holy Strikes misses!")
                                time.sleep(5)
                                #############################TestBattle1_Phase5()#############################

                ## IRON MASTERY CAST
                if key == 25:
                    if PlayerCharacter.get_SpecialPoints(PC) >= SpecialMoves.get_cost(IronMastery):
                        newSP = PlayerCharacter.get_SpecialPoints(PC) - SpecialMoves.get_cost(IronMastery)
                        PlayerCharacter.set_SpecialPoints(PC, newSP)

                        # NPC1
                        if PartyMember.get_SpecSlot1Name(NPC1) == "Iron Mastery":
                            clear()
                            BattleStatus()
                            print(PartyMember.get_name(NPC1) + " uses Iron Mastery!")
                            time.sleep(5)
                            roll = randrange(1, 100)
                            rolltarget = SpecialMoves.get_probability(IronMastery) - enemyACdivision
                            if roll <= rolltarget:
                                damage = SpecialMoves.get_damage(IronMastery)
                                modifier = PartyMember.get_AttackModifier(NPC1)
                                dmgtotal = damage + modifier
                                clear()
                                BattleStatus()
                                print("Iron Mastery hits for " + str(dmgtotal) + "!")
                                time.sleep(5)
                                newEnemyHealth = Enemy.get_Health(TestEnemy) - dmgtotal
                                Enemy.set_Health(TestEnemy, newEnemyHealth)
                                #############################TestBattle1_Phase5()#############################
                            else:
                                clear()
                                BattleStatus()
                                print("Iron Mastery misses!")
                                time.sleep(5)
                                #############################TestBattle1_Phase5()#############################
                        # NPC2
                        elif PartyMember.get_SpecSlot1Name(NPC2) == "Iron Mastery":
                            clear()
                            BattleStatus()
                            print(PartyMember.get_name(NPC2) + " uses Iron Mastery!")
                            time.sleep(5)
                            roll = randrange(1, 100)
                            rolltarget = SpecialMoves.get_probability(IronMastery) - enemyACdivision
                            if roll <= rolltarget:
                                damage = SpecialMoves.get_damage(IronMastery)
                                modifier = PartyMember.get_AttackModifier(NPC2)
                                dmgtotal = damage + modifier
                                clear()
                                BattleStatus()
                                print("Iron Mastery hits for " + str(dmgtotal) + "!")
                                time.sleep(5)
                                newEnemyHealth = Enemy.get_Health(TestEnemy) - dmgtotal
                                Enemy.set_Health(TestEnemy, newEnemyHealth)
                                #############################TestBattle1_Phase5()#############################
                            else:
                                clear()
                                BattleStatus()
                                print("Holy Strikes misses!")
                                time.sleep(5)
                                #############################TestBattle1_Phase5()#############################
                        # NPC3
                        elif PartyMember.get_SpecSlot1Name(NPC3) == "Iron Mastery":
                            clear()
                            BattleStatus()
                            print(PartyMember.get_name(NPC3) + " uses Iron Mastery!")
                            time.sleep(5)
                            roll = randrange(1, 100)
                            rolltarget = SpecialMoves.get_probability(IronMastery) - enemyACdivision
                            if roll <= rolltarget:
                                damage = SpecialMoves.get_damage(IronMastery)
                                modifier = PartyMember.get_AttackModifier(NPC3)
                                dmgtotal = damage + modifier
                                clear()
                                BattleStatus()
                                print("Iron Mastery hits for " + str(dmgtotal) + "!")
                                time.sleep(5)
                                newEnemyHealth = Enemy.get_Health(TestEnemy) - dmgtotal
                                Enemy.set_Health(TestEnemy, newEnemyHealth)
                                #############################TestBattle1_Phase5()#############################
                            else:
                                clear()
                                BattleStatus()
                                print("Iron Mastery misses!")
                                time.sleep(5)
                                #############################TestBattle1_Phase5()#############################
                        else:
                            clear()
                            BattleStatus()
                            print("Somebody in the party used Iron Mastery!")
                            roll = randrange(1, 100)
                            rolltarget = SpecialMoves.get_probability(IronMastery) - enemyACdivision
                            if roll <= rolltarget:
                                damage = SpecialMoves.get_damage(IronMastery)
                                modifier = 0
                                dmgtotal = damage + modifier
                                clear()
                                BattleStatus()
                                print("Iron Mastery hits for " + str(dmgtotal) + "!")
                                time.sleep(5)
                                newEnemyHealth = Enemy.get_Health(TestEnemy) - dmgtotal
                                Enemy.set_Health(TestEnemy, newEnemyHealth)
                                #############################TestBattle1_Phase5()#############################
                            else:
                                clear()
                                BattleStatus()
                                print("Iron Mastery misses!")
                                time.sleep(5)
                                #############################TestBattle1_Phase5()#############################

                ## Fire Strike
                if key == 82:
                    if PlayerCharacter.get_SpecialPoints(PC) >= SpecialMoves.get_cost(FireStrike):
                        newSP = PlayerCharacter.get_SpecialPoints(PC) - SpecialMoves.get_cost(
                            FireStrike)
                        PlayerCharacter.set_SpecialPoints(PC, newSP)

                        # NPC1
                        if PartyMember.get_SpecSlot1Name(NPC1) == "Fire Strike":
                            clear()
                            BattleStatus()
                            print(PartyMember.get_name(NPC1) + " uses Fire Strike!")
                            time.sleep(5)
                            roll = randrange(1, 100)
                            rolltarget = SpecialMoves.get_probability(FireStrike) - enemyACdivision
                            if roll <= rolltarget:
                                damage = SpecialMoves.get_damage(FireStrike)
                                modifier = PartyMember.get_AttackModifier(NPC1)
                                dmgtotal = damage + modifier
                                clear()
                                BattleStatus()
                                print("Fire Strike hits for " + str(dmgtotal) + "!")
                                time.sleep(5)
                                newEnemyHealth = Enemy.get_Health(TestEnemy) - dmgtotal
                                Enemy.set_Health(TestEnemy, newEnemyHealth)
                                #############################TestBattle1_Phase5()#############################
                            else:
                                clear()
                                BattleStatus()
                                print("Fire Strike misses!")
                                time.sleep(5)
                                #############################TestBattle1_Phase5()#############################
                        # NPC2
                        elif PartyMember.get_SpecSlot1Name(NPC2) == "Fire Strike":
                            clear()
                            BattleStatus()
                            print(PartyMember.get_name(NPC2) + " uses Fire Strike!")
                            time.sleep(5)
                            roll = randrange(1, 100)
                            rolltarget = SpecialMoves.get_probability(FireStrike) - enemyACdivision
                            if roll <= rolltarget:
                                damage = SpecialMoves.get_damage(FireStrike)
                                modifier = PartyMember.get_AttackModifier(NPC2)
                                dmgtotal = damage + modifier
                                clear()
                                BattleStatus()
                                print("Fire Strike hits for " + str(dmgtotal) + "!")
                                time.sleep(5)
                                newEnemyHealth = Enemy.get_Health(TestEnemy) - dmgtotal
                                Enemy.set_Health(TestEnemy, newEnemyHealth)
                                #############################TestBattle1_Phase5()#############################
                            else:
                                clear()
                                BattleStatus()
                                print("Fire Strike misses!")
                                time.sleep(5)
                                #############################TestBattle1_Phase5()#############################
                        # NPC3
                        elif PartyMember.get_SpecSlot1Name(NPC3) == "Fire Strike":
                            clear()
                            BattleStatus()
                            print(PartyMember.get_name(NPC3) + " uses Fire Strike!")
                            time.sleep(5)
                            roll = randrange(1, 100)
                            rolltarget = SpecialMoves.get_probability(FireStrike) - enemyACdivision
                            if roll <= rolltarget:
                                damage = SpecialMoves.get_damage(FireStrike)
                                modifier = PartyMember.get_AttackModifier(NPC3)
                                dmgtotal = damage + modifier
                                clear()
                                BattleStatus()
                                print("Fire Strike hits for " + str(dmgtotal) + "!")
                                time.sleep(5)
                                newEnemyHealth = Enemy.get_Health(TestEnemy) - dmgtotal
                                Enemy.set_Health(TestEnemy, newEnemyHealth)
                                #############################TestBattle1_Phase5()#############################
                            else:
                                clear()
                                BattleStatus()
                                print("Fire Strike misses!")
                                time.sleep(5)
                                #############################TestBattle1_Phase5()#############################
                        else:
                            clear()
                            BattleStatus()
                            print("Somebody in the party used Fire Strike")
                            roll = randrange(1, 100)
                            rolltarget = SpecialMoves.get_probability(IronMastery) - enemyACdivision
                            if roll <= rolltarget:
                                damage = SpecialMoves.get_damage(IronMastery)
                                modifier = 0
                                dmgtotal = damage + modifier
                                clear()
                                BattleStatus()
                                print("Fire Strike hits for " + str(dmgtotal) + "!")
                                time.sleep(5)
                                newEnemyHealth = Enemy.get_Health(TestEnemy) - dmgtotal
                                Enemy.set_Health(TestEnemy, newEnemyHealth)
                                #############################TestBattle1_Phase5()#############################
                            else:
                                clear()
                                BattleStatus()
                                print("Fire Strike misses!")
                                time.sleep(5)
                                #############################TestBattle1_Phase5()#############################

                ## Sleeping God
                if key == 99999:
                    if PlayerCharacter.get_SpecialPoints(PC) >= SpecialMoves.get_cost(SleepingGod):
                        newSP = PlayerCharacter.get_SpecialPoints(PC) - SpecialMoves.get_cost(
                            SleepingGod)
                        PlayerCharacter.set_SpecialPoints(PC, newSP)

                        # NPC1
                        if PartyMember.get_SpecSlot1Name(NPC1) == "Sleeping God":
                            clear()
                            BattleStatus()
                            print(PartyMember.get_name(NPC1) + " uses Sleeping God!")
                            time.sleep(5)
                            roll = randrange(1, 100)
                            rolltarget = SpecialMoves.get_probability(SleepingGod) - enemyACdivision
                            if roll <= rolltarget:
                                damage = SpecialMoves.get_damage(SleepingGod)
                                modifier = PartyMember.get_AttackModifier(NPC1)
                                dmgtotal = damage + modifier
                                clear()
                                BattleStatus()
                                print("Sleeping God hits for " + str(dmgtotal) + "!")
                                time.sleep(5)
                                newEnemyHealth = Enemy.get_Health(TestEnemy) - dmgtotal
                                Enemy.set_Health(TestEnemy, newEnemyHealth)
                                #############################TestBattle1_Phase5()#############################
                            else:
                                clear()
                                BattleStatus()
                                print("Sleeping God misses!")
                                time.sleep(5)
                                #############################TestBattle1_Phase5()#############################
                        # NPC2
                        elif PartyMember.get_SpecSlot1Name(NPC2) == "Sleeping God":
                            clear()
                            BattleStatus()
                            print(PartyMember.get_name(NPC2) + " uses Sleeping God!")
                            time.sleep(5)
                            roll = randrange(1, 100)
                            rolltarget = SpecialMoves.get_probability(SleepingGod) - enemyACdivision
                            if roll <= rolltarget:
                                damage = SpecialMoves.get_damage(SleepingGod)
                                modifier = PartyMember.get_AttackModifier(NPC2)
                                dmgtotal = damage + modifier
                                clear()
                                BattleStatus()
                                print("Sleeping God hits for " + str(dmgtotal) + "!")
                                time.sleep(5)
                                newEnemyHealth = Enemy.get_Health(TestEnemy) - dmgtotal
                                Enemy.set_Health(TestEnemy, newEnemyHealth)
                                #############################TestBattle1_Phase5()#############################
                            else:
                                clear()
                                BattleStatus()
                                print("Sleeping God misses!")
                                time.sleep(5)
                                #############################TestBattle1_Phase5()#############################
                        # NPC3
                        elif PartyMember.get_SpecSlot1Name(NPC3) == "Sleeping God":
                            clear()
                            BattleStatus()
                            print(PartyMember.get_name(NPC3) + " uses Sleeping God!")
                            time.sleep(5)
                            roll = randrange(1, 100)
                            rolltarget = SpecialMoves.get_probability(SleepingGod) - enemyACdivision
                            if roll <= rolltarget:
                                damage = SpecialMoves.get_damage(SleepingGod)
                                modifier = PartyMember.get_AttackModifier(NPC3)
                                dmgtotal = damage + modifier
                                clear()
                                BattleStatus()
                                print("Sleeping God hits for " + str(dmgtotal) + "!")
                                time.sleep(5)
                                newEnemyHealth = Enemy.get_Health(TestEnemy) - dmgtotal
                                Enemy.set_Health(TestEnemy, newEnemyHealth)
                                #############################TestBattle1_Phase5()#############################
                            else:
                                clear()
                                BattleStatus()
                                print("Sleeping God misses!")
                                time.sleep(5)
                                #############################TestBattle1_Phase5()#############################
                        else:
                            clear()
                            BattleStatus()
                            print("Somebody in the party used Sleeping God")
                            roll = randrange(1, 100)
                            rolltarget = SpecialMoves.get_probability(SleepingGod) - enemyACdivision
                            if roll <= rolltarget:
                                damage = SpecialMoves.get_damage(SleepingGod)
                                modifier = 0
                                dmgtotal = damage + modifier
                                clear()
                                BattleStatus()
                                print("Sleeping God hits for " + str(dmgtotal) + "!")
                                time.sleep(5)
                                newEnemyHealth = Enemy.get_Health(TestEnemy) - dmgtotal
                                Enemy.set_Health(TestEnemy, newEnemyHealth)
                                #############################TestBattle1_Phase5()#############################
                            else:
                                clear()
                                BattleStatus()
                                print("Sleeping God misses!")
                                time.sleep(5)
                                #############################TestBattle1_Phase5()#############################

                ## DemonMagic
                if key == 666:
                    if PlayerCharacter.get_SpecialPoints(PC) >= SpecialMoves.get_cost(DemonMagic):
                        newSP = PlayerCharacter.get_SpecialPoints(PC) - SpecialMoves.get_cost(
                            DemonMagic)
                        PlayerCharacter.set_SpecialPoints(PC, newSP)

                        # NPC1
                        if PartyMember.get_SpecSlot1Name(NPC1) == "Demon Magic":
                            clear()
                            BattleStatus()
                            print(PartyMember.get_name(NPC1) + " uses Demon Magic!")
                            time.sleep(5)
                            roll = randrange(1, 100)
                            rolltarget = SpecialMoves.get_probability(DemonMagic) - enemyACdivision
                            if roll <= rolltarget:
                                damage = SpecialMoves.get_damage(DemonMagic)
                                modifier = PartyMember.get_AttackModifier(NPC1)
                                dmgtotal = damage + modifier
                                clear()
                                BattleStatus()
                                print("Demon Magic hits for " + str(dmgtotal) + "!")
                                time.sleep(5)
                                newEnemyHealth = Enemy.get_Health(TestEnemy) - dmgtotal
                                Enemy.set_Health(TestEnemy, newEnemyHealth)
                                #############################TestBattle1_Phase5()#############################
                            else:
                                clear()
                                BattleStatus()
                                print("Demon Magic misses!")
                                time.sleep(5)
                                #############################TestBattle1_Phase5()#############################
                        # NPC2
                        elif PartyMember.get_SpecSlot1Name(NPC2) == "Demon Magic":
                            clear()
                            BattleStatus()
                            print(PartyMember.get_name(NPC2) + " uses Demon Magic!")
                            time.sleep(5)
                            roll = randrange(1, 100)
                            rolltarget = SpecialMoves.get_probability(DemonMagic) - enemyACdivision
                            if roll <= rolltarget:
                                damage = SpecialMoves.get_damage(DemonMagic)
                                modifier = PartyMember.get_AttackModifier(NPC2)
                                dmgtotal = damage + modifier
                                clear()
                                BattleStatus()
                                print("Demon Magic hits for " + str(dmgtotal) + "!")
                                time.sleep(5)
                                newEnemyHealth = Enemy.get_Health(TestEnemy) - dmgtotal
                                Enemy.set_Health(TestEnemy, newEnemyHealth)
                                #############################TestBattle1_Phase5()#############################
                            else:
                                clear()
                                BattleStatus()
                                print("Demon Magic misses!")
                                time.sleep(5)
                                #############################TestBattle1_Phase5()#############################
                        # NPC3
                        elif PartyMember.get_SpecSlot1Name(NPC3) == "Demon Magic":
                            clear()
                            BattleStatus()
                            print(PartyMember.get_name(NPC3) + " uses Demon Magic!")
                            time.sleep(5)
                            roll = randrange(1, 100)
                            rolltarget = SpecialMoves.get_probability(DemonMagic) - enemyACdivision
                            if roll <= rolltarget:
                                damage = SpecialMoves.get_damage(DemonMagic)
                                modifier = PartyMember.get_AttackModifier(NPC3)
                                dmgtotal = damage + modifier
                                clear()
                                BattleStatus()
                                print("Demon Magic hits for " + str(dmgtotal) + "!")
                                time.sleep(5)
                                newEnemyHealth = Enemy.get_Health(TestEnemy) - dmgtotal
                                Enemy.set_Health(TestEnemy, newEnemyHealth)

                                #############################TestBattle1_Phase5()#############################
                            else:
                                clear()
                                BattleStatus()
                                print("Demon Magic misses!")
                                time.sleep(5)
                                #############################TestBattle1_Phase5()#############################
                        else:
                            clear()
                            BattleStatus()
                            print("Somebody in the party used Demon Magic")
                            roll = randrange(1, 100)
                            rolltarget = SpecialMoves.get_probability(DemonMagic) - enemyACdivision
                            if roll <= rolltarget:
                                damage = SpecialMoves.get_damage(DemonMagic)
                                modifier = 0
                                dmgtotal = damage + modifier
                                clear()
                                BattleStatus()
                                print("Demon Magic hits for " + str(dmgtotal) + "!")
                                time.sleep(5)
                                newEnemyHealth = Enemy.get_Health(TestEnemy) - dmgtotal
                                Enemy.set_Health(TestEnemy, newEnemyHealth)
                                #############################TestBattle1_Phase5()#############################
                            else:
                                clear()
                                BattleStatus()
                                print("Demon Magic misses!")
                                time.sleep(5)
                                #############################estBattle1_Phase5()#############################

                ## AnimalFamiliar
                if key == 35:
                    if PlayerCharacter.get_SpecialPoints(PC) >= SpecialMoves.get_cost(AnimalFamiliar):
                        newSP = PlayerCharacter.get_SpecialPoints(PC) - SpecialMoves.get_cost(
                            AnimalFamiliar)
                        PlayerCharacter.set_SpecialPoints(PC, newSP)

                        # NPC1
                        if PartyMember.get_SpecSlot1Name(NPC1) == "Animal Familiar":
                            clear()
                            BattleStatus()
                            print(PartyMember.get_name(NPC1) + " uses Animal Familiar!")
                            time.sleep(5)
                            roll = randrange(1, 100)
                            rolltarget = SpecialMoves.get_probability(AnimalFamiliar) - enemyACdivision
                            if roll <= rolltarget:
                                damage = SpecialMoves.get_damage(AnimalFamiliar)
                                modifier = PartyMember.get_AttackModifier(NPC1)
                                dmgtotal = damage + modifier
                                clear()
                                BattleStatus()
                                print("Animal Familiar hits for " + str(dmgtotal) + "!")
                                time.sleep(5)
                                newEnemyHealth = Enemy.get_Health(TestEnemy) - dmgtotal
                                Enemy.set_Health(TestEnemy, newEnemyHealth)

                                #############################TestBattle1_Phase5()#############################
                            else:
                                clear()
                                BattleStatus()
                                print("Animal Familiar misses!")
                                time.sleep(5)
                                #############################TestBattle1_Phase5()#############################
                        # NPC2
                        elif PartyMember.get_SpecSlot1Name(NPC2) == "Animal Familiar":
                            clear()
                            BattleStatus()
                            print(PartyMember.get_name(NPC2) + " uses Animal Familiar!")
                            time.sleep(5)
                            roll = randrange(1, 100)
                            rolltarget = SpecialMoves.get_probability(AnimalFamiliar) - enemyACdivision
                            if roll <= rolltarget:
                                damage = SpecialMoves.get_damage(AnimalFamiliar)
                                modifier = PartyMember.get_AttackModifier(NPC2)
                                dmgtotal = damage + modifier
                                clear()
                                BattleStatus()
                                print("Animal Familiar hits for " + str(dmgtotal) + "!")
                                time.sleep(5)
                                newEnemyHealth = Enemy.get_Health(TestEnemy) - dmgtotal
                                Enemy.set_Health(TestEnemy, newEnemyHealth)

                                #############################TestBattle1_Phase5()#############################
                            else:
                                clear()
                                BattleStatus()
                                print("Animal Familiar misses!")
                                time.sleep(5)
                                #############################TestBattle1_Phase5()#############################
                        # NPC3
                        elif PartyMember.get_SpecSlot1Name(NPC3) == "Animal Familiar":
                            clear()
                            BattleStatus()
                            print(PartyMember.get_name(NPC3) + " uses Animal Familiar!")
                            time.sleep(5)
                            roll = randrange(1, 100)
                            rolltarget = SpecialMoves.get_probability(AnimalFamiliar) - enemyACdivision
                            if roll <= rolltarget:
                                damage = SpecialMoves.get_damage(AnimalFamiliar)
                                modifier = PartyMember.get_AttackModifier(NPC3)
                                dmgtotal = damage + modifier
                                clear()
                                BattleStatus()
                                print("Animal Familiar hits for " + str(dmgtotal) + "!")
                                time.sleep(5)
                                newEnemyHealth = Enemy.get_Health(TestEnemy) - dmgtotal
                                Enemy.set_Health(TestEnemy, newEnemyHealth)
                                #############################TestBattle1_Phase5()#############################
                            else:
                                clear()
                                BattleStatus()
                                print("Animal Familiar misses!")
                                time.sleep(5)
                                #############################TestBattle1_Phase5()#############################
                        else:
                            clear()
                            BattleStatus()
                            print("Somebody in the party used Animal Familiar")
                            roll = randrange(1, 100)
                            rolltarget = SpecialMoves.get_probability(AnimalFamiliar) - enemyACdivision
                            if roll <= rolltarget:
                                damage = SpecialMoves.get_damage(AnimalFamiliar)
                                modifier = 0
                                dmgtotal = damage + modifier
                                clear()
                                BattleStatus()
                                print("Animal Familiar hits for " + str(dmgtotal) + "!")
                                time.sleep(5)
                                newEnemyHealth = Enemy.get_Health(TestEnemy) - dmgtotal
                                Enemy.set_Health(TestEnemy, newEnemyHealth)
                                #############################TestBattle1_Phase5()#############################
                            else:
                                clear()
                                BattleStatus()
                                print("Animal Familiar misses!")
                                time.sleep(5)
                                #############################TestBattle1_Phase5()#############################

                ## WaterChain
                if key == 22:
                    if PlayerCharacter.get_SpecialPoints(PC) >= SpecialMoves.get_cost(
                            WaterChain):
                        newSP = PlayerCharacter.get_SpecialPoints(PC) - SpecialMoves.get_cost(
                            WaterChain)
                        PlayerCharacter.set_SpecialPoints(PC, newSP)

                        # NPC1
                        if PartyMember.get_SpecSlot1Name(NPC1) == "Water Chain":
                            clear()
                            BattleStatus()
                            print(PartyMember.get_name(NPC1) + " uses Water Chain!")
                            time.sleep(5)
                            roll = randrange(1, 100)
                            rolltarget = SpecialMoves.get_probability(WaterChain) - enemyACdivision
                            if roll <= rolltarget:
                                damage = SpecialMoves.get_damage(WaterChain)
                                modifier = PartyMember.get_AttackModifier(NPC1)
                                dmgtotal = damage + modifier
                                clear()
                                BattleStatus()
                                print("Water Chain hits for " + str(dmgtotal) + "!")
                                time.sleep(5)
                                newEnemyHealth = Enemy.get_Health(TestEnemy) - dmgtotal
                                Enemy.set_Health(TestEnemy, newEnemyHealth)
                                CurrentTurn = Enemy.get_BattleTurn(TestEnemy)
                                #############################TestBattle1_Phase5()#############################
                            else:
                                clear()
                                BattleStatus()
                                print("Water Chain misses!")
                                time.sleep(5)
                                #############################TestBattle1_Phase5()#############################
                        # NPC2
                        elif PartyMember.get_SpecSlot1Name(NPC2) == "Water Chain":
                            clear()
                            BattleStatus()
                            print(PartyMember.get_name(NPC2) + " uses Water Chain!")
                            time.sleep(5)
                            roll = randrange(1, 100)
                            rolltarget = SpecialMoves.get_probability(WaterChain) - enemyACdivision
                            if roll <= rolltarget:
                                damage = SpecialMoves.get_damage(WaterChain)
                                modifier = PartyMember.get_AttackModifier(NPC2)
                                dmgtotal = damage + modifier
                                clear()
                                BattleStatus()
                                print("Water Chain hits for " + str(dmgtotal) + "!")
                                time.sleep(5)
                                newEnemyHealth = Enemy.get_Health(TestEnemy) - dmgtotal
                                Enemy.set_Health(TestEnemy, newEnemyHealth)
                                #############################TestBattle1_Phase5()#############################
                            else:
                                clear()
                                BattleStatus()
                                print("Water Chain misses!")
                                time.sleep(5)
                                #############################TestBattle1_Phase5()#############################
                        # NPC3
                        elif PartyMember.get_SpecSlot1Name(NPC3) == "Water Chain":
                            clear()
                            BattleStatus()
                            print(PartyMember.get_name(NPC3) + " uses Water Chain!")
                            time.sleep(5)
                            roll = randrange(1, 100)
                            rolltarget = SpecialMoves.get_probability(WaterChain) - enemyACdivision
                            if roll <= rolltarget:
                                damage = SpecialMoves.get_damage(WaterChain)
                                modifier = PartyMember.get_AttackModifier(NPC3)
                                dmgtotal = damage + modifier
                                clear()
                                BattleStatus()
                                print("Water Chain hits for " + str(dmgtotal) + "!")
                                time.sleep(5)
                                newEnemyHealth = Enemy.get_Health(TestEnemy) - dmgtotal
                                Enemy.set_Health(TestEnemy, newEnemyHealth)

                                #############################TestBattle1_Phase5()#############################
                            else:
                                clear()
                                BattleStatus()
                                print("Water Chain misses!")
                                time.sleep(5)

                                #############################TestBattle1_Phase5()#############################
                        else:
                            clear()
                            BattleStatus()
                            print("Somebody in the party used Water Chain")
                            roll = randrange(1, 100)
                            rolltarget = SpecialMoves.get_probability(WaterChain) - enemyACdivision
                            if roll <= rolltarget:
                                damage = SpecialMoves.get_damage(WaterChain)
                                modifier = 0
                                dmgtotal = damage + modifier
                                clear()
                                BattleStatus()
                                print("Water Chain hits for " + str(dmgtotal) + "!")
                                time.sleep(5)
                                newEnemyHealth = Enemy.get_Health(TestEnemy) - dmgtotal
                                Enemy.set_Health(TestEnemy, newEnemyHealth)
                                #############################TestBattle1_Phase5()#############################
                            else:
                                clear()
                                BattleStatus()
                                print("Water Chain misses!")
                                time.sleep(5)
                                #############################TestBattle1_Phase5()#############################

                ## PsychicBomb
                if key == 4444:
                    if PlayerCharacter.get_SpecialPoints(PC) >= SpecialMoves.get_cost(
                            PsychicBomb):
                        newSP = PlayerCharacter.get_SpecialPoints(PC) - SpecialMoves.get_cost(
                            PsychicBomb)
                        PlayerCharacter.set_SpecialPoints(PC, newSP)

                        # NPC1
                        if PartyMember.get_SpecSlot1Name(NPC1) == "Psychic Bomb":
                            clear()
                            BattleStatus()
                            print(PartyMember.get_name(NPC1) + " uses Psychic Bomb!")
                            time.sleep(5)
                            roll = randrange(1, 100)
                            rolltarget = SpecialMoves.get_probability(PsychicBomb) - enemyACdivision
                            if roll <= rolltarget:
                                damage = SpecialMoves.get_damage(PsychicBomb)
                                modifier = PartyMember.get_AttackModifier(NPC1)
                                dmgtotal = damage + modifier
                                clear()
                                BattleStatus()
                                print("Psychic Bomb hits for " + str(dmgtotal) + "!")
                                time.sleep(5)
                                newEnemyHealth = Enemy.get_Health(TestEnemy) - dmgtotal
                                Enemy.set_Health(TestEnemy, newEnemyHealth)
                                #############################TestBattle1_Phase5()#############################
                            else:
                                clear()
                                BattleStatus()
                                print("Psychic Bomb misses!")
                                time.sleep(5)
                                #############################TestBattle1_Phase5()#############################
                        # NPC2
                        elif PartyMember.get_SpecSlot1Name(NPC2) == "Psychic Bomb":
                            clear()
                            BattleStatus()
                            print(PartyMember.get_name(NPC2) + " uses Psychic Bomb!")
                            time.sleep(5)
                            roll = randrange(1, 100)
                            rolltarget = SpecialMoves.get_probability(PsychicBomb) - enemyACdivision
                            if roll <= rolltarget:
                                damage = SpecialMoves.get_damage(PsychicBomb)
                                modifier = PartyMember.get_AttackModifier(NPC2)
                                dmgtotal = damage + modifier
                                clear()
                                BattleStatus()
                                print("Psychic Bomb hits for " + str(dmgtotal) + "!")
                                time.sleep(5)
                                newEnemyHealth = Enemy.get_Health(TestEnemy) - dmgtotal
                                Enemy.set_Health(TestEnemy, newEnemyHealth)

                                #############################TestBattle1_Phase5()#############################
                            else:
                                clear()
                                BattleStatus()
                                print("Psychic Bomb misses!")
                                time.sleep(5)

                                #############################TestBattle1_Phase5()#############################
                        # NPC3
                        elif PartyMember.get_SpecSlot1Name(NPC3) == "Psychic Bomb":
                            clear()
                            BattleStatus()
                            print(PartyMember.get_name(NPC3) + " uses Psychic Bomb!")
                            time.sleep(5)
                            roll = randrange(1, 100)
                            rolltarget = SpecialMoves.get_probability(PsychicBomb) - enemyACdivision
                            if roll <= rolltarget:
                                damage = SpecialMoves.get_damage(PsychicBomb)
                                modifier = PartyMember.get_AttackModifier(NPC3)
                                dmgtotal = damage + modifier
                                clear()
                                BattleStatus()
                                print("Psychic Bomb hits for " + str(dmgtotal) + "!")
                                time.sleep(5)
                                newEnemyHealth = Enemy.get_Health(TestEnemy) - dmgtotal
                                Enemy.set_Health(TestEnemy, newEnemyHealth)

                                #############################TestBattle1_Phase5()#############################
                            else:
                                clear()
                                BattleStatus()
                                print("Psychic Bomb misses!")
                                time.sleep(5)

                                #############################TestBattle1_Phase5()#############################
                        else:
                            clear()
                            BattleStatus()
                            print("Somebody in the party used Psychic Bomb")
                            roll = randrange(1, 100)
                            rolltarget = SpecialMoves.get_probability(PsychicBomb) - enemyACdivision
                            if roll <= rolltarget:
                                damage = SpecialMoves.get_damage(PsychicBomb)
                                modifier = 0
                                dmgtotal = damage + modifier
                                clear()
                                BattleStatus()
                                print("Psychic Bomb hits for " + str(dmgtotal) + "!")
                                time.sleep(5)
                                newEnemyHealth = Enemy.get_Health(TestEnemy) - dmgtotal
                                Enemy.set_Health(TestEnemy, newEnemyHealth)

                                #############################TestBattle1_Phase5()#############################
                            else:
                                clear()
                                BattleStatus()
                                print("Psychic Bomb misses!")
                                time.sleep(5)

                                #############################TestBattle1_Phase5()#############################

                ## ShieldBash
                if key == 111:
                    if PlayerCharacter.get_SpecialPoints(PC) >= SpecialMoves.get_cost(
                            ShieldBash):
                        newSP = PlayerCharacter.get_SpecialPoints(PC) - SpecialMoves.get_cost(
                            ShieldBash)
                        PlayerCharacter.set_SpecialPoints(PC, newSP)

                        # NPC1
                        if PartyMember.get_SpecSlot1Name(NPC1) == "Shield Bash":
                            clear()
                            BattleStatus()
                            print(PartyMember.get_name(NPC1) + " uses Shield Bash!")
                            time.sleep(5)
                            roll = randrange(1, 100)
                            rolltarget = SpecialMoves.get_probability(ShieldBash) - enemyACdivision
                            if roll <= rolltarget:
                                damage = SpecialMoves.get_damage(ShieldBash)
                                modifier = PartyMember.get_AttackModifier(NPC1)
                                dmgtotal = damage + modifier
                                clear()
                                BattleStatus()
                                print("Shield Bash hits for " + str(dmgtotal) + "!")
                                time.sleep(5)
                                newEnemyHealth = Enemy.get_Health(TestEnemy) - dmgtotal
                                Enemy.set_Health(TestEnemy, newEnemyHealth)

                                #############################TestBattle1_Phase5()#############################
                            else:
                                clear()
                                BattleStatus()
                                print("Shield Bash misses!")
                                time.sleep(5)

                                #############################TestBattle1_Phase5()#############################
                        # NPC2
                        elif PartyMember.get_SpecSlot1Name(NPC2) == "Shield Bash":
                            clear()
                            BattleStatus()
                            print(PartyMember.get_name(NPC2) + " uses Shield Bash!")
                            time.sleep(5)
                            roll = randrange(1, 100)
                            rolltarget = SpecialMoves.get_probability(ShieldBash) - enemyACdivision
                            if roll <= rolltarget:
                                damage = SpecialMoves.get_damage(ShieldBash)
                                modifier = PartyMember.get_AttackModifier(NPC2)
                                dmgtotal = damage + modifier
                                clear()
                                BattleStatus()
                                print("Shield Bash hits for " + str(dmgtotal) + "!")
                                time.sleep(5)
                                newEnemyHealth = Enemy.get_Health(TestEnemy) - dmgtotal
                                Enemy.set_Health(TestEnemy, newEnemyHealth)

                                #############################TestBattle1_Phase5()#############################
                            else:
                                clear()
                                BattleStatus()
                                print("Shield Bash misses!")
                                time.sleep(5)

                                #############################TestBattle1_Phase5()#############################
                        # NPC3
                        elif PartyMember.get_SpecSlot1Name(NPC3) == "Shield Bash":
                            clear()
                            BattleStatus()
                            print(PartyMember.get_name(NPC3) + " uses Shield Bash!")
                            time.sleep(5)
                            roll = randrange(1, 100)
                            rolltarget = SpecialMoves.get_probability(ShieldBash) - enemyACdivision
                            if roll <= rolltarget:
                                damage = SpecialMoves.get_damage(ShieldBash)
                                modifier = PartyMember.get_AttackModifier(NPC3)
                                dmgtotal = damage + modifier
                                clear()
                                BattleStatus()
                                print("Shield Bash hits for " + str(dmgtotal) + "!")
                                time.sleep(5)
                                newEnemyHealth = Enemy.get_Health(TestEnemy) - dmgtotal
                                Enemy.set_Health(TestEnemy, newEnemyHealth)

                                #############################TestBattle1_Phase5()#############################
                            else:
                                clear()
                                BattleStatus()
                                print("Shield Bash misses!")
                                time.sleep(5)

                                #############################TestBattle1_Phase5()#############################
                        else:
                            clear()
                            BattleStatus()
                            print("Somebody in the party used Shield Bash")
                            roll = randrange(1, 100)
                            rolltarget = SpecialMoves.get_probability(ShieldBash) - enemyACdivision
                            if roll <= rolltarget:
                                damage = SpecialMoves.get_damage(ShieldBash)
                                modifier = 0
                                dmgtotal = damage + modifier
                                clear()
                                BattleStatus()
                                print("Shield Bash hits for " + str(dmgtotal) + "!")
                                time.sleep(5)
                                newEnemyHealth = Enemy.get_Health(TestEnemy) - dmgtotal
                                Enemy.set_Health(TestEnemy, newEnemyHealth)

                                #############################TestBattle1_Phase5()#############################
                            else:
                                clear()
                                BattleStatus()
                                print("Shield Bash misses!")
                                time.sleep(5)
                                #############################TestBattle1_Phase5()#############################


                else:
                    #print("Sorry, input not recognized. ERROR3.")
                    time.sleep(1)

                if key == "3":
                    roll = randrange(1, 100)
                    if roll < 34:
                        clear()
                        LobbyStatus()
                        time.sleep(2)
                        print("You escaped with incident! Must be your lucky day...")
                        time.sleep(3)
                        clear()
                        LobbyStatus()
                        levelUp()
                    else:
                        newPChealth = PlayerCharacter.get_Health(PC) - randrange(1, 20) - randrange(1, 20)
                        PlayerCharacter.set_Health(PC, newPChealth)
                        newNPChealth = PartyMember.get_Health(NPC1) - randrange(1, 20) - randrange(1, 20)
                        PartyMember.set_Health(NPC1, newNPChealth)
                        newNPChealth = PartyMember.get_Health(NPC2) - randrange(1, 20) - randrange(1, 20)
                        PartyMember.set_Health(NPC2, newNPChealth)
                        newNPChealth = PartyMember.get_Health(NPC3) - randrange(1, 20) - randrange(1, 20)
                        PartyMember.set_Health(NPC3, newNPChealth)

                        clear()
                        LobbyStatus()
                        print("You escaped, but were injured in the process.")
                        time.sleep(4)
                        clear()
                        LobbyStatus()
                        levelUp()

            #newenemyHealth = Enemy.get_Health(TestEnemy) - totaldmg
            #Enemy.set_Health(TestEnemy, newenemyHealth)

            if key == "2":
                print(PlayerCharacter.get_name(PC) + " attacks " + Enemy.get_name(TestEnemy) + "!")
                time.sleep(2)
                roll = randrange(1, 20)
                rollbonus = PlayerCharacter.get_attackModifier(PC)
                rollTotal = roll + rollbonus
                enemyAC = Enemy.get_ArmourClass(TestEnemy)
                if rollTotal >= enemyAC:
                    print("The attack hits!")
                    time.sleep(2)
                    dmgroll1 = randrange(1, 20)
                    dmgroll2 = randrange(1, 20)
                    totaldmg = dmgroll1 * 3 + dmgroll2 * 3
                    print(PlayerCharacter.get_name(PC) + " hits " + Enemy.get_name(TestEnemy) + " for " + str(
                        totaldmg) + " total damage.")
                    time.sleep(2)

                    if totaldmg > Enemy.get_Health(TestEnemy):
                        newEnemyHealth = Enemy.get_Health(TestEnemy) - totaldmg
                        Enemy.set_Health(TestEnemy, newEnemyHealth)
                        clear()
                        BattleStatus()
                        print(PartyMember.get_name(NPC2) + " slayed " + Enemy.get_name(TestEnemy) + ".")
                        time.sleep(4)
                        enemyDied()

                    #############################TestBattle1_Phase5()#############################
                else:
                    print("The attack misses!")
                    time.sleep(2)
                    #############################TestBattle1_Phase5()#############################



            if key == "3":
                roll = randrange(1,100)
                if roll < 34:
                    clear()
                    LobbyStatus()
                    time.sleep(2)
                    print("You escaped with incident! Must be your lucky day...")
                    time.sleep(4)
                    clear()
                    LobbyStatus()
                    levelUp()
                else:
                    newPChealth = PlayerCharacter.get_Health(PC) - randrange(1, 20) - randrange(1, 20)
                    PlayerCharacter.set_Health(PC, newPChealth)
                    newNPChealth = PartyMember.get_Health(NPC1) - randrange(1, 20) - randrange(1, 20)
                    PartyMember.set_Health(NPC1, newNPChealth)
                    newNPChealth = PartyMember.get_Health(NPC2) - randrange(1, 20) - randrange(1, 20)
                    PartyMember.set_Health(NPC2, newNPChealth)
                    newNPChealth = PartyMember.get_Health(NPC3) - randrange(1, 20) - randrange(1, 20)
                    PartyMember.set_Health(NPC3, newNPChealth)
                    clear()
                    LobbyStatus()
                    print("You escaped, but were injured in the process.")
                    time.sleep(4)
                    clear()
                    LobbyStatus()
                    levelUp()
        if key == "3":
            roll = randrange(1,100)
            if roll < 34:
                clear()
                LobbyStatus()
                time.sleep(2)
                print("You escaped with incident! Must be your lucky day...")
                time.sleep(4)
                clear()
                LobbyStatus()
                levelUp()
            else:
                newPChealth = PlayerCharacter.get_Health(PC) - randrange(1, 20) - randrange(1, 20)
                PlayerCharacter.set_Health(PC, newPChealth)
                newNPChealth = PartyMember.get_Health(NPC1) - randrange(1, 20) - randrange(1, 20)
                PartyMember.set_Health(NPC1, newNPChealth)
                newNPChealth = PartyMember.get_Health(NPC2) - randrange(1, 20) - randrange(1, 20)
                PartyMember.set_Health(NPC2, newNPChealth)
                newNPChealth = PartyMember.get_Health(NPC3) - randrange(1, 20) - randrange(1, 20)
                PartyMember.set_Health(NPC3, newNPChealth)
                clear()
                LobbyStatus()
                print("You escaped, but were injured in the process.")
                time.sleep(4)
                clear()
                LobbyStatus()
                levelUp()



        clear()
        BattleStatus()
        print("End of Player turn.")
        time.sleep(3)
        clear()



    else:
        print("Battle over!")
        print("")






def EnemyAttackNPC1():
    NPC1isAlive = PartyMember.get_isAlive(NPC1)
    if NPC1isAlive == False:
        #print(Enemy.get_name(TestEnemy) + " wonders who to attack...")
        EnemyAttackNPC2()
    else:
        time.sleep(1)

        print(Enemy.get_name(TestEnemy) + " attacks " + PartyMember.get_name(NPC1) + "!")
        time.sleep(2)
        roll = randrange(1, 100)
        enemyTarget = Enemy.get_EnemyAccuracy(TestEnemy)
        NPC1Defense = PartyMember.get_ArmourClass(NPC1)
        enemyTargetmodded = enemyTarget - NPC1Defense
        if roll < enemyTargetmodded:
            # print("The attack hits!")
            time.sleep(1)
            # print(str(enemyTarget) + " - " + str(playerDefense) + " = " + str(enemyTargetmodded) + " vs. " + str(roll))
            time.sleep(2)
            dmgroll1 = randrange(1, 20)
            dmgroll2 = randrange(1, 20)
            totaldmg = dmgroll1 * 3 + dmgroll2 * 3 + Enemy.get_EnemyDamage(TestEnemy) - PartyMember.get_ArmourClass(NPC1)
            if totaldmg < 0:
                totaldmg = 0
            print(Enemy.get_name(TestEnemy) + " hits " + PartyMember.get_name(
                NPC1) + " for " + str(totaldmg) + " total damage.")
            time.sleep(4)
            newNPChealth = PartyMember.get_Health(NPC1) - totaldmg
            PartyMember.set_Health(NPC1, newNPChealth)
            if newNPChealth > 0:
                time.sleep(1)
                ###############TestBattle1_Phase4()#####################################################
            else:
                print(PartyMember.get_name(NPC1) + " has died!")
                PartyMember.set_isAlive(NPC1, False)
                time.sleep(2)
                #######################TestBattle1_Phase4()#################################################
        else:
            print("The attack misses!")
            time.sleep(1)
            # print(str(enemyTarget) + " - " + str(playerDefense) + " = " + str(enemyTargetmodded) + " vs. " + str(roll))
            time.sleep(2)
            ################################TestBattle1_Phase4()###########################################





def EnemyAttackNPC2():
    NPC2isAlive = PartyMember.get_isAlive(NPC2)
    if NPC2isAlive == False:
        #print(Enemy.get_name(TestEnemy) + " wonders who to attack...")
        EnemyAttackNPC3()
    else:
        time.sleep(1)

        print(Enemy.get_name(TestEnemy) + " attacks " + PartyMember.get_name(NPC2) + "!")
        time.sleep(2)
        roll = randrange(1, 100)
        enemyTarget = Enemy.get_EnemyAccuracy(TestEnemy)
        NPC2Defense = PartyMember.get_ArmourClass(NPC2)
        enemyTargetmodded = enemyTarget - NPC2Defense
        if roll < enemyTargetmodded:
            # print("The attack hits!")
            time.sleep(1)
            # print(str(enemyTarget) + " - " + str(playerDefense) + " = " + str(enemyTargetmodded) + " vs. " + str(roll))
            time.sleep(2)
            dmgroll1 = randrange(1, 20)
            dmgroll2 = randrange(1, 20)
            totaldmg = dmgroll1 * 3 + dmgroll2 * 3 + Enemy.get_EnemyDamage(TestEnemy) - PartyMember.get_ArmourClass(NPC2)
            if totaldmg < 0:
                totaldmg = 0
            print(Enemy.get_name(TestEnemy) + " hits " + PartyMember.get_name(
                NPC2) + " for " + str(totaldmg) + " total damage.")
            time.sleep(4)
            newNPChealth = PartyMember.get_Health(NPC2) - totaldmg
            PartyMember.set_Health(NPC2, newNPChealth)
            if newNPChealth > 0:
                time.sleep(1)
                ###########################TestBattle1_Phase4()################################################
            else:
                print(PartyMember.get_name(NPC2) + " has died!")
                PartyMember.set_isAlive(NPC2, False)
                time.sleep(2)
                ############################TestBattle1_Phase4()################################################
        else:
            print("The attack misses!")
            time.sleep(1)
            # print(str(enemyTarget) + " - " + str(playerDefense) + " = " + str(enemyTargetmodded) + " vs. " + str(roll))
            time.sleep(2)
            #######################TestBattle1_Phase4()##########################################################




def EnemyAttackNPC3():
    NPC3isAlive = PartyMember.get_isAlive(NPC3)
    if NPC3isAlive == False:
        #print(Enemy.get_name(TestEnemy) + " wonders who to attack...")
        EnemyAttackPC()
    else:
        time.sleep(1)
        print(Enemy.get_name(TestEnemy) + " attacks " + PartyMember.get_name(NPC3) + "!")
        time.sleep(2)
        roll = randrange(1, 100)
        enemyTarget = Enemy.get_EnemyAccuracy(TestEnemy)
        NPC3Defense = PartyMember.get_ArmourClass(NPC3)
        enemyTargetmodded = enemyTarget - NPC3Defense
        if roll < enemyTargetmodded:
            print("The attack hits!")
            time.sleep(1)
            # print(str(enemyTarget) + " - " + str(playerDefense) + " = " + str(enemyTargetmodded) + " vs. " + str(roll))
            time.sleep(2)
            dmgroll1 = randrange(1, 20)
            dmgroll2 = randrange(1, 20)
            totaldmg = dmgroll1 * 3 + dmgroll2 * 3 + Enemy.get_EnemyDamage(TestEnemy) - PartyMember.get_ArmourClass(NPC3)
            if totaldmg < 0:
                totaldmg = 0
            print(Enemy.get_name(TestEnemy) + " hits " + PartyMember.get_name(
                NPC3) + " for " + str(totaldmg) + " total damage.")
            time.sleep(4)
            newNPChealth = PartyMember.get_Health(NPC3) - totaldmg
            PartyMember.set_Health(NPC3, newNPChealth)
            if newNPChealth > 0:
                time.sleep(1)
                ########################TestBattle1_Phase4()##################################################
            else:
                print(PartyMember.get_name(NPC3) + " has died!")
                PartyMember.set_isAlive(NPC3, False)
                time.sleep(2)
                ############################TestBattle1_Phase4()#################################################
        else:
            print("The attack misses!")
            time.sleep(1)
            # print(str(enemyTarget) + " - " + str(playerDefense) + " = " + str(enemyTargetmodded) + " vs. " + str(roll))
            time.sleep(2)
            ############TestBattle1_Phase4()################




def EnemyAttackPC():

    print(Enemy.get_name(TestEnemy) + " attacks " + PlayerCharacter.get_name(PC) + "!")
    time.sleep(2)
    roll = randrange(1, 100)
    enemyTarget = Enemy.get_EnemyAccuracy(TestEnemy)
    playerDefense = PlayerCharacter.get_ArmourClass(PC)
    enemyTargetmodded = enemyTarget - playerDefense
    if roll < enemyTargetmodded:
        # print("The attack hits!")
        time.sleep(1)
        # print(str(enemyTarget) + " - " + str(playerDefense) + " = " + str(enemyTargetmodded) + " vs. " + str(roll))
        time.sleep(2)
        dmgroll1 = randrange(1, 20)
        dmgroll2 = randrange(1, 20)
        totaldmg = dmgroll1 * 3 + dmgroll2 * 3 + Enemy.get_EnemyDamage(TestEnemy) - PlayerCharacter.get_ArmourClass(PC)
        if totaldmg < 0:
            totaldmg = 0
        print(Enemy.get_name(TestEnemy) + " hits " + PlayerCharacter.get_name(
            PC) + " for " + str(totaldmg) + " total damage.")
        time.sleep(4)
        newPChealth = PlayerCharacter.get_Health(PC) - totaldmg
        PlayerCharacter.set_Health(PC, newPChealth)
        if newPChealth > 0:
            time.sleep(1)
            #############TestBattle1_Phase4()############################################
        else:
            playerDied()
    else:
        print("The attack misses!")
        time.sleep(1)
        # print(str(enemyTarget) + " - " + str(playerDefense) + " = " + str(enemyTargetmodded) + " vs. " + str(roll))
        time.sleep(2)
        ##################TestBattle1_Phase4()###########################################

########################
##
##  GENERIC ENEMY ROUND -- REUSABLE
##
########################
def GenericEnemyPhase():




    newBattleTurn = Enemy.get_BattleTurn(TestEnemy) + 1
    Enemy.set_BattleTurn(TestEnemy, newBattleTurn)

    clear()
    BattleStatus()



    dialogueroll = randrange(1,100)
    if dialogueroll < 90:
        time.sleep(1)
    if dialogueroll > 89:
        print("\n")
    if dialogueroll == 90:
        print(Enemy.get_name(TestEnemy) + " shouts, 'You disgust me!'")
        time.sleep(3)
    if dialogueroll == 91:
        print(Enemy.get_name(TestEnemy) + " shouts, 'Gods damn you!'")
        time.sleep(3)
    if dialogueroll == 92:
        print(Enemy.get_name(TestEnemy) + " shouts, 'I'll meet you in Hell!'")
        time.sleep(3)
    if dialogueroll == 93:
        print(Enemy.get_name(TestEnemy) + " screams up at the sky to their Gods.")
        time.sleep(3)
    if dialogueroll == 94:
        print(Enemy.get_name(TestEnemy) + " whispers, 'This is only the beginning...'")
        time.sleep(3)
    if dialogueroll == 95:
        print(Enemy.get_name(TestEnemy) + " sneers, 'Fine fighting, for a lowlife..'")
        time.sleep(3)
    if dialogueroll == 96:
        print(Enemy.get_name(TestEnemy) + " mumbles something about RNG.")
        time.sleep(3)
    if dialogueroll == 97:
        print(Enemy.get_name(TestEnemy) + " shouts, 'Fight me, you coward!'")
        time.sleep(3)
    if dialogueroll == 98:
        print(Enemy.get_name(TestEnemy) + " mutters, 'Could this be the end?'")
        time.sleep(3)
    if dialogueroll == 99:
        print(Enemy.get_name(TestEnemy) + " shouts, 'You'll never vanquish me alive!'")
        time.sleep(3)
    if dialogueroll == 100:
        print(Enemy.get_name(TestEnemy) + " whispers, 'Transcendence...I feel it coming...'")
        time.sleep(3)
    else:
        time.sleep(1)

    print("Enemy turn.\n")
    time.sleep(2)
    ## ENEMY ATTACKS PC
    attacktargeter = randrange(1, 7)
    if attacktargeter == 1:
        EnemyAttackPC()


    ## ENEMY ATTACKS NPC1
    if attacktargeter == 2 or attacktargeter == 3:


        EnemyAttackNPC1()

    ## ENEMY ATTACKS NPC2
    if attacktargeter == 4 or attacktargeter == 5:
        EnemyAttackNPC2()


    ## ENEMY ATTACKS NPC3
    if attacktargeter == 6 or attacktargeter == 7:
        EnemyAttackNPC3()


    print("\n(Press enter to continue)")
    key = input("")
    if key != "`":
        clear()
        BattleStatus()
        #print("End of Enemy Round")
        #time.sleep(4)
    else:
        clear()
        BattleStatus()
        #print("End of Enemy Round")
        #time.sleep(4)






def BattleStatus():


    CurrentStage = Stage.get_number(TestStage1)
    CurrentTurn = Enemy.get_BattleTurn(TestEnemy)
    CurrentStageName = Stage.get_name(TestStage1)
    UpperStageName = CurrentStageName.upper()

    # print("BATTLE TEXT STATUS PLACEHOLDER -----------------------")
    print("STAGE " + str(CurrentStage) + " - BATTLE OF " + str(UpperStageName) + " - TURN " + str(CurrentTurn))
    print("\n")
    print("Enemy: " + Enemy.get_name(TestEnemy) + " " + Enemy.get_Personality(TestEnemy) + Enemy.get_Omen(TestEnemy))
    if Enemy.get_EnemyClass(TestEnemy) != "None":
        print("Class: " + Enemy.get_EnemyClass(TestEnemy))
    print("Health: " + str(Enemy.get_Health(TestEnemy)) + "/" + str(Enemy.get_MaxHealth(TestEnemy)))
    print("Armour Class: " + str(Enemy.get_ArmourClass(TestEnemy)))
    print("Accuracy: " + str(Enemy.get_EnemyAccuracy(TestEnemy)) + "\nBonus Damage: " + str(Enemy.get_EnemyDamage(TestEnemy)))
    print("")
    print("                      VS.")
    print("")
    print("PC: " + PlayerCharacter.get_name(PC))
    print("Class: " + PlayerCharacter.get_playerclass(PC))
    print("   Health: " + str(PlayerCharacter.get_Health(PC))+ "/" + str(PlayerCharacter.get_MaxHealth(PC)))
    print("   Armour Class: " + str(PlayerCharacter.get_ArmourClass(PC)) + "   STR: " + str(PlayerCharacter.get_Strength(PC)) + "   INT: " + str(PlayerCharacter.get_Intellect(PC)))
    print("   AttackMod: " + str(PlayerCharacter.get_attackModifier(PC)) + "      DEX: " + str(PlayerCharacter.get_Dexterity(PC)) + "   CHA: " + str(PlayerCharacter.get_Charisma(PC)))
    print("   Special Points: " + str(PlayerCharacter.get_SpecialPoints(PC)) + "      Gold: " + str(PlayerCharacter.get_Gold(PC)))
    print("                          Blood: " + str(PlayerCharacter.get_Blood(PC)))
    print("Party: ")
    if PartyMember.get_Health(NPC1) > 0:
        print(PartyMember.get_name(NPC1) + " " + PartyMember.get_Personality(NPC1)  +  "\n   Health: " + str(PartyMember.get_Health(NPC1)) + "/" + str(PartyMember.get_MaxHealth(NPC1))+"\n   Armour Class: " + str(PartyMember.get_ArmourClass(NPC1)) + "\n   AttackMod: " + str(PartyMember.get_AttackModifier(NPC1)))
        if PartyMember.get_SpecSlot1Name(NPC1) != "None":
            print("      Special: " + PartyMember.get_SpecSlot1Name(NPC1))
    else:
        print(PartyMember.get_name(NPC1) + "\n   (Dead)")
    if PartyMember.get_Health(NPC2) > 0:
        print(PartyMember.get_name(NPC2)  + " " + PartyMember.get_Personality(NPC2) +  "\n   Health: " + str(PartyMember.get_Health(NPC2)) + "/" + str(PartyMember.get_MaxHealth(NPC2))+"\n   Armour Class: " + str(PartyMember.get_ArmourClass(NPC2)) + "\n   AttackMod: " + str(PartyMember.get_AttackModifier(NPC2)))
        if PartyMember.get_SpecSlot1Name(NPC2) != "None":
            print("      Special: " + PartyMember.get_SpecSlot1Name(NPC2))
    else:
        print(PartyMember.get_name(NPC2) + "\n   (Dead)")
    if PartyMember.get_Health(NPC3) > 0:
        print(PartyMember.get_name(NPC3)  + " " + PartyMember.get_Personality(NPC3) +  "\n   Health: " + str(PartyMember.get_Health(NPC3)) + "/" + str(PartyMember.get_MaxHealth(NPC3))+"\n   Armour Class: " + str(PartyMember.get_ArmourClass(NPC3)) + "\n   AttackMod: " + str(PartyMember.get_AttackModifier(NPC3)))
        if PartyMember.get_SpecSlot1Name(NPC3) != "None":
            print("      Special: " + PartyMember.get_SpecSlot1Name(NPC3))
    else:
        print(PartyMember.get_name(NPC3) + "\n   (Dead)")
    print("_______________________________________________\n")

    time.sleep(3)










def stageConditions():
    roll = randrange(1,1000)
    if roll < 15:
        clear()
        BattleStatus()
        print("Apocalypse! Eldritch magic crackles through the battlegrounds, tearing the fabric of your reality.")
        time.sleep(5)
        clear()
        BattleStatus()
        print("Everyone takes 20d20 damage!")
        time.sleep(3)
        rolls = 20
        total = 0
        while rolls > 1:
            rolldice = randrange(1,20)
            total += rolldice
            rolls = rolls - 1
        print("Everyone takes " + str(total) + " damage!")
        time.sleep(4)
        newPChealth = PlayerCharacter.get_Health(PC) - total
        PlayerCharacter.set_Health(PC, newPChealth)
        newEnemyHealth = Enemy.get_Health(TestEnemy) - total
        Enemy.set_Health(TestEnemy, newEnemyHealth)
        NPC1health = PartyMember.get_Health(NPC1) - total
        PartyMember.set_Health(NPC1, NPC1health)
        NPC2health = PartyMember.get_Health(NPC2) - total
        PartyMember.set_Health(NPC2, NPC2health)
        NPC3health = PartyMember.get_Health(NPC3) - total
        PartyMember.set_Health(NPC3, NPC3health)
    elif roll < 100:
        clear()
        BattleStatus()
        print("A storm cast by the Gods rolls in, thundering and pouring at the combatants.")
        time.sleep(3)
        clear()
        BattleStatus()
        print("Everyone takes 5d20 damage!")
        time.sleep(3)
        rolls = 5
        total = 0
        while rolls > 1:
            rolldice = randrange(1,20)
            total += rolldice
            rolls = rolls - 1
        print("Everyone takes " + str(total) + " damage!")
        time.sleep(4)
        newPChealth = PlayerCharacter.get_Health(PC) - total
        PlayerCharacter.set_Health(PC, newPChealth)
        newEnemyHealth = Enemy.get_Health(TestEnemy) - total
        Enemy.set_Health(TestEnemy, newEnemyHealth)
        NPC1health = PartyMember.get_Health(NPC1) - total
        PartyMember.set_Health(NPC1, NPC1health)
        NPC2health = PartyMember.get_Health(NPC2) - total
        PartyMember.set_Health(NPC2, NPC2health)
        NPC3health = PartyMember.get_Health(NPC3) - total
        PartyMember.set_Health(NPC3, NPC3health)
    elif roll > 950:
        clear()
        BattleStatus()
        print("Merciful Gods! Some form of divine intervention restores life to everyone!")
        time.sleep(3)
        clear()
        BattleStatus()
        print("Everyone heals 4d20 Health!")
        time.sleep(3)
        rolls = 4
        total = 0
        while rolls > 1:
            rolldice = randrange(1,20)
            total += rolldice
            rolls = rolls - 1
        print("Everyone heals " + str(total) + " Health!")
        time.sleep(4)

        oldHealth = PlayerCharacter.get_MaxHealth(PC)
        if total + oldHealth >= PlayerCharacter.get_MaxHealth(PC):
            PlayerCharacter.set_Health(PC, PlayerCharacter.get_MaxHealth(PC))
        else:
            newPChealth = PlayerCharacter.get_Health(PC) + total
            PlayerCharacter.set_Health(PC, newPChealth)

        oldEnemyHealth = Enemy.get_Health(TestEnemy)
        if total + oldEnemyHealth >= Enemy.get_MaxHealth(TestEnemy):
            Enemy.set_Health(TestEnemy, Enemy.get_MaxHealth(TestEnemy))
        else:
            newEnemyHealth = Enemy.get_Health(TestEnemy) + total
            Enemy.set_Health(TestEnemy, newEnemyHealth)

        oldNPC1Health = PartyMember.get_Health(NPC1)
        if total + oldNPC1Health >= PartyMember.get_MaxHealth(NPC1):
            PartyMember.set_Health(NPC1, PartyMember.get_MaxHealth(NPC1))
        else:
            NPC1health = PartyMember.get_Health(NPC1) + total
            PartyMember.set_Health(NPC1, NPC1health)
        oldNPC2Health = PartyMember.get_Health(NPC2)
        if total + oldNPC2Health >= PartyMember.get_MaxHealth(NPC2):
            PartyMember.set_Health(NPC2, PartyMember.get_MaxHealth(NPC2))
        else:
            NPC2health = PartyMember.get_Health(NPC2) + total
            PartyMember.set_Health(NPC2, NPC2health)
        oldNPC3Health = PartyMember.get_Health(NPC3)
        if total + oldNPC3Health >= PartyMember.get_MaxHealth(NPC3):
            PartyMember.set_Health(NPC3, PartyMember.get_MaxHealth(NPC3))
        else:
            NPC3health = PartyMember.get_Health(NPC3) + total
            PartyMember.set_Health(NPC3, NPC3health)


    elif roll > 900:
        clear()
        BattleStatus()
        print("A gentle sea breeze in the distance revitalizes everyone in the area!")
        time.sleep(3)
        clear()
        BattleStatus()
        print("Everyone heals 2d20 Health!")
        time.sleep(3)
        rolls = 2
        total = 0
        while rolls > 1:
            rolldice = randrange(1,20)
            total += rolldice
            rolls = rolls - 1
        print("Everyone heals " + str(total) + " Health!")
        time.sleep(4)


        if total + PlayerCharacter.get_Health(PC) >= PlayerCharacter.get_MaxHealth(PC):
            PlayerCharacter.set_Health(PC, PlayerCharacter.get_MaxHealth(PC))
        else:
            newPChealth = PlayerCharacter.get_Health(PC) + total
            PlayerCharacter.set_Health(PC, newPChealth)

        if total + PartyMember.get_Health(NPC1) >= PartyMember.get_MaxHealth(NPC1):
            PartyMember.set_Health(NPC1, PartyMember.get_MaxHealth(NPC1))
        else:
            NPC1health = PartyMember.get_Health(NPC1) + total
            PartyMember.set_Health(NPC1, NPC1health)
        if total + PartyMember.get_Health(NPC2) >= PartyMember.get_MaxHealth(NPC2):
            PartyMember.set_Health(NPC2, PartyMember.get_MaxHealth(NPC2))
        else:
            NPC2health = PartyMember.get_Health(NPC2) + total
            PartyMember.set_Health(NPC2, NPC2health)
        if total + PartyMember.get_Health(NPC3) >= PartyMember.get_MaxHealth(NPC3):
            PartyMember.set_Health(NPC3, PartyMember.get_MaxHealth(NPC3))
        else:
            NPC3health = PartyMember.get_Health(NPC3) + total
            PartyMember.set_Health(NPC3, NPC3health)

    else:
        clear()
        BattleStatus()
        #print("The next round begins...")
        #time.sleep(5)

    time.sleep(5)



def buildpartySpecials():
    print("")

def buildparty():
    assignSpecials()
    rollforPersonality()


    clear()
    #print(str(PartyMember.get_SpecSlot1Num(NPC1)))
    #print(str(PartyMember.get_SpecSlot1Num(NPC2)))
    #print(str(PartyMember.get_SpecSlot1Num(NPC3)))

    secstr1 = str(PartyMember.get_SpecSlot1Num(NPC1))
    secstr2 = str(PartyMember.get_SpecSlot1Num(NPC2))
    secstr3 = str(PartyMember.get_SpecSlot1Num(NPC3))


    time.sleep(1)

    PCmaxhealth = PlayerCharacter.get_Health(PC)
    PlayerCharacter.set_MaxHealth(PC, PCmaxhealth)
    NPC1maxhealth = PartyMember.get_Health(NPC1)
    PartyMember.set_MaxHealth(NPC1, NPC1maxhealth)
    NPC2maxhealth = PartyMember.get_Health(NPC2)
    PartyMember.set_MaxHealth(NPC2, NPC2maxhealth)
    NPC3maxhealth = PartyMember.get_Health(NPC3)
    PartyMember.set_MaxHealth(NPC3, NPC3maxhealth)
    enemyMaxHealth = Enemy.get_Health(TestEnemy)
    Enemy.set_MaxHealth(TestEnemy, enemyMaxHealth)




    SaveGame()
    ListParty()

def main():

    MainMenu()


main()