import random

"""
Пишем игру в 21. Создать массив "карт" рандомно их перемешать и выдавать "игроку" пока не скажет стоп или не проиграет.
"""


def make_deck(deck):
    suits = ('♠', '♣', '♥', '♦')
    names = ('Туз', "Король", 'Королева', 'Валет', '10', '9', '8', '7', '6', '5', '4', '3', '2')
    value = (1, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2)
    for suit in suits:
        for i, name in enumerate(names):
            deck.append({
                'suit': suit,
                'name': name,
                'value': value[i]
            })
    return deck


def deck_shuffle(deck):
    random.shuffle(deck)
    return deck


def give_cards_to_player(deck, player):
    player.append(deck.pop())
    return deck


def count_score(player):
    pscore = 0
    for i in range(len(player)):
        pscore += player[i]['value']
    return pscore


def print_cards_score(cards):
    print('Ваши карты: ')
    for i in range(len(cards)):
        print(f'{cards[i]["name"]} {cards[i]["suit"]}')
    print(f'Количество очков: {score}')


if __name__ == "__main__":
    ans = input('Press S to start, or E to exit \n').upper()
    if ans == 'S':
        deck = []
        comp_cards = []
        c_score = 0
        player_cards = []
        score = 0
        make_deck(deck)
        deck_shuffle(deck)
        give_cards_to_player(deck, player_cards)
        give_cards_to_player(deck, player_cards)
        score = count_score(player_cards)
        print_cards_score(player_cards)
        if score == 21:
            print(chalk.green("Поздравляю, вы выирали!"))
        elif score > 21:
            print(chalk.red("Вы проиграли!"))
        else:
            take_card_answ = input('Взять еще карту - "Y". Нет - "N" \n').upper()
            if take_card_answ == 'Y':
                give_cards_to_player(deck, player_cards)
                score = count_score(player_cards)
                print_cards_score(player_cards)
                if score == 21:
                    print("Поздравляю, вы выирали!")
                elif score > 21:
                    print("Вы проиграли!")
                else:
                    take_card_answ = input('Взять еще карту - "Y". Нет - "N" \n').upper()
                    if take_card_answ == 'Y':
                        give_cards_to_player(deck, player_cards)
                        score = count_score(player_cards)
                        print_cards_score(player_cards)

                        if score == 21:
                            print("Поздравляю, вы выирали!")
                        elif score > 21:
                            print("Вы проиграли!")
                        else:
                            take_card_answ = input('Взять еще карту - "Y". Нет - "N" \n').upper()
                            if take_card_answ == 'Y':
                                give_cards_to_player(deck, player_cards)
                                count_score(player_cards)
                                print_cards_score(player_cards)
                                if score == 21:
                                    print("Поздравляю, вы выирали!")
                                elif score > 21:
                                    print("Вы проиграли!")
                                else:
                                    take_card_answ = input('Взять еще карту - "Y". Нет - "N" \n').upper()
                                    if take_card_answ == 'Y':
                                        give_cards_to_player(deck, player_cards)
                                        count_score(player_cards)
                                        print_cards_score(player_cards)
                                        if score == 21:
                                            print("Поздравляю, вы выирали!")
                                        elif score > 21:
                                            print("Вы проиграли!")
                                        else:
                                            take_card_answ = input('Взять еще карту - "Y". Нет - "N" \n').upper()
                                    elif take_card_answ == 'N':
                                        give_cards_to_player(deck, comp_cards)
                                        c_score = count_score(comp_cards)
                                        if c_score > 21:
                                            print('Поздравляю, вы выирали!')
                                        elif c_score < 18:
                                            give_cards_to_player(deck, comp_cards)
                                            c_score = count_score(comp_cards)
                                            if c_score > 21:
                                                print('Поздравляю, вы выирали!')
                                            elif c_score < 18:
                                                give_cards_to_player(deck, comp_cards)
                                                c_score = count_score(comp_cards)
                                                if c_score > 21:
                                                    print('Поздравляю, вы выирали!')
                                                elif c_score < 18:
                                                    give_cards_to_player(deck, comp_cards)
                                                    c_score = count_score(comp_cards)
                                                else:
                                                    if c_score > score:
                                                        print("Вы проиграли!")
                                                    elif c_score < score:
                                                        print('Поздравляю, вы выирали!')
                                                    else:
                                                        print('Ничья')
                                            else:
                                                if c_score > score:
                                                    print("Вы проиграли!")
                                                elif c_score < score:
                                                    print('Поздравляю, вы выирали!')
                                                else:
                                                    print('Ничья')
                                        else:
                                            if c_score > score:
                                                print("Вы проиграли!")
                                            elif c_score < score:
                                                print('Поздравляю, вы выирали!')
                                            else:
                                                print('Ничья')
                            elif take_card_answ == 'N':
                                give_cards_to_player(deck, comp_cards)
                                c_score = count_score(comp_cards)
                                if c_score > 21:
                                    print('Поздравляю, вы выирали!')
                                elif c_score < 18:
                                    give_cards_to_player(deck, comp_cards)
                                    c_score = count_score(comp_cards)
                                    if c_score > 21:
                                        print('Поздравляю, вы выирали!')
                                    elif c_score < 18:
                                        give_cards_to_player(deck, comp_cards)
                                        c_score = count_score(comp_cards)
                                        if c_score > 21:
                                            print('Поздравляю, вы выирали!')
                                        elif c_score < 18:
                                            give_cards_to_player(deck, comp_cards)
                                            c_score = count_score(comp_cards)
                                        else:
                                            if c_score > score:
                                                print("Вы проиграли!")
                                            elif c_score < score:
                                                print('Поздравляю, вы выирали!')
                                            else:
                                                print('Ничья')
                                    else:
                                        if c_score > score:
                                            print("Вы проиграли!")
                                        elif c_score < score:
                                            print('Поздравляю, вы выирали!')
                                        else:
                                            print('Ничья')
                                else:
                                    if c_score > score:
                                        print("Вы проиграли!")
                                    elif c_score < score:
                                        print('Поздравляю, вы выирали!')
                                    else:
                                        print('Ничья')

                    elif take_card_answ == 'N':
                        give_cards_to_player(deck, comp_cards)
                        c_score = count_score(comp_cards)
                        if c_score > 21:
                            print('Поздравляю, вы выирали!')
                        elif c_score < 18:
                            give_cards_to_player(deck, comp_cards)
                            c_score = count_score(comp_cards)
                            if c_score > 21:
                                print('Поздравляю, вы выирали!')
                            elif c_score < 18:
                                give_cards_to_player(deck, comp_cards)
                                c_score = count_score(comp_cards)
                                if c_score > 21:
                                    print('Поздравляю, вы выирали!')
                                elif c_score < 18:
                                    give_cards_to_player(deck, comp_cards)
                                    c_score = count_score(comp_cards)
                                else:
                                    if c_score > score:
                                        print("Вы проиграли!")
                                    elif c_score < score:
                                        print('Поздравляю, вы выирали!')
                                    else:
                                        print('Ничья')
                            else:
                                if c_score > score:
                                    print("Вы проиграли!")
                                elif c_score < score:
                                    print('Поздравляю, вы выирали!')
                                else:
                                    print('Ничья')
                        else:
                            if c_score > score:
                                print("Вы проиграли!")
                            elif c_score < score:
                                print('Поздравляю, вы выирали!')
                            else:
                                print('Ничья')


            else:
                give_cards_to_player(deck, comp_cards)
                c_score = count_score(comp_cards)
                if c_score > 21:
                    print('Поздравляю, вы выирали!')
                elif c_score < 18:
                    give_cards_to_player(deck, comp_cards)
                    c_score = count_score(comp_cards)
                    if c_score > 21:
                        print('Поздравляю, вы выирали!')
                    elif c_score < 18:
                        give_cards_to_player(deck, comp_cards)
                        c_score = count_score(comp_cards)
                        if c_score > 21:
                            print('Поздравляю, вы выирали!')
                        elif c_score < 18:
                            give_cards_to_player(deck, comp_cards)
                            c_score = count_score(comp_cards)
                        else:
                            if c_score > score:
                                print("Вы проиграли!")
                            elif c_score < score:
                                print('Поздравляю, вы выирали!')
                            else:
                                print('Ничья')
                    elif c_score == 21:
                        print("Вы проиграли!")
                    else:
                        if c_score > score:
                            print("Вы проиграли!")
                        elif c_score < score:
                            print('Поздравляю, вы выирали!')
                        else:
                            print('Ничья')
                elif c_score == 21:
                    print("Вы проиграли!")
                else:
                    if c_score > score:
                        print("Вы проиграли!")
                    elif c_score < score:
                        print('Поздравляю, вы выирали!')
                    else:
                        print('Ничья')
