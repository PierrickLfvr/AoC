from collections import Counter

class Hand:
    def __init__(self, cards, bid, joker=False):
        if joker:
            card_mapper = {'T': 10, 'J': 1, 'Q': 12, 'K': 13, 'A': 14}
        else:
            card_mapper = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        self.cards = [int(card) if card.isdigit() else card_mapper[card] for card in cards]
        self.bid = int(bid)
        self.joker = joker
    
    def __lt__(self, other):

        if not self.joker:
            self_counter = sorted(list(Counter(self.cards).values()), reverse=True)
            other_counter = sorted(list(Counter(other.cards).values()), reverse=True)
        
        else:
            self_counter = Counter(self.cards)
            other_counter = Counter(other.cards)
            self_bonus = other_bonus = 0
            if 1 in self_counter:
                #delete 11 from counter
                self_bonus = self_counter[1]
                del self_counter[1]
            if 1 in other_counter:
                other_bonus = other_counter[1]
                del other_counter[1]
            self_counter = sorted(list(self_counter.values()), reverse=True)
            other_counter = sorted(list(other_counter.values()), reverse=True)

            if len(self_counter) == 0:
                self_counter.append(0)
            if len(other_counter) == 0:
                other_counter.append(0)
            self_counter[0] += self_bonus
            other_counter[0] += other_bonus

        for i in range(min(len(self_counter), len(other_counter))):

            if self_counter[i] != other_counter[i]:
                return self_counter[i] < other_counter[i]
        
        for i in range(5):
            if self.cards[i] != other.cards[i]:
               return self.cards[i] < other.cards[i]
        return None
    
    def __str__(self):
        return f"hand: {self.cards}, bid: {self.bid}"
    
hands = []
hands2 = []
for line in open("inputs/7.txt"):
    cards, bid = line.strip().split(" ")
    hands.append(Hand(cards, bid))
    hands2.append(Hand(cards, bid,True))

#part 1
def part1():
    sum=0
    sorted_hands = sorted(hands)
    for i, hand in enumerate(sorted_hands):
        sum+=hand.bid*(i+1)
    print(f'part 1: {sum}')

part1()

#part 2

def part2():
    sum=0
    sorted_hands = sorted(hands2)
    for i, hand in enumerate(sorted_hands):
        sum+=hand.bid*(i+1)
    print(f'part 2: {sum}')

part2()

