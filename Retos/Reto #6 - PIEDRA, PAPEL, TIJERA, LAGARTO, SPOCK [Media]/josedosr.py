def rock_paper_scissor(games):

    options = { '🗿': 0,
                '📄': 1,
                '✂️': 2,
                '🦎': 3,
                '🖖': 4}
    
    rules = [[0, -1, 1, 1, -1],
             [1, 0, -1, -1, 1],
             [-1, 1, 0, 1, -1],
             [-1, 1, -1, 0, 1],
             [1, -1, 1, -1, 0]]

    player_1 = 0
    player_2 = 0

    for game in games:

        p1_choice = options[game[0]]
        p2_choice = options[game[1]]

        result = rules[p1_choice][p2_choice]

        if result > 0:
            player_1 += 1

        elif result < 0: 
            player_2 += 1

    return 'Tie' if player_1 == player_2 else 'Player 1 wins' if player_1 > player_2 else 'Player 2 wins'

print(rock_paper_scissor([("🗿", "🗿")]))
print(rock_paper_scissor([("🗿", "✂️")]))
print(rock_paper_scissor([("✂️", "🗿")]))
print(rock_paper_scissor([("🗿", "🗿"), ("🗿", "🗿"), ("🗿", "🗿"), ("🗿", "🗿")]))
print(rock_paper_scissor([("🖖", "🗿"), ("✂️", "📄"), ("🗿", "🗿"), ("🦎", "🖖")]))