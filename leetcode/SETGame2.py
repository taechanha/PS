import itertools


def is_set(card1, card2, card3):
    """
    Check if the three cards are a set.
    """
    for i in range(4):
        if (card1[i] == card2[i] == card3[i]) or (card1[i] != card2[i] and card2[i] != card3[i] and card1[i] != card3[i]):
            continue
        else:
            return False
    return True


def find_max_sets(cards):
    """
    Find the maximum number of sets that can be made with the cards.
    """
    max_sets = 0
    for i in range(len(cards)):
        for j in range(i+1, len(cards)):
            for k in range(j+1, len(cards)):
                if is_set(cards[i], cards[j], cards[k]):
                    max_sets += 1
    return max_sets


def main():
    T = int(input())
    for i in range(1, T + 1):
        N = int(input())
        cards = []
        for j in range(N):
            cards.append(input())

        print('#{} {}'.format(i, find_max_sets(cards)))


if __name__ == "__main__":
    main()
