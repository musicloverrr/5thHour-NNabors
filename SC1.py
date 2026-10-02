#Name: Neely Nabors
#Class: 5th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#Other than damage which is required, it is up to you to decide what properties are
#important and the theme of the game.

enemy_creatures = {
    "enemy_1" : {
        "Name" : "Eleven",
        "Damage" : 95,
        "Strength" : 1000000,
        "Ability" : "Telekinesis",
        "Weakness" : "Telekinesis can wear Eleven out the longer it is used",
    },
    "enemy_2" : {
        "Name" : "Old man",
        "Damage" : 5,
        "Strength" : 10,
        "Ability" : "Says mean words",
        "Weakness" : "Likes to sleep",
    },
    "enemy_3" : {
        "Name" : "Neji",
        "Damage" : 80,
        "Strength" : 115,
        "Ability" : "X-ray vision",
        "Weakness" : "Blind spot in Byakugan",
    },
    "enemy_4" : {
        "Name" : "Vecna",
        "Damage" : 90,
        "Strength" : 10000,
        "Ability" : "Telekinesis",
        "Weakness" : "The Mind Flayer",
    },
    "enemy_5" : {
        "Name" : "Kakashi",
        "Damage" : 85,
        "Strength" : 150,
        "Ability" : "A Copy Ninja",
        "Weakness" : "Low natural chakura",
    },
}
print(enemy_creatures)
enemy_creatures["enemy_3"].update({"Damage" : 85})
print(enemy_creatures["enemy_3"])


