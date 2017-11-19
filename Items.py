from enum import Enum

# I want to user numbers for identifying gear slots but I don't want to
# have to memorize what numbers correspond to so I want to make an enum instead

class Gear(Enum):
    Head = 0
    Chest = 1
    Shoulders = 2
    Leg = 3
    Boots = 4
    Hands = 5
    Weapon = 6
    Shield = 7

class Collections:
    all_items = \
    {
        "Sword of Autism": {
            "Field": Gear.Weapon,
            "Description": "A mighty sword, only for the worthiest of the autists",
            "Stats": {"Strength": 4}
        },

        "Boots of Swiftness": {
            "Field": Gear.Boots,
            "Description": "Boots of the swiftiest swiftosity.",
            "Stats": {"Dexterity": 2}
        }
    }
