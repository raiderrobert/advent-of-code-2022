with open('two.txt') as f:
    lines = f.readlines()

SHAPE_SCOPE = {
    "R": 1,
    "P": 2,
    "S": 3,
}

GAME_SCORE = {
    "W": 6,
    "D": 3,
    "L": 0
} 

OPP_CHOICES = {
    "A": "R",
    "B": "P",
    "C": "S",
}

MY_CHOICES = {
    "X": "L",
    "Y": "D",
    "Z": "W",
}

WL_COMBO = {
    "PP": "D",
    "PR": "L",
    "PS": "W",
    "RR": "D",
    "RS": "L",
    "RP": "W",
    "SS": "D",
    "SR": "W",
    "SP": "L"
}

WIN_PATTERN = {
    "R": "S",
    "S": "P",
    "P": "R"
}

LOSE_PATTERN = {
    "S": "R",
    "P": "S",
    "R": "P"
}



def normalize(game: str):
    """
    convert all inputs into standard form
    """
    opp_choice, my_choice = game.split()
    return OPP_CHOICES.get(opp_choice), MY_CHOICES.get(my_choice)



def score_game(opp, my):
    score = SHAPE_SCOPE.get(my)
    game_result = WL_COMBO.get(opp+my)
    score = score + GAME_SCORE.get(game_result)
    return score

def my_choice(opp_choice, game_result) -> str:

    if game_result == "D":
        return opp_choice
    elif game_result == "L":
        return WIN_PATTERN.get(opp_choice)
    elif game_result == "W":
        return LOSE_PATTERN.get(opp_choice)



elf_calories_totals = []
current = 0
scores = []
for l in lines:
    
    opp, result = normalize(l)
    my = my_choice(opp, result)
    score = score_game(opp, my)
    print(f"{l}:{opp}{my}:{score}")
    scores.append(score)

print(sum(scores))
