from time import sleep

class Hero:
    def __init__(self, name, health, armor, power, weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon

    def print_info(self):
        print(f'Поприветсвтуйте героя -> {self.name}')
        sleep(1)
        print(f"Уровень здоровья: {self.health}")
        sleep(1)
        print(f"Уровень брони: {self.armor}")
        sleep(1)
        print(f"Урон: {self.power} едениц")
        sleep(1)
        print(f"Вид оружия: {self.weapon}")

        def strike(self, enemy):
            print(f"-> УДАР! {self.name} атакует {enemy.name} с силой {self.power} используя {self.weapon} \n")
            enemy.armor -= self.power
            if enemy.armor < 0:
                enemy.health += enemy.armor
                enemy.armor = 0
            print(f"{enemy.name} покачнулся(-ась). \nКласс брони упал до {enemy.armor}, а уровень здоровья до {enemy.health} \n")

knight = Hero("Ричард", 50, 25, 10, "меч")
knight.print_info()
rascal = Hero("Хелен", 20, 10, 3, "лук")
rascal.print_info()
knight.strike(rascal)