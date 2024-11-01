#If >= 17 CPU does not pick another card
from art import logo
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
playing = True
while playing:
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': " )
    if play == 'y':
        print(logo)
        player_cards = []
        dealer_cards = []

        #Give 2 cards to player
        player_cards.append(cards[random.randint(0, len(cards) - 1)])
        player_cards.append(cards[random.randint(0, len(cards) - 1)])

        #Give 1 card to dealer
        dealer_cards.append(cards[random.randint(0, len(cards) - 1)])

        player_sum = sum(player_cards)
        dealer_sum = sum(dealer_cards)

        print(f"Your cards {player_cards}, current score: {player_sum}")
        print(f"Computer's first card: {dealer_cards[0]}")

        continue_playing = True
        while continue_playing:
            get_another = input("Type 'y' to get another card, type 'n' to pass: ")
            if get_another == 'n':
                continue_playing = False
                while dealer_sum < 17:
                    dealer_cards.append(cards[random.randint(0, len(cards) - 1)])

                if dealer_sum > 21:
                    print(f"You win. Computer sum {dealer_sum} exceeds 21")
                else:
                    if dealer_sum < player_sum:
                        print(f"You win. Your sum {sum(player_cards)}. Computer sum {sum(dealer_cards)}")
            else:
                player_cards.append(cards[random.randint(0, len(cards) - 1)])
                player_sum = sum(player_cards)
                if player_sum > 21:
                    print(f"You lose. Your sum {player_sum} exceeds 21")
                    continue_playing = False
                else:
                    print(f"Your cards {player_cards}, current score: {player_sum}")
                    print(f"Computer's first card: {dealer_cards[0]}")



    else:
        playing = False
