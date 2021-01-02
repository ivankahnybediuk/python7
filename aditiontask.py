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
def give_cards_to_player(deck):
    player_cards.append(deck.pop())
    return deck
def print_cards_score(player_cards):
    player_score = 0
    print('Ваши карты: ')
    for i in range(len(player_cards)):
        print(f'{player_cards[i]["name"]} {player_cards[i]["suit"]}')
        player_score += player_cards[i]['value']
    print(f'Количество очков: {player_score}')
    return player_score
deck = []
comp_cards = []
c_score = 0
player_cards = []
score = print_cards_score(player_cards)

if __name__ == "__main__":
    ans = input('Press S to start, or E to exit \n').upper()
    if ans == 'S':
        make_deck(deck)
        deck_shuffle(deck)
        give_cards_to_player(deck)
        give_cards_to_player(deck)
        print_cards_score(player_cards)
        if score == 21:
            print("Поздравляю, вы выирали!")
        elif score >21:
            print("Вы проиграли!")
        else:
            take_card_answ = input('Взять еще карту - "Y". Нет - "N" \n').upper()
            if take_card_answ == 'Y':
                give_cards_to_player(deck)
                print_cards_score(player_cards)
                if score == 21:
                    print("Поздравляю, вы выирали!")
                elif score > 21:
                    print("Вы проиграли!")
                else:
                    take_card_answ = input('Взять еще карту - "Y". Нет - "N" \n').upper()
                    if take_card_answ == 'Y':
                        give_cards_to_player(deck)
                        print_cards_score(player_cards)
                        if score == 21:
                            print("Поздравляю, вы выирали!")
                        elif score > 21:
                            print("Вы проиграли!")
                        else:
                            take_card_answ = input('Взять еще карту - "Y". Нет - "N" \n').upper()
                            if take_card_answ == 'Y':
                                give_cards_to_player(deck)
                                print_cards_score(player_cards)
                                if score == 21:
                                    print("Поздравляю, вы выирали!")
                                elif score > 21:
                                    print("Вы проиграли!")
                                else:
                                    take_card_answ = input('Взять еще карту - "Y". Нет - "N" \n').upper()
                                    if take_card_answ == 'Y':
                                        give_cards_to_player(deck)
                                        print_cards_score(player_cards)
                                        if score == 21:
                                            print("Поздравляю, вы выирали!")
                                        elif score > 21:
                                            print("Вы проиграли!")
                                        else:
                                            take_card_answ = input('Взять еще карту - "Y". Нет - "N" \n').upper()


            else:
                pass