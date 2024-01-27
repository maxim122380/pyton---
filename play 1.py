import random
words1_lite = ["москва", "казань", "челябинск","севастополь"]
words2_medium = ["новосибирск", "астрахань", "барнаул", "владимир", "ковров", "владивосток", "воронеж"]
words3_hard = ["абакан", "благовещенск", "вязники", "городец", "добрянка", "ессентуки", "зеленоград", "каменногорск", "карачаевск", "кораблино"]
def randomletter(word):
    list = [i for i in word]
    return random.choice(list)

def get_ask(words):
    return random.choice(words)

def play(word):
    print("Я загадал город, попробуй угадать его!")
    word_ask = "🔲" * len(word)
    hp = 10
    win = False
    print("Загаданный город", word_ask)
    while not win and hp > 0:
        ask = input("Введите букву: ").lower()
        x = random.randint(1,10)
        if x == 5:
            ask = randomletter(word)
            print("Тебе повезло и у тебя открылась одна буква!")

            
        if ask in word and ask != "":
            print("Отлично! Ты угадал букву!")
            word_as_list = list(word_ask)
            indices = [i for i in range(len(word)) if word[i] == ask]
            for index in indices:
                word_as_list[index] = ask
                word_ask = "".join(word_as_list)
                if "🔲" not in word_ask:
                    win = True
                    print(f"Молодец🎉! Ты угадал город🏙️!")
        else:
            hp -= 1
            print(f"Тебе не удалось угадать букву, осталось попыток {hp}")
            if hp == 0:
                print(f"Очень жаль, но ты проиграл😢. Был город: {word}")
        print(word_ask)



answer = input("Сыграем в игру?\n1-Да\n2-Нет\n-> ")
while answer != "2":
    choic = input("Выберите уровень сложности\n1-Лёгкий\n2-Средний\n3-Сложный\n-> ")
    if choic == "1":
        word = get_ask(words1_lite)
        play(word)
    elif choic == "2":
        word = get_ask(words2_medium)
        play(word)
    elif choic == "3":
        word = get_ask(words3_hard)
        play(word)
    answer = input("Сыграем ещё раз?\n1-Да\n2-Нет\n-> ")
if answer == "2":
    print("Очень жаль😢, что ты ушёл. Возвращайся скорее!!!")