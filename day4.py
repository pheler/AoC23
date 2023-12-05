def count_matches(winning_numbers, your_numbers):
    return len([num for num in your_numbers if num in winning_numbers])

def process_cards(cards):
    card_counts = [1] * len(cards)  # Initialize a list to keep track of the number of each card
    total_cards = len(cards)
    for i in range(total_cards):
        matches = count_matches(cards[i]['winning_numbers'], cards[i]['your_numbers'])
        for j in range(1, matches + 1):
            if i + j < total_cards:
                card_counts[i + j] += card_counts[i]
    return sum(card_counts)

def main():
    cards = []
    with open('day4.txt', 'r') as file:
        for line in file:
            parts = line.strip().split(' | ')
            winning_numbers = set(parts[0].split())
            your_numbers = set(parts[1].split())
            cards.append({'winning_numbers': winning_numbers, 'your_numbers': your_numbers})
    total_scratchcards = process_cards(cards)
    print(f"Including the original set, you end up with {total_scratchcards} total scratchcards.")

if __name__ == "__main__":
    main()
