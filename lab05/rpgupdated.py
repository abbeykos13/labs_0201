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

    def __str__(self):
        if self.rarity == "legendary":
            return f"Item: {self.name}, Rarity: {self.rarity}, Owner: {self._ownership or 'None'}"
        return f"Item: {self.name}, Rarity: {self.rarity}, Owner: {self._ownership or 'None'}"

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
    
    def __iter__(self):
        return iter(self.items)
    
    def __contains__(self, item):
        return item in self.items


beleg_backpack = Inventory(owner='Beleg')
belthronding = RangedWeapon(name='Belthronding', rarity='legendary', damage=500, weapon_type='bow')
hp_potion = Item(name='HP Potion', rarity='common')
master_sword = SingleHandedWeapon(name='Master Sword', rarity='legendary', damage=300, weapon_type='sword')
broken_pot_lid = Shield(name='Wooden Lid', description='A simple wooden lid.', defense=5, broken=True)
muramasa = DoubleHandedWeapon(name='Muramasa', rarity='legendary', damage=580, weapon_type='katana')
gungnir = Pike(name='Gungnir', rarity='legendary', damage=290, weapon_type='spear')
round_shield = Shield(name='Round Shield', description='A sturdy round shield.', defense=50, broken=False)

beleg_backpack.add_item(belthronding)
beleg_backpack.add_item(hp_potion)
beleg_backpack.add_item(master_sword)
beleg_backpack.add_item(broken_pot_lid)
beleg_backpack.add_item(muramasa)
beleg_backpack.add_item(gungnir)
beleg_backpack.add_item(round_shield)

beleg_backpack.drop_item(broken_pot_lid)

if master_sword in beleg_backpack:
    master_sword.equip()
    print(master_sword.use())

for item in beleg_backpack: 
    if isinstance(item, Weapon):
        beleg_backpack.view(item_type=item.__class__)

        