import random
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def show(self):
        print("{} of {}".format(self.value, self.suit))

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in ["Spades", "Clubs", "Diamond", "Hearts"]:
            for val in range(1,14):
                self.cards.append(Card(suit, val))
    def show(self):
        for card in self.cards:
            card.show()
    def shuffle(self):
        for i in range(len(self.cards)-1, -1, -1):
            rand_int = random.randint(0,i)
            self.cards[i], self.cards[rand_int] = self.cards[rand_int], self.cards[i]

    def draw_card(self):
        if self.cards:
            return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.draw_card())
        return self

    def show_hand(self):
        for card in self.hand:
            card.show()


def main():
    deck = Deck()
    deck.show()
    deck.shuffle()
    deck.show()
    card = deck.draw_card()
    card.show()

    player = Player("Bob")
    player.draw(deck)

    player.show_hand()


if __name__ == '__main__':
    main()
