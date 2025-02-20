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
        return f"Item: {self.name}, Rarity: {self.rarity}, Owner: {self._ownership or 'None'}"


class Weapon(Item):
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
        return f"{self.name} is used, dealing {self.damage * self.attack_modifier} damage."


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


class Potion(Item):
    def __init__(self, name, potion_type, value, effective_time=0, owner=""):
        super().__init__(name, rarity="common")
        self.potion_type = potion_type
        self.value = value
        self.effective_time = effective_time
        self._ownership = owner
        self.used = False

    @classmethod
    def from_ability(cls, name, owner, potion_type):
        return cls(name, potion_type, 50, 30, owner)

    def use(self):
        if not self._ownership or self.used:
            return "NO OUTPUT"
        self.used = True
        return f"{self._ownership} used {self.name}, and {self.potion_type} increased {self.value} for {self.effective_time}s."


long_bow = Weapon(name='Belthronding', rarity='legendary', damage=5000, weapon_type='bow')
print(long_bow.pick_up('Beleg'))
print(long_bow.equip())
print(long_bow.use())

broken_pot_lid = Shield(name='wooden lid', description='A lid made of wood.', defense=5, broken=True)
print(broken_pot_lid.pick_up('Beleg'))
print(broken_pot_lid.equip())
print(broken_pot_lid.use())
print(broken_pot_lid.throw_away())
print(broken_pot_lid.use())

attack_potion = Potion.from_ability(name='atk potion temp', owner='Beleg', potion_type='attack')
print(attack_potion.use())
print(attack_potion.use())