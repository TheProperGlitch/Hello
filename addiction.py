import random
points = 10
def draw(person):
    """A command to add a card to someone's hand in the game of blackjack.
    Person is the hand that recives the card."""
    card_draw = random.randint(1,13)
    if card_draw < 10:
        person.append(card_draw)
    else:
        person.append(10)

def blackjack(a1,b1):
    """ Runs a simplified game of blackjack.
        You are given 2 cards and can see one of the dealer's cards.
        You can chose to hit or stand. If you hit you get another card.
        If you stand the dealer will draw cards until the sum of their cards is larger to the sum of your cards.
        If the sum of either person's hand is more than 21 they bust and lose.
        Aces count as 1, number cards are worth their number, and face cards are worth 10."""
    player_cards = []
    for i in range (2):
        draw(player_cards)
    dealer_cards = []
    draw(dealer_cards)
    print(f"Dealers cards: {dealer_cards} and Unknown")
    print(f"Your cards: {player_cards}")

    def hitting(a2,b2):
        """A system to run the hitting and standing system in blackjack."""
        total_dealer = 0
        total_player = 0
        hit_stand = input("Do you want to (h)it or (s)tand: ")
        if hit_stand == "h":
            draw(player_cards)
            total_player = 0
            for ele in range(0, len(player_cards)):
                total_player = total_player + player_cards[ele]
            if total_player > 21:
                print(f"Bust! Your cards were: {player_cards}")
                return (a2 - b2)
            elif total_player == 21:
                print(f"Blackjack! You win with a hand of {player_cards}")
                return a2 + b2
            else:
                print(f"Your cards: {player_cards}")
                return hitting(a2,b2)
        else:
                total_player = 0
                total_dealer = 0
                for ele in range(0, len(player_cards)):
                    total_player = total_player + player_cards[ele]
                for ele in range(0, len(dealer_cards)):
                    total_dealer = total_dealer + dealer_cards[ele]
                while total_player > total_dealer and total_dealer <= 17:
                    draw(dealer_cards)
                    total_dealer = 0
                    for ele in range(0, len(dealer_cards)):
                        total_dealer = total_dealer + dealer_cards[ele]
                if total_dealer > 21:
                    print(f"The dealer bust. You win! \n Dealer cards: {dealer_cards} \n Your cards: {player_cards}")
                    return a2 + b2
                elif total_dealer < total_player:
                    print(f"The dealer lost! \n Your cards: {player_cards} \n Dealer cards: {dealer_cards}")
                    return a2 + b2
                elif total_dealer == total_player:
                     print(f"It was a tie! \n Your cards: {player_cards} \n Dealer cards: {dealer_cards}")
                     return a2
                else:
                    print(f"The dealer won. :( \n Your cards: {player_cards} \n Dealer cards: {dealer_cards}")
                    return a2 - b2
    return hitting(a1,b1)
    
def number_game(a3):
    """A game where you pick a number between 1 and 5. 
    If you pick the wrong number you lose (bet) points,
    If you pick the right number you gain (bet) times 5 points. """
    pick = input("Pick a number from 1 to 5: ")
    answer = random.randint(1,5)
    if str(pick) == str(answer):
        print("You win!")
        return a3 * 5
    else:
        print(f"You lose. The correct answer was {answer}, you picked {pick}")
        return a3 * (-1)

def program(start_point):
    """The thing actualy running the games."""
    points = start_point
    print(f"You have {points} points.")
    if points == 0:
        print("You lose!")
        return
    respond = input("Do you want to play (b)lackjack or (g)uessing game: ")  
    if respond == "b":
        bet = int(input(f"You have {points} points. How much do you want to bet: ")) 
        if bet > points:
            bet = points 
        points = blackjack(points, bet)
        program(points)
    elif respond == "g":
        bet = int(input(f"You have {points} points. How much do you want to bet: "))
        if bet > points:
            bet = points 
        points += number_game(bet)
        program(points)
    else:
        print("Goodbye and thanks for playing!")
program(10)