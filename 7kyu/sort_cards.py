# https://www.codewars.com/kata/56f399b59821793533000683/train/python
def sort_cards(cards):
    cards_ranking = {
        "A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, 
        "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13
    }
    try:
        return sorted(cards, key=lambda card: cards_ranking[card])
    except KeyError as e:
        raise ValueError(f"Invalid card: {e}")