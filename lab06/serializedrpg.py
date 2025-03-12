import json
from abc import ABC, abstractmethod

class Item:
    def __init__(self, name, description="", rarity="common"):
        self.name = name
        self.description = description
        self.rarity = rarity
        self._ownership = ""

    def pick_up(self, character):
        self._ownership = character
        return f"{self.name} is now owned by {character}."

    def throw_away(self):
        self._ownership = ""
        return f"{self.name} is thrown away."

    def use(self):
        if not self._ownership:
            return "NO OUTPUT"
        return f"{self.name} is used."

    def to_json(self):
        return {
            "type": self.__class__.__name__,
            "name": self.name,
            "description": self.description,
            "rarity": self.rarity,
            "ownership": self._ownership
        }
    
    @classmethod
    def from_json(cls, data):
        return cls(name=data["name"], description=data.get("description", ""), rarity=data.get("rarity", "common"))

class Weapon(Item, ABC):
    def __init__(self, name, rarity, damage, weapon_type):
        super().__init__(name, rarity=rarity)
        self.damage = damage
        self.weapon_type = weapon_type
        self.attack_modifier = 1.15 if rarity == "legendary" else 1.0
        self.equipped = False

    def equip(self):
        if not self._ownership:
            return "NO OUTPUT"
        self.equipped = True
        return f"{self.name} is equipped by {self._ownership}."

    def use(self):
        if not self._ownership or not self.equipped:
            return "NO OUTPUT"
        return f"{self.attack_move()}\n{self.name} is used, dealing {self.damage * self.attack_modifier} damage."
    
    @abstractmethod
    def attack_move(self):
        pass
    
    def to_json(self):
        data = super().to_json()
        data.update({
            "damage": self.damage,
            "weapon_type": self.weapon_type,
            "equipped": self.equipped
        })
        return data
    
    @classmethod
    def from_json(cls, data):
        return cls(name=data["name"], rarity=data["rarity"], damage=data["damage"], weapon_type=data["weapon_type"])

class SingleHandedWeapon(Weapon):
    def attack_move(self):
        return f"{self._ownership} slashes with {self.name}."

class DoubleHandedWeapon(Weapon):
    def attack_move(self):
        return f"{self._ownership} spins with {self.name}."

class Pike(Weapon):
    def attack_move(self):
        return f"{self._ownership} thrusts with {self.name}."

class RangedWeapon(Weapon):
    def attack_move(self):
        return f"{self._ownership} shoots with {self.name}."

class Shield(Item):
    def __init__(self, name, description, defense, broken=False):
        super().__init__(name, description)
        self.defense = defense
        self.broken = broken
        self.defense_modifier = 1.10 if self.rarity == "legendary" else 1.0
        self.equipped = False

    def equip(self):
        if not self._ownership:
            return "NO OUTPUT"
        self.equipped = True
        return f"{self.name} is equipped by {self._ownership}."

    def use(self):
        if not self._ownership or not self.equipped:
            return "NO OUTPUT"
        broken_modifier = 0.5 if self.broken else 1.0
        return f"{self.name} is used, blocking {self.defense * self.defense_modifier * broken_modifier} damage."
    
    def to_json(self):
        data = super().to_json()
        data.update({
            "defense": self.defense,
            "broken": self.broken
        })
        return data
    
    @classmethod
    def from_json(cls, data):
        return cls(name=data["name"], description=data.get("description", ""), defense=data["defense"], broken=data.get("broken", False))

class Inventory:
    def __init__(self, owner=None):
        self.owner = owner
        self.items = []

    def add_item(self, item):
        item._ownership = self.owner
        self.items.append(item)

    def drop_item(self, item):
        if item in self.items:
            item._ownership = ""
            self.items.remove(item)

    def view(self, item_type=None):
        if item_type:
            return [str(item) for item in self.items if isinstance(item, item_type)]
        return [str(item) for item in self.items]
    
    def to_json(self):
        return {
            "owner": self.owner,
            "items": [item.to_json() for item in self.items]
        }
    
    @classmethod
    def from_json(cls, data):
        inventory = cls(owner=data["owner"])
        for item_data in data["items"]:
            item_type = globals()[item_data["type"]]
            inventory.add_item(item_type.from_json(item_data))
        return inventory

beleg_backpack = Inventory(owner='Beleg')
belthronding = RangedWeapon(name='Belthronding', rarity='legendary', damage=500, weapon_type='bow')
hp_potion = Item(name='HP Potion', rarity='common')
master_sword = SingleHandedWeapon(name='Master Sword', rarity='legendary', damage=300, weapon_type='sword')

beleg_backpack.add_item(belthronding)
beleg_backpack.add_item(hp_potion)
beleg_backpack.add_item(master_sword)

# Serialize
json_data = json.dumps(beleg_backpack.to_json(), indent=4)
print(json_data)

# Deserialize
loaded_inventory = Inventory.from_json(json.loads(json_data))
print(loaded_inventory.view())