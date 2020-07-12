# __init__.py
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# marine3 = Unit("마린")
# TypeError: __init__() missing 2 required positional arguments: 'hp' and 'damage'

# marine3 = Unit("마린", 40)
# TypeError: __init__() missing 1 required positional argument: 'damage'