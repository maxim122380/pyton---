import random
import time

boss = {
    "name" : "Ворон",
    "hp" : 50,
    "dmg" : 2,
}

weapons = ["Меч", "Топор", "Лук"]
weapon = random.choice(weapons)

while boss["hp"] <= 0:
    if weapon == "Меч":
        wep = random.randint(4, 7)
    elif weapon == "Топор":
        wep = random.randint(7, 10)
    elif weapon == "Лук":
        wep = random.randint(5, 10)

player = {
    "name" : "player",
    "hp" : 15,
    "dmg" : wep,
}






locate = ["мрачном", "светлом", "старом"]
loc = ['доме','лесу', 'особняке']
weapons = ["Меч", "Топор", "Лук"]

def fight():
    while player["hp"] > 0 and boss["hp"] > 0:
        time.sleep(2)
        dam = wep
        boss["hp"] -= dam
        print(f"Вы нанесли {dam} урона!")

player["name"] = input("Введите имя вашего игрока:")
while True:
    print(f"Добро пожаловать в игру, {player['name']}!")
    time.sleep(2)
    print(f"Вы появились в {random.choice(locate)} {random.choice(loc)}...")
    print(f"Вам выпало оружие: {weapon}")
    print(f"Перед вами появился босс {boss['name']}")
    fight()
    if boss["hp"] <= 0:
            print("Вы победили босса")


    break