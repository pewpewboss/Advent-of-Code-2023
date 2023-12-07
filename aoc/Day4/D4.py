with open("input.txt") as file:
    total = 0
    for scratch_card in file.read().splitlines():
        colon = scratch_card.find(":")
        number_table = scratch_card[colon + 1:len(scratch_card)]
        split = number_table.split("|")
        winning_numbers = [int(s) for s in split[0].strip().split(" ") if s != ""]
        my_numbers = [int(s) for s in split[1].strip().split(" ") if s != ""]
        card_wins = set(winning_numbers).intersection(my_numbers)
        wins = len(card_wins)
        # 'doubling' 2 by n times can be expressed as 2 to the Power of x
        # assume 2 wins and double by wins, but remember due to the assumption we already doubled once, so wins-1
        points = 2 ** (wins - 1) if wins > 1 else wins
        total = total + points
    print(total)


